from typing import Optional


class AppError(Exception):
    """Base class for app-specific error."""

    def __init__(self, message: Optional[str] = None) -> None:
        self.message = message or self.__class__.__name__
        super().__init__(message)


class UserNotFoundError(AppError):
    def __init__(self, username: str) -> None:
        super().__init__(f"User '{username}' not found.")


class CubeAlreadyExists(AppError):
    def __init__(self, cube_name: str) -> None:
        super().__init__(f"Cube '{cube_name}' already exists.")


class CubeNotFound(AppError):
    def __init__(self, cube_name: str) -> None:
        super().__init__(f"Cube '{cube_name}' not found.")
