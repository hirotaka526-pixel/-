# -*- coding: utf-8 -*-
"""「間取りを広く見せる工夫」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross)


# ── 図1: 同じ30坪でも使える面積が違う ──────────────────────
def fig_menseki_vs_hiroza():
    W, H = 880, 320
    s = []
    s.append(txt(0, 28, '同じ30坪でも、廊下や壁の量で「使える広さ」が変わります', 17, INK, '700'))

    # 左: 廊下・壁が多い間取り(区切りが多い)
    s.append(txt(220, 60, '廊下・壁で区切られた間取り', 14, INK, '700', 'middle'))
    s.append(box(40, 75, 360, 200, TINT, LINE, 1.5, 8))
    # 内部に小部屋を模した仕切り線を複数
    for x in (150, 260):
        s.append(f'<line x1="{x}" y1="75" x2="{x}" y2="275" stroke="{LINE}" stroke-width="3"/>')
    s.append(f'<line x1="40" y1="175" x2="150" y2="175" stroke="{LINE}" stroke-width="3"/>')
    s.append(box(60, 90, 70, 70, CRIT, CRIT, 0, 4))
    s.append(txt(95, 130, '廊下', 12, SURF, '700', 'middle'))
    s.append(txt(220, 296, 'LDKとして使える面積が小さくなる', 13, CRIT_D, '700', 'middle'))

    # 右: 廊下・壁が少ない間取り(LDK中心)
    s.append(txt(660, 60, '廊下を減らした間取り', 14, GOOD_D, '700', 'middle'))
    s.append(box(480, 75, 360, 200, '#f1faf3', GOOD, 1.5, 8))
    s.append(txt(660, 180, 'LDK', 22, GOOD_D, '700', 'middle'))
    s.append(txt(660, 296, '同じ30坪でも、LDKが広く使える', 13, GOOD_D, '700', 'middle'))
    return wrap(''.join(s), W, H,
                '同じ延床面積でも使える広さが異なる図',
                '同じ30坪でも廊下や壁で細かく区切られた間取りはLDKとして使える面積が小さくなる。廊下を減らした間取りは同じ延床面積でもLDKを広く使える。')


# ── 図2: 広く見せる4つの工夫 ──────────────────────
def fig_kufuu_4tsu():
    W, H = 880, 260
    s = []
    s.append(txt(0, 28, '面積を増やさずに広く感じさせる、4つの工夫', 17, INK, '700'))

    items = [
        ('廊下を減らす', 'LDK・収納に回す'),
        ('建具を減らす', '引き戸・部分オープンに'),
        ('天井を高くする', '勾配天井で縦の広がりを'),
        ('視線を抜く窓配置', '奥まで見通せる位置に'),
    ]
    for i, (title, note) in enumerate(items):
        x = 20 + i * 215
        s.append(box(x, 60, 195, 150, TINT, BLUE, 1.5, 10))
        s.append(txt(x + 97, 100, f'{i+1}', 24, BLUE, '700', 'middle'))
        s.append(txt(x + 97, 135, title, 14, INK, '700', 'middle'))
        s.append(txt(x + 97, 160, note, 12, INK2, '400', 'middle'))
    return wrap(''.join(s), W, H,
                '広く見せる4つの工夫',
                '廊下を減らす、建具を減らす、天井を高くする、視線が抜ける窓配置にするという4つの工夫で面積を増やさずに広く感じさせることができる。')


# ── 図3: 耐力壁と間仕切り壁の違い ──────────────────────
def fig_tairyokuheki():
    W, H = 880, 280
    s = []
    s.append(txt(0, 28, '壁には「抜ける壁」と「抜けない壁」があります', 17, INK, '700'))

    # 左: 耐力壁(抜けない)
    s.append(box(40, 60, 380, 170, '#fdf2f2', CRIT, 1.5, 10))
    s.append(txt(230, 90, '耐力壁', 16, CRIT_D, '700', 'middle'))
    s.append(cross(70, 130, CRIT))
    s.append(txt(90, 135, '見た目だけでは判断できない', 13, INK, '600'))
    s.append(txt(230, 190, '建物を支えている壁', 13, CRIT_D, '600', 'middle'))
    s.append(txt(230, 212, '安易に抜くと耐震性能が低下する', 12, INK2, '400', 'middle'))

    # 右: 間仕切り壁(抜ける)
    s.append(box(460, 60, 380, 170, '#f1faf3', GOOD, 1.5, 10))
    s.append(txt(650, 90, '間仕切り壁', 16, GOOD_D, '700', 'middle'))
    s.append(check(490, 130, GOOD))
    s.append(txt(510, 135, '構造計算に基づいて判断', 13, INK, '600'))
    s.append(txt(650, 190, '部屋を仕切っているだけの壁', 13, GOOD_D, '600', 'middle'))
    s.append(txt(650, 212, '構造上、抜くことができる', 12, INK2, '400', 'middle'))

    s.append(txt(0, 260, 'どちらか見た目だけでは分からず、構造を理解した建築士の判断が必要です', 13, INK2, '700'))
    return wrap(''.join(s), W, H,
                '耐力壁と間仕切り壁の違いの図',
                '耐力壁は建物を支えている壁で見た目だけでは判断できず安易に抜くと耐震性能が低下する。間仕切り壁は部屋を仕切っているだけの壁で構造計算に基づいて抜くことができる。どちらかは構造を理解した建築士の判断が必要。')


FIGURES = {
    'menseki-vs-hiroza': (fig_menseki_vs_hiroza, '図1：同じ延床面積でも使える広さが異なる図'),
    'kufuu-4tsu':        (fig_kufuu_4tsu,        '図2：広く見せる4つの工夫'),
    'tairyokuheki':      (fig_tairyokuheki,      '図3：耐力壁と間仕切り壁の違い'),
}
