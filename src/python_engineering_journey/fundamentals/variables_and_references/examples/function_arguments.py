def mutate(items: list[int]) -> None:
    """Mutate the object referenced by items."""
    items.append(4)


def rebind(items: list[int]) -> None:
    """Rebind the local name items."""
    items = [100, 200]

    print("Inside rebind:")
    print("items:", items)


numbers = [1, 2, 3]

print("Before mutate:")
print("numbers:", numbers)

mutate(numbers)

print("\nAfter mutate:")
print("numbers:", numbers)

rebind(numbers)

print("\nAfter rebind:")
print("numbers:", numbers)
