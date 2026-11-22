#!/usr/bin/env python3
"""Ship the v3 front page image to the grader's output directory."""

import os
from pathlib import Path

SRC_NAME = "entry.png"

repo = Path(__file__).resolve().parent
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
out.joinpath(SRC_NAME).write_bytes(repo.joinpath(SRC_NAME).read_bytes())
