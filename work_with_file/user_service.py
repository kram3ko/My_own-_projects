import hashlib

from pydantic import ValidationError

from work_with_file.input_handler import InputHandler
from work_with_file.iuser_repository import IUserRepository
from work_with_file.iuser_service import IUserService
from work_with_file.models import User


class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository) -> None:
        self.user_repository = user_repository

    def create_user(self) -> None:
        user_name = input("Enter your user_name: ")
        password = input("Enter your password: ")
        age = int(input("Enter your age: "))
        first_name = input("Enter your first_name: ")
        last_name = InputHandler.handle_input("Enter your last_name: ")

        try:
            user = User(
                id_=User.last_id + 1,
                user_name=user_name,
                password=password,
                age=age,
                first_name=first_name,
                last_name=last_name,
            )
        except ValidationError as e:
            print(e)
            return
        User.last_id += 1
        if self.user_repository.add_user(user):
            print("user created!")

    def read_user(self) -> None:
        name = InputHandler.handle_input("Write user name to get info: ")
        if not name:
            return
        user = self.user_repository.find_user(name)

        if user:
            print(user)
        else:
            print("User not found.")

    def update_user(self) -> None:
        user_name = InputHandler.handle_input("Enter name for update: ")
        user = self.user_repository.find_user(user_name)

        if not user:
            print("User not found")
            return

        password = InputHandler.handle_input("Enter new password: ")
        new_age = InputHandler.handle_input("Enter new age: ", int)
        first_name = InputHandler.handle_input("Enter new first_name: ")
        last_name = InputHandler.handle_input("Enter new last_name: ")

        user.password = hashlib.sha256(password.encode()).hexdigest()
        user.age = new_age
        user.first_name = first_name
        user.last_name = last_name

        is_updated = self.user_repository.update_user(user)

        if is_updated:
            print("User updated !")
        else:
            print("User not updated!")

    def delete_user(self) -> None:
        name = InputHandler.handle_input("Enter name for delete: ")
        user = self.user_repository.find_user(name)

        if not user:
            print("User not found")
            return

        if self.user_repository.delete_user(user):
            print(f"User with ID: {user.id_} user_name: {user.user_name} deleted")
