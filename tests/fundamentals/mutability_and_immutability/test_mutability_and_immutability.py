"""Tests for Lesson 03: Mutability and Immutability."""

from __future__ import annotations

from typing import Any

import pytest

from python_engineering_journey.fundamentals.mutability_and_immutability.exercises import (
    exercise_02,
    exercise_03,
)

# --- Language semantics (always run) -----------------------------------------


def test_list_mutation_preserves_identity() -> None:
    numbers = [1, 2, 3]

    original_id = id(numbers)
    numbers.append(4)

    assert numbers == [1, 2, 3, 4]
    assert id(numbers) == original_id


def test_int_rebinding_changes_identity() -> None:
    total = 1000

    original_id = id(total)
    total += 1

    assert total == 1001
    assert id(total) != original_id


def test_tuple_does_not_support_item_assignment() -> None:
    point: Any = (1, 2)

    with pytest.raises(TypeError):
        point[0] = 99


def test_tuple_freezes_only_its_direct_references() -> None:
    record = ("config", ["logging", "metrics"])

    record[1].append("tracing")

    assert record == ("config", ["logging", "metrics", "tracing"])


def test_list_is_unhashable() -> None:
    with pytest.raises(TypeError):
        hash([1, 2, 3])


def test_tuple_of_hashables_is_hashable() -> None:
    assert isinstance(hash((1, 2, 3)), int)


def test_tuple_with_list_is_unhashable() -> None:
    with pytest.raises(TypeError):
        hash((1, [2, 3]))


def test_frozenset_is_hashable_and_usable_as_key() -> None:
    mapping = {frozenset({"admin"}): "full-access"}

    assert mapping[frozenset({"admin"})] == "full-access"


def test_dict_rejects_unhashable_key() -> None:
    with pytest.raises(TypeError):
        _ = {["a"]: 1}


def test_set_rejects_unhashable_member() -> None:
    with pytest.raises(TypeError):
        _ = {["a"]}


def test_string_methods_return_new_objects() -> None:
    text = "duy"

    upper = text.upper()

    assert upper == "DUY"
    assert upper is not text
    assert text == "duy"


# --- Exercise 02: immutable updates ------------------------------------------


@pytest.mark.exercise
def test_add_permission_returns_new_frozenset() -> None:
    roles = frozenset({"read"})

    updated = exercise_02.add_permission(roles, "write")

    assert updated == frozenset({"read", "write"})
    assert roles == frozenset({"read"})
    assert updated is not roles


@pytest.mark.exercise
def test_make_point_is_hashable_and_equal() -> None:
    assert exercise_02.make_point(1, 2) == exercise_02.make_point(1, 2)

    grid = {exercise_02.make_point(0, 0): "origin"}

    assert grid[exercise_02.make_point(0, 0)] == "origin"


# --- Exercise 03: defensive copying ------------------------------------------


@pytest.mark.exercise
def test_playlist_ignores_external_mutation() -> None:
    source = ["Song A", "Song B"]

    playlist = exercise_03.Playlist(source)
    source.append("Song C")

    assert playlist.get_songs() == ["Song A", "Song B"]


@pytest.mark.exercise
def test_playlist_returns_a_defensive_copy() -> None:
    playlist = exercise_03.Playlist(["Song A"])

    exported = playlist.get_songs()
    exported.append("Song Z")

    assert playlist.get_songs() == ["Song A"]


@pytest.mark.exercise
def test_playlist_add_appends_a_song() -> None:
    playlist = exercise_03.Playlist(["Song A"])

    playlist.add("Song B")

    assert playlist.get_songs() == ["Song A", "Song B"]
