class User:
    """A simple user object."""

    def __init__(self, username: str) -> None:
        self.username = username

    def greet(self) -> str:
        """Return a greeting."""
        return f"Hello, {self.username}"


user = User("duy")

print("Object:")
print(user)

print()

print("Type:")
print(type(user))

print()

print("Identity:")
print(id(user))

print()

print("Is User:")
print(isinstance(user, User))

print()

print("User class:")
print(User)

print("Type of User:")
print(type(User))

print()

print("User attributes and methods:")

for name in dir(user):
    print(f"  - {name}")
