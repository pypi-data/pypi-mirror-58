import _version

__version__ = _version.__version__
__author__ = 'Daniel Nyga'

from .debug import out, stop, trace, stoptrace
from .tools import ifnone, ifnot, allnone, allnot, edict, idxif, first, last, LinearScale
from .signals import add_handler, rm_handler, enable_ctrlc
from .threads import Lock, RLock, Condition, Event, Semaphore, BoundedSemaphore, Barrier, Relay, Thread, \
    SuspendableThread, ThreadInterrupt, sleep, waitabout, Timer
from .logs import (loggers, newlogger, getlogger, DEBUG, INFO, WARNING, ERROR, CRITICAL, expose, inspect,
    active_exposures, ExposureEmptyError, ExposureLockedError, exposure, set_exposure_dir)
from .console import ProgressBar, StatusMsg, bf

enable_ctrlc()