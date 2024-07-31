"""Defines the Fixer class.
"""
from pathlib import Path

from keepass_conflict_fixer.exceptions import NotEnoughDatabasesError


class Fixer:
  """Contains the logic to fix conflicts in KeePass databases.

  Args:
    database_folder: Path to the folder containing the various KeePass databases

  Raises:
    NotADirectoryError: If `database_folder` is not a directory
    NotEnoughDatabasesError: If there are not enough databeases 
      to fix a conflict (less than 2)
  """

  def __init__(self, database_folder: str | Path):
    if isinstance(database_folder, str):
      database_folder = Path(database_folder)

    if not database_folder.is_dir():
      raise NotADirectoryError(f"{database_folder} is not a directory")

    kdbx_files = tuple(file for file in database_folder.iterdir()
                       if file.is_file() and file.suffix == ".kdbx")
    if len(kdbx_files) < 2:
      raise NotEnoughDatabasesError(
          str(database_folder.resolve().absolute()), len(kdbx_files))

    self._database_folder = database_folder
