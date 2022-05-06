import colorsys
import pathlib

DARK = "dark"
LIGHT = "light"

THIS = pathlib.Path(__file__)
HERE = THIS.parent

COLORS_16 = HERE / "base16"
COLORS_EXT = HERE / "colors"

WEIGHT = 0.25
MAP16 = {
    "black": "0",
    "red": "1",
    "green": "2",
    "yellow": "3",
    "blue": "4",
    "magenta": "5",
    "cyan": "6",
    "white": "7",
}


class TerminalPallette:
    # terminal_color_code -> hexstring
    colors: dict[str, str]

    # environement_variable_name -> environment_variable_value
    #   if name starts with 'xCS_' the value is a hexstring
    #   if name starts with 'CS_' the value is a color code (int <= 255)
    env: dict[str, str]

    def __init__(self, theme, high_contrast=False):
        self.colors = dict()
        self.env = dict()

        self._theme = theme
        self._high_contrast = high_contrast
        self._definition_lines = list()
        self._generation_lines = list()
        self._code_generator = self._color_code_generator()
        self._handle_theme()

    def process(self):
        self._read_config()
        self._process_color_definitions()
        self._process_generation_directives()

    def _handle_theme(self):
        if self._theme == DARK:
            self._bg_color_code = MAP16["black"]
            self._generation_lines.append("!foreground white")
        else:
            self._bg_color_code = MAP16["white"]
            self._generation_lines.append("!foreground black")

    @property
    def _bg_hexstr(self):
        assert self.colors, "colors should be defined before calling this"
        return self.colors[self._bg_color_code]

    def _read_config(self):
        all_lines = []

        with open(COLORS_16, "r") as f:
            all_lines.extend(f.readlines())
        with open(COLORS_EXT, "r") as f:
            all_lines.extend(f.readlines())

        self._definition_lines.extend(
            filter(lambda l: l.startswith("#"), all_lines)
        )
        self._generation_lines.extend(
            filter(lambda l: l.startswith("!"), all_lines)
        )

    def _process_color_definitions(self):
        for color, code in map(str.split, self._definition_lines):
            if self._high_contrast and (code != self._bg_color_code):
                self.colors[code] = contrast_against_theme(color, self._theme)
            else:
                self.colors[code] = color

    def _process_generation_directives(self):
        self.env = {
            "CS_BACKGROUND": self._bg_color_code,
            "xCS_BACKGROUND": self._bg_hexstr,
        }

        for ln in self._generation_lines:
            parts = ln.split()
            directive_name = parts[0][1:]
            directive_value = parts[1].lower()

            if directive_value in MAP16:
                hexstr = self.colors[MAP16[directive_value]]
            elif directive_value.startswith("#"):
                hexstr = directive_value
            else:
                hexstr = self.colors[directive_value]

            self._generate_color_class(directive_name, hexstr)

    def _generate_color_class(self, name, hexstr):
        name = name.upper()
        color_class = {
            f"CS_{name}_cc": very_low_contrast(hexstr, self._bg_hexstr),
            f"CS_{name}_c": low_contrast(hexstr, self._bg_hexstr),
            f"CS_{name}": hexstr,
            f"CS_{name}_C": high_contrast(hexstr, self._bg_hexstr),
            f"CS_{name}_CC": very_high_contrast(hexstr, self._bg_hexstr),
        }
        env = {}
        for name, hexstr in color_class.items():
            code = next(self._code_generator)
            self.colors[code] = hexstr
            env[name] = code
            env["x" + name] = hexstr
        self.env.update(env)

    @staticmethod
    def _color_code_generator():
        # don't override the base 16
        current = 16
        while current < 256:
            yield str(current)
            current += 1
        raise RuntimeError("can't go beyond 256 colors")


def hexstr_to_hsv(hexstr):
    offset = 1 if hexstr.startswith("#") else 0
    r = int(hexstr[offset : offset + 2], 16)
    g = int(hexstr[offset + 2 : offset + 4], 16)
    b = int(hexstr[offset + 4 : offset + 6], 16)
    return colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)


def hsv_to_hexstr(hsv):
    rgb = colorsys.hsv_to_rgb(*hsv)
    hexs = map(lambda x: hex(round(255 * x)), rgb)
    rx, gx, bx = map(lambda x: "0" + x[2:] if len(x) == 3 else x[2:], hexs)
    return f"#{rx}{gx}{bx}"


def contrast_against_theme(hexstr, theme, weight=WEIGHT):
    contrast_v = 1 if theme == DARK else 0
    h, s, v = hexstr_to_hsv(hexstr)
    return hsv_to_hexstr((h, s, lerp(v, contrast_v, weight)))


def high_contrast(hexstr, bg_hexstr, weight=WEIGHT):
    h1, s1, v1 = hexstr_to_hsv(hexstr)
    _, s2, v2 = hexstr_to_hsv(bg_hexstr)

    # diff if we were to be going for low contrast
    ds = lerp(s1, s2, weight) - s1
    dv = lerp(v1, v2, weight) - v1

    return hsv_to_hexstr((h1, clamp1f(s1 - ds), clamp1f(v1 - dv)))


def low_contrast(hexstr, bg_hexstr, weight=WEIGHT):
    h1, s1, v1 = hexstr_to_hsv(hexstr)
    _, s2, v2 = hexstr_to_hsv(bg_hexstr)

    return hsv_to_hexstr((h1, lerp(s1, s2, weight), lerp(v1, v2, weight)))


def very_high_contrast(hexstr, bg_hexstr, weight=WEIGHT):
    return high_contrast(hexstr, bg_hexstr, weight * 2)


def very_low_contrast(hexstr, bg_hexstr, weight=WEIGHT):
    return low_contrast(hexstr, bg_hexstr, weight * 2)


def lerp(a, b, t):
    return a + (b - a) * t


def clamp1f(n):
    return min(1, max(0, n))
