# -*- coding: utf-8 -*-
"""「予算オーバーしたら、次は『水回りの配置』を見直す」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD, GOLD_D,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, arrow, icon_badge, pin_icon)


# ── 図1: 水回りの集約配置と分散配置の比較 ──────────────────────
def fig_haikan_kyori_hikaku():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '水回りをまとめると、配管の距離を短くできる場合があります', 18))

    rooms_scattered = [('キッチン', 60, 100), ('浴室', 260, 70), ('洗面', 200, 170), ('トイレ', 340, 150)]
    s.append(card(30, 64, 380, 170, SURF, accent=WARN))
    s.append(txt(60, 92, '水回りが分散している例', 15, INK, '700'))
    for label, dx, dy in rooms_scattered:
        s.append(box(40 + dx * 0.78, 110 + dy * 0.32, 70, 36, TINT, WARN_D, 1, 8))
        s.append(txt(40 + dx * 0.78 + 35, 110 + dy * 0.32 + 23, label, 13, INK2, '700', 'middle'))

    rooms_grouped = [('キッチン', 20, 20), ('洗面', 110, 20), ('浴室', 20, 70), ('トイレ', 110, 70)]
    s.append(card(470, 64, 380, 170, SURF, accent=GOOD))
    s.append(txt(500, 92, '水回りをまとめた例', 15, INK, '700'))
    for label, dx, dy in rooms_grouped:
        s.append(box(500 + dx, 110 + dy, 80, 36, TINT, GOOD_D, 1, 8))
        s.append(txt(500 + dx + 40, 110 + dy + 23, label, 13, INK2, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '水回りの集約配置と分散配置の比較',
                '水回りが建物のあちこちに分散していると、それぞれに給排水の配管を長く引き回す必要があり材料費や施工の手間が増えることがある。水回りをある程度近くにまとめて配置できると配管の距離を短くできる場合がある。')


# ── 図2: 2階の水回りから1階を通る配管ルート ──────────────────────
def fig_2kai_haikan_route():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '2階に水回りがある場合、1階を通る配管ルートを確認します', 18))

    s.append(card(260, 60, 360, 70, SURF, accent=NAVY))
    s.append(txt(440, 100, '2階：水回り(キッチン・浴室など)', 15, INK, '700', 'middle'))

    s.append(txt(440, 150, '↓ 配管', 16, MUTE, '700', 'middle'))

    s.append(card(100, 170, 680, 70, TINT, accent=BLUE_M))
    s.append(txt(440, 210, '1階：水回りの配管が通れる位置になっているか', 15, INK, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '2階の水回りから1階を通る配管ルート',
                '2階にキッチンや浴室、トイレを配置する場合、1階を通って外部へ排水するための配管ルートが必要になる。1階の間取りと2階の水回りの位置がかみ合っていないと配管が複雑な経路を通ることになり施工の手間が増えることがある。')


# ── 図3: 見直すときに確認したいポイント ──────────────────────
def fig_mizumawari_kakunin_point():
    W = 880
    s = []
    s.append(heading(0, 34, '水回りの配置を見直すときに、これを確認してください', 18))

    items = [
        ('配管距離の変化', 'まとめた場合の配管距離と、具体的な差額を確認する'),
        ('2階水回りの配管ルート', '1階のどこを通って配管が抜けるかを確認する'),
        ('家事動線への影響', '費用だけでなく、暮らしやすさへの影響もあわせて確認する'),
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
                '水回りの配置を見直すときに確認したい3つのポイント',
                'まとめた場合の配管距離と具体的な差額を確認すること、2階に水回りがある場合は1階のどこを通って配管が抜けるかを確認すること、費用だけでなく暮らしやすさへの影響もあわせて確認することの3点。')


FIGURES = {
    'haikan-kyori-hikaku':       (fig_haikan_kyori_hikaku,       '図1：水回りの集約配置と分散配置の比較'),
    '2kai-haikan-route':         (fig_2kai_haikan_route,         '図2：2階の水回りから1階を通る配管ルート'),
    'mizumawari-kakunin-point':  (fig_mizumawari_kakunin_point,  '図3：見直すときに確認したい3つのポイント'),
}
