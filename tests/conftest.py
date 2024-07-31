# pylint: disable=missing-docstring, redefined-outer-name
import os
import time
import tempfile
import pytest
from pykeepass import create_database, PyKeePass


def random_file(modified_time: float | None = None):
  file = tempfile.NamedTemporaryFile(prefix='keepass_conflict_fixer_fixture')

  if isinstance(modified_time, float):
    os.utime(file.name, (modified_time, modified_time))

  return file


@pytest.fixture
def database_without_password():
  filename = random_file()
  database = create_database(filename)
  return database


@pytest.fixture
def empty_database():
  filename = random_file()
  database = create_database(filename, 'password')
  return database


@pytest.fixture
def empty_old_database():
  current_time = time.time()
  filename_foo = random_file(modified_time=current_time - 100)
  database_foo = create_database(filename_foo, 'password')
  return database_foo


@pytest.fixture
def empty_new_database():
  current_time = time.time()
  filename_bar = random_file(modified_time=current_time - 50)
  database_bar = create_database(filename_bar, 'password')
  return database_bar


@pytest.fixture
def old_database_with_foo_entry(empty_old_database: PyKeePass):
  empty_old_database.add_entry('', 'Foo', 'foo', 'foo')
  return empty_old_database


@pytest.fixture
def old_database_with_bar_entry(empty_old_database: PyKeePass):
  empty_old_database.add_entry('', 'Bar', 'bar', 'bar')
  return empty_old_database


@pytest.fixture
def new_database_with_foo_entry(empty_new_database: PyKeePass):
  empty_new_database.add_entry('', 'Foo', 'foo', 'foo')
  return empty_new_database


@pytest.fixture
def new_database_with_bar_entry(empty_new_database: PyKeePass):
  empty_new_database.add_entry('', 'Bar', 'bar', 'bar')
  return empty_new_database
