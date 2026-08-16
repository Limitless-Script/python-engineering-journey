def calculate_tax(amount: float) -> float:
    """Calculate a simple 10% tax."""
    return amount * 0.10


# TODO:
# Investigate calculate_tax:
#
# 1. What is its type?
# 2. What is its identity?
# 3. Is it an object?
#
# Fill in the code below.

print("type:", type(calculate_tax))
print("id:", id(calculate_tax))

# TODO:
# Assign calculate_tax to another name.

tax_calculator = calculate_tax

print("same object:", calculate_tax is tax_calculator)

# TODO:
# Call the function through tax_calculator.

result = tax_calculator(100)

print("result:", result)


# TODO:
# Answer:
#
# Why does this work?
#
# Your answer:
# ...
