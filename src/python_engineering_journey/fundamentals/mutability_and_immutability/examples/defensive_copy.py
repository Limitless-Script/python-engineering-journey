def store_reference(source: list[str]) -> list[str]:
    """Keep the caller's list directly. The caller can still mutate it."""
    return source


def store_defensive_copy(source: list[str]) -> list[str]:
    """Keep an independent copy. Later caller mutations cannot leak in."""
    return list(source)


original = ["logging", "metrics"]

shared = store_reference(original)
owned = store_defensive_copy(original)

print("After construction both look equal:")
print("shared:", shared)
print("owned: ", owned)

original.append("tracing")

print("\nAfter the caller mutates its own list:")
print("shared (leaked): ", shared)
print("owned (protected):", owned)
