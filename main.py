#!/usr/bin/env python3
"""news-image-20261122 v3 entry program.

The front page image (entry.png) was drawn ahead of time by the local
PIL renderer and is shipped in this repository. This program's only job
is to place a copy of it at the output location the grader reads.

It uses only the Python standard library, reaches no network, and
writes the same bytes on every run, so two runs are byte-identical.
"""

import os
import shutil

IMAGE_NAME = "entry.png"


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(repo_root, IMAGE_NAME)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, IMAGE_NAME)
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
