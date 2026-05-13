#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class RGB:
    r: int
    g: int
    b: int
    def to_hex(self) -> str:
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}"

@dataclass
class WindowsColors:
    active_title: RGB = field(default_factory=lambda: RGB(10, 36, 106))
    inactive_title: RGB = field(default_factory=lambda: RGB(128, 128, 128))
    gradient_active_title: RGB = field(default_factory=lambda: RGB(166, 202, 240))
    gradient_inactive_title: RGB = field(default_factory=lambda: RGB(192, 192, 192))
    title_text: RGB = field(default_factory=lambda: RGB(255, 255, 255))
    inactive_title_text: RGB = field(default_factory=lambda: RGB(212, 208, 200))
    button_face: RGB = field(default_factory=lambda: RGB(212, 208, 200))
    button_shadow: RGB = field(default_factory=lambda: RGB(128, 128, 128))
    button_dk_shadow: RGB = field(default_factory=lambda: RGB(64, 64, 64))
    button_hilight: RGB = field(default_factory=lambda: RGB(255, 255, 255))
    button_light: RGB = field(default_factory=lambda: RGB(212, 208, 200))
    button_text: RGB = field(default_factory=lambda: RGB(0, 0, 0))
    window: RGB = field(default_factory=lambda: RGB(255, 255, 255))
    window_text: RGB = field(default_factory=lambda: RGB(0, 0, 0))
    window_frame: RGB = field(default_factory=lambda: RGB(0, 0, 0))
    hilight: RGB = field(default_factory=lambda: RGB(10, 36, 106))
    hilight_text: RGB = field(default_factory=lambda: RGB(255, 255, 255))
    menu: RGB = field(default_factory=lambda: RGB(212, 208, 200))
    menu_text: RGB = field(default_factory=lambda: RGB(0, 0, 0))
    scrollbar: RGB = field(default_factory=lambda: RGB(212, 208, 200))
    display_name: str = "Custom"

def parse_theme_file(path: Path) -> WindowsColors:
    content = path.read_text(errors="replace")
    colors = WindowsColors()
    
    m_name = re.search(r"DisplayName=(.*)", content)
    if m_name: colors.display_name = m_name.group(1).strip()
    
    m_colors = re.search(r"\[Control Panel\\Colors\](.*?)\n\[", content, re.DOTALL)
    if not m_colors:
        m_colors = re.search(r"\[Control Panel\\Colors\](.*)", content, re.DOTALL)
    
    if m_colors:
        block = m_colors.group(1)
        mapping = {
            "ActiveTitle": "active_title",
            "InactiveTitle": "inactive_title",
            "GradientActiveTitle": "gradient_active_title",
            "GradientInactiveTitle": "gradient_inactive_title",
            "TitleText": "title_text",
            "InactiveTitleText": "inactive_title_text",
            "ButtonFace": "button_face",
            "ButtonShadow": "button_shadow",
            "ButtonDkShadow": "button_dk_shadow",
            "ButtonHilight": "button_hilight",
            "ButtonLight": "button_light",
            "ButtonText": "button_text",
            "Window": "window",
            "WindowText": "window_text",
            "WindowFrame": "window_frame",
            "Hilight": "hilight",
            "HilightText": "hilight_text",
            "Menu": "menu",
            "MenuText": "menu_text",
            "Scrollbar": "scrollbar"
        }
        for k, attr in mapping.items():
            m = re.search(fr"^{k}\s*=\s*(\d+\s+\d+\s+\d+)", block, re.IGNORECASE | re.MULTILINE)
            if m:
                parts = [int(x) for x in m.group(1).split()]
                setattr(colors, attr, RGB(*parts))
    return colors

def generate_conf_text(c: WindowsColors) -> str:
    theme_name = re.sub(r"[^\w\s-]", "", c.display_name).strip() or "Custom"
    
    return f"""
Theme_name="{theme_name}"

fgcolor="{c.button_text.to_hex()}"

bgcolor="{c.button_face.to_hex()}"

basecolor="{c.window.to_hex()}"

basefg="{c.window_text.to_hex()}"

selectedbg="{c.hilight.to_hex()}"

selectedtext="{c.hilight_text.to_hex()}"

activetitletext="{c.title_text.to_hex()}"

inactivetitletext="{c.inactive_title_text.to_hex()}"

activetitle="{c.active_title.to_hex()}"
activetitle1="{c.gradient_active_title.to_hex()}"

inactivetitle="{c.inactive_title.to_hex()}"
inactivetitle1="{c.gradient_inactive_title.to_hex()}"

border="{c.button_dk_shadow.to_hex()}"

csd_style="1"

saturation_level="1"

enable_overdrive="false"

window_R="0.1"
window_G="-0.1"
window_B="-0.2"

highlight_multiplier="1.3"

shadow_multiplier="0.7"

disabled_fg_multiplier="0.8"

hl_R="0.1"
hl_G="0.1"
hl_B="0.1"

s_R="0"
s_G="0"
s_B="0"

high_contrast="false"

enable_alternate_menu="false"

menu_side_text="Pastel97"

menu_side_width="23"

menu_side_text_size="23"

menu_side_text_offset="10,22"
"""

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input.theme>")
        sys.exit(1)

    theme_file = Path(sys.argv[1])
    if not theme_file.exists():
        print(f"Error: {theme_file} not found.")
        sys.exit(1)

    colors = parse_theme_file(theme_file)
    output = generate_conf_text(colors)
    
    out_name = f"{theme_file.stem}.conf"
    Path(out_name).write_text(output)
    print(f"Generated configuration saved to: {out_name}")

if __name__ == "__main__":
    main()
