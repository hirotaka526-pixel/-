# -*- coding: utf-8 -*-
"""「断熱等級4が『最低ライン』になった、本当の意味」の図解。

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


# ── 図1: 断熱等級の基準変遷(2022年〜2025年) ──────────────────────
def fig_toukyu_hensen():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '断熱等級の基準は、2022年から2025年にかけて大きく変わりました', 18))

    events = [
        ('2022年3月まで', '等級4が最高等級', NAVY, NAVY_L),
        ('2022年4月', '等級5が新設', GOLD_D, TINT),
        ('2022年10月', '等級6・7が新設', GOLD_D, TINT),
        ('2025年4月', '等級4以上が義務化\n(最低ラインに)', CRIT_D, '#f7e9e6'),
    ]
    card_w, gap = 196, 16
    x0, y0, card_h = 30, 70, 160
    for i, (date, label, color, tint) in enumerate(events):
        x = x0 + i * (card_w + gap)
        s.append(card(x, y0, card_w, card_h, tint, accent=color))
        s.append(txt(x + card_w / 2, y0 + 36, date, 15, color, '700', 'middle'))
        lines = label.split('\n')
        for j, line in enumerate(lines):
            s.append(txt(x + card_w / 2, y0 + 78 + j * 24, line, 15, INK, '700', 'middle'))
        if i < len(events) - 1:
            ax = x + card_w + 2
            s.append(arrow(ax, y0 + card_h / 2, MUTE, gap - 4))

    s.append(txt(0, y0 + card_h + 40, 'それまで「最高」だった等級4は、今は「これより下は建てられない」という最低ラインになった', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '断熱等級の基準変遷(2022年〜2025年)',
                '2022年3月まで等級4が最高等級だったが、同年4月に等級5、10月に等級6・7が新設された。2025年4月には改正建築物省エネ法により等級4以上の適合が義務化され、かつて最高だった等級4が最低ラインになった。')


# ── 図2: 等級4の位置づけの変化(かつて vs 今) ──────────────────────
def fig_dankyu4_ichizuke():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, '等級4の位置づけは、ピラミッドの頂点から底辺に変わりました', 18))

    # 左: かつて(2022年3月まで)
    s.append(txt(30, 72, '2022年3月まで', 15, INK2, '700'))
    s.append(card(30, 86, 360, 180, NAVY_L, accent=NAVY))
    s.append(txt(210, 180, '等級4', 24, NAVY, '700', 'middle'))
    s.append(txt(210, 212, '= 最高等級', 15, NAVY, '700', 'middle'))

    # 右: 今(2025年4月〜)、下から等級4・5・6・7
    s.append(txt(490, 72, '2025年4月〜', 15, INK2, '700'))
    rows = [
        ('等級7', GOOD_D, TEAL_L),
        ('等級6', GOOD, FOREST_L),
        ('等級5', BLUE_M, TEAL_L),
        ('等級4(最低ライン・義務化)', CRIT_D, '#f7e9e6'),
    ]
    row_h, row_w = 40, 360
    y0 = 100
    for i, (label, color, tint) in enumerate(rows):
        y = y0 + i * (row_h + 6)
        s.append(card(490, y, row_w, row_h, tint, accent=color, r=10))
        s.append(txt(490 + row_w / 2, y + row_h / 2 + 5, label, 15, INK, '700', 'middle'))

    s.append(txt(0, 300, '2030年目安で、さらに上の等級が最低基準になる予定。断熱性能は新築時にしか選べない判断です', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '等級4の位置づけの変化',
                '2022年3月までは等級4が最高等級だったが、2025年4月以降は等級4が義務化された最低ラインとなり、等級5・6・7がその上に位置する。自治体資料では2030年を目安にさらに上の等級が最低基準になる可能性があるとされている。')


# ── 図3: 6地域における断熱等級ごとのUA値基準値 ──────────────────────
def fig_toukyu_ua_hikaku():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '6地域(高浜市含む)では、等級が上がるほどUA値の基準値は小さくなります', 18))

    x0, x1 = 170, 820
    scale_max = 1.0
    def sx(v):
        return x0 + (x1 - x0) * v / scale_max

    rows = [
        ('等級4(義務化の最低基準)', 0.87, CRIT_D, '#f7e9e6'),
        ('等級5(ZEH水準)', 0.60, WARN_D, TINT),
        ('等級6', 0.46, GOOD, FOREST_L),
        ('等級7', 0.26, GOOD_D, TEAL_L),
    ]
    row_h = 52
    y0 = 78
    for i, (label, val, color, tint) in enumerate(rows):
        y = y0 + i * row_h
        s.append(txt(0, y + 22, label, 14, INK, '700'))
        bw = sx(val) - x0
        s.append(box(x0, y, bw, 26, tint, color, 1.5, 13))
        s.append(txt(x0 + bw + 10, y + 19, f'UA値 {val}', 14, color, '700'))

    s.append(txt(0, y0 + 4 * row_h + 22, '数値が小さいほど、外皮から逃げる熱が少なく断熱性能が高い。正式な地域区分は国交省の地域区分一覧でご確認ください', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '6地域における断熱等級ごとのUA値基準値',
                '6地域(高浜市含む)でのUA値基準値は、等級4が0.87、等級5(ZEH水準)が0.60、等級6が0.46、等級7が0.26。数値が小さいほど断熱性能が高い。')


FIGURES = {
    'toukyu-hensen':     (fig_toukyu_hensen,     '図1：断熱等級の基準変遷(2022年〜2025年)'),
    'dankyu4-ichizuke':  (fig_dankyu4_ichizuke,  '図2：等級4の位置づけの変化(かつて vs 今)'),
    'toukyu-ua-hikaku':  (fig_toukyu_ua_hikaku,  '図3：6地域における断熱等級ごとのUA値基準値'),
}
