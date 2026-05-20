# pylint: disable=invalid-name
class MyClass:

    def method_01(self) -> None:
        print("method_01")
        self.__method_02()  # To call a private method of the class

    def method_03(self) -> None:
        print("method_03")

    def __method_02(self) -> None:
        print("method_02")


obj = MyClass()
obj.method_01()
# obj.__method_02()


# To call a private method of the class


class Register:

    # Public method to call the private methods
    def register(self) -> None:
        print("Start Process")
        self.__verify()
        self.__verify_register()
        self.__insert_database()

    def describe(self) -> str:
        return "Handles the full registration process"

    def __verify(self) -> None:
        print("Verify Data")

    def __verify_register(self) -> None:
        print("Verify Register")

    def __insert_database(self) -> None:
        print("Insert Database")


register = Register()
register.register()
