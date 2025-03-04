from abc import ABC, abstractmethod

from work_with_file.models import User


class IUserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User) -> None:
        pass

    @abstractmethod
    def find_user(self, user_name: int) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> bool:
        pass

    @abstractmethod
    def delete_user(self, user: User) -> bool:
        pass
