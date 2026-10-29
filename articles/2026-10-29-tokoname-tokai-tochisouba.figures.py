# -*- coding: utf-8 -*-
"""「常滑市・東海市、土地相場は市内でも差が大きい」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, arrow, icon_badge, pin_icon)


# ── 図1: 常滑市・東海市の坪単価レンジ比較 ──────────────────────
def fig_tsubotanka_range():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '常滑市・東海市は、坪単価のレンジ(幅)が大きいエリアです', 18))

    x0, x1 = 120, 840
    scale_max = 60  # 万円/坪
    def sx(v):
        return x0 + (x1 - x0) * v / scale_max

    # 軸目盛り
    axis_y = 220
    for v in range(0, scale_max + 1, 10):
        x = sx(v)
        s.append(box(x, axis_y, 1, 6, MUTE, MUTE, 0, 0))
        s.append(txt(x, axis_y + 22, f'{v}万円', 14, MUTE, '400', 'middle'))

    rows = [
        ('常滑市', 5, 35, NAVY, NAVY_L),
        ('東海市', 10, 58, BLUE, BLUE_L),
    ]
    row_h = 60
    y0 = 80
    for i, (city, lo, hi, color, tint) in enumerate(rows):
        y = y0 + i * row_h
        s.append(txt(0, y + 22, city, 16, INK, '700'))
        bx0, bx1 = sx(lo), sx(hi)
        s.append(box(bx0, y, bx1 - bx0, 30, tint, color, 1.5, 15))
        s.append(txt(bx0, y - 8, f'{lo}万円', 14, color, '700', 'middle'))
        s.append(txt(bx1, y - 8, f'{hi}万円', 14, color, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '常滑市・東海市の坪単価のレンジ比較',
                '常滑市は坪5万円から35万円、東海市は坪10万円から58万円と、同じ市内でもエリアによって坪単価に大きな幅がある。市全体の平均値だけで判断すると、実際の価格感から大きく外れることがある。')


# ── 図2: 沿岸部と内陸部の地盤の傾向 ──────────────────────
def fig_enkai_naichiku_hikaku():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '沿岸部と内陸部で、地盤の傾向が変わることがあります', 18))

    s.append(card(30, 64, 380, 150, SURF, accent=WARN))
    s.append(pin_icon(70, 100, 26, WARN_D))
    s.append(txt(100, 106, '沿岸部', 16, INK, '700'))
    s.append(txt(60, 136, '埋立によって造成された土地を', 14, INK2, '400'))
    s.append(txt(60, 156, '含むことがあり、地盤調査の結果', 14, INK2, '400'))
    s.append(txt(60, 176, '次第で改良が必要になることがある', 14, INK2, '400'))

    s.append(card(470, 64, 380, 150, SURF, accent=NAVY))
    s.append(pin_icon(510, 100, 26, NAVY))
    s.append(txt(540, 106, '内陸部', 16, INK, '700'))
    s.append(txt(500, 136, '比較的安定した地盤であることが', 14, INK2, '400'))
    s.append(txt(500, 156, '多いが、「このエリアだから大丈夫」', 14, INK2, '400'))
    s.append(txt(500, 176, 'と決めつけず個別の確認が必要', 14, INK2, '400'))

    return wrap(''.join(s), W, H,
                '沿岸部と内陸部における地盤の傾向の違い',
                '沿岸部は埋立によって造成された土地を含むことがあり、地盤調査の結果次第で改良が必要になることがある。内陸部は比較的安定した地盤であることが多いが、エリアだけで決めつけず個別の確認が必要である。')


# ── 図3: 契約前に確認したいこと ──────────────────────
def fig_tochi_kakunin_point():
    W = 880
    s = []
    s.append(heading(0, 34, '常滑市・東海市で土地を探すときに、これを確認してください', 18))

    items = [
        ('このエリアの実勢価格', '市の平均値だけでなく、具体的な町名での価格を確認する'),
        ('土地の履歴', '元々何だったか(埋立地かどうか)で地盤の傾向が変わる'),
        ('台風・塩害への対策', '沿岸部では標準仕様に含まれているかを確認する'),
    ]
    row_h = 64
    y0 = 108
    for i, (label, note) in enumerate(items):
        y = y0 + i * row_h
        s.append(icon_badge(20, y - 18, 32, NAVY, NAVY_L, 'pin'))
        s.append(txt(70, y - 2, label, 15, INK, '700'))
        s.append(txt(70, y + 18, note, 14, INK2, '400'))

    H = y0 + 2 * row_h + 56
    return wrap(''.join(s), W, H,
                '常滑市・東海市で土地を探すときに確認したい3つのポイント',
                '市の平均値だけでなく具体的な町名での実勢価格を確認すること、土地が元々何だったか(埋立地かどうか)で地盤の傾向が変わること、沿岸部では台風・塩害への対策が標準仕様に含まれているかを確認することの3点。')


FIGURES = {
    'tsubotanka-range':        (fig_tsubotanka_range,        '図1：常滑市・東海市の坪単価のレンジ比較'),
    'enkai-naichiku-hikaku':   (fig_enkai_naichiku_hikaku,   '図2：沿岸部と内陸部の地盤の傾向の違い'),
    'tochi-kakunin-point':     (fig_tochi_kakunin_point,     '図3：土地を探すときに確認したい3つのポイント'),
}
