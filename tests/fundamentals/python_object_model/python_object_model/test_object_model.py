def test_objects_have_identity_and_type() -> None:
    value = 42

    assert id(value)
    assert type(value) is int


def test_aliases_reference_the_same_object() -> None:
    numbers = [1, 2, 3]
    alias = numbers

    assert alias is numbers


def test_separate_objects_can_be_equal() -> None:
    first = [1, 2, 3]
    second = [1, 2, 3]

    assert first == second
    assert first is not second


def test_identity_is_transitive_through_aliases() -> None:
    first = [1, 2, 3]
    second = first
    third = second

    assert first is second
    assert second is third
    assert first is third


def test_functions_are_objects() -> None:
    def greet() -> str:
        return "hello"

    assert isinstance(greet, object)


def test_function_aliases_reference_the_same_object() -> None:
    def greet() -> str:
        return "hello"

    say_hello = greet

    assert say_hello is greet
    assert say_hello() == "hello"


def test_classes_are_objects() -> None:
    class User:
        pass

    assert isinstance(User, object)


def test_class_and_instance_are_different_objects() -> None:
    class User:
        pass

    user = User()

    # The class object and its instance are distinct objects. mypy statically
    # knows their types can never overlap, hence the targeted ignore.
    assert User is not user  # type: ignore[comparison-overlap]


def test_instance_has_expected_type() -> None:
    class User:
        pass

    user = User()

    assert type(user) is User
    assert isinstance(user, User)


def test_class_has_type_type() -> None:
    class User:
        pass

    assert type(User) is type


def test_none_should_be_checked_with_is() -> None:
    value = None

    assert value is None
