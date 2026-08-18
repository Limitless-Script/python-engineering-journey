print("Immutable values work as dictionary keys:")
distances = {
    ("Hanoi", "Hue"): 668,
    ("Hue", "Saigon"): 1097,
}
print(distances[("Hanoi", "Hue")])

print("\nA list cannot be used as a key:")
invalid_key: object = ["Hanoi", "Hue"]
try:
    broken_mapping = {invalid_key: 668}
except TypeError as error:
    print("TypeError:", error)

print("\nSet members must be hashable too:")
tags = {("py", 3), ("py", 2)}
print("set of tuples:", tags)

invalid_member: object = ["py", 3]
try:
    broken_set = {invalid_member}
except TypeError as error:
    print("TypeError:", error)
