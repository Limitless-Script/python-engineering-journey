numbers = [1, 2, 3]
alias = numbers

print("Before rebinding:")
print("numbers:", numbers)
print("alias:", alias)
print("numbers is alias:", numbers is alias)

alias = [4, 5, 6]

print("\nAfter rebinding alias:")
print("numbers:", numbers)
print("alias:", alias)
print("numbers is alias:", numbers is alias)
