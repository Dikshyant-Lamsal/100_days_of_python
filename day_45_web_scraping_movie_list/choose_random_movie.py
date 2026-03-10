import random

MOVIE = "movies.txt"
WATCHED_TAG = "[WATCHED]"

def load_movies(filepath=MOVIE):
    """Load movies from file, returning raw lines and parsed movie dicts."""
    with open(filepath, "r") as f:
        lines = f.readlines()

    movies = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Skip header and separator
        if i < 2 or not stripped:
            continue
        watched = stripped.endswith(WATCHED_TAG)
        clean = stripped.replace(WATCHED_TAG, "").strip()
        parts = clean.split(None, 1)
        if len(parts) == 2:
            movie_id, title = parts
            movies.append({
                "line_index": i,
                "id": movie_id,
                "title": title.strip(),
                "watched": watched,
            })
    return lines, movies


def mark_watched(filepath, lines, movie):
    """Append [WATCHED] tag to a movie's line in the file."""
    i = movie["line_index"]
    original = lines[i].rstrip("\n")
    if not original.strip().endswith(WATCHED_TAG):
        lines[i] = original.rstrip() + f" {WATCHED_TAG}\n"
        with open(filepath, "w") as f:
            f.writelines(lines)
        print(f"  Marked '{movie['title']}' as watched.")


def pick_movie(filepath=MOVIE):
    lines, movies = load_movies(filepath)

    unwatched = [m for m in movies if not m["watched"]]
    watched_count = len(movies) - len(unwatched)

    if not unwatched:
        print(" You've watched all 100 movies on the list! Amazing!")
        return

    print(f"\n🎥 Movie Picker  ({watched_count}/{len(movies)} watched)\n")

    movie = random.choice(unwatched)
    print(f"  Random pick: [{movie['id']}] {movie['title']}")

    answer = input("\n  Have you already watched this? (y/n): ").strip().lower()

    if answer == "y":
        mark_watched(filepath, lines, movie)
        # Reload and pick again
        print("\n  Picking a different movie...\n")
        lines, movies = load_movies(filepath)
        unwatched = [m for m in movies if not m["watched"]]
        if unwatched:
            new_movie = random.choice(unwatched)
            print(f"  New pick: [{new_movie['id']}] {new_movie['title']}")
            answer2 = input("\n  Mark this one as watched too? (y/n): ").strip().lower()
            if answer2 == "y":
                mark_watched(filepath, lines, new_movie)
            else:
                print(f"\n Enjoy watching '{new_movie['title']}'!")
        else:
            print(" No more unwatched movies left!")
    else:
        print(f"\n Enjoy watching '{movie['title']}'!")
        answer2 = input("  Mark as watched now? (y/n): ").strip().lower()
        if answer2 == "y":
            mark_watched(filepath, lines, movie)


if __name__ == "__main__":
    pick_movie(MOVIE)