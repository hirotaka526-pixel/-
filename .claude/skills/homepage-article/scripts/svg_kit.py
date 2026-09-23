# -*- coding: utf-8 -*-
"""記事に埋め込む図解SVGを書くための共通部品。

記事ごとの図解ファイル(articles/<slug>.figures.py)から import して使う。
色はインザホームのブランドイメージ(ネイビー基調+ゴールドアクセント+複数色、
2026年9月改訂)に合わせてある。WCAGコントラスト比を確認済み。勝手に増やさないこと。

変数名(NAVY/BLUE/BLUE_L/BLUE_M)は旧パレット(青系→アースグリーン系)からの互換のため
残しているが、値はネイビー・ゴールド系に変更済み。過去の記事のfigures.pyはコード変更
なしで新パレットに切り替わる(再度 export_png.py を実行すれば新しい配色でPNGが出力される)。
"""

FONT = '"Hiragino Kaku Gothic ProN","Hiragino Sans","Yu Gothic","Meiryo",sans-serif'

# ── パレット(ネイビー基調+ゴールドアクセント+複数色。2026年9月、まえちゃんの指定) ──
# 「NAVY/BLUE/BLUE_L/BLUE_M」等の変数名は互換のため維持。中身はネイビー・ゴールド系
NAVY   = '#1b3a5c'   # ブランドの濃いネイビー(見出し・強調・バッジの地色。主色)
BLUE   = '#2f6b52'   # 3色比較の2色目(深緑寄り。旧「BLUE」を差し替え)
BLUE_L = '#e2e8ee'   # 淡いネイビー系のフィル用(「淡い感じ」の背景・薄い塗り面)
BLUE_M = '#1f6d77'   # 3色比較の3色目(ティール。BLUEより寒色寄りで差別化)
GREEN_D, GREEN, GREEN_L, GREEN_M = NAVY, BLUE, BLUE_L, BLUE_M  # 分かりやすい別名(互換維持用)
NAVY_L = '#e2e8ee'   # NAVYの淡色(アイコン地・薄いフィル)
FOREST   = BLUE       # 新規コードではこちらの名前を推奨(3色比較の2色目=深緑)
FOREST_L = '#e1ebe5'  # FORESTの淡色
TEAL     = BLUE_M     # 新規コードではこちらの名前を推奨(3色比較の3色目)
TEAL_L   = '#e0edee'  # TEALの淡色
MULTI  = [NAVY, FOREST, TEAL]  # 3項目を色分けするときはこの順で使う
GOLD   = '#c99a2e'   # アクセントカラー(タイトル下のバー、強調に使う暖色)
GOLD_D = '#8a6a1a'
TAN    = GOLD         # 互換用(木目・土色アクセントとして使っていた箇所はGOLDに統一)
TAN_D  = GOLD_D
GOOD   = '#3f9142'   # status good(明快なグリーン)
GOOD_D = '#256b2c'
CRIT   = '#c0392b'   # status critical(はっきりした赤)
CRIT_D = '#8a2f22'
WARN   = '#b8862a'   # status warning(アンバー系。GOLDより少し濃い)
WARN_D = '#7a5a17'
INK    = '#22303f'   # 本文の黒に相当。ネイビー寄りの濃いグレー
INK2   = '#5b6673'
MUTE   = '#8b93a0'
LINE   = '#dde3ea'   # 境界線。寒色寄りの淡いグレー
SURF   = '#ffffff'   # 背景。純白
TINT   = '#eef2f6'   # 薄い塗り面。淡いネイビー寄りのグレー

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


def heading(x, y, s, size=18, fill=NAVY, accent=GOLD):
    """図解タイトル用の見出し。左に小さいアクセントの角丸バーを添えて、
    ただの黒文字よりデザイン性を出す。本文中のtxt()と役割を分けるために用意。
    文字色はNAVY、アクセントバーはGOLDが標準(2026年9月改訂)。
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
# ただし2026年9月の参考画像で「建物・地図ピンなどの簡素な線画アイコン」は
# 使ってよいと確認が取れたため、以下の line-icon 系は使用可(家の絵を描くのとは別物、
# 情報を示す記号としてのアイコンに徹すること。装飾的なイラストにはしない)。


def building_icon(cx, cy, size=22, color=NAVY):
    """簡易な建物(市役所・役場)の線画アイコン。(cx,cy)を中心に描く。"""
    w, h = size, size * 0.88
    x0, y0 = cx - w / 2, cy - h / 2
    roof_h = h * 0.3
    body_y = y0 + roof_h
    body_h = h - roof_h
    sw = max(1.6, size * 0.09)
    s = [
        f'<path d="M{x0 - 2} {body_y} L{cx} {y0} L{x0 + w + 2} {body_y}" '
        f'fill="none" stroke="{color}" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round"/>',
        f'<rect x="{x0}" y="{body_y}" width="{w}" height="{body_h}" '
        f'fill="none" stroke="{color}" stroke-width="{sw}" rx="{size*0.06}"/>',
    ]
    for i in range(3):
        lx = x0 + w * 0.22 + i * (w * 0.28)
        s.append(f'<line x1="{lx}" y1="{body_y + body_h*0.2}" x2="{lx}" y2="{body_y + body_h*0.82}" '
                  f'stroke="{color}" stroke-width="{sw*0.75}" stroke-linecap="round"/>')
    return ''.join(s)


def pin_icon(cx, cy, size=22, color=NAVY):
    """簡易な地図ピンの線画アイコン。(cx,cy)を中心(ピン全体の中心)に描く。"""
    r = size * 0.32
    top = cy - size * 0.42
    sw = max(1.6, size * 0.09)
    return (
        f'<path d="M{cx} {top} a{r} {r} 0 0 1 {r} {r} c0 {r*1.4} -{r} {size*0.58} -{r} {size*0.58} '
        f'c0 0 -{r} -{size*0.58-r*1.4} -{r} -{size*0.58} a{r} {r} 0 0 1 {r} -{r}z" '
        f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>'
        f'<circle cx="{cx}" cy="{top + r}" r="{r*0.42}" fill="{color}"/>'
    )


def icon_badge(x, y, size, color, tint=None, icon='building'):
    """角丸正方形の淡色地に、線画アイコンを乗せたバッジ。表の左端などに使う。

    tintを省略した場合はNAVY_L相当(呼び出し側で行の色に合わせたtintを渡すのが望ましい)。
    """
    tint = tint or NAVY_L
    fn = pin_icon if icon == 'pin' else building_icon
    return (
        f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{size*0.22}" fill="{tint}"/>'
        f'{fn(x + size / 2, y + size / 2, size * 0.56, color)}'
    )
