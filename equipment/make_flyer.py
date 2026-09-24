"""LauterMobil flyer: DIN A5 (148x210 mm), 2 mm bleed (152x214 mm canvas), front + back.
Text outlined; approved logo files embedded as vector; approved AI photos embedded as images."""
import io, os, re, base64
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
PROJ = os.path.join(REPO, "live", "pipeline-branding", "projects", "medpfalz-mobil")   # project folder (LauterMobil)
LOGO = os.path.join(PROJ, "logo", "final")
PHOTOS = os.path.join(PROJ, "flyer", "photos-generated")
OUT = os.path.join(PROJ, "flyer")

BLUE, GREEN, LIGHTBLUE, WHITE = "#043575", "#2F8D27", "#0C75CB", "#FFFFFF"
TINT = "#9CC7EE"                         # light-blue tint for small labels on dark blue
W, H, BLEED = 152.0, 214.0, 2.0
SAFE = 6.0
SX0, SY0, SX1, SY1 = BLEED + SAFE, BLEED + SAFE, W - BLEED - SAFE, H - BLEED - SAFE
CX = W / 2
PT = 0.3528

FONTS = {"open": os.path.join(HERE, "fonts", "OpenSans[wdth,wght].ttf"),
         "quick": os.path.join(HERE, "fonts", "Quicksand[wght].ttf")}
_cache = {}
def font(key, wght):
    k = (key, wght)
    if k not in _cache:
        axes = {"wght": wght, **({"wdth": 100} if key == "open" else {})}
        inst = instantiateVariableFont(TTFont(FONTS[key]), axes)
        buf = io.BytesIO(); inst.save(buf); data = buf.getvalue()
        _cache[k] = (TTFont(io.BytesIO(data)), data)
    return _cache[k]

def measure(s, key, wght, size_pt, tracking=0.0):
    _, data = font(key, wght)
    face = hb.Face(data); f = hb.Font(face); upem = face.upem
    b = hb.Buffer(); b.add_str(s); b.guess_segment_properties(); hb.shape(f, b, {"kern": True})
    g = b.glyph_positions
    return (sum(p.x_advance for p in g) + tracking * upem * (len(g) - 1)) * size_pt * PT / upem

def text(s, key, wght, size_pt, x, y, fill, tracking=0.0, anchor="start"):
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
    return f'<path d="{" ".join(parts)}" fill="{fill}"/>', total, x

def embed_logo(svgfile, x, y, width):
    src = open(os.path.join(LOGO, svgfile), encoding="utf-8").read()
    vb = re.search(r'viewBox="([^"]+)"', src).group(1)
    vx, vy, vw, vh = map(float, vb.split())
    inner = re.sub(r"<title>.*?</title>", "", src.split(">", 1)[1].rsplit("</svg>", 1)[0])
    h = width * vh / vw
    return f'<svg x="{x:.3f}" y="{y:.3f}" width="{width:.3f}" height="{h:.3f}" viewBox="{vb}">{inner}</svg>', h

def photo(fname, x, y, w, h, clip_id, rx=0):
    data = base64.b64encode(open(os.path.join(PHOTOS, fname), "rb").read()).decode()
    clip = (f'<clipPath id="{clip_id}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/></clipPath>')
    return (f'<defs>{clip}</defs><image href="data:image/png;base64,{data}" x="{x}" y="{y}" width="{w}" '
            f'height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip_id})"/>')

def check_icon(cx, cy, r=2.6, bg=GREEN, fg=WHITE):
    return (f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{bg}"/>'
            f'<path d="M{cx-1.2:.2f} {cy+0.05:.2f} L{cx-0.25:.2f} {cy+1.0:.2f} L{cx+1.35:.2f} {cy-0.9:.2f}" '
            f'fill="none" stroke="{fg}" stroke-width="0.6" stroke-linecap="round" stroke-linejoin="round"/>')

def stripe():
    y = H - BLEED - 2.0
    return (f'<rect x="0" y="{y}" width="{W/2}" height="{H-y}" fill="{LIGHTBLUE}"/>'
            f'<rect x="{W/2}" y="{y}" width="{W/2}" height="{H-y}" fill="{GREEN}"/>')

def page(body, bg=WHITE):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>{body}</svg>')

checks = []
def fits(label, x0, x1):
    checks.append((label, SX0 - 1e-6 <= x0 and x1 <= SX1 + 1e-6, round(x0, 1), round(x1, 1)))

def centered(s, key, wght, pt, y, fill, tracking=0.0, label=None):
    t, w, x = text(s, key, wght, pt, CX, y, fill, tracking, anchor="middle")
    fits(label or s, x, x + w)
    return t

# =================================================================== FRONT
f = []
HERO_H = 92.0
f.append(photo("3-comfortable-passenger.png", 0, 0, W, HERO_H, "hero"))
# thin brand line under the photo
f.append(f'<rect x="0" y="{HERO_H}" width="{W/2}" height="1.2" fill="{LIGHTBLUE}"/>'
         f'<rect x="{W/2}" y="{HERO_H}" width="{W/2}" height="1.2" fill="{GREEN}"/>')

LOGO_W = 88.0
lg, lh = embed_logo("logo-with-slogan.svg", CX - LOGO_W / 2, HERO_H + 6.0, LOGO_W)
f.append(lg)
y = HERO_H + 6.0 + lh + 8.5
f.append(centered("Ihr Krankenfahrdienst für", "open", 700, 15, y, BLUE))
f.append(centered("Katzweiler und Umgebung", "open", 700, 15, y + 6.6, BLUE))

# three key facts
fy = y + 15.0
cols = [("Rund um die Uhr", "erreichbar"), ("Abrechnung mit den", "Krankenkassen"), ("Rollstuhlgerechte", "Fahrzeuge")]
colw = (SX1 - SX0) / 3
for i, (a, b2) in enumerate(cols):
    cx = SX0 + colw * (i + 0.5)
    f.append(check_icon(cx, fy, r=3.0))
    for j, line in enumerate((a, b2)):
        t, w, x = text(line, "open", 600, 8.5, cx, fy + 7.8 + j * 3.7, BLUE, anchor="middle")
        f.append(t); fits(f"fact '{line}'", x, x + w)

# bottom band: call to action
BAND_Y = 177.0
f.append(f'<rect x="0" y="{BAND_Y}" width="{W}" height="{H-BAND_Y}" fill="{BLUE}"/>')
f.append(centered("JETZT FAHRT VEREINBAREN", "quick", 700, 8.5, BAND_Y + 10.0, TINT, tracking=0.2))
f.append(centered("+49 6301 252536", "open", 800, 24, BAND_Y + 22.0, WHITE))
f.append(stripe())
FRONT = page("".join(f))

# =================================================================== BACK
b = []
t, w, x = text("UNSERE LEISTUNGEN", "quick", 700, 10, SX0, SY0 + 6.0, LIGHTBLUE, tracking=0.2); b.append(t); fits("heading", x, x + w)
intro = ["Wir bringen Sie sicher und bequem ans Ziel – zu Arzt, Klinik,",
         "Dialyse oder Reha und wieder zurück nach Hause."]
for j, line in enumerate(intro):
    t, w, x = text(line, "open", 400, 9.5, SX0, SY0 + 13.0 + j * 4.6, BLUE); b.append(t); fits("intro", x, x + w)

services_l = ["Rollstuhlfahrten", "Tragestuhlfahrten", "Liegendtransporte", "Serienfahrten"]
services_r = ["Senioren- und Pflegefahrten", "Privatfahrten", "Fahrten für Einrichtungen", "Begleit- und Tür-zu-Tür-Service"]
sy = SY0 + 30.0
col_r = SX0 + 62.0
for col_x, items in ((SX0, services_l), (col_r, services_r)):
    for j, s in enumerate(items):
        yy = sy + j * 7.0
        b.append(f'<rect x="{col_x:.2f}" y="{yy - 2.55:.2f}" width="2.0" height="2.0" fill="{GREEN}"/>')
        t, w, x = text(s, "open", 600, 10, col_x + 4.0, yy, BLUE); b.append(t); fits(f"service '{s}'", col_x, x + w)

# photo grid: one large + two stacked, caption strips on the photos
py = sy + 3 * 7.0 + 8.0
gap = 3.0
bw = 80.0; bh = bw * 2 / 3
sw_ = SX1 - SX0 - bw - gap; sh_ = (bh - gap) / 2
cells = [("2-wheelchair-ramp.png", "Rollstuhlfahrten", SX0, py, bw, bh),
         ("1-door-to-door.png", "Tür-zu-Tür-Service", SX0 + bw + gap, py, sw_, sh_),
         ("4-arrival-clinic.png", "Sicher in die Praxis", SX0 + bw + gap, py + sh_ + gap, sw_, sh_)]
for i, (fn, cap, x0, y0, cw, ch) in enumerate(cells):
    b.append(photo(fn, x0, y0, cw, ch, f"p{i}", rx=1.5))
    capw = measure(cap, "open", 700, 8) + 5.0
    b.append(f'<g clip-path="url(#p{i})"><rect x="{x0}" y="{y0 + ch - 6.2:.2f}" width="{capw:.2f}" height="6.2" fill="{BLUE}" opacity="0.88"/></g>')
    t, w, x = text(cap, "open", 700, 8, x0 + 2.5, y0 + ch - 2.0, WHITE); b.append(t); fits(f"caption '{cap}'", x, x + w)

# advantages
ay = py + bh + 12.0
t, w, x = text("IHRE VORTEILE", "quick", 700, 10, SX0, ay, LIGHTBLUE, tracking=0.2); b.append(t)
adv = [("Rund um die Uhr erreichbar", "Abrechnung mit den Krankenkassen"),
       ("Rollstuhlgerechte Fahrzeuge", "Katzweiler und Umgebung")]
for j, pair in enumerate(adv):
    for k, s in enumerate(pair):
        x0 = SX0 + k * 62.0
        yy = ay + 8.0 + j * 6.8
        b.append(check_icon(x0 + 2.2, yy - 1.25, r=2.2))
        t, w, x = text(s, "open", 600, 9.5, x0 + 6.0, yy, BLUE); b.append(t); fits(f"adv '{s}'", x0, x + w)

# contact band
CB_Y = ay + 23.0
b.append(f'<rect x="0" y="{CB_Y}" width="{W}" height="{H-CB_Y}" fill="{BLUE}"/>')
lg, lh = embed_logo("logo-reversed.svg", SX0 - 1.5, CB_Y + 6.0, 62.0); b.append(lg)
cx = SX1
t, w, x = text("+49 6301 252536", "open", 800, 15, cx, CB_Y + 13.5, WHITE, anchor="end"); b.append(t); fits("phone", x, x + w)
t, w, x = text("RUND UM DIE UHR ERREICHBAR", "quick", 700, 7, cx, CB_Y + 18.5, TINT, tracking=0.15, anchor="end"); b.append(t); fits("24h", x, x + w)
lines = ["info@lautermobil.de", "lautermobil.de", "Kurpfalzstr. 3 · 67734 Katzweiler"]
for j, s in enumerate(lines):
    t, w, x = text(s, "open", 400, 9.5, cx, CB_Y + 27.0 + j * 4.6, WHITE, anchor="end"); b.append(t); fits(f"contact '{s}'", x, x + w)
b.append(stripe())
BACK = page("".join(b))

# =================================================================== write
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "flyer-front.svg"), "w", encoding="utf-8").write(FRONT)
open(os.path.join(OUT, "flyer-back.svg"), "w", encoding="utf-8").write(BACK)
html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
        f'@page{{size:{W}mm {H}mm;margin:0}}html,body{{margin:0;padding:0}}'
        f'.p{{page-break-after:always;width:{W}mm;height:{H}mm;overflow:hidden}}.p:last-child{{page-break-after:auto}}'
        'svg{display:block}</style></head><body>' +
        f'<div class="p">{FRONT}</div><div class="p">{BACK}</div></body></html>')
TMP = os.path.join(REPO, ".tmp"); os.makedirs(TMP, exist_ok=True)
PRINT_HTML = os.path.join(TMP, "flyer_print.html")   # ~15 MB (embedded photos), kept out of git
open(PRINT_HTML, "w", encoding="utf-8").write(html)
print(f"contact band starts at y={CB_Y:.1f} mm (trim bottom {H-BLEED}); front band {BAND_Y}")
for c in checks:
    print(("OK  " if c[1] else "OUT ") + c[0], c[2:])
