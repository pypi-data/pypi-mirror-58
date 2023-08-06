import abc
import logging
import typing as tp
import threading
logger = logging.getLogger(__name__)
from .metric_types.base import RUNTIME, DISABLED, DEBUG, INHERIT

__all__ = ['getMetric', 'DISABLED', 'RUNTIME', 'DEBUG', 'INHERIT']


metrics = {}
metrics_lock = threading.Lock()


def getMetric(name: str):
    """
    Obtain a metric of given name
    :param name: must be a module name
    """
    name = name.split('.')
    with metrics_lock:
        root_metric = metrics['']
        for name_index, name_part in enumerate(name):
            tentative_name = '.'.join(name[:name_index])
            if tentative_name not in metrics:
                metric = Metric(tentative_name, root_metric)
                if tentative_name == '':
                    metric.level = RUNTIME
                metrics[tentative_name] = Metric(tentative_name, root_metric)
            else:
                metric = metrics[tentative_name]
            root_metric = metric

        return metric
