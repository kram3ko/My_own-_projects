from user_repository import UserRepository
from user_service import UserService



def main():
    user_repository = UserRepository("users.txt")
    user_service = UserService(user_repository)

    COMMANDS = {
        "create": user_service.create_user,
        "read": user_service.read_user,
        "update": user_service.update_user,
        "delete": user_service.delete_user,

    }

    while True:
        print(f"allowed commands: {list(COMMANDS.keys()) + ["stop"]} ")
        command = input("please write yours command: ")
        if command == "stop":
            print("thank you for use our service see you later :)")
            break
        operation = COMMANDS.get(command)
        try:
            operation()
        except TypeError:
            print("Wrong command! check allowed")
            continue


if __name__ == "__main__":
    main()
