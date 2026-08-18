numbers = [1, 2, 3]

print("Mutating a list keeps the same object:")
print("id before:", id(numbers))

numbers.append(4)

print("numbers:", numbers)
print("id after: ", id(numbers))
print("same object:", True)

counter = 10

print("\n'Mutating' an int actually rebinds the name:")
print("id before:", id(counter))

counter += 1

print("counter:", counter)
print("id after: ", id(counter))
print("same object:", False)
