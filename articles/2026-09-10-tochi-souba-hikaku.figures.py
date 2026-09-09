# -*- coding: utf-8 -*-
"""「高浜市・西三河・知多で土地を探すなら？」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
坪単価は複数の公開情報源（SUUMO・ハウスボカン・tochidai.info等）の目安レンジの中間値。
実際の数値は駅からの距離・区画によって大きく変動するため、あくまで比較用の推定値。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box)

# 市, 坪単価レンジ下限, 坪単価レンジ上限(万円) ※中間値をグラフに使用。昇順。
CITIES = [
    ('碧南市', 25, 28),
    ('半田市', 26, 29),
    ('高浜市', 33, 36),
    ('安城市', 48, 54),
    ('大府市', 50, 53),
    ('刈谷市', 54, 62),
]


def _hbar_chart(title, desc, heading, unit_label, values, value_fmt, note):
    """横棒グラフの共通処理。values: [(label, value, is_highlight)]"""
    W = 880
    row_h = 46
    top = 70
    H = top + row_h * len(values) + 50
    s = []
    s.append(txt(0, 28, heading, 17, INK, '700'))
    s.append(txt(0, 50, note, 12, INK2))

    max_v = max(v for _, v, _ in values) * 1.15
    track_x, track_w = 140, 560

    for i, (label, v, hi) in enumerate(values):
        y = top + i * row_h
        bar_w = track_w * v / max_v
        color = NAVY if hi else BLUE
        s.append(txt(track_x - 14, y + 24, label, 14, INK, '700', 'end'))
        s.append(box(track_x, y + 6, track_w, 26, TINT, LINE, 1, 4))
        s.append(box(track_x, y + 6, bar_w, 26, color, color, 0, 4))
        s.append(txt(track_x + bar_w + 12, y + 24, value_fmt(v), 14, color, '700'))

    s.append(txt(0, H - 18, unit_label, 12, INK2))
    return wrap(''.join(s), W, H, title, desc)


# ── 図1: 6市の土地坪単価比較 ──────────────────────
def fig_tochi_souba_hikaku():
    values = [(city, (lo + hi) / 2, city == '高浜市') for city, lo, hi in CITIES]
    return _hbar_chart(
        '西三河・知多6市の土地坪単価比較（目安）',
        '碧南市・半田市が坪25万から29万円程度と比較的落ち着いた水準である一方、刈谷市は坪54万から62万円程度と6市の中で最も高く、隣接する市でも坪単価に2倍以上の差がある。',
        '西三河・知多6市の土地坪単価比較（目安）',
        '※ 公開データ（公示地価・不動産情報サイト）の目安レンジの中間値。実際は駅からの距離や区画で変動します',
        values,
        lambda v: f'約{v:.1f}万円/坪',
        '',
    )


# ── 図2: 100坪購入時の総額比較 ──────────────────────
def fig_tochi_gokei_hikaku():
    values = [(city, (lo + hi) / 2 * 100, city == '高浜市') for city, lo, hi in CITIES]
    return _hbar_chart(
        '100坪の土地を買う場合の総額比較（目安）',
        '碧南市や半田市であれば2600万円台で買える広さの土地が刈谷市では5800万円程度になる計算で、エリアによって土地の総額に3000万円以上の差が出ることがある。',
        '同じ100坪の土地でも、総額はこれだけ変わる（目安）',
        '※ 坪単価の目安×100坪で計算した参考値。実際の総額は個別の土地ごとに確認してください',
        values,
        lambda v: f'約{v/10000:.2f}億円' if v >= 10000 else f'約{v:.0f}万円',
        '',
    )


FIGURES = {
    'tochi-souba-hikaku':  (fig_tochi_souba_hikaku,  '図1：西三河・知多6市の土地坪単価比較'),
    'tochi-gokei-hikaku':  (fig_tochi_gokei_hikaku,  '図2：100坪購入時の総額比較'),
}
