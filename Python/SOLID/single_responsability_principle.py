# Original Code
# class Process:
#     def handle(self, username: str, password: str) -> None:
#         if isinstance(username, str) and isinstance(password, str):
#             print('Database access')
#             print('User checking process')
#             print('User input validation - success')
#         else:
#             raise Exception('Data invalid')


class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_database_access(username, password):
            self.__verify_user_exists(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_error("Data invalid")

    def describe(self) -> str:
        return "Handles user registration process"

    def __verify_database_access(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __verify_user_exists(self, username: str) -> None:
        print("Database access")
        print(f"User checking process for: {username}")

    def __insert_new_user(self, username: str, password: str) -> None:
        print(f"User {username} created successfully")
        _ = password  # acknowledged, used for validation upstream

    def __raise_error(self, message: str) -> None:
        raise ValueError(message)
