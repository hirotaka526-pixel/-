# -*- coding: utf-8 -*-
"""記事に埋め込む図解SVGを書くための共通部品。

記事ごとの図解ファイル(articles/<slug>.figures.py)から import して使う。
色はインザホームのブランドイメージ(アースカラー基調+淡いグリーン、2026年9月改訂)に
合わせてある。WCAGコントラスト比を確認済み。勝手に増やさないこと。

変数名(NAVY/BLUE/BLUE_L/BLUE_M)は旧パレット(青系)からの互換のため残しているが、
値はアース・グリーン系に変更済み。過去の記事のfigures.pyはコード変更なしで
新パレットに切り替わる(再度 export_png.py を実行すれば新しい配色でPNGが出力される)。
"""

FONT = '"Hiragino Kaku Gothic ProN","Hiragino Sans","Yu Gothic","Meiryo",sans-serif'

# ── パレット(アースカラー基調+淡いグリーン。2026年9月、まえちゃんの指定) ──
# 「NAVY/BLUE」等の変数名は互換のため維持。中身はグリーン系のブランドカラー
NAVY   = '#3d5c34'   # 旧NAVY相当 → ブランドの濃いグリーン(見出し・強調・バッジの地色)
BLUE   = '#6f9c5f'   # 旧BLUE相当 → ブランドの中間グリーン(中立情報・アクセントバー)
BLUE_L = '#cfe0bd'   # 旧BLUE_L相当 → 淡いグリーン(塗り面・薄いフィル用。「淡い感じ」の主役)
BLUE_M = '#517a44'   # 旧BLUE_M相当 → やや濃いグリーン(BLUEより強調したい時)
GREEN_D, GREEN, GREEN_L, GREEN_M = NAVY, BLUE, BLUE_L, BLUE_M  # 分かりやすい別名(新規コードではこちらを推奨)
TAN    = '#b98a55'   # アースカラーの木目・土色アクセント(屋根・木材などのイラストに)
TAN_D  = '#7c5c34'   # TANの濃色(文字用)
GOOD   = '#4d7a3f'   # status good(ブランドグリーンと同系統でまとめる)
GOOD_D = '#2e4a26'   # good の濃い文字色
CRIT   = '#b3402c'   # status critical(赤ではなくテラコッタ寄りの暖色でアースカラーに馴染ませる)
CRIT_D = '#7a2a1c'
WARN   = '#b8811f'   # status warning(マスタード系)
WARN_D = '#6b4a10'
INK    = '#332e26'   # 本文の黒に相当。純黒ではなく温かみのある焦げ茶黒
INK2   = '#5c5748'
MUTE   = '#8f8874'
LINE   = '#ddd7c4'   # 境界線。暖色寄りのグレー
SURF   = '#fbf9f4'   # 背景。純白ではなくアイボリー寄り
TINT   = '#eef1e4'   # 薄い塗り面。淡いグリーン寄りのクリーム

# 図の標準幅。880で描き、モバイルでは横スクロールさせる(min-width 660px)
STD_W = 880
MIN_W = 660

# カードの標準角丸・影(box()のr=8はレガシー互換用に残す。新規の図はcard()を使う)
RADIUS = 14
_SHADOW_DEFS = (
    '<filter id="cardShadow" x="-20%" y="-20%" width="140%" height="140%">'
    f'<feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="{NAVY}" flood-opacity="0.14"/>'
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


def txt(x, y, s, size=16, fill=INK, weight='400', anchor='start', spacing=None):
    sp = f' letter-spacing="{spacing}"' if spacing else ''
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}"{sp}>{s}</text>')


def heading(x, y, s, size=18, fill=INK, accent=NAVY):
    """図解タイトル用の見出し。左に小さいアクセントの角丸バーを添えて、
    ただの黒文字よりデザイン性を出す。本文中のtxt()と役割を分けるために用意。
    """
    return (f'<rect x="{x}" y="{y - size * 0.78}" width="5" height="{size * 0.95}" '
            f'rx="2.5" fill="{accent}"/>'
            f'{txt(x + 14, y, s, size, fill, "700")}')


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


# house_icon()は2026年9月に試作したが、まえちゃんのイメージと合わず不採用。
# イラスト要素は使わない方針。図解はテキスト・図形・数値の可視化に徹すること。
