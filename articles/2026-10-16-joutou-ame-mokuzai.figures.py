# -*- coding: utf-8 -*-
"""「上棟後に雨で木材が濡れたら、何を確認すればいいか」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, arrow, icon_badge)


# ── 図1: 建方から防水完了までの工程と、雨の影響を受けやすい期間 ──────────────────────
def fig_koutei_timeline():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '建方から屋根の防水が終わるまでの間、雨の影響を受けやすい期間があります', 18))

    steps = ['①建方\n(上棟)', '②野地板を\n張る', '③ルーフィング\n(防水シート)', '④屋根材を\n葺く']
    n = len(steps)
    box_w, box_h = 170, 70
    gap = (880 - box_w * n) / (n - 1)
    y = 86
    for i, label in enumerate(steps):
        x = i * (box_w + gap)
        color = NAVY if i >= 2 else WARN
        s.append(card(x, y, box_w, box_h, SURF, accent=color))
        lines = label.split('\n')
        s.append(txt(x + box_w / 2, y + 30, lines[0], 15, INK, '700', 'middle'))
        s.append(txt(x + box_w / 2, y + 52, lines[1], 15, INK, '700', 'middle'))
        if i < n - 1:
            s.append(arrow(x + box_w + 6, y + box_h / 2 - 2, MUTE, gap - 12))

    bracket_x1 = 0
    bracket_x2 = 2 * (box_w + gap) + box_w
    s.append(box(bracket_x1, y + box_h + 24, bracket_x2 - bracket_x1, 34, WARN_D, WARN_D, 0, 8))
    s.append(txt((bracket_x1 + bracket_x2) / 2, y + box_h + 46, 'この間に雨が降ると、組み上がった木材が濡れることがあります', 14, SURF, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '建方から屋根の防水が終わるまでの工程と、雨の影響を受けやすい期間',
                '建方(上棟)、野地板を張る、ルーフィング(防水シート)を張る、屋根材を葺くという4つの工程があり、ルーフィングが終わるまでの間に雨が降ると、組み上がったばかりの木材が濡れることがある。')


# ── 図2: 乾燥を確認してから進む場合と、濡れたまま進んでしまう場合 ──────────────────────
def fig_nureta_ato_hikaku():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '本当に注意すべきは、「濡れたこと」より「その後どう進めるか」です', 18))

    s.append(card(30, 64, 380, 170, SURF, accent=NAVY))
    s.append(txt(220, 100, '乾燥を確認してから次の工程へ', 16, INK, '700', 'middle'))
    s.append(check_badge(60, 136, 11, NAVY))
    s.append(txt(86, 141, '含水率などで乾燥を確認', 14, INK2, '400'))
    s.append(check_badge(60, 164, 11, NAVY))
    s.append(txt(86, 169, '断熱材や壁で覆う前に時間を置く', 14, INK2, '400'))
    s.append(txt(220, 204, '過度に心配する必要はない', 14, MUTE, '400', 'middle'))

    s.append(card(470, 64, 380, 170, SURF, accent=CRIT))
    s.append(txt(660, 100, '濡れたまま次の工程へ進む', 16, INK, '700', 'middle'))
    s.append(cross_badge(500, 136, 11, CRIT))
    s.append(txt(526, 141, '乾燥を確認しないまま壁で覆う', 14, INK2, '400'))
    s.append(cross_badge(500, 164, 11, CRIT))
    s.append(txt(526, 169, '水分が木材や床下に閉じ込められる', 14, INK2, '400'))
    s.append(txt(660, 204, 'カビ・腐朽のリスクが高まる', 14, CRIT_D, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '乾燥を確認してから次の工程に進む場合と、濡れたまま進んでしまう場合の違い',
                '含水率などで乾燥を確認し、断熱材や壁で覆う前に時間を置けば、過度に心配する必要はない。一方、乾燥を確認しないまま濡れた状態で壁などで覆ってしまうと、水分が木材や床下に閉じ込められ、カビや腐朽のリスクが高まる。')


# ── 図3: 契約前に確認したいこと ──────────────────────
def fig_kakunin_checklist():
    W = 880
    s = []
    s.append(heading(0, 34, '契約前に、雨養生についてこれを確認してください', 18))

    items = [
        ('雨養生の方法', 'ブルーシートなどで、どの程度の養生をする方針か'),
        ('乾燥を確認する方法', '含水率計などを使って、目視だけで判断していないか'),
        ('工程を急がない姿勢', '雨の後、乾燥を待たずに次の工程を急いでいないか'),
    ]
    row_h = 64
    y0 = 108
    for i, (label, note) in enumerate(items):
        y = y0 + i * row_h
        s.append(icon_badge(20, y - 18, 32, NAVY, NAVY_L, 'building'))
        s.append(txt(70, y - 2, label, 15, INK, '700'))
        s.append(txt(70, y + 18, note, 14, INK2, '400'))

    H = y0 + 2 * row_h + 56
    return wrap(''.join(s), W, H,
                '契約前に雨養生について確認したい3つのポイント',
                '雨養生の方法としてブルーシートなどでどの程度養生する方針か、含水率計などを使って乾燥を確認しているか、雨の後に乾燥を待たず次の工程を急いでいないかの3点を契約前に確認するとよい。')


FIGURES = {
    'koutei-timeline':     (fig_koutei_timeline,     '図1：建方から防水完了までの工程と雨の影響を受けやすい期間'),
    'nureta-ato-hikaku':   (fig_nureta_ato_hikaku,   '図2：乾燥を確認してから進む場合と濡れたまま進む場合の違い'),
    'kakunin-checklist':   (fig_kakunin_checklist,   '図3：契約前に雨養生について確認したいポイント'),
}
