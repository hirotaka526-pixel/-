# -*- coding: utf-8 -*-
"""「地盤改良費は、なぜ契約前に確定しないのか」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, arrow, icon_badge)


# ── 図1: 地盤改良費が決まるまでの順番 ──────────────────────
def fig_kingaku_kakutei_jyunban():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '地盤改良費は、この順番で初めて金額が決まります', 18))

    steps = ['①間取りの\n検討', '②地盤調査\n(建物の配置が決まってから)', '③地耐力に応じて\n改良の要否・工法を判断', '④金額が\n確定']
    n = len(steps)
    box_w, box_h = 195, 80
    gap = (880 - box_w * n) / (n - 1)
    y = 70
    for i, label in enumerate(steps):
        x = i * (box_w + gap)
        color = NAVY if i == n - 1 else NAVY_L
        fill = NAVY if i == n - 1 else SURF
        tcol = SURF if i == n - 1 else INK
        s.append(card(x, y, box_w, box_h, fill, accent=(None if i == n - 1 else NAVY)))
        lines = label.split('\n')
        ty = y + 32 if len(lines) == 1 else y + 28
        for li, line in enumerate(lines):
            s.append(txt(x + box_w / 2, ty + li * 20, line, 14, tcol, '700', 'middle'))
        if i < n - 1:
            s.append(arrow(x + box_w + 6, y + box_h / 2 - 2, MUTE, gap - 12))

    s.append(txt(0, y + box_h + 40, '※間取りが固まる前の契約段階では、地盤調査がまだ行われていないため、地盤改良費は確定しません', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '地盤改良費が確定するまでの4つの段階',
                '間取りの検討、建物の配置が決まってからの地盤調査、地耐力に応じた改良の要否・工法の判断、金額の確定という順番で進む。間取りが固まる前の契約段階ではまだ地盤調査が行われていないため、地盤改良費は確定しない。')


# ── 図2: 代表的な3つの改良工法と費用の目安 ──────────────────────
def fig_kouhou_hikaku():
    W = 880
    s = []
    s.append(heading(0, 34, '代表的な改良工法と、費用の目安(30坪前後の家の場合)', 18))

    items = [
        ('表層改良', '硬い地盤が浅い位置にある場合に使う工法', '目安：30万円台〜90万円程度'),
        ('柱状改良', '土とセメントを混ぜた柱を地中に作る工法', '目安：100万円台〜150万円程度'),
        ('鋼管杭', '鋼管を地中に押し込み硬い地層まで到達させる工法', '目安：150万円台〜200万円程度'),
    ]
    row_h = 70
    y0 = 108
    for i, (label, note, price) in enumerate(items):
        y = y0 + i * row_h
        s.append(icon_badge(20, y - 20, 36, NAVY, NAVY_L, 'building'))
        s.append(txt(74, y - 4, label, 16, INK, '700'))
        s.append(txt(74, y + 18, note, 14, INK2, '400'))
        s.append(txt(74, y + 38, price, 14, NAVY, '700'))

    H = y0 + 2 * row_h + 70
    s.append(txt(0, H - 20, '※地盤調査の結果や敷地条件で大きく変わる、あくまで一般的な目安です', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '代表的な3つの地盤改良工法と費用の目安',
                '表層改良は硬い地盤が浅い位置にある場合に使う工法で30万円台から90万円程度が目安。柱状改良は土とセメントを混ぜた柱を地中に作る工法で100万円台から150万円程度が目安。鋼管杭は鋼管を地中に押し込み硬い地層まで到達させる工法で150万円台から200万円程度が目安。いずれも地盤調査の結果や敷地条件で大きく変わる一般的な目安である。')


# ── 図3: 契約前に確認したいこと ──────────────────────
def fig_kakunin_point():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '契約前に、地盤改良費についてこれを確認してください', 18))

    s.append(card(30, 64, 380, 170, SURF, accent=NAVY))
    s.append(txt(220, 100, '地盤調査はいつ行いますか', 16, INK, '700', 'middle'))
    s.append(txt(220, 132, '間取りが固まる前か後かで', 14, INK2, '400', 'middle'))
    s.append(txt(220, 152, '金額の確定時期が変わる', 14, INK2, '400', 'middle'))
    s.append(txt(220, 182, '上限の目安はいくらですか', 14, INK2, '700', 'middle'))
    s.append(txt(220, 202, '数字で答えられるかを見る', 14, INK2, '400', 'middle'))

    s.append(card(470, 64, 380, 170, SURF, accent=GOLD))
    s.append(txt(660, 100, '近隣の施工実績はありますか', 16, INK, '700', 'middle'))
    s.append(txt(660, 132, '同じエリアでの改良の有無や', 14, INK2, '400', 'middle'))
    s.append(txt(660, 152, '工法の傾向を聞いておく', 14, INK2, '400', 'middle'))
    s.append(txt(660, 182, '※エリアだけでは判断できない', 14, MUTE, '400', 'middle'))
    s.append(txt(660, 202, 'ことには注意が必要', 14, MUTE, '400', 'middle'))

    return wrap(''.join(s), W, H,
                '契約前に地盤改良費について確認したいポイント',
                '地盤調査はいつ行うか、間取りが固まる前か後かで金額の確定時期が変わる。上限の目安を数字で答えられるか。近隣の施工実績を聞いておくとよいが、エリアだけでは判断できないことには注意が必要。')


FIGURES = {
    'kingaku-kakutei-jyunban': (fig_kingaku_kakutei_jyunban, '図1：地盤改良費が確定するまでの4つの段階'),
    'kouhou-hikaku':           (fig_kouhou_hikaku,           '図2：代表的な3つの地盤改良工法と費用の目安'),
    'kakunin-point':           (fig_kakunin_point,           '図3：契約前に地盤改良費について確認したいポイント'),
}
