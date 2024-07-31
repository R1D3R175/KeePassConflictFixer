"""Tests that check the correct initialization of the Fixer class.
"""
import pytest
from keepass_conflict_fixer.exceptions import NotEnoughDatabasesError
from keepass_conflict_fixer.fixer import Fixer
import tests.utils


def test_raises_if_not_directory():
  with pytest.raises(NotADirectoryError):
    Fixer('not_a_directory')


def test_raises_if_not_enough_databases(database_directory, empty_database):
  # pylint: disable=unused-argument
  with pytest.raises(NotEnoughDatabasesError):
    Fixer(database_directory)


def test_doesnt_raise_with_enough_databases(database_directory,
                                            empty_old_database,
                                            empty_new_database):
  # pylint: disable=unused-argument
  with tests.utils.not_raises(NotEnoughDatabasesError):
    Fixer(database_directory)
