#!/usr/bin/env python3

import re
import argparse
import pathlib
import colorscheme

THIS = pathlib.Path(__file__)
HERE = THIS.parent
ENV_DEST = HERE / "env"

KITTY_COLORS_DEST = HERE.parent / "kitty/colors.conf"
KITTY_SCHEME_DEST = HERE.parent / "kitty/colorscheme.conf"
KITTY_COLORSCHEME_TEMPLATES = {
    colorscheme.DARK: HERE.parent / "kitty/colorscheme-template-dark.conf",
    colorscheme.LIGHT: HERE.parent / "kitty/colorscheme-template-light.conf",
}

GENERATED_FILE_HEADER = f"### GENERATED FROM {THIS} ###\n"


def create_environment_file(env):
    print(f"writing file -> {ENV_DEST}")
    lines = [GENERATED_FILE_HEADER]
    lines.extend(f"export {k}={v}" for k, v in env.items())
    script = "\n".join(lines)
    with open(ENV_DEST, "w") as f:
        f.write(script)


def create_kitty_configuration_files(colors, theme):
    # write colors definition file in kitty format
    source_lines = [GENERATED_FILE_HEADER]
    source_lines.extend(
        (f"color{code} {color}" for code, color in colors.items())
    )
    print(f"writing file -> {KITTY_COLORS_DEST}")
    with open(KITTY_COLORS_DEST, "w") as f:
        f.write("\n".join(source_lines))

    # put hex literals into kitty colorscheme template
    template = KITTY_COLORSCHEME_TEMPLATES[theme]
    print(f"writing file -> {KITTY_SCHEME_DEST}")
    with open(template, "r") as f:
        template = f.read()
    rendered = re.sub(
        r"color(\d+)", lambda m: colors[str(m.group(1))], template
    )
    with open(KITTY_SCHEME_DEST, "w") as f:
        f.write(rendered)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--theme", choices=("light", "dark"), default="dark"
    )
    parser.add_argument(
        "-C", "--high-contrast", action="store_true", default=False
    )

    args = parser.parse_args()

    theme = colorscheme.DARK if args.theme == "dark" else colorscheme.LIGHT
    pallette = colorscheme.TerminalPallette(
        theme, high_contrast=args.high_contrast
    )
    pallette.process()

    create_environment_file(pallette.env)
    create_kitty_configuration_files(pallette.colors, theme)

    return 0


if __name__ == "__main__":
    exitcode = main()
    raise SystemExit(exitcode)
