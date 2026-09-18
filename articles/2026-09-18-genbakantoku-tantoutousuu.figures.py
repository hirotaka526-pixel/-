# -*- coding: utf-8 -*-
"""「現場監督は何棟を掛け持ちしていますか？」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はアースカラー+淡いグリーン。イラストは使わない方針。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, heading, card, badge, check, cross)


# ── 図1: 担当棟数が増えると起きること ──────────────────────
def fig_tantoutousuu_eikyou():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, '担当棟数が増えると、1棟あたりに割ける時間が減ります', 18))

    items = [
        '現場に来る頻度が減る',
        'チェックが後回しになる',
        '食い違いに気づくのが遅れる',
        '判断が職人任せになる',
    ]
    gap = 20
    card_w = (880 - gap * 5) / 4
    for i, note in enumerate(items):
        x = gap + i * (card_w + gap)
        y = 66
        h = 150
        s.append(card(x, y, card_w, h, SURF, accent=CRIT))
        s.append(cross(x + card_w / 2 - 8, y + 40, CRIT))
        # 折り返し(短く2分割)
        mid = len(note) // 2 + (1 if len(note) % 2 else 0)
        s.append(txt(x + card_w / 2, y + 78, note[:mid], 14, INK, '700', 'middle'))
        s.append(txt(x + card_w / 2, y + 100, note[mid:], 14, INK, '700', 'middle'))
    s.append(txt(0, 300, '悪意ではなく、単純に「現場を見る時間」が足りないことが原因です', 14, INK2, '700'))
    return wrap(''.join(s), W, H,
                '担当棟数が増えると起きること',
                '現場監督の担当棟数が増えると、現場に来る頻度が減る、チェックが後回しになる、図面と現場の食い違いに気づくのが遅れる、判断が職人任せになるといったことが起きやすくなる。悪意ではなく現場を見る時間が足りないことが原因。')


# ── 図2: 設計と現場管理が同じ人か、別の人か ──────────────────────
def fig_sekkei_genba_icchi():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '設計者と現場管理者が同じかどうかで、意図の伝わり方が変わります', 18))

    # 左: 別々
    s.append(card(30, 64, 380, 170, SURF, accent=CRIT))
    s.append(txt(220, 100, '設計者と現場管理者が別', 15, INK, '700', 'middle'))
    s.append(txt(120, 150, '設計', 15, INK2, '700', 'middle'))
    s.append(txt(320, 150, '現場', 15, INK2, '700', 'middle'))
    s.append(cross(220, 148, CRIT))
    s.append(txt(220, 200, '意図が正しく伝わらないことがある', 13, CRIT_D, '600', 'middle'))

    # 右: 同じ
    s.append(card(470, 64, 380, 170, SURF, accent=GOOD))
    s.append(txt(660, 100, '設計者が現場管理も担当', 15, INK, '700', 'middle'))
    s.append(txt(660, 150, '設計 ＝ 現場', 17, GOOD_D, '700', 'middle'))
    s.append(check(590, 148, GOOD))
    s.append(txt(660, 200, '意図をその場で正しく反映できる', 13, GOOD_D, '600', 'middle'))
    return wrap(''.join(s), W, H,
                '設計者と現場管理者が同じ場合と別の場合の違い',
                '設計者と現場管理者が別の場合、図面に書かれていない部分の判断で意図が正しく伝わらないことがある。設計者が現場管理も担当する場合は、設計の意図をその場で正しく反映できる。')


FIGURES = {
    'tantoutousuu-eikyou': (fig_tantoutousuu_eikyou, '図1：担当棟数が増えると起きること'),
    'sekkei-genba-icchi':  (fig_sekkei_genba_icchi,  '図2：設計者と現場管理者が同じ場合と別の場合の違い'),
}
