"""
Aggregate tasks from individual task modules in this package.
"""

from invoke import Collection
from invoke_tasks.run_all import examples
from invoke_tasks.validate_output import validate

namespace = Collection(validate, examples)
