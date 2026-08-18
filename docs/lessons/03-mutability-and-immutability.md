# Lesson 03 — Mutability and Immutability

## Learning Goals

By the end of this lesson, you should be able to explain:

- What it means for an object to be mutable
- What it means for an object to be immutable
- Which built-in types are mutable and which are immutable
- Why mutation preserves identity but rebinding does not
- Why integers and strings feel immutable
- Why immutability in Python is shallow, not deep
- What hashability means
- Why immutability enables hashing
- Why dictionary keys must be hashable
- Why set members must be hashable
- Why a tuple is only conditionally hashable
- What `frozenset` is for
- What defensive copying protects against
- How immutability shapes API and class design
- When to choose a mutable versus an immutable interface

---

# 1. What Mutability Means

An object is **mutable** if its internal state can change after it is created,
while keeping the same identity.

An object is **immutable** if its state can never change after creation.

The crucial phrase is *the same identity*.

    mutable:    same object, new state
    immutable:  new state means a new object

Mutability is a property of the **object**, not of the name that refers to it.

---

# 2. Identity Is the Test

Recall from Lesson 01 that every object has an identity, available through
`id()`.

The reliable test for "did I change the object, or did I create a new one?" is:

    Did id() stay the same?

Consider a list:

    numbers = [1, 2, 3]
    numbers.append(4)

The object graph never changes shape:

    numbers ──────► [1, 2, 3, 4]   (same id)

Now consider an integer:

    counter = 10
    counter += 1

This does not modify the object `10`. It creates the object `11` and rebinds
the name:

    counter ──────► 10      (before)
    counter ──────► 11      (after, different id)

The list was **mutated**. The integer was **rebound**.

See `examples/identity_under_mutation.py`.

---

# 3. The Immutable Types

The core immutable built-in types are:

- `int`
- `float`
- `bool`
- `str`
- `bytes`
- `tuple`
- `frozenset`

Any operation that appears to "change" one of these actually produces a new
object:

    text = "duy"
    text = text.upper()   # a new string, not an edit

`str.upper()` returns a new string. The original `"duy"` is untouched.

---

# 4. The Mutable Types

The core mutable built-in types are:

- `list`
- `dict`
- `set`
- `bytearray`

These provide methods that change the object in place:

    numbers = [1, 2, 3]
    numbers.append(4)     # in place

    config = {"debug": False}
    config["debug"] = True  # in place

    tags = {"a"}
    tags.add("b")           # in place

No new object is created. The identity is preserved.

---

# 5. Rebinding Is Not Mutation

This is the single most common source of confusion.

    x = [1, 2, 3]
    x = [1, 2, 3, 4]

The second line does **not** mutate the first list. It creates a brand new list
and rebinds the name `x` to it. The first list may now be unreferenced and
garbage-collected.

Compare with:

    x = [1, 2, 3]
    x.append(4)

Here the same list object is mutated in place.

    rebinding:  name points at a different object
    mutation:   the object itself changes

Immutability restricts mutation. It never restricts rebinding, because
rebinding is a property of the name, not the object.

---

# 6. Why Integers and Strings Feel Immutable

Beginners often say "I changed the number":

    total = 0
    total = total + 5

But `total + 5` evaluates to a new integer object, and `total` is rebound to
it. The integer `0` was never modified.

Because you almost always use `int` and `str` through rebinding, their
immutability is invisible in everyday code. It only becomes visible when you
try to mutate them directly:

    text = "duy"
    text[0] = "D"     # TypeError: 'str' object does not support item assignment

---

# 7. Immutability Is Shallow

An immutable container freezes **its own references**, not the objects those
references point to.

A tuple cannot be reassigned:

    point = (1, 2)
    point[0] = 99     # TypeError

But a tuple can hold a mutable object, and that object can still change:

    record = ("config", ["logging", "metrics"])
    record[1].append("tracing")

    record is now ("config", ["logging", "metrics", "tracing"])

The tuple still points to the same list. The tuple did not change; the list
inside it did.

    record ──► ( "config", ● )
                          │
                          ▼
                   ["logging", "metrics", "tracing"]   (mutable)

"Immutable" means the container's own slots are fixed, not that the whole
object graph beneath it is frozen.

See `examples/tuple_shallow_immutability.py`.

---

# 8. Hashability

An object is **hashable** if it has a hash value that never changes during its
lifetime, exposed through `hash()`.

    hash(42)
    hash("duy")
    hash((1, 2))

Hashability requires two things that must stay consistent for the object's
whole life:

- A `__hash__` result
- An `__eq__` result

If two objects are equal, they must have the same hash.

See `examples/hashability.py`.

---

# 9. Why Immutability Enables Hashing

Hash-based containers (`dict`, `set`) place an object into a bucket chosen by
its hash value.

If an object's hash could change after it was stored, the container would look
in the wrong bucket and lose the object.

    stored using hash H1
    object mutates, hash becomes H2
    lookup computes H2 → wrong bucket → not found

To prevent this, hash-based containers only accept **hashable** objects, and
mutable built-in types deliberately make themselves unhashable:

    hash([1, 2, 3])   # TypeError: unhashable type: 'list'

Immutability is what makes a stable hash possible.

---

# 10. Dictionary Keys Must Be Hashable

A dictionary key must be hashable, because the dictionary stores entries by the
hash of the key.

Valid keys:

    {("Hanoi", "Hue"): 668}     # tuple of immutables
    {"user_id": 1}              # str
    {frozenset({"admin"}): 1}   # frozenset

Invalid keys:

    {["Hanoi", "Hue"]: 668}     # TypeError: unhashable type: 'list'

See `examples/dict_keys_and_set_members.py`.

---

# 11. Set Members Must Be Hashable

A set is a hash-based collection, so every member must be hashable for the same
reason keys must be:

    {("py", 3), ("py", 2)}      # fine
    {["py", 3]}                 # TypeError: unhashable type: 'list'

This is why you can build a set of tuples but not a set of lists.

---

# 12. Tuples Are Conditionally Hashable

A tuple is hashable **only if all of its elements are hashable**, because a
tuple computes its hash from the hashes of its contents.

    hash((1, 2))        # fine
    hash((1, [2, 3]))   # TypeError: unhashable type: 'list'

So a tuple is not automatically a valid dictionary key. It is a valid key only
when everything inside it is also immutable and hashable.

---

# 13. frozenset

A `frozenset` is the immutable, hashable version of a `set`.

    roles = frozenset({"admin", "editor"})

Because it is hashable, a `frozenset` can be used where a `set` cannot:

- As a dictionary key
- As a member of another set

    permissions = {
        frozenset({"admin"}): "full-access",
        frozenset({"editor", "viewer"}): "read-write",
    }

Use `frozenset` when you need set semantics (unordered, unique members) plus
hashability.

See `examples/frozenset_demo.py`.

---

# 14. Nested Mutable Structures

Real programs rarely use flat data. They use dictionaries of lists, lists of
dictionaries, and deeper graphs.

    account = {
        "name": "Duy",
        "roles": ["admin", "editor"],
    }

The outer dictionary is mutable. The inner list is mutable. Sharing either one
means a caller can change your state from a distance.

This connects directly to Lesson 02: assignment and shallow copy share nested
objects; only a deep copy fully separates them.

---

# 15. The Leaking Reference Problem

Suppose a class stores a list it was handed:

    class Playlist:
        def __init__(self, songs: list[str]) -> None:
            self._songs = songs

    source = ["Song A", "Song B"]
    playlist = Playlist(source)

    source.append("Song C")

Now `playlist._songs` also contains `"Song C"`, because `self._songs` and
`source` are the same list.

    source ───────┐
                  ▼
            ["Song A", "Song B", "Song C"]
                  ▲
                  │
    self._songs ──┘

The object's private state leaked because it shared a reference with the
outside world.

---

# 16. Defensive Copying On the Way In

The fix is to store a copy, so the object owns its own list:

    class Playlist:
        def __init__(self, songs: list[str]) -> None:
            self._songs = list(songs)   # defensive copy

Now the caller's later mutations cannot reach into the object:

    source ──► ["Song A", "Song B", "Song C"]
    self._songs ──► ["Song A", "Song B"]     (independent)

This is called **defensive copying**: copy at the boundary so ownership is
unambiguous.

See `examples/defensive_copy.py`.

---

# 17. Defensive Copying On the Way Out

Leaks can also happen in the other direction. If a getter returns the internal
list directly, callers can mutate private state:

    def get_songs(self) -> list[str]:
        return self._songs          # leaks internal state

    exported = playlist.get_songs()
    exported.append("Song Z")       # mutates the playlist!

Returning a copy closes the hole:

    def get_songs(self) -> list[str]:
        return list(self._songs)    # safe

A well-encapsulated object copies mutable state both when it accepts it and
when it hands it back.

---

# 18. Immutable Design

Defensive copying protects mutable state. Another strategy is to avoid mutable
shared state altogether by preferring immutable objects.

Instead of mutating a shared collection:

    def add_permission(permissions: set[str], permission: str) -> None:
        permissions.add(permission)   # mutates a shared set

produce a new immutable value and leave the input untouched:

    def add_permission(
        permissions: frozenset[str], permission: str
    ) -> frozenset[str]:
        return permissions | {permission}   # new frozenset

Immutable values are safe to share freely, because no one can change them out
from under you. This is why immutability simplifies caching, concurrency, and
reasoning about code.

---

# 19. Choosing Mutable or Immutable APIs

Neither style is universally correct.

A mutable, in-place API:

    def append_tag(tags: list[str], tag: str) -> None:
        tags.append(tag)

- Efficient (no copying)
- Requires clear ownership
- Easy to misuse across boundaries

An immutable, value-returning API:

    def with_tag(tags: tuple[str, ...], tag: str) -> tuple[str, ...]:
        return (*tags, tag)

- Safe to share
- No spooky action at a distance
- Allocates a new object each time

The engineering decision depends on:

- Ownership
- Performance
- Concurrency
- API expectations
- How widely the object is shared

---

# 20. Example — Identity Under Mutation

See:

    examples/identity_under_mutation.py

The example demonstrates:

- Mutation keeps the same `id`
- Rebinding produces a new `id`

Run:

    uv run python src/python_engineering_journey/fundamentals/mutability_and_immutability/examples/identity_under_mutation.py

---

# 21. Example — Shallow Immutability of Tuples

See:

    examples/tuple_shallow_immutability.py

The example demonstrates that a tuple freezes its own slots but not the mutable
objects it references.

Run:

    uv run python src/python_engineering_journey/fundamentals/mutability_and_immutability/examples/tuple_shallow_immutability.py

---

# 22. Example — Hashability

See:

    examples/hashability.py

The example demonstrates which objects are hashable and why hashing a list,
dict, set, or list-containing tuple raises `TypeError`.

Run:

    uv run python src/python_engineering_journey/fundamentals/mutability_and_immutability/examples/hashability.py

---

# 23. Example — Dictionary Keys and Set Members

See:

    examples/dict_keys_and_set_members.py

The example demonstrates why immutable values work as keys and members while
mutable values do not.

Run:

    uv run python src/python_engineering_journey/fundamentals/mutability_and_immutability/examples/dict_keys_and_set_members.py

---

# 24. Example — Defensive Copying

See:

    examples/defensive_copy.py

The example compares storing a shared reference with storing a defensive copy.

Run:

    uv run python src/python_engineering_journey/fundamentals/mutability_and_immutability/examples/defensive_copy.py

---

# 25. Example — frozenset

See:

    examples/frozenset_demo.py

The example demonstrates using a `frozenset` as a dictionary key and as a set
member.

Run:

    uv run python src/python_engineering_journey/fundamentals/mutability_and_immutability/examples/frozenset_demo.py

---

# 26. Exercise 01 — Predict Mutability and Identity

File:

    exercises/exercise_01.py

Given:

    numbers = [1, 2, 3]
    total = 0

Before running, predict whether `id()` stays the same or changes after:

    numbers.append(4)
    total += 10

Then predict the same for:

    text = "duy"
    text = text.upper()

Your explanation must use:

- Mutable
- Immutable
- Identity
- Rebinding

Do not simply write the output. Explain the identities.

---

# 27. Exercise 02 — Immutable Updates

File:

    exercises/exercise_02.py

Implement:

    def add_permission(
        permissions: frozenset[str], permission: str
    ) -> frozenset[str]:
        ...


    def make_point(x: int, y: int) -> tuple[int, int]:
        ...

Expected behavior:

    roles = frozenset({"read"})
    updated = add_permission(roles, "write")

    assert updated == frozenset({"read", "write"})
    assert roles == frozenset({"read"})     # original unchanged

    grid = {make_point(0, 0): "origin"}
    assert grid[make_point(0, 0)] == "origin"

`add_permission` must return a new `frozenset` without mutating the input.
`make_point` must return a hashable value usable as a dictionary key.

---

# 28. Exercise 03 — Defensive Copying

File:

    exercises/exercise_03.py

Implement a `Playlist` that owns its songs:

    class Playlist:
        def __init__(self, songs: list[str]) -> None: ...
        def add(self, song: str) -> None: ...
        def get_songs(self) -> list[str]: ...

Expected behavior:

    source = ["Song A", "Song B"]
    playlist = Playlist(source)
    source.append("Song C")

    assert playlist.get_songs() == ["Song A", "Song B"]   # input isolated

    exported = playlist.get_songs()
    exported.append("Song Z")

    assert playlist.get_songs() == ["Song A", "Song B"]   # output isolated

The playlist must copy on the way in and on the way out.

---

# 29. Challenge — The Frozen Config

Design a read-only configuration object.

Requirements:

- It is constructed from a plain dictionary.
- After construction, callers cannot mutate its values.
- Two configs built from equal data compare equal.
- It can be used as a dictionary key.

Explain which immutable types you used and why. Explain what would break if any
nested value were mutable.

---

# 30. Challenge — Cache Key Detective

You are given a function that caches results in a dictionary keyed by its
arguments:

    cache: dict[object, int] = {}

    def compute(key: object) -> int:
        ...

Answer:

- Which argument types can safely be cache keys?
- What happens if a caller passes a list?
- How would you convert an unhashable argument into a valid key without losing
  information?

Draw the object graph for one hashable key and one unhashable key.

---

# 31. Common Misconceptions

## Misconception 1

> `total += 1` mutates the integer.

It does not. It creates a new integer and rebinds the name.

---

## Misconception 2

> A tuple is deeply immutable.

A tuple only freezes its own references. A mutable object inside it can still
change.

---

## Misconception 3

> Any object can be a dictionary key.

Only hashable objects can. Lists, dicts, and sets cannot.

---

## Misconception 4

> Storing the list I was given is fine.

Not if you want to own it. Without a defensive copy, the caller can mutate your
internal state.

---

## Misconception 5

> Immutable objects are always the better choice.

Immutability adds safety but can add allocation cost. The right choice depends
on ownership, sharing, and performance.

---

# 32. Engineering Perspective

Mutability decisions shape the contracts of your functions and classes.

When designing an interface, ask:

### Ownership

Does this object own its data, or is it borrowing a reference?

### Boundaries

Do I copy mutable inputs when I accept them, and mutable state when I return it?

### Sharing

Is this value shared widely? If so, would immutability remove a whole class of
bugs?

### Keys

Am I about to use something as a dictionary key or set member? Is it hashable
today, and will it stay hashable?

### Cost

Is defensive copying or immutable rebuilding cheap enough here, or is in-place
mutation justified?

A common professional rule of thumb:

> Accept the most permissive type you can, but never store a mutable reference
> you do not own.

---

# 33. Reflection

Answer these without looking at the previous sections.

### Question 1

What is the difference between a mutable and an immutable object?

### Question 2

Which test reliably distinguishes mutation from rebinding?

### Question 3

Name three immutable built-in types and three mutable ones.

### Question 4

Why does `total += 1` change the id of `total`?

### Question 5

Why is immutability in Python described as shallow?

### Question 6

What does it mean for an object to be hashable?

### Question 7

Why must dictionary keys be hashable?

### Question 8

Why is a tuple only conditionally hashable?

### Question 9

What problem does defensive copying solve?

### Question 10

When would you prefer an immutable API over a mutable one?

---

# 34. Key Takeaways

Mutation changes an object in place and preserves its identity:

    name ──► object   (same id, new state)

Rebinding points a name at a different object:

    name ──► object A
    name ──► object B   (new id)

Immutable types cannot be changed in place; operations return new objects.

Immutability is shallow: an immutable container can still reference mutable
objects.

Hashability requires a stable hash, which is why only immutable objects are
reliably hashable.

Dictionary keys and set members must be hashable.

Defensive copying protects an object's private state at both boundaries.

The most important principle is:

> Decide who owns each mutable object, and never let it change from a place
> that should not own it.

---

# 35. Definition of Done

- [ ] Define mutability and immutability
- [ ] Use `id()` to distinguish mutation from rebinding
- [ ] List the core mutable and immutable built-in types
- [ ] Explain why integers and strings feel immutable
- [ ] Explain why immutability is shallow
- [ ] Define hashability
- [ ] Explain why immutability enables hashing
- [ ] Explain why dictionary keys and set members must be hashable
- [ ] Explain why a tuple is only conditionally hashable
- [ ] Use `frozenset` as a key and as a set member
- [ ] Apply defensive copying on input and output
- [ ] Complete all exercises
- [ ] Complete the Frozen Config and Cache Key Detective challenges

---

# 36. Next Lesson

## Lesson 04 — Scope and Namespaces (LEGB)

Topics:

- Namespaces
- Scope
- Local scope
- Enclosing scope
- Global scope
- Built-in scope
- The LEGB resolution rule
- `global`
- `nonlocal`
- Closures
- Late binding in closures
- Shadowing built-in names
- Comprehension scope

The key question:

> When you write a name, how does Python decide which object it refers to?
