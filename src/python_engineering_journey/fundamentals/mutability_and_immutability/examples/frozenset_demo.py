mutable_roles = {"admin", "editor"}

print("A set is mutable, so it cannot be a dictionary key or a set member.")
print("mutable_roles:", mutable_roles)

mutable_roles.add("viewer")
print("after add:", mutable_roles)

frozen_roles = frozenset({"admin", "editor"})

print("\nA frozenset is immutable and hashable.")
print("frozen_roles:", frozen_roles)

permissions_by_role = {
    frozenset({"admin"}): "full-access",
    frozenset({"editor", "viewer"}): "read-write",
}

print("frozenset used as a dict key:", permissions_by_role[frozenset({"admin"})])

set_of_sets = {frozenset({1, 2}), frozenset({3, 4})}
print("frozenset used as a set member:", set_of_sets)
