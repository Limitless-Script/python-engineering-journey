first = [1, 2, 3]
second = [1, 2, 3]
third = first

print("first == second:", first == second)
print("first is second:", first is second)

print()

print("first == third:", first == third)
print("first is third:", first is third)

print()

print("id(first):", id(first))
print("id(second):", id(second))
print("id(third):", id(third))

print()

value = 42

print("value:", value)
print("type(value):", type(value))
print("isinstance(value, int):", isinstance(value, int))

print()

missing_value = None

# Don't use `== None` in production code.
# Use `is None` instead.
print("missing_value is None:", missing_value is None)
# print("missing_value == None:", missing_value == None)
