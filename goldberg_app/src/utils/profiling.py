# Python imports
import time

# Local imports

# Third party imports

class Stopwatch:
    """
    'Stopwatch' performs timekeeping functionality. It has `tic` and `toc` functions similar to Matlab

    Constructor ArgsParameters
    ----------
    start : *bool*
        Whether to start the timer on creation

    Keyword Args
    ------------
    _func : *function*
        Function for keeping time, must implement interface of 'time.perf_time', to which it is defaulted

    Returns
    -------
    output : *(bool, str)*
        (Did the test pass?, Error message)

    Examples
    --------
    import time  # time.sleep will be used as a stand in for processor intensive function

    # Create Stopwatch
    ss = Stopwatch()  # Create stopwatch
    ss.start()  # Start it, i.e. get it ready to record tic-tocs

    # Tic-toc 1
    ss.tic()
    time.sleep(5)  # Processing intensive function 1
    ss.toc()

    # Tic-toc 2
    ss.tic()
    time.sleep(5)  # Processing intensive function 2
    ss.toc()

    >>>
    [4.9998727294143475, 5.000292467076484]


    print(ss.tic_tocs)
    """

    def __init__(self, start=False, name=None, _func=time.perf_counter):
        self.name = name
        self.elapsed = 0.0
        self.tic_tocs = []
        self._func = _func
        self._start = None
        self._tics = []
        self._tocs = []
        if start:
            self.start()

    def reset(self):
        self.elapsed = 0.0
        self.tic_tocs.clear()
        self._tics.clear()
        self._tocs.clear()

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def tic(self):
        self.stop()
        self._tics.append(self.elapsed)
        if len(self._tocs) != len(self._tics) - 1:
            raise RuntimeError('Tic-tocs unaligned')
        self.start()

    def toc(self):
        self.stop()
        self._tocs.append(self.elapsed)
        if len(self._tics) != len(self._tocs):
            raise RuntimeError('Tic-tocs unaligned!')

        tic_last = self._tics[-1]
        toc_last = self._tocs[-1]
        tic_toc = toc_last - tic_last

        if tic_toc < 0:
            raise RuntimeError('Tic-tocs unaligned!')
        # Append latest tic_toc and restart
        self.tic_tocs.append(tic_toc)
        self.start()

if __name__ == '__main__':

    # Create Stopwatch
    ss = Stopwatch()  # Create stopwatch
    ss.start()  # Start it, i.e. get it ready to record tic-tocs

    # Tic-toc 1
    ss.tic()
    time.sleep(5)  # Processing intensive function 1
    ss.toc()

    # Tic-toc 2
    ss.tic()
    time.sleep(5)  # Processing intensive function 2
    ss.toc()

    print(ss.tic_tocs)

