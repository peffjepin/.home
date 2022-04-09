#!/usr/bin/env python3

import os
import pathlib
import shutil

BASE = pathlib.Path(__file__).parent
HOME = pathlib.Path.home()
DEPS = BASE / "deps"
BACKUP = BASE / "backup"


repos = (
    "https://github.com/zsh-users/zsh-autosuggestions",
    "https://github.com/zsh-users/zsh-syntax-highlighting",
    "https://github.com/zsh-users/zsh-completions",
    "https://github.com/sindresorhus/pure",
)

# links to make: (relative to .git, relative to $HOME)
symlinks = (
    ("vim", ".vim"),
    ("zsh/.zshenv", ".zshenv"),
    ("zsh", ".config/zsh"),
    ("kitty", ".config/kitty"),
    ("scripts", "scripts"),
    ("sxhkd", ".config/sxhkd"),
    ("qtile", ".config/qtile"),
)


def make_symlink(file, target):
    init_path = BASE / file
    target_path = HOME / target
    if target_path.exists():
        if target_path.is_symlink():
            target_path.unlink()
        else:
            print(f"backing up {target_path}")
            backup_path = BACKUP / target
            backup_path.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(target_path, backup_path)
    target_path.symlink_to(init_path)


def clone_repo(url):
    os.system(f"cd {DEPS} && git clone {url}")


if __name__ == "__main__":
    for url in repos:
        clone_repo(url)
    for pair in symlinks:
        make_symlink(*pair)
