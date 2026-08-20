point = (1, 2)

print("A tuple cannot be reassigned in place:")
try:
    point[0] = 99  # type: ignore[index]
except TypeError as error:
    print("TypeError:", error)

record = ("config", ["logging", "metrics"])

print("\nBut a tuple only freezes its direct references:")
print("before:", record)

record[1].append("tracing")

print("after: ", record)
print("The tuple is unchanged; the list it points to was mutated.")
