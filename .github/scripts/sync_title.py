"""Build GitHub-safe titles for automated skill sync pull requests."""

TITLE_PREFIX = "chore: sync skills ("
TITLE_SUFFIX = ",...)"
GITHUB_TITLE_LIMIT = 256


def format_title(changed: str, limit: int = GITHUB_TITLE_LIMIT) -> str:
    """Return a readable sync title that never exceeds GitHub's limit."""
    full = f"{TITLE_PREFIX}{changed})"
    if len(full) <= limit:
        return full

    available = limit - len(TITLE_PREFIX) - len(TITLE_SUFFIX)
    if available <= 0:
        raise ValueError("title limit is too small for the sync title prefix")

    compact = changed[:available].rsplit(",", 1)[0]
    if not compact:
        compact = changed[:available]
    return f"{TITLE_PREFIX}{compact}{TITLE_SUFFIX}"


if __name__ == "__main__":
    import sys

    print(format_title(sys.stdin.read().strip()))
