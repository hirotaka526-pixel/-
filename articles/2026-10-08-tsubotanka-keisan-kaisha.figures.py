# -*- coding: utf-8 -*-
"""「坪単価の計算方法は、会社によって違います」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, icon_badge)


# ── 図1: 同じ建物でも、割る面積で坪単価の見え方が変わる ──────────────────────
def fig_menseki_kijun_2tsu():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '同じ建物でも、割る面積が違うと坪単価の見え方が変わります', 18))

    s.append(card(30, 64, 380, 170, SURF, accent=NAVY))
    s.append(txt(220, 100, '延床面積(40坪)で割ると', 16, INK, '700', 'middle'))
    s.append(txt(220, 130, '本体価格3,000万円 ÷ 40坪', 14, INK2, '400', 'middle'))
    s.append(txt(220, 168, '坪単価 約75万円', 22, NAVY, '700', 'middle'))
    s.append(txt(220, 202, '法律上の基準で、どの会社でも同じ数値', 14, MUTE, '400', 'middle'))

    s.append(card(470, 64, 380, 170, SURF, accent=WARN))
    s.append(txt(660, 100, '施工面積(45坪)で割ると', 16, INK, '700', 'middle'))
    s.append(txt(660, 130, '本体価格3,000万円 ÷ 45坪', 14, INK2, '400', 'middle'))
    s.append(txt(660, 168, '坪単価 約66.7万円', 22, WARN_D, '700', 'middle'))
    s.append(txt(660, 202, '同じ建物・同じ価格でも低く見える', 14, MUTE, '400', 'middle'))

    return wrap(''.join(s), W, H,
                '同じ建物でも割る面積が違うと坪単価の見え方が変わる図',
                '本体価格3,000万円の同じ建物でも、延床面積40坪で割ると坪単価は約75万円になる。一方、ベランダやポーチなどを含む施工面積45坪で割ると坪単価は約66.7万円になり、同じ建物・同じ価格でも坪単価が低く見える。')


# ── 図2: 延床面積と施工面積、入るか入らないか ──────────────────────
def fig_menseki_hanni_itiran():
    W = 880
    s = []
    s.append(heading(0, 34, 'バルコニーやロフトは、延床面積と施工面積で扱いが変わります', 18))

    s.append(txt(560, 72, '延床面積', 15, INK, '700', 'middle'))
    s.append(txt(760, 72, '施工面積', 15, INK, '700', 'middle'))

    items = [
        ('バルコニー', 'cross', 'check'),
        ('玄関ポーチ', 'cross', 'check'),
        ('ロフト(条件により異なる)', 'dash', 'check'),
        ('吹き抜け(屋根のない部分)', 'cross', 'check'),
    ]
    row_h = 58
    y0 = 112
    for i, (label, a, b) in enumerate(items):
        y = y0 + i * row_h
        s.append(txt(20, y, label, 15, INK, '700'))
        if a == 'cross':
            s.append(cross_badge(560, y - 6, 11, CRIT))
        else:
            s.append(dash(550, y - 6, MUTE))
        s.append(check_badge(760, y - 6, 11, GOOD))

    H = y0 + 3 * row_h + 50
    return wrap(''.join(s), W, H,
                'バルコニーやロフトなど、延床面積と施工面積で扱いが変わる項目の一覧',
                'バルコニー・玄関ポーチ・吹き抜け(屋根のない部分)は、法律上の延床面積には入らないことが多いが、施工面積には含める会社が多い。ロフトは条件によって延床面積に含まれるかどうかが変わる。')


# ── 図3: 本体工事費に含まれるかどうかが分かれやすい項目 ──────────────────────
def fig_honntai_hani_itiran():
    W = 880
    s = []
    s.append(heading(0, 34, '本体工事費に含まれるかどうかも、会社によって分かれやすい項目です', 18))

    items = [
        ('照明器具・カーテンレール', '標準仕様に含む会社と、別途費用になる会社があります'),
        ('給排水・ガスの屋外配管', '本体価格に含む範囲が会社によって違います'),
        ('地盤改良費', '契約後に追加費用として発生することが多い項目です'),
        ('外構・諸費用', '本体価格にはほとんど含まれないのが一般的です'),
    ]
    row_h = 64
    y0 = 108
    for i, (label, note) in enumerate(items):
        y = y0 + i * row_h
        s.append(icon_badge(20, y - 18, 32, WARN_D, NAVY_L, 'building'))
        s.append(txt(70, y - 2, label, 15, INK, '700'))
        s.append(txt(70, y + 18, note, 14, INK2, '400'))

    H = y0 + 3 * row_h + 56
    return wrap(''.join(s), W, H,
                '本体工事費に含まれるかどうかが会社によって分かれやすい項目の一覧',
                '照明器具やカーテンレール、給排水・ガスの屋外配管は、標準仕様に含む会社と別途費用になる会社がある。地盤改良費は契約後に追加費用として発生することが多く、外構・諸費用は本体価格にはほとんど含まれないのが一般的である。')


FIGURES = {
    'menseki-kijun-2tsu':  (fig_menseki_kijun_2tsu,  '図1：同じ建物でも割る面積が違うと坪単価の見え方が変わる'),
    'menseki-hanni-itiran': (fig_menseki_hanni_itiran, '図2：バルコニーやロフトなど、延床面積と施工面積で扱いが変わる項目'),
    'honntai-hani-itiran':  (fig_honntai_hani_itiran,  '図3：本体工事費に含まれるかどうかが分かれやすい項目'),
}
