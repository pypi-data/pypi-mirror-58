import typing as tp
import abc
from satella.json import JSONAble

DISABLED: int = 0
RUNTIME: int = 1
DEBUG: int = 2
INHERIT: int = 3


class Metric(JSONAble):
    """
    A base metric class
    """
    name: str = None

    def __init__(self, name, root_metric: 'Metric' = None):
        self.name = name
        self.root_metric = root_metric
        self.level = RUNTIME
        self.children = []

    def appendChild(self, metric: 'Metric'):
        self.children.append(metric)

    def switchLevel(self, level: str) -> None:
        self.level = level

    def to_json(self) -> tp.Union[list, dict, str, int, float, None]:
        return {
            child.name[len(self.name)+1:]: child.to_json() for child in self.children
        }

    @abc.abstractmethod
    def handle(self, level, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        self.handle(DEBUG, *args, **kwargs)

    def runtime(self, *args, **kwargs):
        self.handle(RUNTIME, *args, **kwargs)

