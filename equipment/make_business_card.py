"""LauterMobil business card: 85x55 mm, 2 mm bleed (89x59 mm canvas), front + back.
All text outlined (no font dependency at the printer). Uses the approved logo files."""
import io, os, re
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
PROJ = os.path.join(REPO, "live", "pipeline-branding", "projects", "medpfalz-mobil")   # project folder (LauterMobil)
LOGO = os.path.join(PROJ, "logo", "final")
OUT = os.path.join(PROJ, "business-card")

BLUE, GREEN, LIGHTBLUE, WHITE = "#043575", "#2F8D27", "#0C75CB", "#FFFFFF"
W, H, BLEED = 89.0, 59.0, 2.0           # canvas incl. bleed (mm)
TRIM = (BLEED, BLEED, W - BLEED, H - BLEED)
SAFE = 4.0                              # safe margin inside trim (mm)
SX0, SY0, SX1, SY1 = BLEED + SAFE, BLEED + SAFE, W - BLEED - SAFE, H - BLEED - SAFE
PT = 0.3528                             # 1 pt in mm

FONTS = {
    "open": os.path.join(HERE, "fonts", "OpenSans[wdth,wght].ttf"),
    "quick": os.path.join(HERE, "fonts", "Quicksand[wght].ttf"),
}
_cache = {}
def font(key, wght):
    k = (key, wght)
    if k not in _cache:
        inst = instantiateVariableFont(TTFont(FONTS[key]), {"wght": wght, **({"wdth": 100} if key == "open" else {})})
        buf = io.BytesIO(); inst.save(buf); data = buf.getvalue()
        _cache[k] = (TTFont(io.BytesIO(data)), data)
    return _cache[k]

def text(s, key, wght, size_pt, x, y, fill, tracking=0.0, anchor="start"):
    """Outlined text; size in pt, position in mm (baseline). Returns (svg, width_mm)."""
    tt, data = font(key, wght)
    face = hb.Face(data); f = hb.Font(face); upem = face.upem
    b = hb.Buffer(); b.add_str(s); b.guess_segment_properties()
    hb.shape(f, b, {"kern": True, "liga": True})
    glyphs = list(zip(b.glyph_infos, b.glyph_positions))
    size = size_pt * PT; sc = size / upem
    total = (sum(p.x_advance for _, p in glyphs) + tracking * upem * (len(glyphs) - 1)) * sc
    if anchor == "end": x -= total
    elif anchor == "middle": x -= total / 2
    gs = tt.getGlyphSet(); order = tt.getGlyphOrder(); pen = 0; parts = []
    for i, (info, pos) in enumerate(glyphs):
        sp = SVGPathPen(gs)
        gs[order[info.codepoint]].draw(TransformPen(sp, (sc, 0, 0, -sc, x + (pen + pos.x_offset) * sc, y - pos.y_offset * sc)))
        parts.append(sp.getCommands())
        pen += pos.x_advance + (tracking * upem if i < len(glyphs) - 1 else 0)
    return f'<path d="{" ".join(parts)}" fill="{fill}"/>', total

def embed(svgfile, x, y, width):
    """Place an approved logo SVG (keeping its own viewBox) at x,y with given width (mm)."""
    src = open(os.path.join(LOGO, svgfile), encoding="utf-8").read()
    vb = re.search(r'viewBox="([^"]+)"', src).group(1)
    vx, vy, vw, vh = map(float, vb.split())
    inner = src.split(">", 1)[1].rsplit("</svg>", 1)[0]
    inner = re.sub(r"<title>.*?</title>", "", inner)
    h = width * vh / vw
    return f'<svg x="{x:.3f}" y="{y:.3f}" width="{width:.3f}" height="{h:.3f}" viewBox="{vb}">{inner}</svg>', h

def stripe():
    # thin brand stripe along the bottom edge, running into the bleed
    y = H - BLEED - 1.6
    return (f'<rect x="0" y="{y}" width="{W/2}" height="{H - y}" fill="{LIGHTBLUE}"/>'
            f'<rect x="{W/2}" y="{y}" width="{W/2}" height="{H - y}" fill="{GREEN}"/>')

def page(body, bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>{body}</svg>')

checks = []
def fits(label, x0, x1, y0=None, y1=None):
    ok = x0 >= SX0 - 1e-6 and x1 <= SX1 + 1e-6 and (y0 is None or (y0 >= SY0 - 1e-6 and y1 <= SY1 + 1e-6))
    checks.append((label, ok, round(x0, 2), round(x1, 2), y0 and round(y0, 2), y1 and round(y1, 2)))

# ------------------------------------------------------------------ FRONT (white, approved logo)
LW = 66.0
logo_h = LW * 682 / 1754
fx, fy = (W - LW) / 2, (H - 1.6 - logo_h) / 2
front_logo, _ = embed("logo-with-slogan.svg", fx, fy, LW)
fits("front logo", fx, fx + LW, fy, fy + logo_h)
FRONT = page(front_logo + stripe(), WHITE)

# ------------------------------------------------------------------ BACK (dark blue)
body = []
bl, bh = embed("logo-reversed.svg", SX0 - 0.6, SY0 - 0.6, 36.0)   # logo file has its own 40-unit padding
body.append(bl)
ry = SY0 + bh - 0.2
body.append(f'<rect x="{SX0}" y="{ry:.2f}" width="{SX1 - SX0}" height="0.25" fill="{LIGHTBLUE}"/>')

# services (left column)
col1 = SX0
sy = ry + 7.6
t, w = text("UNSERE FAHRTEN", "quick", 600, 6.0, col1, sy, "#9CC7EE", tracking=0.18); body.append(t)
fits("services heading", col1, col1 + w)
services = ["Arztpraxen & Kliniken", "Dialyse & Strahlentherapie", "Klinikaufnahme & -entlassung", "Kur- & Rehakliniken"]
yy = sy + 4.6
for s in services:
    indent = 2.6
    if not s.startswith("&"):
        body.append(f'<rect x="{col1:.2f}" y="{yy - 1.9:.2f}" width="1.4" height="1.4" fill="{GREEN}"/>')
    t, w = text(s, "open", 400, 7.5, col1 + indent, yy, WHITE); body.append(t)
    fits(f"service '{s}'", col1, col1 + indent + w, yy - 2.5, yy + 0.6)
    yy += 3.9

# contact (right column, right-aligned to safe edge)
cx = SX1
cy = sy
t, w = text("Tel. +49 6301 252536", "open", 700, 9.5, cx, cy + 0.6, WHITE, anchor="end"); body.append(t)
fits("phone", cx - w, cx)
lines = [("info@lautermobil.de", 400), ("lautermobil.de", 400), ("", 0), ("Kurpfalzstr. 3", 400), ("67734 Katzweiler", 400)]
yy = cy + 5.6
for s, wt in lines:
    if s:
        t, w = text(s, "open", wt, 8.0, cx, yy, WHITE, anchor="end"); body.append(t)
        fits(f"contact '{s}'", cx - w, cx, yy - 2.7, yy + 0.7)
    yy += 3.7 if s else 1.6

BACK = page("".join(body) + stripe(), BLUE)

# ------------------------------------------------------------------ write files
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "card-front.svg"), "w", encoding="utf-8").write(FRONT)
open(os.path.join(OUT, "card-back.svg"), "w", encoding="utf-8").write(BACK)
html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
        f'@page{{size:{W}mm {H}mm;margin:0}}html,body{{margin:0;padding:0}}'
        '.p{page-break-after:always;width:%smm;height:%smm;overflow:hidden}.p:last-child{page-break-after:auto}'
        'svg{display:block}</style></head><body>' % (W, H) +
        f'<div class="p">{FRONT}</div><div class="p">{BACK}</div></body></html>')
open(os.path.join(OUT, "_print.html"), "w", encoding="utf-8").write(html)
for c in checks:
    print(("OK  " if c[1] else "OUT ") + c[0], c[2:])
