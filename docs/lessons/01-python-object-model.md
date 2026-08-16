# Lesson 01 — Python Object Model

## Learning Goals

By the end of this lesson, you should be able to explain:

* What an object is in Python
* What a variable/name is
* The difference between identity and equality
* What `id()` represents
* What `type()` represents
* Why `is` and `==` are different
* Why Python can treat functions and classes as objects
* How names reference objects
* How object identity affects program behavior

---

# 1. Everything Is an Object

One of the most important ideas in Python is:

> Everything in Python is an object.

Consider:

```python
x = 42
```

It is tempting to think:

```text
x → 42
```

A better mental model is:

```text
x ───────► integer object
           value: 42
           type: int
           identity: ...
```

The name `x` is not the object itself.

`x` is a **name bound to an object**.

This distinction becomes extremely important when learning:

* Variables
* Function arguments
* Mutable objects
* Immutable objects
* Classes
* Inheritance
* Decorators
* Descriptors
* Metaclasses

---

# 2. Objects Have Identity, Type, and Value

Every Python object can be understood through three properties:

```text
Object
├── Identity
├── Type
└── Value
```

## 2.1 Identity

Identity answers:

> Is this the exact same object?

Python exposes an object's identity through:

```python
id(obj)
```

Example:

```python
x = 42

print(id(x))
```

The exact number returned by `id()` is not important.

What matters is the concept:

> An object has an identity that distinguishes it from other objects during its lifetime.

---

## 2.2 Type

Every object has a type.

```python
x = 42

print(type(x))
```

Output:

```text
<class 'int'>
```

The type determines the object's behavior and the operations available to it.

For example:

```python
x = 42

print(x + 10)
```

works because `x` is an `int`.

Another example:

```python
message = "hello"

print(message.upper())
```

works because `message` is a `str`.

---

## 2.3 Value

The value represents the data associated with an object.

For example:

```python
x = 42
```

Conceptually:

```text
Identity → some object
Type     → int
Value    → 42
```

Another object:

```python
name = "Duy"
```

can be viewed as:

```text
Identity → some object
Type     → str
Value    → "Duy"
```

---

# 3. Names and Objects

Consider:

```python
x = 10
y = x
```

A common beginner mental model is:

```text
x = 10
y = 10
```

A better mental model is:

```text
      ┌─────────────┐
x ───►│             │
      │ int object  │
y ───►│ value = 10  │
      │             │
      └─────────────┘
```

Both `x` and `y` refer to the same object.

We can verify this:

```python
x = 10
y = x

print(x == y)
print(x is y)
```

The result may be:

```text
True
True
```

The important distinction is:

```text
==  → equality
is  → identity
```

---

# 4. Equality vs Identity

This is one of the most important distinctions in Python.

## 4.1 Equality

When we write:

```python
a == b
```

we are asking:

> Do these objects represent equivalent values?

Example:

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first == second)
```

Output:

```text
True
```

The two lists contain the same values.

---

## 4.2 Identity

When we write:

```python
a is b
```

we are asking:

> Are `a` and `b` references to the exact same object?

Example:

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first is second)
```

Output:

```text
False
```

The objects have the same value, but they are different objects.

Conceptually:

```text
first ───────► [1, 2, 3]

second ──────► [1, 2, 3]
```

There are two different list objects.

---

# 5. `is` vs `==`

Consider:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

Why?

Because:

```text
a == b
```

asks about **value equality**.

While:

```text
a is b
```

asks about **object identity**.

A useful mental model is:

```text
==

"What do these objects contain?"
```

versus:

```text
is

"Are these literally the same object?"
```

---

# 6. When Should You Use `is`?

The most common use of `is` is checking against singleton objects.

The most important example is `None`.

Use:

```python
if value is None:
    ...
```

Do not use:

```python
if value == None:
    ...
```

Similarly:

```python
if value is not None:
    ...
```

This is the idiomatic Python approach.

---

# 7. Why `is` Should Not Replace `==`

Consider:

```python
user_input = "admin"
```

Do not write:

```python
if user_input is "admin":
    print("Welcome")
```

Use:

```python
if user_input == "admin":
    print("Welcome")
```

Why?

Because the requirement is:

> Does the value equal `"admin"`?

It is not:

> Is this the exact same string object as `"admin"`?

Identity and equality are different concepts.

---

# 8. Everything Is an Object

Let's inspect different Python values:

```python
number = 42
message = "Hello"
items = [1, 2, 3]
coordinates = (10, 20)
config = {"debug": True}
```

We can inspect their types:

```python
print(type(number))
print(type(message))
print(type(items))
print(type(coordinates))
print(type(config))
```

We get:

```text
<class 'int'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
```

All of them are objects.

But Python goes further.

Functions are objects too.

Classes are objects too.

---

# 9. Functions Are Objects

Consider:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

The function itself is an object.

We can inspect it:

```python
print(type(greet))
print(id(greet))
```

We can assign it to another name:

```python
say_hello = greet
```

Now:

```python
print(say_hello("Duy"))
```

Output:

```text
Hello, Duy
```

Both names reference the same function object:

```python
print(greet is say_hello)
```

Output:

```text
True
```

Conceptually:

```text
greet ────────┐
              │
              ▼
       ┌──────────────┐
       │ function     │
       │ greet(...)   │
       └──────────────┘
              ▲
              │
say_hello ────┘
```

This idea is fundamental to understanding:

* Higher-order functions
* Decorators
* Callbacks
* Closures
* Functional programming techniques

---

# 10. Classes Are Objects Too

Consider:

```python
class User:
    pass
```

We normally think:

```text
User → class
```

But the class itself is also an object.

Try:

```python
print(type(User))
```

You will get:

```text
<class 'type'>
```

This may look strange at first.

We will not dive deeply into metaclasses yet.

For now, remember:

> A class is itself an object.

This becomes extremely important later when studying:

* `type`
* Metaclasses
* Descriptors
* Class creation
* `__new__`
* `__init_subclass__`

---

# 11. Objects Can Be Inspected

Python provides several built-in tools for introspection.

Important functions include:

```python
type(obj)
id(obj)
dir(obj)
isinstance(obj, SomeType)
issubclass(SomeClass, SomeBaseClass)
```

Example:

```python
name = "Python"

print(type(name))
print(id(name))
print(dir(name))
```

`dir()` shows many attributes and methods available on an object.

For example:

```python
message = "hello"

print(message.upper())
print(message.lower())
print(message.replace("h", "H"))
```

You can inspect the available behavior with:

```python
print(dir(message))
```

However:

> `dir()` is a discovery tool, not a replacement for documentation.

---

# 12. `type()` and `isinstance()`

Consider:

```python
value = 42
```

You can inspect the exact type:

```python
print(type(value))
```

You can also ask whether an object is an instance of a particular type:

```python
print(isinstance(value, int))
```

Output:

```text
True
```

In application code, `isinstance()` is often more useful than directly comparing types.

For example:

```python
if isinstance(value, int):
    print("value is an integer")
```

We will revisit this when discussing:

* Inheritance
* Polymorphism
* Protocols
* Duck typing

---

# 13. A Better Mental Model

When reading Python code, try to think in terms of:

```text
Names
  │
  ▼
Objects
  │
  ├── Identity
  ├── Type
  └── Value
```

Instead of thinking:

```text
variable = box containing value
```

Think:

> A name is bound to an object.

For example:

```python
user = User("duy")
```

A useful mental model is:

```text
user ───────────────► User object
                       │
                       ├── identity
                       ├── type
                       └── state
                           username = "duy"
```

This model will become increasingly important as we learn OOP.

---

# 14. Object Lifetime

Objects have a lifetime.

Conceptually:

```text
Object created
      │
      ▼
Object exists
      │
      ▼
References disappear
      │
      ▼
Object can be reclaimed
```

Python uses automatic memory management.

For example:

```python
user = User("duy")
```

creates an object and binds the name `user` to it.

If the object is no longer reachable, Python can eventually reclaim its memory.

The exact implementation details depend on the Python implementation.

For CPython, reference counting plays an important role, together with garbage collection for reference cycles.

Do not rely on object destruction happening at an exact moment.

---

# 15. Names Are Not Boxes

This distinction is important.

In some programming languages, developers commonly visualize:

```text
variable
┌─────────┐
│ value   │
└─────────┘
```

Python is better understood as:

```text
name ─────────► object
```

For example:

```python
a = [1, 2, 3]
b = a
```

Think:

```text
a ───────┐
         ▼
      [1, 2, 3]
         ▲
         │
b ───────┘
```

Not:

```text
a = [1, 2, 3]
b = [1, 2, 3]
```

This difference becomes critical when we study mutable objects.

---

# 16. Example — Everything Is an Object

Create:

```text
src/python_engineering_journey/fundamentals/python_object_model/examples/everything_is_object.py
```

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


number = 42
message = "Hello"
items = [1, 2, 3]


def describe(name: str, obj: object) -> None:
    print(f"{name}:")
    print(f"  value    = {obj!r}")
    print(f"  type     = {type(obj)}")
    print(f"  id       = {id(obj)}")
    print()


describe("number", number)
describe("message", message)
describe("items", items)
describe("greet", greet)
```

Run:

```bash
uv run python src/python_engineering_journey/fundamentals/python_object_model/examples/everything_is_object.py
```

Focus on:

```text
number → int object
message → str object
items → list object
greet → function object
```

The exact `id()` values are not important.

---

# 17. Example — Identity vs Equality

Create:

```text
src/python_engineering_journey/fundamentals/python_object_model/examples/identity_and_type.py
```

```python
first = [1, 2, 3]
second = [1, 2, 3]
third = first

print("first == second:", first == second)
print("first is second:", first is second)

print("first == third:", first == third)
print("first is third:", first is third)
```

Expected result:

```text
first == second: True
first is second: False
first == third: True
first is third: True
```

Mental model:

```text
first ────────┐
              ▼
          [1, 2, 3]

second ─────► [1, 2, 3]
```

Two separate list objects.

While:

```text
first ────────┐
              ▼
          [1, 2, 3]
              ▲
              │
third ────────┘
```

`first` and `third` refer to the same object.

---

# 18. Example — Object Introspection

Create:

```text
src/python_engineering_journey/fundamentals/python_object_model/examples/object_introspection.py
```

```python
class User:
    def __init__(self, username: str) -> None:
        self.username = username

    def greet(self) -> str:
        return f"Hello, {self.username}"


user = User("duy")

print("Object:", user)
print("Type:", type(user))
print("Identity:", id(user))
print("Is User:", isinstance(user, User))
print("Attributes and methods:")

for name in dir(user):
    print(f"  - {name}")
```

Run:

```bash
uv run python src/python_engineering_journey/fundamentals/python_object_model/examples/object_introspection.py
```

Observe:

```python
type(user)
```

returns the `User` class.

Also observe:

```python
type(User)
```

returns:

```text
<class 'type'>
```

Do not worry about metaclasses yet.

Just record this observation for a later lesson.

---

# 19. Exercise 01 — Names and Objects

Create:

```text
src/python_engineering_journey/fundamentals/python_object_model/exercises/exercise_01.py
```

Given:

```python
numbers = [1, 2, 3]

alias = numbers

copy = [1, 2, 3]
```

Answer the following questions by writing Python code:

1. Which objects are equal?
2. Which names refer to the same object?
3. Compare:

   * `numbers == alias`
   * `numbers is alias`
   * `numbers == copy`
   * `numbers is copy`
4. Print the identity of each object.
5. Explain the result in comments.

Before running the code, predict the results.

Then run the program and compare your prediction with the actual result.

---

# 20. Exercise 02 — Function Objects

Create a function:

```python
def calculate_tax(amount: float) -> float:
    return amount * 0.1
```

Then:

1. Print its type.
2. Print its identity.
3. Assign it to another name.
4. Check whether both names refer to the same object.
5. Call the function through the second name.

Expected conceptual model:

```text
calculate_tax ──────┐
                    ▼
              function object
                    ▲
                    │
tax ────────────────┘
```

---

# 21. Exercise 03 — Class Objects

Create:

```python
class Customer:
    pass
```

Investigate:

```python
type(Customer)
id(Customer)
isinstance(Customer, object)
```

Then create:

```python
customer = Customer()
```

Compare:

```python
type(Customer)
type(customer)
```

Questions:

1. Is `Customer` an object?
2. Is `customer` an object?
3. Are they the same object?
4. What is the relationship between `Customer` and `customer`?
5. What is the type of `Customer`?
6. What is the type of `customer`?

Do not research metaclasses yet.

Record your observations first.

---

# 22. Tests

Create:

```text
tests/fundamentals/python_object_model/test_object_model.py
```

```python
def test_aliases_reference_the_same_object() -> None:
    numbers = [1, 2, 3]
    alias = numbers

    assert alias is numbers


def test_separate_objects_can_be_equal() -> None:
    first = [1, 2, 3]
    second = [1, 2, 3]

    assert first == second
    assert first is not second


def test_functions_are_objects() -> None:
    def greet() -> str:
        return "hello"

    assert isinstance(greet, object)


def test_classes_are_objects() -> None:
    class User:
        pass

    assert isinstance(User, object)


def test_instance_has_expected_type() -> None:
    class User:
        pass

    user = User()

    assert type(user) is User
    assert isinstance(user, User)
```

Run:

```bash
uv run pytest
```

---

# 23. Challenge — Object Detective

Before running the following code, predict the result:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

b.append(4)
```

Answer:

1. What is the value of `a`?
2. What is the value of `b`?
3. What is the value of `c`?
4. Which objects are identical?
5. Which objects are equal?

Then investigate:

```python
print(a is b)
print(a is c)
print(a == c)
```

Explain why.

---

# 24. Advanced Challenge — Function Arguments

Investigate:

```python
def add_item(items: list[int]) -> None:
    items.append(100)


numbers = [1, 2, 3]

add_item(numbers)

print(numbers)
```

Why was `numbers` changed?

Do not simply answer:

> Python passes lists by reference.

That explanation is incomplete.

Try to explain what actually happened in terms of:

* Names
* Objects
* References
* Function arguments
* Mutation

We will revisit this deeply in the next lessons.

---

# 25. Reflection

Before moving to the next lesson, answer these questions without looking at the theory.

### Question 1

Is a variable an object?

### Question 2

What does `is` compare?

### Question 3

What does `==` compare?

### Question 4

Are two equal objects necessarily the same object?

### Question 5

What does it mean when we say:

> Everything is an object in Python?

### Question 6

What is the difference between:

```python
x = 10
```

and:

```python
x = [1, 2, 3]
```

from the perspective of names and objects?

### Question 7

Why is this:

```python
value is None
```

preferred over:

```python
value == None
```

---

# 26. Key Takeaways

The most important ideas from this lesson are:

```text
1. Python programs work with objects.

2. Names are bound to objects.

3. Objects have:
   - identity
   - type
   - value

4. `==` checks equality.

5. `is` checks identity.

6. Two objects can have equal values without being the same object.

7. Multiple names can refer to the same object.

8. Functions are objects.

9. Classes are objects.

10. Understanding objects and references is essential for understanding OOP.
```

The most important mental model to carry forward is:

```text
        Name
          │
          │ references / binds to
          ▼
       Object
       ┌───────┐
       │       │
       │ value │
       │ type  │
       │ id    │
       │       │
       └───────┘
```

---

# 27. Further Questions

Do not solve these yet. Keep them as questions for future lessons.

### Question 1

If two variables reference the same mutable object, what happens when one variable mutates it?

### Question 2

Why can immutable objects behave differently from mutable objects?

### Question 3

What exactly happens when an object is passed to a function?

### Question 4

Why does this work?

```python
def greet():
    return "hello"


functions = [greet]
```

### Question 5

Why is a class itself an object?

### Question 6

If a class is an object, what is its type?

### Question 7

Who creates the class object?

These questions lead naturally into later topics such as:

```text
References
Mutation
Function arguments
Classes
Inheritance
Descriptors
Metaclasses
```

---

# 28. Definition of Done

This lesson is complete when you can:

* [ ] Explain what an object is
* [ ] Explain what a name is
* [ ] Explain identity
* [ ] Explain type
* [ ] Explain value
* [ ] Explain `id()`
* [ ] Explain `type()`
* [ ] Explain `is`
* [ ] Explain `==`
* [ ] Explain why `is None` is idiomatic
* [ ] Explain why functions are objects
* [ ] Explain why classes are objects
* [ ] Draw a simple object-reference diagram
* [ ] Complete all exercises
* [ ] Complete the Object Detective challenge
* [ ] Explain function argument behavior without saying only "pass by reference"

---

# 29. Next Lesson

After completing this lesson:

**Lesson 02 — Variables and References**

Topics:

* Namespaces
* Name binding
* Assignment
* Multiple references
* Rebinding
* Aliasing
* Shallow copy
* Deep copy
* Function arguments
* `copy.copy()`
* `copy.deepcopy()`
* Object graphs

The key question will be:

> What exactly happens when Python executes an assignment?
