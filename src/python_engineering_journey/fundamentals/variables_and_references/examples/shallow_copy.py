import copy


original = [
    ["Python", "Java"],
    ["Go", "Rust"],
]

clone = copy.copy(original)

print("Outer objects:")
print("original is clone:", original is clone)

print("\nNested objects:")
print(
    "original[0] is clone[0]:",
    original[0] is clone[0],
)

clone[0].append("C++")

print("\nOriginal:")
print(original)

print("\nClone:")
print(clone)
