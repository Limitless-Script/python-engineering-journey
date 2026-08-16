"""Exercise 02: Mutation vs Rebinding.

Implement mutate() and rebind() according to their contracts.

Do not change the tests or expected behavior.
"""


def mutate(data: list[int]) -> None:
    """Mutate the existing list.

    Requirements:
    - Do not create a replacement list.
    - Add the value 4 to the existing list.
    """
    raise NotImplementedError


def rebind(data: list[int]) -> None:
    """Rebind the local name.

    Requirements:
    - Rebind `data` to a new list.
    - Do not mutate the original list.
    """
    raise NotImplementedError


def main() -> None:
    numbers = [1, 2, 3]

    mutate(numbers)

    print("After mutate:")
    print(numbers)

    rebind(numbers)

    print("\nAfter rebind:")
    print(numbers)


if __name__ == "__main__":
    main()
