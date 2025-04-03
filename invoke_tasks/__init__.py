"""
Aggregate tasks from individual task modules in this package.
"""

from invoke import Collection
from invoke_tasks.run_all import run_all
from invoke_tasks.validate_output import validate_output

namespace = Collection(validate_output, run_all)
