"""Exercise 01: Predict the object graph.

Before running the program, predict the result of each expression.

Then run the program and compare your prediction with the actual result.
"""


def main() -> None:
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print("Initial state")
    print("a is b:", a is b)
    print("a is c:", a is c)
    print("a == b:", a == b)
    print("a == c:", a == c)

    print("\nAfter b.append(4)")

    b.append(4)

    print("a:", a)
    print("b:", b)
    print("c:", c)

    print("\nIdentity")
    print("a is b:", a is b)
    print("a is c:", a is c)


if __name__ == "__main__":
    main()
