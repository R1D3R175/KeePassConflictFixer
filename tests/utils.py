"""Utility functions for testing.
"""
from contextlib import contextmanager


@contextmanager
def not_raises(ExpectedException):
  # pylint: disable=invalid-name
  try:
    yield
  except ExpectedException as error:
    raise AssertionError(
      (f"Raised exception {error.__class__.__name__} when it should not!")
    ) from error
  except Exception as error:
    raise AssertionError(f"An unexpected exception {error} raised.") from error
