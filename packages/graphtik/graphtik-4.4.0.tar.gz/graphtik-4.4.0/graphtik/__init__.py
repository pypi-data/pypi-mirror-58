# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
"""Lightweight :term:`computation` graphs for Python."""

__author__ = "hnguyen, ankostis"
__version__ = "4.4.0"
__release_date__ = "21 Dec 2019, 18:58"
__license__ = "Apache-2.0"
__title__ = "graphtik"
__summary__ = __doc__.splitlines()[0]
__uri__ = "https://github.com/pygraphkit/graphtik"


from .base import NO_RESULT
from .modifiers import *  # noqa, on purpose to include any new modifiers
from .netop import compose
from .network import (
    AbortedException,
    abort_run,
    get_execution_pool,
    is_abort,
    is_endure_execution,
    is_marshal_parallel_tasks,
    is_skip_evictions,
    set_endure_execution,
    set_execution_pool,
    set_marshal_parallel_tasks,
    set_skip_evictions,
)
from .op import operation
