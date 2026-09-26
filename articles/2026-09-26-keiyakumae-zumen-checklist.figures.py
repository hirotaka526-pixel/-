# -*- coding: utf-8 -*-
"""「契約前に見せてもらうべき図面」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge, cross_badge)


# ── 図1: 契約前によく出る図面／契約後になりがちな図面 ──────────────────────
def fig_zumen_bunrui():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, '図面には、契約前に出やすいものと出にくいものがあります', 18))

    # 左: 契約前によく出る3種
    s.append(card(20, 64, 410, 230, SURF, accent=NAVY))
    s.append(txt(45, 96, '契約前によく出る図面', 16, INK, '700'))
    left_items = [
        ('配置図', '敷地内での建物の位置、道路との関係'),
        ('平面図', '各階の部屋の配置と広さ'),
        ('立面図', '4方向から見た外観のデザイン'),
    ]
    for i, (name, note) in enumerate(left_items):
        y = 130 + i * 50
        s.append(badge(58, y, 13, str(i + 1), NAVY, SURF, 14))
        s.append(txt(82, y + 5, name, 15, INK, '700'))
        s.append(txt(82, y + 25, note, 13, INK2, '400'))

    # 右: 契約後になりがちな3種
    s.append(card(450, 64, 410, 230, SURF, accent=WARN))
    s.append(txt(475, 96, '契約後にならないと出ないことが多い図面', 15, INK, '700'))
    right_items = [
        ('構造図', '耐力壁・柱の配置、構造の安全性'),
        ('電気配線図', 'コンセント・スイッチ・照明の位置'),
        ('展開図', '各部屋の壁ごとの高さ、収納の納まり'),
    ]
    for i, (name, note) in enumerate(right_items):
        y = 130 + i * 50
        s.append(badge(488, y, 13, str(i + 4), WARN, SURF, 14))
        s.append(txt(512, y + 5, name, 15, INK, '700'))
        s.append(txt(512, y + 25, note, 13, INK2, '400'))

    return wrap(''.join(s), W, H,
                '契約前に出やすい図面と出にくい図面の分類',
                '配置図・平面図・立面図は契約前によく出てくる図面。一方、構造図・電気配線図・展開図は契約後にならないと出てこないことが多い図面で、いずれも暮らしやすさや安全性に直結する内容を含む。')


# ── 図2: 変更のタイミングと、かかる手間の関係 ──────────────────────
def fig_henkou_taimingu():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '同じ変更でも、気づくタイミングが遅いほど手間が増えます', 18))

    stages = [
        ('契約前', '図面を見て要望を伝えるだけ', 1, NAVY),
        ('実施設計中', '図面を描き直す必要がある', 2, FOREST),
        ('着工後', '工事のやり直しが発生することも', 3, CRIT),
    ]
    track_x, track_w = 200, 480
    max_v = 3.4
    row_h = 66
    top = 70
    for i, (label, note, v, color) in enumerate(stages):
        y = top + i * row_h
        bar_w = track_w * v / max_v
        s.append(txt(track_x - 14, y + 24, label, 15, INK, '700', 'end'))
        s.append(box(track_x, y + 6, track_w, 28, TINT, LINE, 1, 6))
        s.append(box(track_x, y + 6, bar_w, 28, color, color, 0, 6))
        s.append(txt(track_x + bar_w + 14, y + 25, note, 14, color, '700'))

    s.append(txt(0, H - 18, '※ 変更にかかる手間・費用の目安を段階的に示したイメージ図(具体的な金額は工事内容による)', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                '変更のタイミングと手間の関係を示す図',
                '契約前であれば図面を見て要望を伝えるだけで済むが、実施設計中に気づくと図面を描き直す必要があり、着工後に気づくと工事のやり直しが発生することもある。気づくタイミングが遅いほど、変更にかかる手間や費用は増えていく。')


# ── 図3: 体制の違い(簡潔に) ──────────────────────
def fig_taisei_chigai():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '図面が早く出てくる会社ほど、体制が整っている傾向があります', 18))

    s.append(card(30, 64, 380, 150, SURF, accent=WARN))
    s.append(txt(220, 100, '営業担当が間取りを描く体制', 16, INK, '700', 'middle'))
    s.append(txt(220, 132, '構造や配線の確認は', 14, INK2, '400', 'middle'))
    s.append(txt(220, 154, '契約後、別の担当者が行う', 14, INK2, '400', 'middle'))
    s.append(txt(220, 188, '→ 契約後に図面が変わりやすい', 14, WARN_D, '700', 'middle'))

    s.append(card(470, 64, 380, 150, SURF, accent=NAVY))
    s.append(txt(660, 100, '建築士が最初から関わる体制', 16, INK, '700', 'middle'))
    s.append(txt(660, 132, '構造・配線まで見据えて', 14, INK2, '400', 'middle'))
    s.append(txt(660, 154, '建築士自身が間取りを描く', 14, INK2, '400', 'middle'))
    s.append(txt(660, 188, '→ 契約前から図面の精度が高い', 14, NAVY, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '設計体制の違いを示す図',
                '営業担当が間取りを描き、構造や配線の確認を契約後に別の担当者が行う体制では、契約後に図面が変わりやすい。建築士が最初から構造や配線まで見据えて間取りを描く体制では、契約前から図面の精度が高くなる傾向がある。')


FIGURES = {
    'zumen-bunrui':      (fig_zumen_bunrui,      '図1：契約前に出やすい図面と出にくい図面の分類'),
    'henkou-taimingu':   (fig_henkou_taimingu,   '図2：変更のタイミングと手間の関係'),
    'taisei-chigai':     (fig_taisei_chigai,     '図3：設計体制の違い'),
}
