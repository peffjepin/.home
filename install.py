#!/usr/bin/env python3

import os
import pathlib
import shutil

BASE = pathlib.Path(__file__).parent.resolve()
HOME = pathlib.Path.home()
DEPS = BASE / "deps"
CLRS = BASE / "colorscheme"
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
    ("colorscheme", ".config/colorscheme"),
    ("zsh", ".config/zsh"),
    ("kitty", ".config/kitty"),
    ("scripts", "scripts"),
    ("sxhkd", ".config/sxhkd"),
    ("qtile", ".config/qtile"),
)


def make_symlink(file, dest):
    init_path = BASE / file
    dest_path = HOME / dest

    if dest_path.is_symlink():
        dest_path.unlink()
    elif dest_path.exists():
        backup_path = BACKUP / dest
        move_to_backup_directory(dest_path, backup_path)

    print(f"creating symlink: {init_path} -> {dest_path}")
    dest_path.symlink_to(init_path)


def move_to_backup_directory(filepath, backup_path):
    print(f"moving {filepath} to backup directory")
    backup_path.parent.mkdir(exist_ok=True, parents=True)
    shutil.move(filepath, backup_path)


def clone_repo(url):
    os.system(f"cd {DEPS} && git clone {url}")


if __name__ == "__main__":
    for url in repos:
        clone_repo(url)
    for (file, dest) in symlinks:
        make_symlink(file, dest)
