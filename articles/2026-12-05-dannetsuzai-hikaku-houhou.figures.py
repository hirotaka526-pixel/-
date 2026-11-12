# -*- coding: utf-8 -*-
"""「断熱材は、熱伝導率だけで比べると判断を誤る」の図解。

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


# ── 図1: 断熱材の比較計算(熱伝導率だけでは逆転する例) ──────────────────────
def fig_dannetsuzai_hikaku_keisan():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '熱伝導率だけで比べると、実際の性能とは逆の順番になることがあります', 18))

    headers = ['', '厚み', '熱伝導率', '熱抵抗値(厚み÷熱伝導率)']
    col_x = [0, 180, 340, 520]
    s.append(txt(col_x[0], 68, '断熱材', 14, MUTE, '700'))
    s.append(txt(col_x[1], 68, '厚み', 14, MUTE, '700'))
    s.append(txt(col_x[2], 68, '熱伝導率', 14, MUTE, '700'))
    s.append(txt(col_x[3], 68, '熱抵抗値', 14, MUTE, '700'))

    rows = [
        ('A', '50mm', '0.024', '2.08', WARN_D, TINT),
        ('B', '100mm', '0.036', '2.77', BLUE_M, TEAL_L),
        ('C', '120mm', '0.040', '3.00', GOOD_D, FOREST_L),
    ]
    row_h = 54
    y0 = 84
    for i, (name, thick, lam, r, color, tint) in enumerate(rows):
        y = y0 + i * row_h
        s.append(card(0, y, 820, row_h - 8, tint, accent=color, r=10))
        s.append(txt(col_x[0] + 24, y + 32, f'断熱材{name}', 16, color, '700'))
        s.append(txt(col_x[1] + 20, y + 32, thick, 15, INK, '400'))
        s.append(txt(col_x[2] + 20, y + 32, lam, 15, INK, '400'))
        s.append(txt(col_x[3] + 20, y + 32, r, 18, color, '700'))

    s.append(txt(0, y0 + 3 * row_h + 20, '熱伝導率だけならA→B→Cの順に性能が良く見えるが、熱抵抗値で比べるとC→B→Aの順になる', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '断熱材の比較計算例',
                '厚さ50mm・熱伝導率0.024の断熱材A、厚さ100mm・熱伝導率0.036のB、厚さ120mm・熱伝導率0.040のCを熱抵抗値(厚み÷熱伝導率)で計算すると、A=2.08、B=2.77、C=3.00となり、熱伝導率だけで見た順番とは逆の結果になる。')


# ── 図2: 気密性と結露の悪循環 ──────────────────────
def fig_kimitsu_kekkai_akujunkan():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '隙間があると、結露からの悪循環が始まります', 18))

    steps = ['隙間から\n冷気が侵入', '結露が\n発生', 'カビ・ダニ\n発生', '断熱材が\n水分を吸収', '断熱性能が\n低下']
    n = len(steps)
    card_w = 150
    total_w = n * card_w + (n - 1) * 20
    x0 = (880 - total_w) / 2
    y0 = 90
    card_h = 90
    for i, label in enumerate(steps):
        x = x0 + i * (card_w + 20)
        color = CRIT_D if i >= 2 else WARN_D
        tint = '#f7e9e6' if i >= 2 else TINT
        s.append(card(x, y0, card_w, card_h, tint, accent=color, r=10))
        lines = label.split('\n')
        for j, line in enumerate(lines):
            s.append(txt(x + card_w / 2, y0 + 42 + j * 22, line, 14, color, '700', 'middle'))
        if i < n - 1:
            s.append(arrow(x + card_w + 2, y0 + card_h / 2, MUTE, 16))

    s.append(txt(x0 + total_w / 2, y0 - 16, '↑ さらに冷気が入りやすくなり、この輪を繰り返す', 13, MUTE, '400', 'middle'))
    s.append(txt(0, y0 + card_h + 36, '窓の結露対策だけでは、壁の中など見えない場所の結露までは防げない', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '気密性と結露の悪循環',
                '隙間から冷気が侵入すると結露が発生し、カビ・ダニが発生、断熱材が水分を吸収して断熱性能が低下し、さらに冷気が入りやすくなるという悪循環が起きる。窓の結露対策だけでは、壁の中など見えない場所の結露までは防げない。')


# ── 図3: 断熱性能を決める3つの視点 ──────────────────────
def fig_dannetsu_seino_3shiten():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '断熱性能は、窓だけでなく3つの視点で決まります', 18))

    items = [
        ('① 断熱材', '熱伝導率だけでなく、厚みまで含めた熱抵抗値で比較する', NAVY, NAVY_L),
        ('② 気密性能', '隙間をなくし、結露からの悪循環を防ぐ前提を整える', BLUE_M, TEAL_L),
        ('③ 換気計画', '換気量だけでなく、室内の空気がうまく対流するよう計画する', GOLD_D, TINT),
    ]
    row_h, gap = 64, 12
    y0 = 70
    for i, (label, desc, color, tint) in enumerate(items):
        y = y0 + i * (row_h + gap)
        s.append(card(0, y, 880, row_h, tint, accent=color))
        s.append(txt(26, y + 28, label, 16, color, '700'))
        s.append(txt(26, y + 50, desc, 14, INK2, '400'))

    return wrap(''.join(s), W, H,
                '断熱性能を決める3つの視点',
                '断熱性能は窓だけでなく、断熱材(熱抵抗値)、気密性能、換気計画の3つの視点で決まる。')


FIGURES = {
    'dannetsuzai-hikaku-keisan':  (fig_dannetsuzai_hikaku_keisan,  '図1：断熱材の比較計算例'),
    'kimitsu-kekkai-akujunkan':   (fig_kimitsu_kekkai_akujunkan,   '図2：気密性と結露の悪循環'),
    'dannetsu-seino-3shiten':     (fig_dannetsu_seino_3shiten,     '図3：断熱性能を決める3つの視点'),
}
