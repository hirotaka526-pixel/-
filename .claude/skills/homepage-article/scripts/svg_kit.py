# -*- coding: utf-8 -*-
"""記事に埋め込む図解SVGを書くための共通部品。

記事ごとの図解ファイル(articles/<slug>.figures.py)から import して使う。
色は dataviz スキルの検証済みパレットに合わせてある。勝手に増やさないこと。
"""

FONT = '"Hiragino Kaku Gothic ProN","Hiragino Sans","Yu Gothic","Meiryo",sans-serif'

# ── パレット(dataviz reference palette) ──────────────────
NAVY   = '#0d366b'   # blue 700   見出し・強調
BLUE   = '#2a78d6'   # blue 450   中立情報
BLUE_L = '#86b6ef'   # blue 250   ordinalの最淡ステップ(これより淡くしない)
BLUE_M = '#184f95'   # blue 600
GOOD   = '#0ca30c'   # status good
GOOD_D = '#0a5c2e'   # good の濃い文字色
CRIT   = '#d03b3b'   # status critical
CRIT_D = '#8f2b2b'
WARN   = '#fab219'   # status warning
WARN_D = '#6b4d00'
INK    = '#1a1a19'
INK2   = '#52514e'
MUTE   = '#8a8a86'
LINE   = '#d8d8d4'
SURF   = '#ffffff'
TINT   = '#f4f7fb'

# 図の標準幅。880で描き、モバイルでは横スクロールさせる(min-width 660px)
STD_W = 880
MIN_W = 660

# カードの標準角丸・影(box()のr=8はレガシー互換用に残す。新規の図はcard()を使う)
RADIUS = 14
_SHADOW_DEFS = (
    '<filter id="cardShadow" x="-20%" y="-20%" width="140%" height="140%">'
    '<feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0d366b" flood-opacity="0.12"/>'
    '</filter>'
)


def wrap(inner, w, h, title, desc):
    """SVG本体を組み立てる。title/descはスクリーンリーダー用なので必ず書く。"""
    tid = f't{abs(hash(title)) % 99999}'
    did = f'd{abs(hash(desc)) % 99999}'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'role="img" aria-labelledby="{tid} {did}" '
        f'style="width:100%;min-width:{MIN_W}px;height:auto;display:block;font-family:{FONT}">'
        f'<title id="{tid}">{title}</title><desc id="{did}">{desc}</desc>'
        f'<defs>{_SHADOW_DEFS}</defs>'
        f'<rect width="{w}" height="{h}" fill="{SURF}"/>{inner}</svg>'
    )


def txt(x, y, s, size=16, fill=INK, weight='400', anchor='start'):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{s}</text>')


def box(x, y, w, h, fill=SURF, stroke=LINE, sw=1.5, r=8):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def check(x, y, color=GOOD):
    return (f'<path d="M{x} {y} l4 4 l7-9" fill="none" stroke="{color}" '
            f'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')


def cross(x, y, color=CRIT):
    return (f'<path d="M{x-4} {y-4} l9 9 M{x+5} {y-4} l-9 9" fill="none" '
            f'stroke="{color}" stroke-width="2.6" stroke-linecap="round"/>')


def dash(x, y, color=MUTE):
    """「該当しない」ではなく「別の方法で扱う」を表すときの中立マーク。"""
    return (f'<line x1="{x}" y1="{y}" x2="{x+14}" y2="{y}" stroke="{color}" '
            f'stroke-width="2.6" stroke-linecap="round"/>')


def arrow(x, y, color=GOOD, length=26):
    return (f'<path d="M{x} {y} l{length} 0" stroke="{color}" stroke-width="2.4" '
            f'stroke-linecap="round"/>'
            f'<path d="M{x+length-6} {y-5} l6 5 l-6 5" fill="none" stroke="{color}" '
            f'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')


def pill(x, y, w, label, fill, stroke, tcol, size=13):
    return box(x, y, w, 26, fill, stroke, 1.2, 13) + \
           txt(x + w / 2, y + 18, label, size, tcol, '700', 'middle')


def chip(x, y, w, h, label, fill, tcol=SURF, size=15):
    return box(x, y, w, h, fill, fill, 1.5) + \
           txt(x + w / 2, y + h / 2 + 6, label, size, tcol, '700', 'middle')


def card(x, y, w, h, fill=SURF, accent=None, r=RADIUS, shadow=True):
    """box()の上位版。角丸を大きくし、柔らかい影を付ける。

    accentを指定すると、カード上端に4px幅のアクセントバーが入る
    (色分けを「全面塗り」ではなく「アクセント1本」で示すので、白背景+濃い文字が保て、
    ボックスが重く見えない)。囲み線は入れない(影で輪郭が付くため)。
    """
    f = ' filter="url(#cardShadow)"' if shadow else ''
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{f}/>'
    if accent:
        # 上端だけ角丸に沿わせた帯(rectをクリップして重ねる簡易実装)
        s += (f'<clipPath id="ac{abs(hash((x,y,w,h))) % 99999}">'
              f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>'
              f'<rect x="{x}" y="{y}" width="{w}" height="6" fill="{accent}" '
              f'clip-path="url(#ac{abs(hash((x,y,w,h))) % 99999})"/>')
    return s


def badge(cx, cy, r, label, fill=BLUE, tcol=SURF, size=18):
    """円形バッジ。番号(①②③やSTEP数字)をテキストより目立たせたいときに使う。"""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'
            f'{txt(cx, cy + size * 0.36, label, size, tcol, "700", "middle")}')


def check_badge(cx, cy, r=11, color=GOOD):
    """check()の円形バッジ版。小さい線だけより視認性が高い。"""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            f'<path d="M{cx - r*0.45} {cy} l{r*0.35} {r*0.35} l{r*0.6}-{r*0.7}" '
            f'fill="none" stroke="{SURF}" stroke-width="2.2" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def cross_badge(cx, cy, r=11, color=CRIT):
    """cross()の円形バッジ版。"""
    d = r * 0.4
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            f'<path d="M{cx-d} {cy-d} l{2*d} {2*d} M{cx+d} {cy-d} l-{2*d} {2*d}" '
            f'stroke="{SURF}" stroke-width="2.2" stroke-linecap="round"/>')
