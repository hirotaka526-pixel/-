# -*- coding: utf-8 -*-
"""「設計と施工が分かれていると、何が起きるのか」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge, cross_badge, arrow)


# ── 図1: 3つの体制パターン ──────────────────────
def fig_taisei_3pattern():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, '「設計」と「施工」のつながり方には、3つのパターンがあります', 18))

    patterns = [
        ('分離発注', '施主', '設計事務所', '工務店(施工)', WARN),
        ('社内で担当者が別', '施主', '設計担当者', '工事担当者', WARN),
        ('設計施工一貫', '施主', '建築士(設計+現場管理)', None, NAVY),
    ]
    row_h = 80
    y0 = 70
    for i, (label, a, b, c, color) in enumerate(patterns):
        y = y0 + i * row_h
        s.append(txt(20, y + 20, label, 15, INK, '700'))
        bx = 190
        s.append(box(bx, y, 90, 36, TINT, LINE, 1, 6))
        s.append(txt(bx + 45, y + 23, a, 13, INK2, '700', 'middle'))
        s.append(arrow(bx + 100, y + 18, color, 40))
        bx2 = bx + 150
        w2 = 220 if c else 300
        s.append(box(bx2, y, w2, 36, color, color, 0, 6))
        s.append(txt(bx2 + w2 / 2, y + 23, b, 13, SURF, '700', 'middle'))
        if c:
            s.append(arrow(bx2 + w2 + 10, y + 18, color, 40))
            bx3 = bx2 + w2 + 60
            s.append(box(bx3, y, 220, 36, color, color, 0, 6))
            s.append(txt(bx3 + 110, y + 23, c, 13, SURF, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '設計と施工のつながり方の3つのパターン',
                '分離発注は施主から設計事務所、さらに工務店へと情報が伝わる。社内で担当者が別の場合も施主から設計担当者、工事担当者へと情報が伝わる。設計施工一貫は施主から建築士へ直接つながり、その建築士が設計と現場管理の両方を担当する。')


# ── 図2: 分かれていると起きやすい2つのこと ──────────────────────
def fig_risk_2tsu():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '設計と施工が分かれていると、起きやすいことが2つあります', 18))

    s.append(card(30, 64, 380, 160, SURF, accent=WARN))
    s.append(txt(220, 98, '設計意図が伝わりきらない', 16, INK, '700', 'middle'))
    s.append(txt(220, 130, '図面に描ききれない細かい', 14, INK2, '400', 'middle'))
    s.append(txt(220, 150, '納まりやこだわりの部分が', 14, INK2, '400', 'middle'))
    s.append(txt(220, 170, '現場に伝わらないことがある', 14, INK2, '400', 'middle'))

    s.append(card(470, 64, 380, 160, SURF, accent=WARN))
    s.append(txt(660, 98, '責任の所在があいまいになる', 16, INK, '700', 'middle'))
    s.append(txt(660, 130, 'トラブルが起きたとき', 14, INK2, '400', 'middle'))
    s.append(txt(660, 150, '「設計のせいか施工のせいか」', 14, INK2, '400', 'middle'))
    s.append(txt(660, 170, 'で話が進みにくいことがある', 14, INK2, '400', 'middle'))

    return wrap(''.join(s), W, H,
                '設計と施工が分かれていると起きやすい2つのこと',
                '図面に描ききれない細かい納まりやこだわりの部分が現場に伝わらないことがある。また、トラブルが起きたときに設計のせいか施工のせいかで責任の所在があいまいになり、話が進みにくいことがある。')


# ── 図3: 分離発注にもメリットはある ──────────────────────
def fig_merit_balance():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '分かれているから悪い、というわけではありません', 18))

    s.append(card(30, 64, 380, 150, SURF, accent=NAVY))
    s.append(txt(220, 100, '分離発注のメリット', 16, INK, '700', 'middle'))
    s.append(check_badge(220, 136, 11, NAVY))
    s.append(txt(246, 141, '施工会社から独立した立場で', 14, INK2, '400'))
    s.append(txt(246, 161, 'チェック機能が働きやすい', 14, INK2, '400'))

    s.append(card(470, 64, 380, 150, SURF, accent=GOLD))
    s.append(txt(660, 100, '大切なのは', 16, INK, '700', 'middle'))
    s.append(txt(660, 132, 'どちらの体制でも、意図の伝達と', 14, INK2, '400', 'middle'))
    s.append(txt(660, 152, '責任の所在を、契約前に', 14, INK2, '400', 'middle'))
    s.append(txt(660, 172, '確認できているかどうか', 14, INK2, '400', 'middle'))

    return wrap(''.join(s), W, H,
                '分離発注のメリットと、確認すべきことを示す図',
                '分離発注には、施工会社から独立した立場でチェック機能が働きやすいというメリットもある。大切なのは体制そのものの良し悪しではなく、どちらの体制でも設計意図の伝達と責任の所在を契約前に確認できているかどうかである。')


FIGURES = {
    'taisei-3pattern':   (fig_taisei_3pattern,   '図1：設計と施工のつながり方の3つのパターン'),
    'risk-2tsu':          (fig_risk_2tsu,          '図2：設計と施工が分かれていると起きやすい2つのこと'),
    'merit-balance':      (fig_merit_balance,      '図3：分離発注のメリットと確認すべきこと'),
}
