# -*- coding: utf-8 -*-
"""「高浜市・西三河で使える住宅補助金」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物の線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。

数字は2026年9月時点でWebSearchにより裏取りしたもの(国の「住宅省エネ2026キャンペーン」
公式サイト、岡崎市公式ホームページ、安城市スマートハウス普及促進補助金交付要綱)。
制度は年度で変わるため、本文・図の両方に「2026年度時点」の注記を必ず入れる。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, NAVY_L,
                     wrap, txt, box, heading, card, badge, check_badge, cross_badge, icon_badge)


# ── 図1: 国の補助金(住宅省エネ2026キャンペーン)の対象別補助額 ──────────────────────
def fig_kuni_hojokin():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, '国の補助金「住宅省エネ2026キャンペーン」対象別の補助額(新築)', 18))

    items = [
        ('GX志向型住宅', '全世帯が対象', '110万円/戸', 'この地域の目安(5〜6地域)', NAVY),
        ('長期優良住宅', '子育て世帯・若者夫婦世帯が対象', '75〜80万円/戸', '', BLUE),
        ('ZEH水準住宅', '子育て世帯・若者夫婦世帯が対象', '35〜40万円/戸', '', BLUE_M),
    ]
    card_w = 266
    for i, (title, cond, amount, note, color) in enumerate(items):
        x = 20 + i * (card_w + 15)
        s.append(card(x, 66, card_w, 220, SURF, accent=color))
        s.append(txt(x + 20, 100, title, 16, INK, '700'))
        s.append(txt(x + 20, 128, cond, 14, INK2, '400'))
        s.append(txt(x + 20, 170, amount, 22, color, '700'))
        if note:
            s.append(txt(x + 20, 196, note, 13, MUTE, '400'))

    s.append(txt(0, H - 40, '※ GX志向型住宅は寒冷地(1〜4地域)で125万円/戸。高浜市・西三河は5〜6地域が目安のため110万円/戸で記載', 14, INK2, '400'))
    s.append(txt(0, H - 18, '※ 2026年度時点の情報。予算上限に達すると年度途中でも終了します', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                '国の補助金「住宅省エネ2026キャンペーン」対象別の補助額',
                'GX志向型住宅は全世帯が対象でこの地域では110万円/戸、長期優良住宅は子育て世帯・若者夫婦世帯が対象で80万円/戸、ZEH水準住宅は同じく対象世帯限定で40万円/戸。2026年度時点の情報で、予算上限に達すると年度途中でも終了する。')


# ── 図2: 高浜市・岡崎市・安城市の独自補助金比較 ──────────────────────
def fig_shi_hikaku():
    W, H = 880, 340
    s = []
    s.append(heading(0, 34, '市独自の補助金は、市によってまったく違う(2026年度時点)', 18))

    rows = [
        ('高浜市', '新築向けの市独自補助金は、今のところ確認されていません', '(リフォーム向けの制度は別にあります)', MUTE, TINT),
        ('岡崎市', '岡崎市産材住宅建設事業費補助金', '主要構造材や内装材に地元の木材を使うと最大30万円', FOREST, FOREST_L),
        ('安城市', 'スマートハウス普及促進補助金', '太陽光+蓄電池+HEMSを併せて導入すると最大21万円', NAVY, NAVY_L),
    ]
    y0 = 70
    row_h = 78
    for i, (name, title, note, color, tint) in enumerate(rows):
        y = y0 + i * row_h
        s.append(card(20, y, 840, row_h - 12, SURF, accent=color, shadow=False))
        s.append(icon_badge(45, y + (row_h - 12) / 2 - 17, 34, color, tint))
        s.append(txt(95, y + 32, name, 16, INK, '700'))
        s.append(txt(190, y + 24, title, 15, INK if color != MUTE else INK2, '700'))
        s.append(txt(190, y + 48, note, 14, INK2, '400'))

    return wrap(''.join(s), W, H,
                '高浜市・岡崎市・安城市の独自補助金比較',
                '高浜市には新築向けの市独自補助金は今のところ確認されていない。岡崎市には岡崎市産材住宅建設事業費補助金があり、主要構造材や内装材に地元の木材を使うと最大30万円。安城市にはスマートハウス普及促進補助金があり、太陽光・蓄電池・HEMSを併せて導入すると最大21万円。いずれも2026年度時点の情報。')


# ── 図3: 補助金を使うときの注意点(申請タイミング) ──────────────────────
def fig_shinsei_timing():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '補助金の多くは、着工前の申請が必要です', 18))

    s.append(card(30, 64, 380, 150, SURF, accent=CRIT))
    s.append(cross_badge(70, 104, 12, CRIT))
    s.append(txt(96, 110, '着工してから申請しようとした', 15, INK, '700'))
    s.append(txt(70, 145, '対象外になり、補助を受けられないことがある', 14, INK2, '400'))
    s.append(txt(70, 170, '(契約・着工前の申請が前提の制度が多いため)', 13, MUTE, '400'))

    s.append(card(470, 64, 380, 150, SURF, accent=GOOD))
    s.append(check_badge(510, 104, 12, GOOD))
    s.append(txt(536, 110, '契約前に使える補助金を確認した', 15, INK, '700'))
    s.append(txt(510, 145, '申請のタイミングを逃さず利用できる', 14, INK2, '400'))
    s.append(txt(510, 170, '(予算上限による早期終了のリスクも減らせる)', 13, MUTE, '400'))

    s.append(txt(0, H - 18, 'この一手間があるかどうかで、使える補助金の額が大きく変わります', 14, INK2, '700'))
    return wrap(''.join(s), W, H,
                '補助金の申請タイミングの注意点',
                '補助金の多くは契約・着工前の申請が前提になっている。着工してから申請しようとすると対象外になり補助を受けられないことがある一方、契約前に使える補助金を確認しておけば申請のタイミングを逃さず利用でき、予算上限による早期終了のリスクも減らせる。')


FIGURES = {
    'kuni-hojokin':     (fig_kuni_hojokin,     '図1：国の補助金「住宅省エネ2026キャンペーン」対象別の補助額'),
    'shi-hikaku':        (fig_shi_hikaku,        '図2：高浜市・岡崎市・安城市の独自補助金比較'),
    'shinsei-timing':    (fig_shinsei_timing,    '図3：補助金の申請タイミングの注意点'),
}
