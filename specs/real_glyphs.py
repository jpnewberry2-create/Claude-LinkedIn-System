# real_glyphs.py — v4 (78-glyph sprite)
# Renders flat-colour icon tiles from the consolidated Claude Design SVG assets.
# Source sprite: icons-sprite.svg (78 line glyphs + 9 background tiles).
# Each glyph: stroke 2 on a 24x24 viewBox. Each tile: 256x256 squircle.
import cairosvg, io, re
from PIL import Image
import numpy as np

# Point this at the directory of standalone SVGs extracted from icons-sprite.svg
# (one file per symbol id, e.g. glyph-save.svg, bg-pink.svg).
UP = '/home/claude/svg_assets_v4'

# Background tile colour keys -> sprite tile filenames. Nine tiles available.
BG = {
    'charcoal':   'bg-charcoal.svg',
    'chart-blue': 'bg-chart-blue.svg',
    'blue':       'bg-chart-blue.svg',   # alias
    'chart-lilac':'bg-chart-lilac.svg',
    'lilac':      'bg-lilac.svg',
    'dark-blue':  'bg-dark-blue.svg',
    'ink-blue':   'bg-ink-blue.svg',
    'ink':        'bg-ink-blue.svg',     # alias
    'orange':     'bg-orange.svg',
    'pink':       'bg-pink.svg',
    'teal':       'bg-teal.svg',
}

# Tiles whose fill is light enough that the glyph must be charcoal, not white.
LIGHT = {'teal', 'orange'}

WHITE = '#FFFFFF'
CHARCOAL = '#1E293B'

# All 78 glyphs in the v4 sprite.
GLYPHS = {
    'ai','arrowdown','arrowleft','arrowright','arrowup','ask-question','audience','bad',
    'board-meeting','calendar','career','chess','code','comment','community','conversation',
    'data','delay','demo','download','engagement','faceangry','facehappy','facelaugh',
    'faceneutral','facesad','facesurprised','faceunamused','facewink','follow','graduate',
    'growth','growthexp','help','idea','insight','learn','learning','like','link',
    'loud-speaker','make','milestone','momentum','momentumslow','network','new','newsletter',
    'no-substance','prediction','present','product','profile','puppet','question','reach',
    'repost','revenue','risk','rocket','save','send','share','shush','slow','speech',
    'strategy','suited-man','swipe1','swipe2','swipe3','template','tired','trust','video',
    'vote','win','write-comment',
}

def render_glyph_svg(name, colour_hex, px):
    """Render a single glyph in the given colour at px x px, transparent background."""
    svg = open(f'{UP}/glyph-{name}.svg').read()
    svg = re.sub(r'stroke="#[0-9A-Fa-f]{6}"', f'stroke="{colour_hex}"', svg)
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=px, output_height=px)
    return Image.open(io.BytesIO(png)).convert('RGBA')

def render_tile_bg(colour_key, size):
    """Render a squircle background tile at size x size."""
    svg = open(f'{UP}/{BG[colour_key]}').read()
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert('RGBA')

def make_real_tile(glyph, colour_key, size=150):
    """Composite: glyph (white, or charcoal on light tiles) centred on a coloured tile.
    Glyph occupies ~54% of the tile, matching the carousel icon construction."""
    tile = render_tile_bg(colour_key, size)
    gcol = CHARCOAL if colour_key in LIGHT else WHITE
    gpx = int(size * 0.54)
    g = render_glyph_svg(glyph, gcol, gpx)
    out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    out.alpha_composite(tile, (0, 0))
    out.alpha_composite(g, ((size - gpx) // 2, (size - gpx) // 2))
    return out

def make_swipe_chevron(colour_hex, px):
    """The SWIPE cue glyph in a flat colour (no tile)."""
    return render_glyph_svg('swipe1', colour_hex, px)

def export_coloured_png(glyph, colour_hex, px, out_path):
    """Export a single glyph as a flat transparent PNG in one colour.
    Used to produce the white/charcoal/ink pre-coloured set for Canva."""
    render_glyph_svg(glyph, colour_hex, px).save(out_path)
