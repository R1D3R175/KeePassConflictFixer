# pylint: disable=missing-docstring, redefined-outer-name
import os
from pathlib import Path
import time
import tempfile
import pytest
from pykeepass import create_database, PyKeePass


def random_file(modified_time: float | None = None):
  file = tempfile.NamedTemporaryFile(
    prefix='keepass_conflict_fixer_fixture', suffix='.kdbx')

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


@pytest.fixture
def database_directory(request, tmp_path):
  to_remove = ('tmp_path_factory', 'tmp_path', 'request', 'database_directory')
  for fixture in request.fixturenames:
    if fixture not in to_remove and 'database' in fixture:
      database = request.getfixturevalue(fixture)
      database_path = Path(database.filename.name)
      database_path.rename(tmp_path / database_path.name)

  return tmp_path
