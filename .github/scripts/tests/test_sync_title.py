import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1]))

from sync_title import format_title


def test_format_title_keeps_github_title_under_limit():
    changed = ",".join(f"component-{i:03d}" for i in range(100))

    title = format_title(changed)

    assert len(title) <= 256
    assert title.startswith("chore: sync skills (")
    assert title.endswith(",...)")
    body = title[len("chore: sync skills (") : -5]
    assert body.split(",")[-1].startswith("component-")
    assert "component-099" not in title


def test_format_title_preserves_short_component_list():
    assert format_title("AIQ,CUDA-Q") == "chore: sync skills (AIQ,CUDA-Q)"
