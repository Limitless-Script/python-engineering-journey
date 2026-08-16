"""Tests for Lesson 02: Variables and References."""

from __future__ import annotations

import copy

from python_engineering_journey.fundamentals.variables_and_references.exercises.exercise_02 import (
    mutate,
    rebind,
)


def test_assignment_creates_alias() -> None:
    numbers = [1, 2, 3]

    alias = numbers

    assert alias is numbers
    assert alias == numbers


def test_equal_lists_are_not_necessarily_the_same_object() -> None:
    first = [1, 2, 3]
    second = [1, 2, 3]

    assert first == second
    assert first is not second


def test_mutation_changes_the_shared_object() -> None:
    numbers = [1, 2, 3]
    alias = numbers

    alias.append(4)

    assert numbers == [1, 2, 3, 4]
    assert alias == [1, 2, 3, 4]
    assert numbers is alias


def test_rebinding_does_not_change_the_original_object() -> None:
    numbers = [1, 2, 3]

    original_id = id(numbers)

    alias = numbers
    alias = [4, 5, 6]

    assert numbers == [1, 2, 3]
    assert alias == [4, 5, 6]
    assert id(numbers) == original_id
    assert numbers is not alias


def test_mutate_changes_the_callers_list() -> None:
    numbers = [1, 2, 3]

    mutate(numbers)

    assert numbers == [1, 2, 3, 4]


def test_rebind_does_not_change_the_callers_list() -> None:
    numbers = [1, 2, 3]

    rebind(numbers)

    assert numbers == [1, 2, 3]


def test_shallow_copy_creates_new_outer_object() -> None:
    original = [
        ["Python", "Java"],
        ["Go", "Rust"],
    ]

    clone = copy.copy(original)

    assert clone is not original
    assert clone == original


def test_shallow_copy_shares_nested_objects() -> None:
    original = [
        ["Python", "Java"],
        ["Go", "Rust"],
    ]

    clone = copy.copy(original)

    assert clone[0] is original[0]
    assert clone[1] is original[1]


def test_shallow_copy_nested_mutation_is_visible() -> None:
    original = [
        ["Python", "Java"],
    ]

    clone = copy.copy(original)

    clone[0].append("C++")

    assert original == [["Python", "Java", "C++"]]
    assert clone == [["Python", "Java", "C++"]]


def test_deep_copy_creates_independent_nested_objects() -> None:
    original = [
        ["Python", "Java"],
        ["Go", "Rust"],
    ]

    clone = copy.deepcopy(original)

    assert clone is not original
    assert clone[0] is not original[0]
    assert clone[1] is not original[1]


def test_deep_copy_nested_mutation_is_independent() -> None:
    original = [
        ["Python", "Java"],
    ]

    clone = copy.deepcopy(original)

    clone[0].append("C++")

    assert original == [["Python", "Java"]]
    assert clone == [["Python", "Java", "C++"]]


def test_mutation_and_rebinding_have_different_semantics() -> None:
    numbers = [1, 2, 3]

    mutate(numbers)

    assert numbers == [1, 2, 3, 4]

    rebind(numbers)

    assert numbers == [1, 2, 3, 4]
