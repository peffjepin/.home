#!/usr/bin/env python3

import os
import pathlib

DEPS = pathlib.Path(__file__).parent / "deps"

repos = (
    "https://github.com/zsh-users/zsh-autosuggestions",
    "https://github.com/zsh-users/zsh-syntax-highlighting",
    "https://github.com/zsh-users/zsh-completions",
    "https://github.com/sindresorhus/pure",
)


if __name__ == "__main__":
    DEPS.mkdir(exist_ok=True)

    for url in repos:
        os.system(f"cd {DEPS} && git clone {url}")
