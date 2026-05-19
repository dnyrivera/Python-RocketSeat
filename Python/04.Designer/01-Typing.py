from typing import Optional, Union


# Examples of typing (Python 3.9+ built-in generics)
def sum_numbers(x: int, y: int) -> int:
    return x + y


def sum_numbers_dict(x: int, y: float) -> dict[str, float]:
    response = x + y
    return {"result": response}


def get_names() -> list[str]:
    return ["Alice", "Bob"]


def get_coordinates() -> tuple[float, float]:
    return (10.0, 20.0)


def get_user() -> dict[str, str]:
    return {"name": "Alice", "email": "alice@example.com"}


def get_unique_tags() -> set[str]:
    return {"python", "flask", "typing"}


def get_frozen_permissions() -> frozenset[str]:
    return frozenset({"read", "write"})


def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice"}
    return users.get(user_id)


def parse_value(value: Union[int, str]) -> str:
    return str(value)


print(sum_numbers(x=10, y=15))
print(sum_numbers_dict(x=10, y=15.5))
print(get_names())
print(get_coordinates())
print(get_user())
print(get_unique_tags())
print(get_frozen_permissions())
print(find_user(1))
print(find_user(99))
print(parse_value(42))
print(parse_value("hello"))
