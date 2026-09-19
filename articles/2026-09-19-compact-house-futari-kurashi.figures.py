# -*- coding: utf-8 -*-
"""「コンパクトハウスのすすめ」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はアースカラー+淡いグリーン。イラストは使わない方針。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。

図1の金利は2026年8月時点の報道値(モゲチェック等)、図2の坪数は国土交通省の
誘導居住面積水準(一般型/戸建て)をもとに計算した目安。いずれも本文中に出典を明記。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, heading, card, badge, check_badge, cross_badge, arrow)


# ── 図1: コンパクトハウスが選ばれる3つの背景 ──────────────────────
def fig_3youin():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, 'コンパクトハウスが選ばれている3つの背景(2026年時点)', 18))

    items = [
        ('土地価格の上昇', ('西三河・知多エリアでも', '坪単価は上昇傾向'), BLUE),
        ('資材価格の高止まり', ('円安・人件費の上昇で、', '以前の水準に戻りにくい'), BLUE_M),
        ('住宅ローン金利の上昇', ('変動金利 約1.08%', 'フラット35 約3.29%'), NAVY),
    ]
    card_w = 266
    for i, (title, (line1, line2), color) in enumerate(items):
        x = 20 + i * (card_w + 15)
        s.append(card(x, 66, card_w, 210, SURF, accent=color))
        s.append(badge(x + 30, 102, 15, str(i + 1), color, SURF, 15))
        s.append(txt(x + 20, 150, title, 16, INK, '700'))
        s.append(txt(x + 20, 178, line1, 14, INK2, '400'))
        s.append(txt(x + 20, 198, line2, 14, INK2, '400'))
        if i == 2:
            s.append(txt(x + 20, 220, '(2026年8月時点)', 13, MUTE, '400'))

    s.append(txt(0, H - 18, '※ 金利は日銀の追加利上げ以降、上昇局面が続く可能性があるとされる(2026年時点の情報)', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                'コンパクトハウスが選ばれている3つの背景',
                '土地価格の上昇、資材価格の高止まり、住宅ローン金利の上昇という3つの背景により、必要以上に大きな家を建てない「コンパクトハウス」という選択肢が見直されている。2026年8月時点で変動金利は約1.08%、フラット35は約3.29%。')


# ── 図2: 世帯人数別の延床面積の目安(国交省・誘導居住面積水準) ──────────────────────
def fig_mensekimokuyasu():
    W = 880
    items = [
        ('単身', 17, False),
        ('夫婦二人', 23, True),
        ('3人', 30, False),
        ('4人(子供部屋を追加)', 38, False),
    ]
    row_h = 56
    top = 76
    H = top + row_h * len(items) + 70
    s = []
    s.append(heading(0, 34, '世帯人数別の延床面積の目安(国土交通省・誘導居住面積水準)', 18))

    max_v = 38 * 1.15
    track_x, track_w = 190, 500
    for i, (label, tsubo, hi) in enumerate(items):
        y = top + i * row_h
        bar_w = track_w * tsubo / max_v
        color = NAVY if hi else BLUE
        s.append(txt(track_x - 14, y + 24, label, 15, INK, '700', 'end'))
        s.append(box(track_x, y + 6, track_w, 26, TINT, LINE, 1, 6))
        s.append(box(track_x, y + 6, bar_w, 26, color, color, 0, 6))
        s.append(txt(track_x + bar_w + 14, y + 24, f'約{tsubo}坪', 15, color, '700'))

    s.append(txt(0, H - 40, '※ 国土交通省「誘導居住面積水準(一般型/戸建て)」の面積を坪換算した目安値', 14, INK2, '400'))
    s.append(txt(0, H - 18, '　実際に必要な広さは、持ち物の量や暮らし方によって変わります', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                '世帯人数別の延床面積の目安',
                '国土交通省の誘導居住面積水準(一般型)を坪換算すると、単身で約17坪、夫婦二人で約23坪、3人で約30坪、4人で約38坪が目安になる。夫婦二人の23坪程度からコンパクトに始め、子供部屋を追加すれば4人家族の目安である38坪程度まで対応できる。')


# ── 図3: コンパクトに始めて、後から広げる間取りの考え方 ──────────────────────
def fig_before_after():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, 'コンパクトに始めて、必要になったら子供部屋を追加する', 18))

    # 左: 夫婦二人の始まりの間取り
    s.append(card(30, 64, 350, 210, SURF, accent=BLUE))
    s.append(txt(205, 96, '夫婦二人・約23坪', 16, INK, '700', 'middle'))
    rooms_a = ['LDK', '主寝室', '趣味室・書斎(可変スペース)']
    for i, r in enumerate(rooms_a):
        y = 130 + i * 30
        s.append(check_badge(60, y, 9, BLUE))
        s.append(txt(78, y + 5, r, 14, INK2, '400'))
    s.append(txt(205, 250, '今の暮らしに、ちょうどいい広さ', 14, BLUE_M, '700', 'middle'))

    # 矢印
    s.append(txt(422, 155, '将来、必要に', 12, GOOD_D, '700', 'middle'))
    s.append(txt(422, 172, 'なったら', 12, GOOD_D, '700', 'middle'))
    s.append(arrow(392, 200, GOOD, 60))

    # 右: 4人家族に対応した間取り
    s.append(card(470, 64, 380, 210, SURF, accent=NAVY))
    s.append(txt(660, 96, '4人家族に対応・約35〜38坪', 16, INK, '700', 'middle'))
    rooms_b = ['LDK', '主寝室', '子供部屋①(元・趣味室を転用)', '子供部屋②(増築 or 小屋裏を居室化)']
    for i, r in enumerate(rooms_b):
        y = 130 + i * 24
        s.append(check_badge(500, y - 4, 8, NAVY))
        s.append(txt(516, y + 1, r, 13, INK2, '400'))
    s.append(txt(660, 252, '間取りを大きく変えずに拡張できる', 14, NAVY, '700', 'middle'))

    return wrap(''.join(s), W, H,
                'コンパクトに始めて後から広げる間取りの考え方を示す図',
                '夫婦二人での暮らしは約23坪のLDK・主寝室・可変スペース(趣味室や書斎)から始め、必要になったらその可変スペースを子供部屋に転用したり、増築や小屋裏の居室化によって子供部屋を追加したりすることで、約35〜38坪の4人家族に対応した家に拡張できるという考え方を示す。')


FIGURES = {
    '3youin':           (fig_3youin,            '図1：コンパクトハウスが選ばれている3つの背景'),
    'mensekimokuyasu':  (fig_mensekimokuyasu,   '図2：世帯人数別の延床面積の目安'),
    'before-after':     (fig_before_after,      '図3：コンパクトに始めて後から広げる間取りの考え方'),
}
