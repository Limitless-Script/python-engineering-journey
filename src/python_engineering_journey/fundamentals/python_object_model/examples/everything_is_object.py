from collections.abc import Callable


def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}"


def describe(name: str, obj: object) -> None:
    """Print basic information about an object."""
    print(f"{name}:")
    print(f"  value = {obj!r}")
    print(f"  type  = {type(obj)}")
    print(f"  id    = {id(obj)}")
    print()

number = 42
message = "Hello"
items = [1, 2, 3]
coordinates = (10, 20)
config = {"debug": True}

describe("number", number)
describe("message", message)
describe("items", items)
describe("coordinates", coordinates)
describe("config", config)
describe("greet", greet)

# Functions are objects, so they can be assigned to another name.
say_hello: Callable[[str], str] = greet

print("greet is say_hello:", greet is say_hello)
print(say_hello("Duy"))
