from satella.coding import merge_dicts

from satella.exceptions import ConfigurationError
from .base import BaseSource

__all__ = [
    'AlternativeSource', 'OptionalSource', 'MergingSource'
]


class AlternativeSource(BaseSource):
    def __init__(self, *sources: BaseSource):
        """
        If one fails, use the next
        """
        self.sources = sources

    def provide(self) -> dict:
        """
        :raises ConfigurationError: when backup fails too
        """
        for source in self.sources:
            try:
                s = source.provide()
                assert isinstance(s, dict), 'provide() returned a non-dict'
                return s
            except ConfigurationError:
                pass
        else:
            raise ConfigurationError('all sources failed!')


class OptionalSource(AlternativeSource):
    def __init__(self, source: BaseSource):
        """
        This will substitute for empty dict if underlying config would fail.

        Apply this to your sources if you expect that they will fail.

        Use as

            OptionalSource(SomeOtherSource1)

        """
        super(OptionalSource, self).__init__(source, BaseSource())


class MergingSource(BaseSource):
    """
    Source that merges configuration from a bunch of sources
    """

    RAISE = 0       # Raise ConfigurationError if one of sources fails
    SILENT = 1      # Silently continue loading from next files if one fails

    def __init__(self, *sources: BaseSource, on_fail: int = RAISE):
        self.sources = sources
        self.on_fail = on_fail

    def provide(self) -> dict:
        cfg = {}

        for source in self.sources:
            try:
                p = source.provide()
            except ConfigurationError as e:
                if self.on_fail == MergingSource.RAISE:
                    raise e
                elif self.on_fail == MergingSource.SILENT:
                    p = {}
                else:
                    raise ConfigurationError('Invalid on_fail parameter %s' % (self.on_fail, ))
            assert isinstance(p, dict), 'what was provided by the config was not a dict'
            cfg = merge_dicts(cfg, p)
            assert isinstance(cfg, dict), 'what merge_dicts returned wasn''t a dict'

        return cfg
