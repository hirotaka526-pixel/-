# -*- coding: utf-8 -*-
"""「UA値は、実際の光熱費にどうつながるのか」の図解。

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


# ── 図1: UA値の定義 ──────────────────────
def fig_uachi_teigi():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, 'UA値は、外皮から逃げる熱の量を面積で割った数値です', 18))

    s.append(card(30, 64, 820, 90, TINT, accent=NAVY))
    s.append(txt(60, 98, 'UA値 =', 17, NAVY, '700'))
    s.append(txt(160, 98, '屋根・外壁・床・窓などから逃げる熱の量の合計', 15, INK, '700'))
    s.append(txt(160, 126, '÷ 外皮全体の面積の合計(換気による熱の出入りは含まない)', 14, INK2, '400'))

    s.append(card(30, 180, 380, 70, SURF, accent=GOOD))
    s.append(txt(60, 212, '数値が小さい', 15, GOOD_D, '700'))
    s.append(txt(60, 236, '→ 熱が逃げにくく、断熱性能が高い', 14, INK2, '400'))

    s.append(card(470, 180, 380, 70, SURF, accent=WARN))
    s.append(txt(500, 212, '数値が大きい', 15, WARN_D, '700'))
    s.append(txt(500, 236, '→ 熱が逃げやすく、断熱性能が低い', 14, INK2, '400'))

    return wrap(''.join(s), W, H,
                'UA値の定義',
                'UA値(外皮平均熱貫流率)は、屋根・外壁・床・窓などの外皮から逃げる熱の量の合計を、外皮全体の面積の合計で割った数値。換気による熱の出入りは含まない。数値が小さいほど熱が逃げにくく断熱性能が高い住宅であることを意味する。')


# ── 図2: 光熱費シミュレーション例(長野県試算) ──────────────────────
def fig_kounetsuhi_sisan_rei():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, 'UA値を下げると、暖冷房費が下がった試算例があります(長野県)', 18))

    x0, x1 = 160, 820
    scale_max = 160000
    def sx(v):
        return x0 + (x1 - x0) * v / scale_max

    rows = [
        ('UA値 0.75', 144973, WARN_D, WARN),
        ('UA値 0.23', 82137, GOOD_D, GOOD),
    ]
    row_h = 64
    y0 = 90
    for i, (label, val, color, tint) in enumerate(rows):
        y = y0 + i * row_h
        s.append(txt(0, y + 22, label, 15, INK, '700'))
        bw = sx(val) - x0
        s.append(box(x0, y, bw, 32, tint, color, 1.5, 15))
        rounded = round(val / 1000) * 1000
        s.append(txt(x0 + bw + 10, y + 22, f'約{rounded // 10000}万{(rounded % 10000) // 1000}千円/年', 14, color, '700'))

    s.append(txt(0, y0 + 2 * row_h + 20, '差額：年間約6万3千円(電気料金 1kWhあたり28.46円で試算)', 15, NAVY, '700'))
    s.append(txt(0, y0 + 2 * row_h + 46, '寒冷地・暖房費中心の試算例。地域や電気料金単価によって削減額は変わる', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '長野県が公開している光熱費シミュレーション例',
                '長野県の試算例では、UA値を0.75から0.23まで下げると年間の暖冷房費が約14万5千円から約8万2千円へ下がり、差額は年間約6万3千円。ただし寒冷地・暖房費中心の試算例であり、地域や電気料金単価によって削減額は変わる。')


# ── 図3: 地域区分と断熱等級の基準値(6地域) ──────────────────────
def fig_chiiki_kubun_kijun():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '6地域(名古屋など)では、UA値の基準値はこう変わります', 18))

    rows = [
        ('断熱等級4(現行基準)', '0.87', NAVY, NAVY_L),
        ('断熱等級5', '0.6', BLUE_M, TINT),
    ]
    row_h = 70
    y0 = 80
    for i, (label, val, color, tint) in enumerate(rows):
        y = y0 + i * row_h
        s.append(card(30, y, 600, 54, tint, accent=color))
        s.append(txt(60, y + 34, label, 16, INK, '700'))
        s.append(txt(680, y + 34, f'UA値 {val}', 18, color, '700', 'middle'))

    s.append(txt(0, y0 + 2 * row_h + 36, '高浜市を含む愛知県の多くは6地域に区分されている可能性が高いとされています', 14, MUTE, '400'))
    s.append(txt(0, y0 + 2 * row_h + 58, '(正式な地域区分は国交省の地域区分一覧でご確認ください)', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '6地域における断熱等級とUA値基準値の対応',
                '名古屋市を含む6地域では、現行の省エネ基準(断熱等級4)のUA値は0.87、断熱等級5の基準値は0.6。高浜市を含む愛知県の多くは6地域に区分されている可能性が高いとされるが、正式な地域区分は国交省の地域区分一覧での確認が必要。')


FIGURES = {
    'uachi-teigi':          (fig_uachi_teigi,          '図1：UA値の定義'),
    'kounetsuhi-sisan-rei': (fig_kounetsuhi_sisan_rei, '図2：長野県が公開している光熱費シミュレーション例'),
    'chiiki-kubun-kijun':   (fig_chiiki_kubun_kijun,   '図3：6地域における断熱等級とUA値基準値の対応'),
}
