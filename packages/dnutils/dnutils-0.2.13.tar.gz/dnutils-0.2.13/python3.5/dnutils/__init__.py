from ._version import __version__

__author__ = 'Daniel Nyga'

from .debug import out, stop, trace, stoptrace
from .tools import ifnone, ifnot, allnone, allnot, edict, idxif, first, last, LinearScale
from .signals import add_handler, rm_handler, enable_ctrlc
from .threads import Lock, RLock, Condition, Event, Semaphore, BoundedSemaphore, Barrier, Relay, Thread, \
    SuspendableThread, sleep, waitabout, Timer
from .logs import (loggers, newlogger, getlogger, DEBUG, INFO, WARNING, ERROR, CRITICAL, expose, inspect,
                   active_exposures, exposure, set_exposure_dir)
from .console import ProgressBar, StatusMsg, bf

from threading import main_thread, current_thread

if current_thread() is main_thread():
    enable_ctrlc()
