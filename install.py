#!/usr/bin/env python3

import subprocess
import pathlib
import shlex
import os

from dataclasses import dataclass
from subprocess import DEVNULL


BASE = pathlib.Path(__file__).parent
DEPS = BASE / "deps"
BACKUP = BASE / "backup"


@dataclass
class PackageManager:
    lookup = dict()

    name: str
    install: str

    @classmethod
    def get_pkg_name(cls, name):
        from_lookup = cls.lookup.get(name)
        return from_lookup if from_lookup is not None else name

    @classmethod
    def get_for_system(cls):
        for pm in cls.__subclasses__():
            cmd = shlex.split(f"which {pm.name}")
            p = subprocess.run(cmd, stdout=DEVNULL, stderr=DEVNULL)
            if p.returncode == 0:
                return pm

        raise ValueError("Could not determine which package manager to use.")


class AptGet(PackageManager):
    name = "apt-get"
    install = "apt-get update && apt-get install"


class Pacman(PackageManager):
    name = "pacman"
    install = "pacman -Syu"


def install_software(*packages: str):
    pkgman = PackageManager.get_for_system()
    os.system(f"{pkgman.install} {' '.join(packages)}")


if __name__ == "__main__":
    install_software("vim", "zsh", "ranger", "sxhkd")
