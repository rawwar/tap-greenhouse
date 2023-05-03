"""Making it easy to import all Schemas."""
from .candidates import schema as candidates
from .applications import schema as applications

__all__ = ["candidates", 'applications']
