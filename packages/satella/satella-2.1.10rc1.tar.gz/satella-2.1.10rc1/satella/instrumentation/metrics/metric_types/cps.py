import typing as tp
from .base import Metric
import time
import collections


class ClicksPerTimeUnitMetric(Metric):
    CLASS_NAME = 'cps'

    def __init__(self, *args, time_unit_vectors: tp.Optional[tp.List[float]] = None, **kwargs):
        """
        :param time_unit_vectors: time units (in seconds) to count the clicks in between.
            Default - track a single value, amount of calls to .handle() in last second
        """
        super().__init__(*args, **kwargs)
        time_unit_vectors = time_unit_vectors or [1]
        self.last_clicks = collections.deque()
        self.cutoff_period = max(time_unit_vectors)
        self.time_unit_vectors = time_unit_vectors

    def handle(self, level: int, *args, **kwargs) -> None:
        monotime = time.monotonic()
        if self.can_process_this_level(level):
            self.last_clicks.append(time.monotonic())
            try:
                while self.last_clicks[0] <= monotime - self.cutoff_period:
                    self.last_clicks.popleft()
            except IndexError:
                pass

    def to_json(self) -> tp.List[int]:
        count_map = [0] * len(self.time_unit_vectors)
        monotime = time.monotonic()
        time_unit_vectors = [monotime-v for v in self.time_unit_vectors]

        for v in self.last_clicks:
            for index, cutoff in enumerate(time_unit_vectors):
                if v >= cutoff:
                    count_map[index] += 1

        return count_map
