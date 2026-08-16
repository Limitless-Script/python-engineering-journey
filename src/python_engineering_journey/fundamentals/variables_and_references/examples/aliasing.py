numbers = [1, 2, 3]

alias = numbers

print("Before mutation:")
print("numbers:", numbers)
print("alias:", alias)
print("numbers is alias:", numbers is alias)
print("id(numbers):", id(numbers))
print("id(alias):", id(alias))

alias.append(4)

print("\nAfter alias.append(4):")
print("numbers:", numbers)
print("alias:", alias)
print("numbers is alias:", numbers is alias)
