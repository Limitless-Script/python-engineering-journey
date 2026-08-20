"""Exercise 03: Defensive copying and ownership.

Implement a Playlist that fully owns its internal list of songs.

The class must protect its internal state from outside mutation in two
directions:

1. On the way in: a copy of the caller's list is stored, so mutating the
   original list later must not change the playlist.
2. On the way out: get_songs() returns a copy, so mutating the returned
   list must not change the playlist.

Do not change the tests or expected behavior.
"""


class Playlist:
    def __init__(self, songs: list[str]) -> None:
        # TODO: Store a defensive copy of ``songs`` on ``self._songs`` so that
        # later mutation of the caller's original list cannot leak in.
        raise NotImplementedError

    def add(self, song: str) -> None:
        # TODO: Append ``song`` to the internal list.
        raise NotImplementedError

    def get_songs(self) -> list[str]:
        # TODO: Return a copy of the internal list, not the internal list
        # itself, so callers cannot mutate the playlist's private state.
        raise NotImplementedError


def main() -> None:
    source = ["Song A", "Song B"]
    playlist = Playlist(source)

    source.append("Song C")

    print("playlist ignores external mutation:", playlist.get_songs())

    exported = playlist.get_songs()
    exported.append("Song D")

    print("playlist ignores exported mutation:", playlist.get_songs())


if __name__ == "__main__":
    main()
