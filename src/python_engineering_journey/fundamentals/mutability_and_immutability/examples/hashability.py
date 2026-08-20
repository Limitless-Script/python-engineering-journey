print("Immutable objects are hashable:")
print("hash(42):", hash(42))
print("hash('duy'):", hash("duy"))
print("hash((1, 2)):", hash((1, 2)))
print("hash(frozenset({1, 2})):", hash(frozenset({1, 2})))

print("\nMutable objects are not hashable:")
mutable_values: list[object] = [[1, 2], {"a": 1}, {1, 2}]
for value in mutable_values:
    try:
        hash(value)
    except TypeError as error:
        print(f"hash({value!r}) -> TypeError: {error}")

print("\nA tuple is only hashable if all its elements are hashable:")
nested: object = (1, [2, 3])
try:
    hash(nested)
except TypeError as error:
    print("hash((1, [2, 3])) -> TypeError:", error)
