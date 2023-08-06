from time import time

from satella.instrumentation.basecounter import Counter

class PulseCounter(Counter):
    """
    Counter that tracks frequency of calls to update()

    Each call to update() signifies a tick that will be tracked
    in time. The value of the counter is the amount of calls to update()
    - ie. ticks - that have been made during the last 'resolution' seconds.
    """

    def __init__(self, name, resolution=1, units=None, description=None):
        """
        Creates a new pulse-counting object

        @param resolution: Resolution of the counter in seconds. It will aggregate
            pulses in these periods
        @type resolution: int or float
        """
        Counter.__init__(self, name, units=units, description=description)
        self.resolution = resolution
        self.pulses = []

    def update(self):
        """A single pulse that will be tracked"""
        if not self.enabled: return
        self.pulses.append(time())

    def get_current(self):
        """Run thru the table"""
        pulses = 0
        stime = time()

        for t in reversed(self.pulses):
            if (stime - t) < self.resolution:
                pulses += 1
            else:
                break

        del self.pulses[:len(self.pulses)-pulses]    # delete pulses before, they are not relevant

        return pulses