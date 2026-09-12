# -*- coding: utf-8 -*-
"""「地盤改良は隣の家を見ても分からない」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はアースカラー+淡いグリーン(2026年9月改訂)。イラストは使わない方針。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, heading, card, badge, check, cross)


# ── 図1: 土地の履歴で地盤の強さが変わる ──────────────────────
def fig_tochi_rireki():
    W, H = 880, 330
    s = []
    s.append(heading(0, 34, '同じエリアでも、土地の「元の姿」で地盤の強さが変わります', 18))

    items = [
        ('工場跡地', ('基礎撤去後の', '表層が緩みやすい')),
        ('擁壁のある造成地', ('擁壁から2m程度', '埋め戻した土になる')),
        ('元が池・田んぼ', ('表層に埋め戻した', '土が入っている')),
    ]
    gap = 24
    card_w = (880 - gap * 4) / 3
    for i, (title, (note1, note2)) in enumerate(items):
        x = gap + i * (card_w + gap)
        y = 66
        h = 190
        s.append(card(x, y, card_w, h, SURF, accent=CRIT))
        s.append(txt(x + card_w / 2, y + 42, title, 16, INK, '700', 'middle'))
        s.append(txt(x + card_w / 2, y + 90, '地盤が', 14, INK2, '400', 'middle'))
        s.append(txt(x + card_w / 2, y + 116, '弱くなりやすい', 17, CRIT_D, '700', 'middle'))
        s.append(txt(x + card_w / 2, y + 152, note1, 13, INK2, '400', 'middle'))
        s.append(txt(x + card_w / 2, y + 172, note2, 13, INK2, '400', 'middle'))
    s.append(txt(0, 310, '「元に何があったか」が、地盤の強さを知る一番の手がかりです', 14, INK2, '700'))
    return wrap(''.join(s), W, H,
                '土地の履歴と地盤の強さの関係',
                '工場跡地、擁壁のある造成地、元が池や田んぼだった土地は、いずれも表層が緩く地盤改良が必要になりやすい。土地の履歴を確認することが地盤の強さを知る手がかりになる。')


# ── 図2: 西三河・知多の実例マップ風リスト ──────────────────────
def fig_jirei_map():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, '西三河・知多で実際に地盤改良が必要になった事例', 18))

    rows = [
        ('安城市 桜井周辺', '地下水位が高い地盤があった'),
        ('刈谷市 原崎町', '一部に地下水が通る弱い場所があった'),
        ('西尾市 徳次町', '矢作川に近く、砂質土だった'),
    ]
    y0 = 64
    row_h = 56
    for i, (place, note) in enumerate(rows):
        y = y0 + i * row_h
        s.append(card(20, y, 840, row_h - 12, SURF, accent=BLUE, shadow=False))
        s.append(badge(56, y + (row_h - 12) / 2, 16, str(i + 1), NAVY, SURF, 15))
        s.append(txt(90, y + 22, place, 16, INK, '700'))
        s.append(txt(90, y + 42, note, 14, INK2, '400'))

    s.append(box(20, y0 + 3 * row_h + 6, 840, 78, TINT, LINE, 1, 8))
    s.append(txt(40, y0 + 3 * row_h + 30, '矢作川付近は砂質土が多く地盤が弱い傾向。地下水位が高い場合は液状化対策も必要', 14, INK2, '600'))
    s.append(txt(40, y0 + 3 * row_h + 54, '知多地区は比較的地盤が強いが、元が池・田んぼの土地は表層が弱い', 14, INK2, '600'))
    s.append(txt(40, y0 + 3 * row_h + 74, '※ 海の近くが弱い傾向は知多・三河に限らずどの地域でも共通', 12, MUTE, '400'))
    return wrap(''.join(s), W, H,
                '西三河・知多で実際に地盤改良が必要になった事例',
                '安城市桜井周辺は地下水位が高い地盤、刈谷市原崎町は一部に地下水が通る弱い場所、西尾市徳次町は矢作川に近く砂質土だったため、いずれも地盤改良が必要になった。矢作川付近は砂質土が多く地盤が弱い傾向、知多地区は比較的地盤が強いが元が池や田んぼの土地は表層が弱い。')


# ── 図3: 盛土と基礎の関係(40cmルール) ──────────────────────
def fig_moridokairyou():
    W, H = 880, 400
    s = []
    s.append(heading(0, 34, '盛土が40cmを超えると、開発許可も地盤改良も必要になります', 18))

    # 断面図的なイメージ: 地面ライン、床付け位置、盛土
    ground_y = 220
    s.append(f'<line x1="60" y1="{ground_y}" x2="820" y2="{ground_y}" stroke="{INK2}" stroke-width="2"/>')
    s.append(txt(30, ground_y + 5, '地盤面', 13, INK2, '600'))

    # 左: 通常(床付け40cm、盛土なし)
    s.append(box(140, ground_y - 40, 160, 40, TINT, LINE, 1, 4))
    s.append(txt(220, ground_y - 16, '床付け', 13, INK, '700', 'middle'))
    s.append(txt(220, ground_y + 26, '約40cm', 13, INK2, '400', 'middle'))
    s.append(check(120, ground_y - 20, GOOD))
    s.append(txt(220, ground_y + 50, '通常の基礎', 14, GOOD_D, '700', 'middle'))

    # 右: 盛土40cm超(弱い土の上に基礎)
    s.append(box(560, ground_y - 40, 160, 40, '#fdf2f2', CRIT, 1.5, 4))
    s.append(txt(640, ground_y - 16, '床付け', 13, INK, '700', 'middle'))
    s.append(box(560, ground_y - 80, 160, 40, TINT, CRIT, 1.5, 4))
    s.append(txt(640, ground_y - 56, '盛土(40cm超)', 12, CRIT_D, '700', 'middle'))
    s.append(cross(540, ground_y - 60, CRIT))
    s.append(txt(640, ground_y + 26, '弱い土の上に基礎', 13, CRIT_D, '600', 'middle'))
    s.append(txt(640, ground_y + 50, '→ 開発許可+地盤改良が必要', 14, CRIT_D, '700', 'middle'))

    s.append(txt(0, 350, '元の地盤が良くても、40cm以上の盛土をすれば改良が必要になります', 14, INK2, '700'))
    s.append(txt(0, 376, '※ 旗竿敷地の水勾配・建て替え時の基礎掘り起こしでも同じ考え方が当てはまります', 12, MUTE, '400'))
    return wrap(''.join(s), W, H,
                '盛土と基礎の関係(40cmルール)',
                '基礎の床付けは地盤から約40cmの深さにあるため、それ以上の盛土をすると弱い土の上に基礎を造ることになり地盤沈下のおそれがある。40cmを超える盛土は開発許可と地盤改良の両方が必要になる。元の地盤が良くても盛土をすれば改良が必要になる。')


FIGURES = {
    'tochi-rireki':    (fig_tochi_rireki,    '図1：土地の履歴と地盤の強さの関係'),
    'jirei-map':       (fig_jirei_map,       '図2：西三河・知多で実際に地盤改良が必要になった事例'),
    'moridokairyou':   (fig_moridokairyou,   '図3：盛土と基礎の関係(40cmルール)'),
}
