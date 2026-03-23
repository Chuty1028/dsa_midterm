import json
import time
from memory_profiler import profile

from ll import Song, Playlist


# time profiling

def load_playlist_timed(filepath: str) -> Playlist:
    start = time.perf_counter()

    pl = Playlist("DSA Midterm Mix")

    with open(filepath, "r", encoding="utf-8") as f:
        songs_data = json.load(f)

    for entry in songs_data:
        song = Song(
            title=entry["title"],
            artist=entry["artist"],
            album=entry["album"],
        )
        pl.add_song(song)

    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"[TIME] Songs loaded: {len(pl)}")
    print(f"[TIME] Elapsed time: {elapsed_ms:.4f} ms")
    return pl


# Memory profiling 

@profile
def load_playlist_memory(filepath: str) -> Playlist:
    pl = Playlist("DSA Midterm Mix")

    with open(filepath, "r", encoding="utf-8") as f:
        songs_data = json.load(f)

    for entry in songs_data:
        song = Song(
            title=entry["title"],
            artist=entry["artist"],
            album=entry["album"],
        )
        pl.add_song(song)

    return pl


# main

if __name__ == "__main__":
    DATA_FILE = "songs_data.json"

    print("=" * 50)
    print("        TIME PROFILING")
    print("=" * 50)
    playlist = load_playlist_timed(DATA_FILE)
    playlist.show()

    print("\n" + "=" * 50)
    print("        MEMORY PROFILING")
    print("=" * 50)
    load_playlist_memory(DATA_FILE)