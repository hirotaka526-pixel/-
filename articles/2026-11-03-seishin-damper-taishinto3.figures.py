# -*- coding: utf-8 -*-
"""「制振ダンパーをつける前に、耐震等級3を確認する理由」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, arrow, icon_badge, pin_icon)


# ── 図1: 制振ダンパーの方式の違い ──────────────────────
def fig_damper_types_hikaku():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '制振ダンパーは、方式によってエネルギーの吸収の仕組みが違います', 18))

    s.append(card(30, 64, 380, 170, SURF, accent=NAVY))
    s.append(txt(60, 102, '鋼材系', 17, INK, '700'))
    s.append(txt(60, 128, '鋼材が変形するときの', 14, INK2, '400'))
    s.append(txt(60, 148, '性質を利用して、地震の', 14, INK2, '400'))
    s.append(txt(60, 168, 'エネルギーを吸収する', 14, INK2, '400'))
    s.append(txt(60, 198, '(筋交い型に組み込む製品など)', 14, MUTE, '400'))

    s.append(card(470, 64, 380, 170, SURF, accent=BLUE_M))
    s.append(txt(500, 102, 'オイル系', 17, INK, '700'))
    s.append(txt(500, 128, 'オイルの粘性(ねばさ)を', 14, INK2, '400'))
    s.append(txt(500, 148, '利用して、地震の', 14, INK2, '400'))
    s.append(txt(500, 168, 'エネルギーを吸収する', 14, INK2, '400'))
    s.append(txt(500, 198, '(ピストンの抵抗力を利用)', 14, MUTE, '400'))

    s.append(txt(0, 254, 'ほかに摩擦の力を利用する「摩擦系」、ゴム等の粘弾性材料を利用する「粘弾性系」もある', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '制振ダンパーの方式の違い',
                '制振ダンパーには複数の方式があり、鋼材系は鋼材が変形する性質を利用してエネルギーを吸収し、オイル系はオイルの粘性を利用してエネルギーを吸収する。ほかに摩擦系・粘弾性系もある。')


# ── 図2: 骨組みの変形と制振ダンパーが効くタイミング ──────────────────────
def fig_hensei_timing():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '制振ダンパーは、骨組みが変形することを前提に働く装置です', 18))

    s.append(card(30, 64, 820, 90, TINT, accent=NAVY))
    s.append(txt(60, 98, 'STEP1', 14, NAVY, '700'))
    s.append(txt(140, 98, '地震の力を受けて、建物の骨組み(柱・梁・壁)が実際に変形する', 15, INK, '700'))
    s.append(txt(60, 126, '制振ダンパーの多くは、この「層間変位」(上下階のズレ)を利用して働く', 14, INK2, '400'))

    s.append(txt(440, 186, '↓', 20, NAVY, '700', 'middle'))

    s.append(card(30, 198, 820, 90, SURF, accent=BLUE_M))
    s.append(txt(60, 232, 'STEP2', 14, BLUE_M, '700'))
    s.append(txt(140, 232, '変形に応じて、ダンパーがエネルギーを吸収し、揺れを抑える', 15, INK, '700'))
    s.append(txt(60, 260, '多くの制振装置は、揺れが大きくなってから効果を発揮しやすい傾向がある', 14, INK2, '400'))

    return wrap(''.join(s), W, H,
                '制振ダンパーが効果を発揮する仕組みの順序',
                '地震の力を受けて建物の骨組みが実際に変形し、その変形(層間変位)を利用して制振ダンパーがエネルギーを吸収し揺れを抑える。多くの制振装置は揺れが大きくなってから効果を発揮しやすい傾向がある。骨組みの変形が前提になる装置であることが分かる。')


# ── 図3: 契約前に確認したいポイント ──────────────────────
def fig_seishin_kakunin_point():
    W = 880
    s = []
    s.append(heading(0, 34, '制振ダンパーの提案を受けたら、これを確認してください', 18))

    items = [
        ('構造計算の方法', '簡易な計算か、1棟ごとの許容応力度計算かを確認する'),
        ('耐震等級の根拠', '等級の表示だけでなく、どの計算方法で確認したかを確認する'),
        ('ダンパーの方式', '鋼材系・オイル系など、エネルギー吸収の仕組みの違いを確認する'),
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
                '制振ダンパーの提案を受けたときに確認したい3つのポイント',
                '構造計算が簡易な計算か許容応力度計算かを確認すること、耐震等級の表示だけでなくどの計算方法で確認したかを確認すること、ダンパーの方式によってエネルギー吸収の仕組みが違うことを確認することの3点。')


FIGURES = {
    'damper-types-hikaku':    (fig_damper_types_hikaku,    '図1：制振ダンパーの方式の違い'),
    'hensei-timing':          (fig_hensei_timing,          '図2：制振ダンパーが効果を発揮する仕組みの順序'),
    'seishin-kakunin-point':  (fig_seishin_kakunin_point,  '図3：契約前に確認したい3つのポイント'),
}
