# Lesson 02 — Variables and References

## Learning Goals

By the end of this lesson, you should be able to explain:

- What assignment means in Python
- What name binding means
- Why Python variables are better understood as names
- What rebinding means
- What aliasing means
- How multiple names can reference the same object
- The difference between mutation and rebinding
- How function arguments work
- Why "pass by reference" is an incomplete explanation
- What call-by-sharing means
- What shallow copy means
- What deep copy means
- When copying is useful
- Why mutable default arguments are dangerous
- How references affect OOP design

---

# 1. From Variables to Names

In many programming languages, we commonly imagine a variable as a box:

    variable
    ┌─────────┐
    │  value  │
    └─────────┘

Python is better understood using this model:

    name ───────────► object

For example:

    name = "Duy"

Think:

    name ───────────► "Duy"

The name is not the object.

The name is bound to the object.

This distinction becomes extremely important when working with:

- Mutable objects
- Function arguments
- Classes
- Object composition
- Copies
- Caches
- Shared state

---

# 2. Assignment Is Name Binding

Consider:

    x = 10

The important operation is:

    x ───────────► integer object 10

If we then write:

    x = 20

Python does not modify the integer `10`.

Instead, the name `x` is rebound:

    x ───────────► integer object 20

The original object `10` was not changed.

This is called **rebinding**.

---

# 3. Assignment Does Not Automatically Copy

Consider:

    numbers = [1, 2, 3]
    alias = numbers

There is only one list.

The object graph is:

    numbers ──────┐
                  ▼
              [1, 2, 3]
                  ▲
                  │
    alias ────────┘

Therefore:

    numbers is alias

returns:

    True

The assignment:

    alias = numbers

does not create a second list.

It creates another name bound to the same list object.

---

# 4. Aliasing

Aliasing means multiple names refer to the same object.

Example:

    user = {
        "name": "Duy"
    }

    account = user

Now:

    user ────────┐
                 ▼
             {"name": "Duy"}
                 ▲
                 │
    account ─────┘

If we execute:

    account["name"] = "Alice"

then:

    print(user["name"])

produces:

    Alice

Why?

Because both names refer to the same dictionary.

Aliasing is not inherently bad.

It becomes dangerous when shared mutable state is accidental or difficult to understand.

---

# 5. Mutation

Mutation means changing an existing object.

Example:

    numbers = [1, 2, 3]

    numbers.append(4)

The name still points to the same list.

Before:

    numbers ───► [1, 2, 3]

After:

    numbers ───► [1, 2, 3, 4]

The object changed.

Its identity did not.

We can demonstrate this:

    numbers = [1, 2, 3]

    original_id = id(numbers)

    numbers.append(4)

    print(original_id == id(numbers))

Result:

    True

---

# 6. Rebinding

Rebinding changes what a name refers to.

Example:

    numbers = [1, 2, 3]

    numbers = [1, 2, 3, 4]

The name is rebound to a new object.

Conceptually:

    Before:

    numbers ───► [1, 2, 3]


    After:

    numbers ───► [1, 2, 3, 4]

The original list was not modified by the assignment.

---

# 7. Mutation vs Rebinding

Compare:

    numbers = [1, 2, 3]

    numbers.append(4)

with:

    numbers = [1, 2, 3]

    numbers = numbers + [4]

The first mutates the existing list.

The second creates a new list and rebinds `numbers`.

This distinction can be observed using identity.

Example:

    numbers = [1, 2, 3]

    before = id(numbers)

    numbers.append(4)

    after = id(numbers)

    print(before == after)

Result:

    True

Now:

    numbers = [1, 2, 3]

    before = id(numbers)

    numbers = numbers + [4]

    after = id(numbers)

    print(before == after)

Result:

    False

---

# 8. Object Graphs

Python programs can be understood as object graphs.

Consider:

    user = {
        "name": "Duy",
        "roles": ["developer", "admin"],
    }

A simplified graph is:

    user
      │
      ▼
    dict
    ├── "name" ─────► "Duy"
    │
    └── "roles" ────► list
                       ├── "developer"
                       └── "admin"

The dictionary references the list.

The list is a separate object.

This model becomes extremely useful when working with:

- Nested data
- Object composition
- Serialization
- Copying
- Caching
- Graph structures
- Domain models

---

# 9. Function Arguments

Consider:

    def add_item(items: list[int]) -> None:
        items.append(4)


    numbers = [1, 2, 3]

    add_item(numbers)

Inside the function, the parameter `items` becomes a local name referring to the same list.

Conceptually:

    Caller:

    numbers ──────────┐
                      ▼
                   [1, 2, 3]
                      ▲
                      │
    items ────────────┘

Therefore:

    items.append(4)

mutates the same object referenced by `numbers`.

After the function call:

    print(numbers)

produces:

    [1, 2, 3, 4]

---

# 10. Python Is Not Simply "Pass by Reference"

You will often hear:

> Python passes objects by reference.

This is an incomplete explanation.

A more precise model is:

> Python uses call-by-sharing.

Function parameters are local names bound to the same objects supplied by the caller.

Consider:

    def replace(items: list[int]) -> None:
        items = [100, 200]


    numbers = [1, 2, 3]

    replace(numbers)

    print(numbers)

The result is:

    [1, 2, 3]

Why?

Because:

    items = [100, 200]

does not modify the original list.

It only rebinds the local name `items`.

Before rebinding:

    numbers ──────┐
                  ▼
               [1, 2, 3]
                  ▲
                  │
    items ────────┘

After rebinding:

    numbers ─────► [1, 2, 3]

    items ────────► [100, 200]

The caller's name `numbers` was never rebound.

---

# 11. Mutation Through a Function Boundary

Now compare:

    def mutate(items: list[int]) -> None:
        items.append(100)

with:

    def rebind(items: list[int]) -> None:
        items = [100, 200]

The first changes the shared object.

The second changes only the local binding.

This gives us a critical rule:

    Mutation
        ↓
    changes an object

    Rebinding
        ↓
    changes what a name refers to

---

# 12. Shallow Copy

Python provides:

    import copy

and:

    copy.copy(obj)

A shallow copy creates a new outer object.

Example:

    original = [1, 2, 3]

    clone = copy.copy(original)

Now:

    original ───► [1, 2, 3]

    clone ──────► [1, 2, 3]

The lists are different objects:

    original is clone

returns:

    False

For a flat list, this is usually straightforward.

---

# 13. Shallow Copy With Nested Objects

Consider:

    original = [
        ["Python", "Java"],
        ["Go", "Rust"],
    ]

Now:

    clone = copy.copy(original)

The outer list is copied.

The nested lists are still shared.

Conceptually:

    original ─────► outer list A
                      │
                      ├──► inner list X
                      └──► inner list Y


    clone ────────► outer list B
                      │
                      ├──► inner list X
                      └──► inner list Y

Therefore:

    original is clone

is:

    False

but:

    original[0] is clone[0]

is:

    True

---

# 14. Deep Copy

A deep copy recursively copies nested objects.

    clone = copy.deepcopy(original)

Conceptually:

    original ─────► outer A
                      │
                      ├──► inner X
                      └──► inner Y


    clone ────────► outer B
                      │
                      ├──► inner X'
                      └──► inner Y'

Now:

    original is clone

is:

    False

and:

    original[0] is clone[0]

is also:

    False

---

# 15. Assignment vs Shallow Copy vs Deep Copy

| Operation | New outer object | New nested objects |
|-----------|------------------|--------------------|
| Assignment | No | No |
| Shallow copy | Yes | No |
| Deep copy | Yes | Yes |

Assignment:

    a ───────┐
             ▼
          object
             ▲
             │
    b ───────┘

Shallow copy:

    a ───────► outer A
                  │
                  ▼
               nested X

    b ───────► outer B
                  │
                  ▼
               nested X

Deep copy:

    a ───────► outer A
                  │
                  ▼
               nested X

    b ───────► outer B
                  │
                  ▼
               nested Y

---

# 16. When Should You Copy?

Copying is not automatically a good design decision.

Before copying an object, ask:

1. Do I need independent state?
2. Is the object mutable?
3. Is sharing intentional?
4. Is a shallow copy sufficient?
5. Is deep copying actually necessary?
6. Is the object graph large?
7. Does the object contain external resources?
8. Would immutable data be a better design?

Deep copying can be expensive.

It can also hide an ownership problem in the design.

Prefer explicit ownership and clear APIs over blindly copying objects.

---

# 17. Mutable Default Arguments

Consider:

    def add_item(
        item: str,
        items: list[str] = [],
    ) -> list[str]:
        items.append(item)
        return items

This is a common Python pitfall.

The default list is created when the function is defined.

It is not created for every function call.

Therefore:

    first = add_item("Python")
    second = add_item("OOP")

can result in:

    ["Python", "OOP"]

for both calls.

The preferred pattern is:

    def add_item(
        item: str,
        items: list[str] | None = None,
    ) -> list[str]:
        if items is None:
            items = []

        items.append(item)
        return items

Now a new list is created whenever the argument is omitted.

---

# 18. References and OOP

These concepts become especially important when designing classes.

Consider:

    class Team:
        def __init__(self, members: list[str]) -> None:
            self.members = members

Then:

    members = ["Alice", "Bob"]

    team = Team(members)

    members.append("Charlie")

What is:

    team.members

It is:

    ["Alice", "Bob", "Charlie"]

The constructor did not automatically copy the list.

Instead:

    members ───────────┐
                       ▼
                    list object
                       ▲
                       │
    self.members ──────┘

This is why reference semantics are a prerequisite for understanding OOP.

---

# 19. Example — Name Binding

See:

    examples/name_binding.py

The example demonstrates:

- Assignment
- Rebinding
- Identity

Run it with:

    uv run python src/python_engineering_journey/fundamentals/variables_and_references/examples/name_binding.py

---

# 20. Example — Aliasing

See:

    examples/aliasing.py

The example demonstrates:

- Multiple names
- Shared objects
- Mutation

Run:

    uv run python src/python_engineering_journey/fundamentals/variables_and_references/examples/aliasing.py

---

# 21. Example — Rebinding

See:

    examples/rebinding.py

The example demonstrates:

- Aliasing
- Rebinding
- Identity changes

Run:

    uv run python src/python_engineering_journey/fundamentals/variables_and_references/examples/rebinding.py

---

# 22. Example — Function Arguments

See:

    examples/function_arguments.py

The example compares:

- Mutation through a function
- Rebinding a function parameter

Run:

    uv run python src/python_engineering_journey/fundamentals/variables_and_references/examples/function_arguments.py

---

# 23. Example — Shallow Copy

See:

    examples/shallow_copy.py

The example demonstrates why nested objects can remain shared after a shallow copy.

Run:

    uv run python src/python_engineering_journey/fundamentals/variables_and_references/examples/shallow_copy.py

---

# 24. Example — Deep Copy

See:

    examples/deep_copy.py

The example demonstrates recursive copying of nested structures.

Run:

    uv run python src/python_engineering_journey/fundamentals/variables_and_references/examples/deep_copy.py

---

# 25. Exercise 01 — Predict the Object Graph

Create:

    exercises/exercise_01.py

Given:

    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

Before running the program, predict:

    a is b
    a is c
    a == b
    a == c

Then execute:

    b.append(4)

Predict:

    print(a)
    print(b)
    print(c)

Your explanation must use:

- Name
- Object
- Identity
- Equality
- Aliasing
- Mutation

Do not simply write the output.

Draw the object graph.

---

# 26. Exercise 02 — Mutation vs Rebinding

Implement:

    def mutate(data: list[int]) -> None:
        ...


    def rebind(data: list[int]) -> None:
        ...

Expected behavior:

    numbers = [1, 2, 3]

    mutate(numbers)

    assert numbers == [1, 2, 3, 4]

    rebind(numbers)

    assert numbers == [1, 2, 3, 4]

The first function must mutate the existing object.

The second must only rebind the local name.

---

# 27. Exercise 03 — Copy Strategy

Given:

    configuration = {
        "database": {
            "host": "localhost",
            "port": 5432,
        },
        "features": [
            "logging",
            "metrics",
        ],
    }

Create:

1. An alias
2. A shallow copy
3. A deep copy

Then compare identity between:

- The outer dictionaries
- The nested database dictionaries
- The features lists

Document your observations in comments.

---

# 28. Challenge — Object Graph Detective

Consider:

    users = [
        {
            "name": "Alice",
            "roles": ["admin"],
        }
    ]

    backup = users.copy()

Draw the complete object graph.

Then execute:

    backup[0]["roles"].append("developer")

Predict:

    print(users)
    print(backup)

Explain why both structures contain `"developer"`.

---

# 29. Challenge — Function Boundary

Investigate:

    def update_user(user: dict[str, object]) -> None:
        user["active"] = True


    def replace_user(user: dict[str, object]) -> None:
        user = {
            "name": "New User",
            "active": False,
        }


    user = {
        "name": "Duy",
        "active": False,
    }

    update_user(user)

    print(user)

    replace_user(user)

    print(user)

Explain:

1. Why `update_user()` changes the caller's object
2. Why `replace_user()` does not replace the caller's object
3. What happened to the local name `user`
4. Why this behavior is consistent with call-by-sharing

---

# 30. Common Misconceptions

## Misconception 1

> Assignment copies the object.

Not necessarily.

    a = b

normally creates another binding to the same object.

---

## Misconception 2

> Python passes everything by reference.

This is an oversimplification.

A better explanation is:

> Python uses call-by-sharing.

---

## Misconception 3

> Reassigning a function parameter changes the caller's variable.

It does not.

The parameter is a local name.

---

## Misconception 4

> A shallow copy makes everything independent.

It only creates a new outer object.

Nested mutable objects can still be shared.

---

## Misconception 5

> Deep copy is always safer.

It is not.

Deep copying can be expensive and can hide poor ownership design.

---

# 31. Engineering Perspective

These concepts directly affect API and class design.

When designing a function or class, ask:

### Ownership

Who owns this object?

### Sharing

Should this object be shared?

### Mutation

Who is allowed to mutate it?

### Copying

Should it be copied?

### API Contract

Does the function intentionally mutate its input?

For example:

    def add_user(users: list[str], user: str) -> None:
        users.append(user)

has a mutation-oriented API.

While:

    def add_user(users: list[str], user: str) -> list[str]:
        return [*users, user]

creates and returns a new list.

Neither strategy is universally correct.

The engineering decision depends on:

- Ownership
- Performance
- API expectations
- Mutability
- Concurrency
- Maintainability

---

# 32. Reflection

Answer these questions without looking at the previous sections.

### Question 1

What does this do?

    a = b

### Question 2

What is aliasing?

### Question 3

What is mutation?

### Question 4

What is rebinding?

### Question 5

Why can mutation affect another variable?

### Question 6

Why does rebinding a function parameter not change the caller's name?

### Question 7

What does shallow copy copy?

### Question 8

What does deep copy copy?

### Question 9

Why is "pass by reference" incomplete when explaining Python?

### Question 10

What does call-by-sharing mean?

---

# 33. Key Takeaways

The core mental model is:

    Name
      │
      │ binds to
      ▼
    Object

Multiple names can reference the same object:

    name_a ──────┐
                 ▼
               Object
                 ▲
                 │
    name_b ──────┘

Mutation changes the object.

Rebinding changes what a name refers to.

Assignment does not automatically create a copy.

Shallow copy creates a new outer object but can share nested objects.

Deep copy recursively copies nested objects.

The most important principle is:

> Always distinguish between changing an object and changing what a name refers to.

---

# 34. Definition of Done

- [ ] Explain assignment as name binding
- [ ] Explain rebinding
- [ ] Explain mutation
- [ ] Explain aliasing
- [ ] Draw object graphs
- [ ] Explain function argument behavior
- [ ] Explain call-by-sharing
- [ ] Explain shallow copy
- [ ] Explain deep copy
- [ ] Explain mutable default arguments
- [ ] Complete all exercises
- [ ] Complete the Object Graph Detective challenge
- [ ] Explain mutation vs rebinding without relying on "pass by reference"

---

# 35. Next Lesson

## Lesson 03 — Mutability and Immutability

Topics:

- Mutable objects
- Immutable objects
- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `frozenset`
- `list`
- `dict`
- `set`
- Hashability
- Dictionary keys
- Set members
- Nested mutable structures
- Defensive copying
- Immutable design
- Practical API design

The key question:

> What does it actually mean for a Python object to be mutable?
