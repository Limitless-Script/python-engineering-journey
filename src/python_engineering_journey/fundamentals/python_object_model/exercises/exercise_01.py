numbers = [1, 2, 3]

alias = numbers

copy = [1, 2, 3]


# TODO:
# Before running the program, predict:
#
# 1. numbers == alias
# 2. numbers is alias
# 3. numbers == copy
# 4. numbers is copy
#
# Then run the program and compare your prediction.


print("numbers == alias:", numbers == alias)
print("numbers is alias:", numbers is alias)

print()

print("numbers == copy:", numbers == copy)
print("numbers is copy:", numbers is copy)

print()

print("id(numbers):", id(numbers))
print("id(alias):", id(alias))
print("id(copy):", id(copy))


# TODO:
# Explain the results using these concepts:
#
# - name
# - object
# - identity
# - value
#
# Write your explanation below.
#
# Your explanation:
# ...
