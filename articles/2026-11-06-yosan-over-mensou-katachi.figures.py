# -*- coding: utf-8 -*-
"""「予算オーバーしたら、まず『面積』より『形』を見直す理由」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, arrow, icon_badge, pin_icon,
                     building_icon)


# ── 図1: シンプルな建物と凹凸の多い建物の比較 ──────────────────────
def fig_gaikan_katachi_hikaku():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '坪数を減らしても、建物の形によっては安くならないことがあります', 18))

    s.append(card(30, 64, 380, 180, SURF, accent=GOOD))
    s.append(building_icon(60, 96, 40, GOOD_D))
    s.append(txt(120, 112, 'シンプルな30坪', 16, INK, '700'))
    s.append(txt(60, 150, '外壁の長さや角が少なく、', 14, INK2, '400'))
    s.append(txt(60, 170, '基礎・屋根の形も単純', 14, INK2, '400'))
    s.append(txt(60, 200, '→ 材料費・施工の手間が', 14, GOOD_D, '700'))
    s.append(txt(60, 220, '　抑えやすい', 14, GOOD_D, '700'))

    s.append(card(470, 64, 380, 180, SURF, accent=WARN))
    s.append(building_icon(500, 96, 40, WARN_D))
    s.append(txt(560, 112, '凹凸の多い28坪', 16, INK, '700'))
    s.append(txt(500, 150, '坪数は少なくても、外壁の', 14, INK2, '400'))
    s.append(txt(500, 170, '長さや角、屋根の形が複雑', 14, INK2, '400'))
    s.append(txt(500, 200, '→ 材料費・施工の手間が', 14, WARN_D, '700'))
    s.append(txt(500, 220, '　増えることがある', 14, WARN_D, '700'))

    return wrap(''.join(s), W, H,
                'シンプルな建物と凹凸の多い建物の比較',
                'シンプルな30坪の建物は外壁の長さや角が少なく基礎・屋根の形も単純で材料費や施工の手間を抑えやすい。一方、凹凸の多い28坪の建物は坪数が少なくても外壁の長さや角、屋根の形が複雑で、材料費や施工の手間が増えることがある。坪数を減らしても形が複雑なままでは期待したほど安くならないことがある。')


# ── 図2: 見積もり基準による見直し効果の違い ──────────────────────
def fig_mitsumori_kijun_hikaku():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '見積もりの基準によって、見直しの効果の出方が変わります', 18))

    s.append(card(30, 64, 380, 150, SURF, accent=NAVY))
    s.append(txt(60, 100, '面積(坪数)基準の会社', 16, INK, '700'))
    s.append(txt(60, 130, '面積を減らすと、', 14, INK2, '400'))
    s.append(txt(60, 150, '金額が下がりやすい傾向', 14, INK2, '400'))
    s.append(txt(60, 180, '「面積を減らす案」が効きやすい', 14, NAVY, '700'))

    s.append(card(470, 64, 380, 150, SURF, accent=BLUE_M))
    s.append(txt(500, 100, '仕様・工事の積み上げ基準の会社', 16, INK, '700'))
    s.append(txt(500, 130, '面積だけ減らしても、', 14, INK2, '400'))
    s.append(txt(500, 150, '思ったほど下がらないことも', 14, INK2, '400'))
    s.append(txt(500, 180, '「形を整理する案」が効きやすい', 14, BLUE_M, '700'))

    s.append(txt(0, 244, 'どちらが効くかは会社によって違うため、両方の案で差額を見積もってもらって比較する', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '見積もり基準による見直し効果の違い',
                '面積(坪数)基準で見積もりを出す会社では面積を減らす案が効きやすい。仕様や工事内容を積み上げて見積もりを出す会社では面積を減らすだけでは思ったほど下がらず、形を整理する案が効きやすい。どちらが効くかは会社によって違うため両方の案で差額を比較することが大切。')


# ── 図3: 削っていい部分・残すべき部分 ──────────────────────
def fig_kezuru_nokosu_point():
    W = 880
    s = []
    s.append(heading(0, 34, '削っていい部分と、残すべき部分を分けて考えます', 18))

    items = [
        ('削る候補', '使い道が曖昧な部屋、通らなくても困らない廊下など', GOOD, GOOD_D),
        ('残すべきもの', '家具を置く場所、生活に必要な収納など', WARN, WARN_D),
        ('会社に確認すること', '「面積を減らす案」と「形を整理する案」の差額と暮らしへの影響', NAVY, NAVY),
    ]
    row_h = 64
    y0 = 108
    for i, (label, note, tint, color) in enumerate(items):
        y = y0 + i * row_h
        s.append(icon_badge(20, y - 18, 32, color, tint, 'pin'))
        s.append(txt(70, y - 2, label, 15, INK, '700'))
        s.append(txt(70, y + 18, note, 14, INK2, '400'))

    H = y0 + 2 * row_h + 56
    return wrap(''.join(s), W, H,
                '削っていい部分と残すべき部分の整理',
                '削る候補は使い道が曖昧な部屋や通らなくても困らない廊下など。残すべきものは家具を置く場所や生活に必要な収納など。会社には面積を減らす案と形を整理する案、両方の差額と暮らしへの影響を確認する。')


FIGURES = {
    'gaikan-katachi-hikaku':   (fig_gaikan_katachi_hikaku,   '図1：シンプルな建物と凹凸の多い建物の比較'),
    'mitsumori-kijun-hikaku':  (fig_mitsumori_kijun_hikaku,  '図2：見積もり基準による見直し効果の違い'),
    'kezuru-nokosu-point':     (fig_kezuru_nokosu_point,     '図3：削っていい部分と残すべき部分の整理'),
}
