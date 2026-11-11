# -*- coding: utf-8 -*-
"""「新築の収納アイデア、暮らしに合わせて選ぶ5つの工夫」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD, GOLD_D,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, arrow, icon_badge, pin_icon,
                     building_icon)


# ── 図1: 5つの収納タイプ、何に向いているか ──────────────────────
def fig_shuunou_5type_ichiran():
    W, H = 880, 450
    s = []
    s.append(heading(0, 34, '5つの収納タイプは、それぞれ向いている暮らし方が違います', 18))

    items = [
        ('① 室内物干し収納', '入れ替わりの早い衣類・タオルを、物干し下のカウンターへ', NAVY, NAVY_L),
        ('② 土間収納', '靴のまま出入り。資源ゴミの一時置き場やかさばる物にも', BLUE, FOREST_L),
        ('③ パントリー', '食品庫に加え、冷蔵庫・冷凍庫を隠してLDKをすっきりと', BLUE_M, TEAL_L),
        ('④ ファミリークローゼット', '家族共有の衣類収納。分け方より置き場所が使われる鍵', GOLD_D, TINT),
        ('⑤ 壁面活用収納', '壁の厚みを利用。断熱材のない間仕切り壁でのみ可能', CRIT_D, '#f7e9e6'),
    ]
    row_h, gap = 64, 10
    y0 = 70
    for i, (label, desc, color, tint) in enumerate(items):
        y = y0 + i * (row_h + gap)
        s.append(card(0, y, 880, row_h, tint, accent=color))
        s.append(txt(26, y + 28, label, 16, color, '700'))
        s.append(txt(26, y + 50, desc, 14, INK2, '400'))

    return wrap(''.join(s), W, H,
                '5つの収納タイプの一覧',
                '室内物干し収納、土間収納、パントリー、ファミリークローゼット、壁面活用収納の5つは、それぞれ向いている暮らし方が異なる。')


# ── 図2: パントリーに家電を隠すとLDKがどう変わるか ──────────────────────
def fig_pantry_before_after():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, 'パントリーに冷蔵庫・冷凍庫を収めると、LDKの印象が変わります', 18))

    # 左: 家電がLDKに見える状態
    s.append(card(30, 70, 380, 170, '#f7e9e6', accent=WARN_D))
    s.append(txt(220, 102, 'LDKに家電が見える', 16, WARN_D, '700', 'middle'))
    s.append(box(90, 130, 110, 60, SURF, WARN_D, 1.5, 10))
    s.append(txt(145, 164, '冷蔵庫', 14, WARN_D, '700', 'middle'))
    s.append(box(250, 130, 110, 60, SURF, WARN_D, 1.5, 10))
    s.append(txt(305, 164, '冷凍庫', 14, WARN_D, '700', 'middle'))
    s.append(txt(220, 220, '冷蔵庫・家電の存在感が大きい', 14, INK2, '400', 'middle'))

    # 右: パントリーに隠れた状態
    s.append(card(470, 70, 380, 170, FOREST_L, accent=BLUE))
    s.append(txt(660, 102, 'パントリーの中に収める', 16, BLUE, '700', 'middle'))
    s.append(box(560, 140, 200, 70, SURF, BLUE, 1.5, 10))
    s.append(txt(660, 170, '冷蔵庫', 14, BLUE, '700', 'middle'))
    s.append(txt(660, 190, '冷凍庫', 14, BLUE, '700', 'middle'))
    s.append(txt(660, 220, 'LDKからは見えない', 14, INK2, '400', 'middle'))

    s.append(arrow(420, 155, MUTE, 36))

    s.append(txt(0, 266, 'どちらを優先するかは暮らし方次第。正解が決まっているわけではない', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                'パントリー収納による家電の見え方の違い',
                '冷蔵庫や冷凍庫をLDKに置くとその存在感が大きくなるが、パントリーの中に収めればLDKからは見えなくなり、すっきりした印象になる。どちらを優先するかは暮らし方次第。')


# ── 図3: 壁面活用収納ができる場所・できない場所 ──────────────────────
def fig_kabekatsuyou_kanou_fukanou():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '壁面活用収納は、外壁ではできず、断熱材のない間仕切り壁でのみ可能です', 18))

    s.append(card(30, 70, 380, 140, '#f7e9e6', accent=CRIT_D))
    s.append(txt(220, 100, '外壁', 17, CRIT_D, '700', 'middle'))
    s.append(txt(220, 128, '断熱材が入っている', 14, INK, '400', 'middle'))
    s.append(txt(220, 150, 'くり抜くと断熱性能が低下するため', 14, INK2, '400', 'middle'))
    s.append(txt(220, 172, '壁面収納は作れない', 15, CRIT_D, '700', 'middle'))

    s.append(card(470, 70, 380, 140, FOREST_L, accent=GOOD_D))
    s.append(txt(660, 100, '室内の間仕切り壁', 17, GOOD_D, '700', 'middle'))
    s.append(txt(660, 128, '断熱材が入っていない', 14, INK, '400', 'middle'))
    s.append(txt(660, 150, '奥行き約10cm程度の', 14, INK2, '400', 'middle'))
    s.append(txt(660, 172, '壁面収納が作れる', 15, GOOD_D, '700', 'middle'))

    s.append(txt(0, 238, '筋交いや耐力面材が入っている壁は、間仕切り壁でも開口を開けられない。希望する場所は設計の早い段階で建築士に伝える', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '壁面活用収納ができる場所とできない場所',
                '外壁は断熱材が入っているため壁面活用収納は作れない。断熱材のない室内の間仕切り壁でのみ、奥行き約10cm程度の壁面収納が作れる。ただし筋交いや耐力面材が入っている壁は開口を開けられないため、早めに建築士へ相談する必要がある。')


FIGURES = {
    'shuunou-5type-ichiran':       (fig_shuunou_5type_ichiran,       '図1：5つの収納タイプの一覧'),
    'pantry-before-after':         (fig_pantry_before_after,         '図2：パントリー収納による家電の見え方の違い'),
    'kabekatsuyou-kanou-fukanou':  (fig_kabekatsuyou_kanou_fukanou,  '図3：壁面活用収納ができる場所とできない場所'),
}
