# metadata
__version__ = '19.12'
__author__ = 'Cisco Systems Inc.'
__contact__ = ['pyats-support@cisco.com', 'pyats-support-ext@cisco.com']
__copyright__ = 'Copyright (c) 2017-2019, Cisco Systems Inc.'

# expose internal modules
from .counter import ResultCounter
from .context import TestResultContext
from .result import (TestResult,
                     Passed,
                     Failed,
                     Aborted,
                     Blocked,
                     Skipped,
                     Errored,
                     Passx)

# limited the # of exports
# (do not export Null)
__all__ = ['Failed', 'Passed', 'Aborted', 'Blocked', 'Skipped',
           'Errored', 'Passx']
