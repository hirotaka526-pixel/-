# -*- coding: utf-8 -*-
"""「窓とサッシのグレードアップ、電気代の元は200年」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。

数字はすべてまえちゃん本人が実際に計算した自社の試算(標準仕様=複合サッシ(LIXIL TW)+
ペアガラス+アルゴンガス、グレードアップ=樹脂サッシ(YKK APW430)+トリプルガラス、
33〜35坪程度の標準的な家の場合)。他社比較の数値ではない。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge, cross_badge, arrow)


# ── 図1: 電気代の計算方法(4ステップ) ──────────────────────
def fig_keisan_step():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '電気代の差は、4つの計算を経て初めて分かります', 18))

    steps = [
        ('UA値を', '計算する', '窓・壁・屋根の断熱性能を数', '値化'),
        ('設備を', '選ぶ', 'その性能に合わせて冷暖房・', '給湯を決める'),
        ('一次消費エネルギーを', '計算する', '家全体で使うエネルギー量を', '算出'),
        ('電気代に', '換算する', '実際の金額として比較できる', '形にする'),
    ]
    card_w = 195
    gap = 15
    for i, (title1, title2, note1, note2) in enumerate(steps):
        x = 20 + i * (card_w + gap)
        s.append(card(x, 64, card_w, 150, SURF, accent=NAVY))
        s.append(badge(x + 26, 96, 14, str(i + 1), NAVY, SURF, 15))
        s.append(txt(x + 20, 126, title1, 14, INK, '700'))
        s.append(txt(x + 20, 146, title2, 14, INK, '700'))
        s.append(txt(x + 20, 170, note1, 13, INK2, '400'))
        s.append(txt(x + 20, 190, note2, 13, INK2, '400'))
        if i < 3:
            s.append(arrow(x + card_w + 2, 138, GOLD, gap - 4))

    s.append(txt(0, H - 18, '※ この4段階を経て初めて「電気代でいくら変わるか」が比較できるようになる', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                '電気代の差を計算する4つのステップ',
                'UA値を計算し、その性能に合わせて設備を選び、一次消費エネルギーを計算し、電気代に換算するという4段階を経て、初めて窓の性能による電気代の差を具体的な金額で比較できるようになる。')


# ── 図2: 標準仕様とグレードアップ、電気代とコストの比較 ──────────────────────
def fig_hiyou_taika():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '窓をグレードアップした場合の電気代とコストの差(自社試算)', 18))

    items = [
        ('年間の電気代の差', '約5,000円/年', 'グレードアップで安くなる金額', NAVY),
        ('窓・サッシの価格差', '約100万円', '33〜35坪程度の標準的な家の場合', FOREST),
        ('電気代だけで元を取るには', '約200年', '価格差 ÷ 年間の電気代の差', TEAL),
    ]
    card_w = 266
    for i, (title, value, note, color) in enumerate(items):
        x = 20 + i * (card_w + 15)
        s.append(card(x, 64, card_w, 200, SURF, accent=color))
        s.append(txt(x + 20, 98, title, 15, INK, '700'))
        s.append(txt(x + 20, 148, value, 26, color, '700'))
        s.append(txt(x + 20, 180, note, 13, INK2, '400'))
        if i < 2:
            s.append(txt(x + card_w + 7, 160, '→', 20, MUTE, '700', 'middle'))

    s.append(txt(0, H - 18, '※ 標準仕様(複合サッシ+ペアガラス+アルゴンガス)と、樹脂サッシ+トリプルガラスへのグレードアップを比較した自社試算', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                '窓をグレードアップした場合の電気代とコストの差',
                '標準仕様の複合サッシとペアガラスから、樹脂サッシとトリプルガラスにグレードアップすると、年間の電気代は約5,000円安くなる。一方、33〜35坪程度の標準的な家で価格差は約100万円になり、電気代だけで元を取るには約200年かかる計算になる。')


# ── 図3: 方角ごとのグレードアップの優先順位 ──────────────────────
def fig_hougaku_yusen():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, 'グレードアップするなら、日射の少ない面を優先する', 18))

    s.append(card(30, 64, 380, 150, SURF, accent=FOREST))
    s.append(txt(220, 100, '南面', 16, INK, '700', 'middle'))
    s.append(txt(220, 130, '日射で暖かさを稼げるため', 14, INK2, '400', 'middle'))
    s.append(txt(220, 152, '標準仕様でも十分なことが多い', 14, INK2, '400', 'middle'))
    s.append(check_badge(220, 188, 11, FOREST))

    s.append(card(470, 64, 380, 150, SURF, accent=NAVY))
    s.append(txt(660, 100, '東・西・北面', 16, INK, '700', 'middle'))
    s.append(txt(660, 130, '日射のメリットが少なく', 14, INK2, '400', 'middle'))
    s.append(txt(660, 152, '熱の出入りの影響が大きい面', 14, INK2, '400', 'middle'))
    s.append(txt(660, 188, '→ グレードアップの優先度が高い', 14, NAVY, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '方角ごとのグレードアップの優先順位を示す図',
                '南面は日射で暖かさを稼げるため標準仕様でも十分なことが多い。東・西・北面は日射のメリットが少なく熱の出入りの影響が大きいため、予算をかけてグレードアップするならこちらを優先するとよい。')


FIGURES = {
    'keisan-step':     (fig_keisan_step,     '図1：電気代の差を計算する4つのステップ'),
    'hiyou-taika':      (fig_hiyou_taika,      '図2：窓をグレードアップした場合の電気代とコストの差'),
    'hougaku-yusen':    (fig_hougaku_yusen,    '図3：方角ごとのグレードアップの優先順位'),
}
