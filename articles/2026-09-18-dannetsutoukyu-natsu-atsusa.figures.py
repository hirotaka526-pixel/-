# -*- coding: utf-8 -*-
"""「断熱等級を上げれば夏は涼しくなる？」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はアースカラー+淡いグリーン。イラストは使わない方針。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, heading, card, badge)


# ── 図1: 冬(熱が逃げる)と夏(熱が入る)の違い ──────────────────────
def fig_fuyu_natsu_chigai():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '断熱等級(UA値)が主に効くのは、冬の「熱が逃げる」場面です', 18))

    # 左: 冬
    s.append(card(30, 64, 380, 190, SURF, accent=BLUE))
    s.append(txt(220, 100, '冬：室内の熱が外へ逃げる', 16, INK, '700', 'middle'))
    s.append(txt(220, 150, '断熱等級(UA値)が', 14, INK2, '400', 'middle'))
    s.append(txt(220, 176, '直接効く場面', 17, NAVY, '700', 'middle'))
    s.append(txt(220, 218, '壁・屋根・窓からの熱の逃げにくさ', 13, INK2, '400', 'middle'))

    # 右: 夏
    s.append(card(470, 64, 380, 190, SURF, accent=CRIT))
    s.append(txt(660, 100, '夏：日射の熱が外から入る', 16, INK, '700', 'middle'))
    s.append(txt(660, 150, '断熱等級だけでは', 14, INK2, '400', 'middle'))
    s.append(txt(660, 176, '防ぎきれない場面', 17, CRIT_D, '700', 'middle'))
    s.append(txt(660, 218, '窓からの日射熱が中心。日射遮蔽が必要', 13, INK2, '400', 'middle'))

    return wrap(''.join(s), W, H,
                '冬と夏で断熱等級の効き方が違うことを示す図',
                '断熱等級(UA値)が直接効くのは主に冬、室内の熱が外へ逃げる場面。夏は日射によって外から熱が入ってくる場面が中心で、断熱等級だけでは防ぎきれず日射遮蔽が必要になる。')


# ── 図2: 庇の効果(夏は遮り、冬は取り込む) ──────────────────────
def fig_hisashi_kouka():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '庇は、夏の高い日射を遮り、冬の低い日射を取り込みます', 18))

    ground_y = 240
    wall_x = 480
    s.append(f'<line x1="60" y1="{ground_y}" x2="820" y2="{ground_y}" stroke="{INK2}" stroke-width="2"/>')
    # 壁と庇
    s.append(box(wall_x, 100, 24, ground_y - 100, TINT, LINE, 1.5, 2))
    s.append(box(wall_x - 60, 96, 84, 14, NAVY, NAVY, 0, 3))
    s.append(txt(wall_x - 18, 84, '庇', 14, INK, '700', 'middle'))

    # 夏の日射(高い角度、庇で遮られる)
    s.append(f'<line x1="720" y1="110" x2="{wall_x-40}" y2="110" stroke="{CRIT}" stroke-width="2.4" stroke-dasharray="5,4"/>')
    s.append(f'<path d="M{wall_x-46} 110 l10 -4 l0 8 Z" fill="{CRIT}"/>')
    s.append(txt(730, 114, '夏の日射(高い角度)', 13, CRIT_D, '700'))
    s.append(txt(wall_x - 70, 130, '庇で遮る', 14, CRIT_D, '600', 'middle'))

    # 冬の日射(低い角度、窓の奥まで届く)
    s.append(f'<line x1="760" y1="200" x2="{wall_x+40}" y2="150" stroke="{BLUE}" stroke-width="2.4" stroke-dasharray="5,4"/>')
    s.append(f'<path d="M{wall_x+34} 150 l11 -2 l-4 7 Z" fill="{BLUE}"/>')
    s.append(txt(730, 204, '冬の日射(低い角度)', 13, BLUE_M, '700'))
    s.append(txt(wall_x + 70, 165, '室内に届く', 14, BLUE_M, '600', 'middle'))

    s.append(txt(0, 280, '季節による太陽高度の違いを利用した、数値では表れにくい工夫です', 14, INK2, '700'))
    return wrap(''.join(s), W, H,
                '庇の効果を示す図',
                '庇は夏の高い角度の日射を遮り、冬の低い角度の日射は室内に取り込める。季節による太陽高度の違いを利用した工夫で、断熱等級の数値では表れにくいが体感に大きく影響する。')


# ── 図3: 断熱等級の基準(2026年時点) ──────────────────────
def fig_toukyu_kijun():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '断熱等級の基準(2026年時点)', 18))

    rows = [
        ('等級4', 'UA値 0.87以下', '2025年4月以降の法的な最低基準', MUTE),
        ('等級5', 'UA値 0.60以下', 'ZEH基準', BLUE_L),
        ('等級6', 'UA値 0.46以下', 'HEAT20 G2グレード相当', BLUE),
        ('等級7', 'UA値 0.26以下', 'HEAT20 G3グレード相当', NAVY),
    ]
    y0 = 62
    row_h = 50
    for i, (grade, ua, note, color) in enumerate(rows):
        y = y0 + i * row_h
        tcol = SURF if color in (BLUE, NAVY) else INK
        s.append(box(20, y, 840, row_h - 10, color, color, 0, 6))
        s.append(txt(45, y + 26, grade, 16, tcol, '700'))
        s.append(txt(150, y + 26, ua, 15, tcol, '700'))
        s.append(txt(400, y + 26, note, 14, tcol, '400'))
    s.append(txt(0, y0 + 4 * row_h + 20, '※ 2030年には等級5が新たな最低基準になる予定です', 14, INK2, '700'))
    return wrap(''.join(s), W, H,
                '断熱等級の基準一覧(2026年時点)',
                '等級4はUA値0.87以下で2025年4月以降の法的な最低基準、等級5はUA値0.60以下でZEH基準、等級6はUA値0.46以下でHEAT20のG2グレード相当、等級7はUA値0.26以下でHEAT20のG3グレード相当。2030年には等級5が新たな最低基準になる予定。')


FIGURES = {
    'fuyu-natsu-chigai': (fig_fuyu_natsu_chigai, '図1：冬と夏で断熱等級の効き方が違うことを示す図'),
    'hisashi-kouka':     (fig_hisashi_kouka,     '図2：庇の効果を示す図'),
    'toukyu-kijun':      (fig_toukyu_kijun,      '図3：断熱等級の基準一覧(2026年時点)'),
}
