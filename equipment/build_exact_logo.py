"""Rebuild Hafsa's chosen LauterMobil logo exactly, as vector, in exact brand colours.

- Monogram: polygons measured edge-by-edge from the reference (it is an embedded image in Canva).
- Lettering: traced from the reference raster with potrace (Canva's name font is proprietary,
  so tracing is the only way to keep the letterforms identical).
All coordinates are in the reference image's 2000x2000 pixel space.
"""
import os
import numpy as np
from PIL import Image
import potrace

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
PROJ = os.path.join(REPO, "live", "pipeline-branding", "projects", "medpfalz-mobil")   # project folder (LauterMobil)
REF = os.path.join(PROJ, "logo", "reference", "chosen-canva-logo-2000px.png")       # the design Hafsa approved
OUT = os.path.join(PROJ, "logo", "final")

LIGHTBLUE = "#0C75CB"   # L
GREEN = "#2F8D27"       # M
BLUE = "#043575"        # lettering
WHITE = "#FFFFFF"

# ------------------------------------------------------------------ monogram (measured)
L_PATH = "M160 686 H234 V1016 H449 V1091 H160 Z"
M_PATH = ("M267 687 L433.5 850 L600 687 V1091 H531 V857 L433.5 952 "
          "L336 857 V978 H267 Z")

# ------------------------------------------------------------------ lettering (traced)
ref = np.array(Image.open(REF).convert("RGB")).astype(int)
r, g, b = ref[..., 0], ref[..., 1], ref[..., 2]

def trace_region(x0, y0, x1, y1, scale=3):
    """Trace dark-blue ink inside a box; returns an SVG path in reference coordinates."""
    crop = Image.fromarray(ref[y0:y1, x0:x1].astype(np.uint8))
    crop = crop.resize(((x1 - x0) * scale, (y1 - y0) * scale), Image.LANCZOS)
    a = np.array(crop).astype(int)
    # distance from white towards the ink colour (0,52,112): use blue-minus-red + darkness
    lum = 0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]
    ink = (lum < 150) & (a[..., 2] - a[..., 0] > 30)
    bmp = potrace.Bitmap(~ink)  # potracer treats False as filled
    plist = bmp.trace(turdsize=8, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY,
                      alphamax=1.0, opticurve=True, opttolerance=0.2)
    def P(pt):
        return f"{x0 + pt.x / scale:.2f} {y0 + pt.y / scale:.2f}"
    d = []
    for curve in plist:
        d.append("M" + P(curve.start_point))
        for seg in curve.segments:
            if seg.is_corner:
                d.append("L" + P(seg.c) + " L" + P(seg.end_point))
            else:
                d.append("C" + P(seg.c1) + " " + P(seg.c2) + " " + P(seg.end_point))
        d.append("Z")
    return " ".join(d)

NAME_LAUTER = trace_region(700, 740, 1309, 975)   # "Lauter" (gap between r and M at x=1304-1314)
NAME_MOBIL = trace_region(1309, 740, 1830, 975)   # "Mobil"
DESC = trace_region(700, 1015, 1800, 1105)
SLOGAN = trace_region(470, 1190, 1860, 1305)

# ------------------------------------------------------------------ assembly
def svg(view, body, bg=None, px_w=None):
    x, y, w, h = view
    px_w = px_w or w
    px_h = px_w * h / w
    bgr = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" '
            f'width="{px_w:.0f}" height="{px_h:.0f}">\n'
            f'  <title>LauterMobil Krankenfahrten</title>\n  {bgr}\n{body}\n</svg>\n')

def mono(lcol=LIGHTBLUE, mcol=GREEN):
    return (f'  <path d="{L_PATH}" fill="{lcol}"/>\n'
            f'  <path d="{M_PATH}" fill="{mcol}"/>')

def text(col, slogan=True, desc_col=None, slogan_col=None, lauter_col=None, mobil_col=None):
    # Name is one colour (Hafsa chose this over a two-colour "Lauter"/"Mobil", 2026-09-24).
    # lauter_col / mobil_col kept only as an option; default = same colour as the rest of the text.
    s = f'  <path d="{NAME_LAUTER}" fill="{lauter_col or col}" fill-rule="evenodd"/>\n'
    s += f'  <path d="{NAME_MOBIL}" fill="{mobil_col or col}" fill-rule="evenodd"/>\n'
    s += f'  <path d="{DESC}" fill="{desc_col or col}" fill-rule="evenodd"/>'
    if slogan:
        s += f'\n  <path d="{SLOGAN}" fill="{slogan_col or col}" fill-rule="evenodd"/>'
    return s

PAD = 40
# content extents: monogram 160-600 x, 686-1091 y; name to 1800; slogan to 1834 / 1288
V_SLOGAN = (160 - PAD, 686 - PAD, 1834 - 160 + 2 * PAD, 1288 - 686 + 2 * PAD)
V_LOGO = (160 - PAD, 686 - PAD, 1800 - 160 + 2 * PAD, 1091 - 686 + 2 * PAD)
V_ICON = (160 - PAD, 686 - PAD, 600 - 160 + 2 * PAD, 1091 - 686 + 2 * PAD)

os.makedirs(OUT, exist_ok=True)
files = {
    "logo-with-slogan.svg": svg(V_SLOGAN, mono() + "\n" + text(BLUE), px_w=1800),
    "logo.svg": svg(V_LOGO, mono() + "\n" + text(BLUE, slogan=False), px_w=1800),
    "icon.svg": svg(V_ICON, mono(), px_w=600),
    "logo-with-slogan-reversed.svg": svg(V_SLOGAN, mono() + "\n" + text(WHITE), bg=BLUE, px_w=1800),
    "logo-reversed.svg": svg(V_LOGO, mono() + "\n" + text(WHITE, slogan=False), bg=BLUE, px_w=1800),
    "logo-mono-blue.svg": svg(V_SLOGAN, mono(BLUE, BLUE) + "\n" + text(BLUE, lauter_col=BLUE, mobil_col=BLUE), px_w=1800),
}
for name, content in files.items():
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(content)
print("wrote", len(files), "files to", OUT)
