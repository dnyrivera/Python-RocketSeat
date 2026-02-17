def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def my_function():
    print("Woo hoo I'm a function")


print(f"\nFunction Decorator: {my_function}")
my_function()


class MyClassDecorator:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> None:
        print("Something is happening before the function is called.")
        self.func()
        print("Something is happening after the function is called.")


@MyClassDecorator
def my_class_function_decorator():
    print("Woo hoo I'm a class function decorator")


print(f"\nClass Decorator: {my_class_function_decorator}")
my_class_function_decorator()
