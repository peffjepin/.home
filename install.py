#!/usr/bin/env python3

import pathlib
import shutil

BASE = pathlib.Path(__file__).parent.resolve()
HOME = pathlib.Path.home()
BACKUP = BASE / "backup"

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
    dest_path.parent.mkdir(exist_ok=True, parents=True)
    dest_path.symlink_to(init_path)


def move_to_backup_directory(filepath, backup_path):
    print(f"moving {filepath} to backup directory")
    backup_path.parent.mkdir(exist_ok=True, parents=True)
    shutil.move(filepath, backup_path)


if __name__ == "__main__":
    for (file, dest) in symlinks:
        make_symlink(file, dest)
