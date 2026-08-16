"""Exercise 03: Copy strategy.

Create three versions of a configuration:

1. An alias
2. A shallow copy
3. A deep copy

Then investigate their object identities.
"""

import copy


configuration = {
    "database": {
        "host": "localhost",
        "port": 5432,
    },
    "features": [
        "logging",
        "metrics",
    ],
}


def main() -> None:
    # TODO: Create an alias.
    alias = None

    # TODO: Create a shallow copy.
    shallow = None

    # TODO: Create a deep copy.
    deep = None

    print("Outer identity")
    print("configuration is alias:", configuration is alias)
    print("configuration is shallow:", configuration is shallow)
    print("configuration is deep:", configuration is deep)

    print("\nNested database identity")
    print(
        "configuration['database'] is alias['database']:",
        configuration["database"] is alias["database"],
    )
    print(
        "configuration['database'] is shallow['database']:",
        configuration["database"] is shallow["database"],
    )
    print(
        "configuration['database'] is deep['database']:",
        configuration["database"] is deep["database"],
    )

    print("\nNested features identity")
    print(
        "configuration['features'] is alias['features']:",
        configuration["features"] is alias["features"],
    )
    print(
        "configuration['features'] is shallow['features']:",
        configuration["features"] is shallow["features"],
    )
    print(
        "configuration['features'] is deep['features']:",
        configuration["features"] is deep["features"],
    )

    print("\nMutating shallow copy")

    shallow["features"].append("tracing")

    print("configuration:", configuration)
    print("shallow:", shallow)
    print("deep:", deep)


if __name__ == "__main__":
    main()
