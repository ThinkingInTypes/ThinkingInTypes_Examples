"""
Aggregate tasks from individual task modules in this package.
"""

from invoke import Collection
from invoke_tasks.run_all import examples
from invoke_tasks.validate_output import validate
from invoke_tasks.extract_examples import extract

namespace = Collection(validate, examples, extract)
