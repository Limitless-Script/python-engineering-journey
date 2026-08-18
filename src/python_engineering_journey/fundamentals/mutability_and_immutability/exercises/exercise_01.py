"""Exercise 01: Predict mutability and identity.

Before running the program, predict the result of each expression.

For every mutation, decide whether the object's identity (id) will stay
the same or change, and explain why using the words:

- Mutable
- Immutable
- Identity
- Rebinding

Then run the program and compare your prediction with the actual result.
"""


def main() -> None:
    numbers = [1, 2, 3]
    total = 0

    print("Initial identities")
    print("id(numbers):", id(numbers))
    print("id(total): ", id(total))

    numbers.append(4)
    total += 10

    print("\nAfter numbers.append(4) and total += 10")
    print("numbers:", numbers)
    print("total: ", total)
    print("id(numbers):", id(numbers))
    print("id(total): ", id(total))

    text = "duy"

    print("\nStrings are immutable")
    print("id(text):", id(text))

    text = text.upper()

    print("text:", text)
    print("id(text):", id(text))


if __name__ == "__main__":
    main()
