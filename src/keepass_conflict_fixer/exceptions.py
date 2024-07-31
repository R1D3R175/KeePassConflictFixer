"""Contains custom exceptions of the package.
"""


class NotEnoughDatabasesError(Exception):
  """Raised when there are not enough databases to fix a conflict.
  """

  def __init__(self, path: str, file_count: int):
    self.path = path
    self.file_count = file_count
    super().__init__(f"{path} contains {file_count} databases, \
                     but at least 2 are required to fix a conflict")
