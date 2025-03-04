import fileinput
from work_with_file.iuser_repository import IUserRepository
from work_with_file.models import User


class UserRepository(IUserRepository):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def add_user(self, user: User) -> None:
        with open(self.filename, "a+") as users_file:
            users_file.seek(0)
            for line in users_file:
                if user.user_name in line:
                    print("User with this username already exists!")
                    return

        with open(self.filename, "a") as users_file:
            users_file.write(user.to_row())
        print(user)
        print("User added successfully!")

    def find_user(self, user_name: int) -> User | None:
        with open(self.filename, "r") as file:
            for line in file:
                if f"{user_name}" in line:
                    return User.from_row(line)

    def update_user(self, user: User) -> bool:
        is_updated = False
        for line in fileinput.input(self.filename, inplace=True):
            if user.user_name in line:
                print(user.to_row(), end="")
                is_updated = True
            else:
                print(line, end="")

        return is_updated

    def delete_user(self, user: User) -> bool:
        is_deleted = False
        for line in fileinput.input(self.filename, inplace=True):
            if user.user_name in line:
                is_deleted = True
                continue
            print(line, end="")
        return is_deleted
