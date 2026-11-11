# -*- coding: utf-8 -*-
"""「住宅会社の実力は、広告やSNSではなく『現場』と『実績』で見る」の図解。

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


# ── 図1: 施工事例を見るときの注意点 ──────────────────────
def fig_sekoujirei_mikata_point():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, 'おしゃれな施工事例には、見ておきたい2つの注意点があります', 18))

    s.append(card(30, 70, 380, 150, TINT, accent=WARN_D))
    s.append(txt(60, 102, '見栄えのための施工', 16, WARN_D, '700'))
    s.append(txt(60, 130, 'お金をかけて見栄えを良くした', 14, INK2, '400'))
    s.append(txt(60, 150, '"見せるための"事例であることも', 14, INK2, '400'))

    s.append(card(470, 70, 380, 150, '#f7e9e6', accent=CRIT_D))
    s.append(txt(500, 102, '他社事例の流用', 16, CRIT_D, '700'))
    s.append(txt(500, 130, '施工事例が売買されることもあり', 14, INK2, '400'))
    s.append(txt(500, 150, 'その会社が建てたとは限らない', 14, INK2, '400'))

    s.append(txt(0, 250, '見栄えの良さと、実際の暮らしやすさは必ずしもイコールではない', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '施工事例を見るときの注意点',
                '施工事例はお金をかけて見栄えを良くしていることがあり、また他社が建てた建物の事例が売買され、自社の実績として掲載されているケースもある。見栄えの良さと実際の暮らしやすさは必ずしも一致しない。')


# ── 図2: 現場公開の3段階 ──────────────────────
def fig_genba_koukai_3dankai():
    W, H = 880, 240
    s = []
    s.append(heading(0, 34, '現場を見せてもらうときは、「説明」まであるかを見てください', 18))

    steps = [
        ('見せてもらえない', '理由なく一切見学できない', CRIT_D, '#f7e9e6'),
        ('見せてもらえるだけ', '見ても何が起きているか分からない', WARN_D, TINT),
        ('見せて説明してくれる', '状態と理由を解説してもらえる', GOOD_D, FOREST_L),
    ]
    card_w, gap = 280, 10
    x0, y0, card_h = 0, 70, 130
    for i, (label, desc, color, tint) in enumerate(steps):
        x = x0 + i * (card_w + gap)
        s.append(card(x, y0, card_w, card_h, tint, accent=color))
        s.append(txt(x + card_w / 2, y0 + 44, label, 16, color, '700', 'middle'))
        s.append(txt(x + card_w / 2, y0 + 78, desc, 14, INK2, '400', 'middle'))
        if i < len(steps) - 1:
            s.append(arrow(x + card_w + 2, y0 + card_h / 2, MUTE, gap - 4))

    s.append(txt(0, 232, '「見せてくれる」だけでなく「説明してくれる」かどうかで、現場見学の意味が変わる', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '現場公開の3段階',
                '現場見学には「見せてもらえない」「見せてもらえるだけ」「見せて説明してくれる」の3段階があり、説明まであって初めて現場を見る意味が生まれる。')


# ── 図3: 不具合への対応スピード比較(実例) ──────────────────────
def fig_taiou_speed_hikaku():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '地域密着かどうかで、不具合への対応スピードは変わります(実例)', 18))

    s.append(card(30, 70, 380, 150, '#f7e9e6', accent=CRIT_D))
    s.append(txt(220, 102, '建てた大手ハウスメーカー', 15, CRIT_D, '700', 'middle'))
    s.append(txt(220, 150, '1年以上放置', 22, CRIT_D, '700', 'middle'))
    s.append(txt(220, 178, 'ドアの丁番交換を依頼しても対応なし', 13, INK2, '400', 'middle'))

    s.append(card(470, 70, 380, 150, FOREST_L, accent=GOOD_D))
    s.append(txt(660, 102, '地域密着の工務店に相談', 15, GOOD_D, '700', 'middle'))
    s.append(txt(660, 150, '約2週間で対応', 22, GOOD_D, '700', 'middle'))
    s.append(txt(660, 178, '調査から金物の調達・取付まで', 13, INK2, '400', 'middle'))

    s.append(txt(0, 250, 'ドアの丁番交換を相談した実際のケース(会社名は伏せています)', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '不具合への対応スピード比較(実例)',
                '大手ハウスメーカーで建てた家でドアの丁番交換を依頼したところ1年以上対応してもらえなかったが、地域密着の工務店に相談したところ約2週間で対応できた実例。')


FIGURES = {
    'sekoujirei-mikata-point': (fig_sekoujirei_mikata_point, '図1：施工事例を見るときの注意点'),
    'genba-koukai-3dankai':    (fig_genba_koukai_3dankai,    '図2：現場公開の3段階'),
    'taiou-speed-hikaku':      (fig_taiou_speed_hikaku,      '図3：不具合への対応スピード比較(実例)'),
}
