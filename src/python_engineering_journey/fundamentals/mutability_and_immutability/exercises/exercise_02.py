"""Exercise 02: Immutable updates.

Implement add_permission() and make_point() according to their contracts.

The key idea: instead of mutating a shared object, produce a new immutable
object and leave the original untouched.

Do not change the tests or expected behavior.
"""


def add_permission(permissions: frozenset[str], permission: str) -> frozenset[str]:
    """Return a new frozenset that also contains ``permission``.

    Requirements:
    - Do not attempt to mutate ``permissions`` (a frozenset is immutable).
    - Return a *new* frozenset containing every original permission plus the
      new one.
    - The original ``permissions`` must remain unchanged.
    """
    raise NotImplementedError


def make_point(x: int, y: int) -> tuple[int, int]:
    """Return an immutable, hashable point usable as a dictionary key.

    Requirements:
    - The result must be hashable (so it can be used as a dict key).
    - Two calls with equal coordinates must compare equal.
    """
    raise NotImplementedError


def main() -> None:
    roles = frozenset({"read"})

    updated = add_permission(roles, "write")

    print("original:", roles)
    print("updated: ", updated)

    grid = {make_point(0, 0): "origin"}

    print("lookup:", grid[make_point(0, 0)])


if __name__ == "__main__":
    main()
