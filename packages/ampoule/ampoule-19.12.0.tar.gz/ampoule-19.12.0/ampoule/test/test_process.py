
from signal import SIGHUP
import os
import os.path
from io import BytesIO as sio
import tempfile

from twisted.internet import error, defer, reactor
from twisted.python import failure
from twisted.trial import unittest
from twisted.protocols import amp
from ampoule import main, child, commands, pool

class ShouldntHaveBeenCalled(Exception):
    pass

def _raise(_):
    raise ShouldntHaveBeenCalled(_)

class _FakeT(object):
    closeStdinCalled = False
    def __init__(self, s):
        self.s = s

    def closeStdin(self):
        self.closeStdinCalled = True

    def write(self, data):
        self.s.write(data)

class FakeAMP(object):
    connector = None
    reason = None
    def __init__(self, s):
        self.s = s

    def makeConnection(self, connector):
        if self.connector is not None:
            raise Exception("makeConnection called twice")
        self.connector = connector

    def connectionLost(self, reason):
        if self.reason is not None:
            raise Exception("connectionLost called twice")
        self.reason = reason

    def dataReceived(self, data):
        self.s.write(data)

class Exit(amp.Command):
    arguments = []
    response = []

class Ping(amp.Command):
    arguments = [(b'data', amp.String())]
    response = [(b'response', amp.String())]

class Pong(amp.Command):
    arguments = [(b'data', amp.String())]
    response = [(b'response', amp.String())]

class Pid(amp.Command):
    response = [(b'pid', amp.Integer())]

class Reactor(amp.Command):
    response = [(b'classname', amp.String())]

class NoResponse(amp.Command):
    arguments = [(b'arg', amp.String())]
    requiresAnswer = False

class GetResponse(amp.Command):
    response = [(b"response", amp.String())]

class Child(child.AMPChild):
    @Ping.responder
    def ping(self, data):
        return self.callRemote(Pong, data=data)

class PidChild(child.AMPChild):
    @Pid.responder
    def pid(self):
        import os
        return {'pid': os.getpid()}

class NoResponseChild(child.AMPChild):
    _set = False
    @NoResponse.responder
    def noresponse(self, arg):
        self._set = arg
        return {}

    @GetResponse.responder
    def getresponse(self):
        return {"response": self._set}

class ReactorChild(child.AMPChild):
    @Reactor.responder
    def reactor(self):
        from twisted.internet import reactor
        return {'classname': reactor.__class__.__name__.encode()}

class First(amp.Command):
    arguments = [(b'data', amp.String())]
    response = [(b'response', amp.String())]

class Second(amp.Command):
    pass

class WaitingChild(child.AMPChild):
    deferred = None
    @First.responder
    def first(self, data):
        self.deferred = defer.Deferred()
        return self.deferred.addCallback(lambda _: {'response': data})

    @Second.responder
    def second(self):
        self.deferred.callback('')
        return {}

class HangForever(amp.Command):
    pass

class TimingOutChild(child.AMPChild):
    @HangForever.responder
    def hangForever(self):
        return defer.Deferred()

    @Ping.responder
    def ping(self, data):
        return {'response': data}

class Die(amp.Command):
    pass

class BadChild(child.AMPChild):
    @Die.responder
    def die(self):
        self.shutdown = False
        self.transport.loseConnection()
        return {}


class ExitingChild(child.AMPChild):
    @Exit.responder
    def exit(self):
        import os
        os._exit(33)

class Write(amp.Command):
    response = [(b"response", amp.String())]


class Writer(child.AMPChild):

    def __init__(self, data=b'hello'):
        child.AMPChild.__init__(self)
        if isinstance(data, str):
            # this is passing through sys.argv, argv is unconditionally unicode
            # on py3; see https://bugs.python.org/issue8776
            data = data.encode()
        self.data = data

    @Write.responder
    def write(self):
        return {'response': self.data}


class GetCWD(amp.Command):

    response = [(b"cwd", amp.Unicode())]


class TempDirChild(child.AMPChild):

    def __init__(self, directory=None):
        child.AMPChild.__init__(self)
        self.directory = directory

    def __enter__(self):
        directory = tempfile.mkdtemp()
        os.chdir(directory)
        if self.directory is not None:
            os.mkdir(self.directory)
            os.chdir(self.directory)

    def __exit__(self, exc_type, exc_val, exc_tb):
        cwd = os.getcwd()
        os.chdir('..')
        os.rmdir(cwd)

    @GetCWD.responder
    def getcwd(self):
        return {'cwd': os.getcwd()}


class TestAMPConnector(unittest.TestCase):
    def setUp(self):
        """
        The only reason why this method exists is to let 'trial ampoule'
        to install the signal handlers (#3178 for reference).
        """
        super(TestAMPConnector, self).setUp()
        d = defer.Deferred()
        reactor.callLater(0, d.callback, None)
        return d

    def _makeConnector(self, s, sa):
        a = FakeAMP(sa)
        ac = main.AMPConnector(a)
        assert ac.name is not None
        ac.transport = _FakeT(s)
        return ac

    def test_protocol(self):
        """
        Test that outReceived writes to AMP and that it triggers the
        finished deferred once the process ended.
        """
        s = sio()
        sa = sio()
        ac = self._makeConnector(s, sa)

        for x in range(99):
            ac.childDataReceived(4, str(x).encode("ascii"))

        ac.processEnded(failure.Failure(error.ProcessDone(0)))
        return ac.finished.addCallback(
            lambda _: self.assertEqual(sa.getvalue(), b''.join(
                str(x).encode("ascii") for x in range(99)
            ))
        )

    def test_protocol_failing(self):
        """
        Test that a failure in the process termination is correctly
        propagated to the finished deferred.
        """
        s = sio()
        sa = sio()
        ac = self._makeConnector(s, sa)

        ac.finished.addCallback(_raise)
        fail = failure.Failure(error.ProcessTerminated())
        self.assertFailure(ac.finished, error.ProcessTerminated)
        ac.processEnded(fail)

    def test_startProcess(self):
        """
        Test that startProcess actually starts a subprocess and that
        it receives data back from the process through AMP.
        """
        s = sio()
        a = FakeAMP(s)
        STRING = b"ciao"
        BOOT = """\
import sys, os
def main(arg):
    os.write(4, arg.encode("utf-8"))
main(sys.argv[1])
"""
        starter = main.ProcessStarter(bootstrap=BOOT,
                                      args=(STRING,),
                                      packages=("twisted", "ampoule"))

        amp, finished = starter.startPythonProcess(main.AMPConnector(a))
        return finished.addCallback(lambda _: self.assertEquals(s.getvalue(), STRING))

    def test_failing_deferToProcess(self):
        """
        Test failing subprocesses and the way they terminate and preserve
        failing information.
        """
        s = sio()
        a = FakeAMP(s)
        STRING = b"ciao"
        BOOT = """\
import sys
def main(arg):
    raise Exception(arg)
main(sys.argv[1])
"""
        starter = main.ProcessStarter(bootstrap=BOOT, args=(STRING,), packages=("twisted", "ampoule"))
        ready, finished = starter.startPythonProcess(main.AMPConnector(a), "I'll be ignored")

        self.assertFailure(finished, error.ProcessTerminated)
        finished.addErrback(lambda reason: self.assertEquals(reason.getMessage(), STRING))
        return finished

    def test_env_setting(self):
        """
        Test that and environment variable passed to the process starter
        is correctly passed to the child process.
        """
        s = sio()
        a = FakeAMP(s)
        STRING = b"ciao"
        BOOT = """\
import sys, io, os
def main():
    with io.open(4, 'w' + ('b' if bytes is str else '')) as f:
        f.write(os.environ['FOOBAR'])
main()
"""
        starter = main.ProcessStarter(bootstrap=BOOT,
                                      packages=("twisted", "ampoule"),
                                      env={"FOOBAR": STRING})
        amp, finished = starter.startPythonProcess(main.AMPConnector(a), "I'll be ignored")
        return finished.addCallback(lambda _: self.assertEquals(s.getvalue(), STRING))

    def test_startAMPProcess(self):
        """
        Test that you can start an AMP subprocess and that it correctly
        accepts commands and correctly answers them.
        """
        STRING = b"ciao"

        starter = main.ProcessStarter(packages=("twisted", "ampoule"))
        c, finished = starter.startAMPProcess(child.AMPChild)
        c.callRemote(commands.Echo, data=STRING
           ).addCallback(lambda response:
                self.assertEquals(response['response'], STRING)
           ).addCallback(lambda _: c.callRemote(commands.Shutdown))
        return finished

    def test_BootstrapContext(self):
        starter = main.ProcessStarter(packages=('twisted', 'ampoule'))
        c, finished = starter.startAMPProcess(TempDirChild)
        cwd = []
        def checkBootstrap(response):
            cwd.append(response['cwd'])
            self.assertNotEquals(cwd, os.getcwd())
        d = c.callRemote(GetCWD)
        d.addCallback(checkBootstrap)
        d.addCallback(lambda _: c.callRemote(commands.Shutdown))
        finished.addCallback(lambda _: self.assertFalse(os.path.exists(cwd[0])))
        return finished

    def test_BootstrapContextInstance(self):
        starter = main.ProcessStarter(packages=('twisted', 'ampoule'))
        c, finished = starter.startAMPProcess(TempDirChild,
                                              ampChildArgs=('foo',))
        cwd = []
        def checkBootstrap(response):
            cwd.append(response['cwd'])
            self.assertTrue(cwd[0].endswith('/foo'))
        d = c.callRemote(GetCWD)
        d.addCallback(checkBootstrap)
        d.addCallback(lambda _: c.callRemote(commands.Shutdown))
        finished.addCallback(lambda _: self.assertFalse(os.path.exists(cwd[0])))
        return finished

    def test_startAMPAndParentProtocol(self):
        """
        Test that you can start an AMP subprocess and the children can
        call methods on their parent.
        """
        DATA = b"CIAO"
        APPEND = b"123"

        class Parent(amp.AMP):
            @Pong.responder
            def pong(self, data):
                return {'response': DATA+APPEND}

        starter = main.ProcessStarter(packages=("twisted", "ampoule"))

        subp, finished = starter.startAMPProcess(ampChild=Child, ampParent=Parent)
        subp.callRemote(Ping, data=DATA
           ).addCallback(lambda response:
                self.assertEquals(response['response'], DATA+APPEND)
           ).addCallback(lambda _: subp.callRemote(commands.Shutdown))
        return finished

    def test_roundtripError(self):
        """
        Test that invoking a child using an unreachable class raises
        a L{RunTimeError} .
        """
        class Child(child.AMPChild):
            pass

        starter = main.ProcessStarter(packages=("twisted", "ampoule"))

        self.assertRaises(RuntimeError, starter.startAMPProcess, ampChild=Child)

class TestProcessPool(unittest.TestCase):

    def test_startStopWorker(self):
        """
        Test that starting and stopping a worker keeps the state of
        the process pool consistent.
        """
        pp = pool.ProcessPool()
        self.assertEquals(pp.started, False)
        self.assertEquals(pp.finished, False)
        self.assertEquals(pp.processes, set())
        self.assertEquals(pp._finishCallbacks, {})

        def _checks():
            self.assertEquals(pp.started, False)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), 1)
            self.assertEquals(len(pp._finishCallbacks), 1)
            return pp.stopAWorker()

        def _closingUp(_):
            self.assertEquals(pp.started, False)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), 0)
            self.assertEquals(pp._finishCallbacks, {})
        pp.startAWorker()
        return _checks().addCallback(_closingUp).addCallback(lambda _: pp.stop())

    def test_startAndStop(self):
        """
        Test that a process pool's start and stop method create the
        expected number of workers and keep state consistent in the
        process pool.
        """
        pp = pool.ProcessPool()
        self.assertEquals(pp.started, False)
        self.assertEquals(pp.finished, False)
        self.assertEquals(pp.processes, set())
        self.assertEquals(pp._finishCallbacks, {})

        def _checks(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.min)
            self.assertEquals(len(pp._finishCallbacks), pp.min)
            return pp.stop()

        def _closingUp(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, True)
            self.assertEquals(len(pp.processes), 0)
            self.assertEquals(pp._finishCallbacks, {})
        return pp.start().addCallback(_checks).addCallback(_closingUp)

    def test_adjustPoolSize(self):
        """
        Test that calls to pool.adjustPoolSize are correctly handled.
        """
        pp = pool.ProcessPool(min=10)
        self.assertEquals(pp.started, False)
        self.assertEquals(pp.finished, False)
        self.assertEquals(pp.processes, set())
        self.assertEquals(pp._finishCallbacks, {})

        def _resize1(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.min)
            self.assertEquals(len(pp._finishCallbacks), pp.min)
            return pp.adjustPoolSize(min=2, max=3)

        def _resize2(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(pp.max, 3)
            self.assertEquals(pp.min, 2)
            self.assertEquals(len(pp.processes), pp.max)
            self.assertEquals(len(pp._finishCallbacks), pp.max)

        def _resize3(_):
            self.assertRaises(AssertionError, pp.adjustPoolSize, min=-1, max=5)
            self.assertRaises(AssertionError, pp.adjustPoolSize, min=5, max=1)
            return pp.stop()

        return pp.start(
            ).addCallback(_resize1
            ).addCallback(_resize2
            ).addCallback(_resize3)

    def test_childRestart(self):
        """
        Test that a failing child process is immediately restarted.
        """
        pp = pool.ProcessPool(ampChild=BadChild, min=1)
        STRING = b"DATA"

        def _checks(_):
            d = next(iter(pp._finishCallbacks.values()))
            pp.doWork(Die).addErrback(lambda _: None)
            return d.addBoth(_checksAgain)

        def _checksAgain(_):
            return pp.doWork(commands.Echo, data=STRING
                    ).addCallback(lambda result: self.assertEquals(result['response'], STRING))

        return pp.start(
            ).addCallback(_checks
            ).addCallback(lambda _: pp.stop())

    def test_parentProtocolChange(self):
        """
        Test that the father can use an AMP protocol too.
        """
        DATA = b"CIAO"
        APPEND = b"123"

        class Parent(amp.AMP):
            @Pong.responder
            def pong(self, data):
                return {'response': DATA+APPEND}

        pp = pool.ProcessPool(ampChild=Child, ampParent=Parent)
        def _checks(_):
            return pp.doWork(Ping, data=DATA
                       ).addCallback(lambda response:
                            self.assertEquals(response['response'], DATA+APPEND)
                       )

        return pp.start().addCallback(_checks).addCallback(lambda _: pp.stop())


    def test_deferToAMPProcess(self):
        """
        Test that deferToAMPProcess works as expected.
        """
        def cleanupGlobalPool():
            d = pool.pp.stop()
            pool.pp = None
            return d
        self.addCleanup(cleanupGlobalPool)

        STRING = b"CIAOOOO"
        d = pool.deferToAMPProcess(commands.Echo, data=STRING)
        d.addCallback(self.assertEquals, {"response": STRING})
        return d

    def test_checkStateInPool(self):
        """
        Test that busy and ready lists are correctly maintained.
        """
        pp = pool.ProcessPool(ampChild=WaitingChild)

        DATA = b"foobar"

        def _checks(_):
            d = pp.callRemote(First, data=DATA)
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.min)
            self.assertEquals(len(pp._finishCallbacks), pp.min)
            self.assertEquals(len(pp.ready), pp.min-1)
            self.assertEquals(len(pp.busy), 1)
            child = pp.busy.pop()
            pp.busy.add(child)
            child.callRemote(Second)
            return d

        return pp.start(
            ).addCallback(_checks
            ).addCallback(lambda _: pp.stop())

    def test_growingToMax(self):
        """
        Test that the pool grows over time until it reaches max processes.
        """
        MAX = 5
        pp = pool.ProcessPool(ampChild=WaitingChild, min=1, max=MAX)

        def _checks(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.min)
            self.assertEquals(len(pp._finishCallbacks), pp.min)

            D = b"DATA"
            d = [pp.doWork(First, data=D) for x in range(MAX)]

            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.max)
            self.assertEquals(len(pp._finishCallbacks), pp.max)

            [child.callRemote(Second) for child in pp.processes]
            return defer.DeferredList(d)

        return pp.start(
            ).addCallback(_checks
            ).addCallback(lambda _: pp.stop())

    def test_growingToMaxAndShrinking(self):
        """
        Test that the pool grows but after 'idle' time the number of
        processes goes back to the minimum.
        """

        MAX = 5
        MIN = 1
        IDLE = 1
        pp = pool.ProcessPool(ampChild=WaitingChild, min=MIN, max=MAX, maxIdle=IDLE)

        def _checks(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.min)
            self.assertEquals(len(pp._finishCallbacks), pp.min)

            D = b"DATA"
            d = [pp.doWork(First, data=D) for x in range(MAX)]

            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.max)
            self.assertEquals(len(pp._finishCallbacks), pp.max)

            [child.callRemote(Second) for child in pp.processes]
            return defer.DeferredList(d).addCallback(_realChecks)

        def _realChecks(_):
            from twisted.internet import reactor
            d = defer.Deferred()
            def _cb():
                def __(_):
                    try:
                        self.assertEquals(pp.started, True)
                        self.assertEquals(pp.finished, False)
                        self.assertEquals(len(pp.processes), pp.min)
                        self.assertEquals(len(pp._finishCallbacks), pp.min)
                        d.callback(None)
                    except Exception as e:
                        d.errback(e)
                return pp._pruneProcesses().addCallback(__)
            # just to be shure we are called after the pruner
            pp.looping.stop() # stop the looping, we don't want it to
                              # this right here
            reactor.callLater(IDLE, _cb)
            return d

        return pp.start(
            ).addCallback(_checks
            ).addCallback(lambda _: pp.stop())

    def test_recycling(self):
        """
        Test that after a given number of calls subprocesses are
        recycled.
        """
        MAX = 1
        MIN = 1
        RECYCLE_AFTER = 1
        pp = pool.ProcessPool(ampChild=PidChild, min=MIN, max=MAX, recycleAfter=RECYCLE_AFTER)
        self.addCleanup(pp.stop)

        def _checks(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.min)
            self.assertEquals(len(pp._finishCallbacks), pp.min)
            return pp.doWork(Pid
                ).addCallback(lambda response: response['pid'])

        def _checks2(pid):
            return pp.doWork(Pid
                ).addCallback(lambda response: response['pid']
                ).addCallback(self.assertNotEquals, pid)


        d = pp.start()
        d.addCallback(_checks)
        d.addCallback(_checks2)
        return d

    def test_recyclingProcessFails(self):
        """
        A process exiting with a non-zero exit code when recycled does not get
        multiple processes started to replace it.
        """
        MAX = 1
        MIN = 1
        RECYCLE_AFTER = 1
        RECYCLE_AFTER = 1
        pp = pool.ProcessPool(ampChild=ExitingChild, min=MIN, max=MAX, recycleAfter=RECYCLE_AFTER)
        self.addCleanup(pp.stop)

        def _checks(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.min)
            self.assertEquals(len(pp._finishCallbacks), pp.min)
            child = list(pp.ready)[0]
            finished = pp._finishCallbacks[child]
            return pp.doWork(Exit).addBoth(lambda _: finished)

        def _checks2(_):
            self.assertEquals(len(pp.processes), pp.max)

        d = pp.start()
        d.addCallback(_checks)
        d.addCallback(_checks2)
        return d


    def test_recyclingWithQueueOverload(self):
        """
        Test that we get the correct number of different results when
        we overload the pool of calls.
        """
        MAX = 5
        MIN = 1
        RECYCLE_AFTER = 10
        CALLS = 60
        pp = pool.ProcessPool(ampChild=PidChild, min=MIN, max=MAX, recycleAfter=RECYCLE_AFTER)
        self.addCleanup(pp.stop)

        def _check(results):
            s = set()
            for succeed, response in results:
                s.add(response['pid'])

            # For the first C{MAX} calls, each is basically guaranteed to go to
            # a different child.  After that, though, there are no guarantees.
            # All the rest might go to a single child, since the child to
            # perform a job is selected arbitrarily from the "ready" set.  Fair
            # distribution of jobs needs to be implemented; right now it's "set
            # ordering" distribution of jobs.
            self.assertTrue(len(s) > MAX)

        def _work(_):
            l = [pp.doWork(Pid) for x in range(CALLS)]
            d = defer.DeferredList(l)
            return d.addCallback(_check)
        d = pp.start()
        d.addCallback(_work)
        return d


    def test_disableProcessRecycling(self):
        """
        Test that by setting 0 to recycleAfter we actually disable process recycling.
        """
        MAX = 1
        MIN = 1
        RECYCLE_AFTER = 0
        pp = pool.ProcessPool(ampChild=PidChild, min=MIN, max=MAX, recycleAfter=RECYCLE_AFTER)

        def _checks(_):
            self.assertEquals(pp.started, True)
            self.assertEquals(pp.finished, False)
            self.assertEquals(len(pp.processes), pp.min)
            self.assertEquals(len(pp._finishCallbacks), pp.min)
            return pp.doWork(Pid
                ).addCallback(lambda response: response['pid'])

        def _checks2(pid):
            return pp.doWork(Pid
                ).addCallback(lambda response: response['pid']
                ).addCallback(self.assertEquals, pid
                ).addCallback(lambda _: pid)

        def finish(reason):
            return pp.stop().addCallback(lambda _: reason)

        return pp.start(
            ).addCallback(_checks
            ).addCallback(_checks2
            ).addCallback(_checks2
            ).addCallback(finish)

    def test_changeChildrenReactor(self):
        """
        Test that by passing the correct argument children change their
        reactor type.
        """
        MAX = 1
        MIN = 1
        FIRST = "select"
        SECOND = "poll"

        def checkDefault():
            pp = pool.ProcessPool(
                starter=main.ProcessStarter(
                    childReactor=FIRST,
                    packages=("twisted", "ampoule")),
                ampChild=ReactorChild, min=MIN, max=MAX)
            pp.start()
            return (pp.doWork(Reactor)
                    .addCallback(self.assertEquals,
                                 {'classname': b"SelectReactor"})
                    .addCallback(lambda _: pp.stop()))
        def checkPool(_):
            pp = pool.ProcessPool(
                starter=main.ProcessStarter(
                    childReactor=SECOND,
                    packages=("twisted", "ampoule")),
                ampChild=ReactorChild, min=MIN, max=MAX)
            pp.start()
            return (pp.doWork(Reactor)
                    .addCallback(self.assertEquals,
                                 {'classname': b"PollReactor"})
                    .addCallback(lambda _: pp.stop()))

        return checkDefault(
            ).addCallback(checkPool)
    try:
        from select import poll
    except ImportError:
        test_changeChildrenReactor.skip = "This architecture doesn't support select.poll, I can't run this test"

    def test_commandsWithoutResponse(self):
        """
        Test that if we send a command without a required answer we
        actually don't have any problems.
        """
        DATA = b"hello"
        pp = pool.ProcessPool(ampChild=NoResponseChild, min=1, max=1)

        def _check(_):
            return pp.doWork(GetResponse
                ).addCallback(self.assertEquals, {"response": DATA})

        def _work(_):
            return pp.doWork(NoResponse, arg=DATA)

        return pp.start(
            ).addCallback(_work
            ).addCallback(_check
            ).addCallback(lambda _: pp.stop())

    def test_supplyChildArgs(self):
        """Ensure that arguments for the child constructor are passed in."""
        pp = pool.ProcessPool(Writer, ampChildArgs=['body'], min=0)
        def _check(result):
            return pp.doWork(Write).addCallback(
            self.assertEquals, {'response': b'body'})

        return pp.start(
            ).addCallback(_check
            ).addCallback(lambda _: pp.stop())

    def processTimeoutTest(self, timeout):
        pp = pool.ProcessPool(WaitingChild, min=1, max=1)

        def _work(_):
            d = pp.callRemote(First, data=b"ciao", _timeout=timeout)
            self.assertFailure(d, error.ProcessTerminated)
            return d

        return pp.start(
            ).addCallback(_work
            ).addCallback(lambda _: pp.stop())

    def test_processTimeout(self):
        """
        Test that a call that doesn't finish within the given timeout
        time is correctly handled.
        """
        return self.processTimeoutTest(1)

    def test_processTimeoutZero(self):
        """
        Test that the process is correctly handled when the timeout is zero.
        """
        return self.processTimeoutTest(0)

    def test_processDeadline(self):
        pp = pool.ProcessPool(WaitingChild, min=1, max=1)

        def _work(_):
            d = pp.callRemote(First, data=b"ciao", _deadline=reactor.seconds())
            self.assertFailure(d, error.ProcessTerminated)
            return d

        return pp.start(
            ).addCallback(_work
            ).addCallback(lambda _: pp.stop())

    def test_processBeforeDeadline(self):
        pp = pool.ProcessPool(PidChild, min=1, max=1)

        def _work(_):
            d = pp.callRemote(Pid, _deadline=reactor.seconds() + 10)
            d.addCallback(lambda result: self.assertNotEqual(result['pid'], 0))
            return d

        return pp.start(
            ).addCallback(_work
            ).addCallback(lambda _: pp.stop())

    def test_processTimeoutSignal(self):
        """
        Test that a call that doesn't finish within the given timeout
        time is correctly handled.
        """
        pp = pool.ProcessPool(WaitingChild, min=1, max=1,
                              timeout_signal=SIGHUP)

        def _work(_):
            d = pp.callRemote(First, data=b"ciao", _timeout=1)
            d.addCallback(lambda d: self.fail())
            text = 'signal %d' % SIGHUP
            d.addErrback(lambda f: self.assertIn(text, str(f.value)))
            return d

        return pp.start(
            ).addCallback(_work
            ).addCallback(lambda _: pp.stop())

    def test_processGlobalTimeout(self):
        """
        Test that a call that doesn't finish within the given global
        timeout time is correctly handled.
        """
        pp = pool.ProcessPool(WaitingChild, min=1, max=1, timeout=1)

        def _work(_):
            d = pp.callRemote(First, data=b"ciao")
            self.assertFailure(d, error.ProcessTerminated)
            return d

        return pp.start(
            ).addCallback(_work
            ).addCallback(lambda _: pp.stop())

    def test_processRestartAfterTimeout(self):
        """
        Test that a call that times out doesn't cause all subsequent requests
        to fail
        """
        pp = pool.ProcessPool(TimingOutChild, min=1, max=1, timeout=1)

        def _work(_):
            d1 = pp.callRemote(HangForever)
            d2 = pp.callRemote(Ping, data=b"hello")

            self.assertFailure(d1, error.ProcessTerminated)

            d2.addCallback(
                lambda result: self.assertEqual(
                    result, {"response": b"hello"}))

            return defer.DeferredList([d1, d2])

        return pp.start(
            ).addCallback(_work
            ).addCallback(lambda _: pp.stop())
