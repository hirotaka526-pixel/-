# -*- coding: utf-8 -*-
"""「間取りの後悔ランキング」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はアースカラー+淡いグリーン。イラストは使わない方針。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。

図1の件数は、2026年5〜8月の個別相談18件を振り返って集計したもの(まえちゃん提供の
「リールネタ帳バンク」の集計に基づく実数)。図2・図3は概念を説明するためのイメージ図で、
特定の実在プロジェクトの数値ではない。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, heading, card, badge, check_badge, cross_badge)


# ── 図1: 間取りの後悔ランキング(個別相談18件の集計) ──────────────────────
def fig_koukai_ranking():
    W = 880
    items = [
        ('窓の方角を「なんとなく」で決めた', 6),
        ('デザイン優先で直下率を犠牲にした', 6),
        ('収納が「多めに」で足りなかった', 4),
    ]
    row_h = 64
    top = 74
    H = top + row_h * len(items) + 56
    s = []
    s.append(heading(0, 34, '間取りの後悔ランキング(個別相談18件の集計)', 18))

    total = 18
    track_x, track_w = 30, 560
    for i, (label, v) in enumerate(items):
        y = top + i * row_h
        bar_w = track_w * v / total
        s.append(txt(track_x, y, f'{i+1}位　{label}', 15, INK, '700'))
        s.append(box(track_x, y + 12, track_w, 26, TINT, LINE, 1, 6))
        s.append(box(track_x, y + 12, bar_w, 26, NAVY if i == 0 else BLUE, NAVY if i == 0 else BLUE, 0, 6))
        s.append(txt(track_x + track_w + 16, y + 30, f'{v}件 / 18件', 15, INK, '700'))

    s.append(txt(0, H - 18, '※ 2026年5〜8月の個別相談18件を振り返って集計(1件の相談で複数該当する場合あり)', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                '間取りの後悔ランキング(個別相談18件の集計)',
                '2026年5月から8月の個別相談18件を振り返ると、窓の方角をなんとなく決めてしまったケースが6件、デザインを優先して直下率を犠牲にしたケースが6件、収納が多めにでは足りなかったケースが4件だった。')


# ── 図2: 直下率(2階の柱が1階の柱の上に乗っているか) ──────────────────────
def fig_chokkaritsu():
    W, H = 880, 430
    s = []
    s.append(heading(0, 34, '直下率とは、2階の柱が1階の柱の真上に乗っている割合のこと', 18))

    def floor_pair(cx0, cap_x, good):
        # 2F(上段)と1F(下段)、それぞれ6本の柱位置を比較する
        xs = [cx0 + 40 + i * 56 for i in range(6)]
        y2f, y1f = 150, 230
        match = [True, True, True, True, True, True] if good else \
                [True, True, False, True, False, True]
        s.append(txt(cap_x, 118, '上段：2階の柱／下段：1階の柱', 14, INK2, '700', 'middle'))
        for x in xs:
            s.append(f'<rect x="{x-11}" y="{y2f-11}" width="22" height="22" rx="4" fill="{NAVY}"/>')
        for x, ok in zip(xs, match):
            if ok:
                s.append(f'<rect x="{x-11}" y="{y1f-11}" width="22" height="22" rx="4" fill="{BLUE}"/>')
                s.append(f'<line x1="{x}" y1="{y2f+11}" x2="{x}" y2="{y1f-11}" stroke="{GOOD}" stroke-width="2" stroke-dasharray="3,3"/>')
                s.append(check_badge(x, y1f + 34, 10, GOOD))
            else:
                s.append(f'<rect x="{x-11}" y="{y1f-11}" width="22" height="22" rx="4" fill="{LINE}" stroke="{MUTE}" stroke-dasharray="2,2"/>')
                s.append(txt(x, y1f + 5, '無', 11, MUTE, '700', 'middle'))
                s.append(cross_badge(x, y1f + 34, 10, CRIT))
        return xs

    s.append(card(20, 90, 410, 300, SURF, accent=GOOD))
    floor_pair(50, 225, True)
    s.append(txt(225, 352, '6本中6本が直下', 15, GOOD_D, '700', 'middle'))
    s.append(txt(225, 376, '(良い例／直下率が高い)', 13, INK2, '400', 'middle'))

    s.append(card(450, 90, 410, 300, SURF, accent=CRIT))
    floor_pair(480, 655, False)
    s.append(txt(655, 352, '6本中4本が直下', 15, CRIT_D, '700', 'middle'))
    s.append(txt(655, 376, '(悪い例／ガレージ・大開口で抜いた)', 13, INK2, '400', 'middle'))

    return wrap(''.join(s), W, H,
                '直下率の考え方を示すイメージ図',
                '2階の柱の位置に対して、1階の同じ位置に柱があるかどうかを示す図。左側は6本中6本の柱が直下にある良い例、右側はガレージや大きな開口部のために2本の柱を抜いたことで6本中4本しか直下にない例。あくまで考え方を説明するためのイメージ図で、実在のプロジェクトの数値ではない。')


# ── 図3: 収納の失敗と対策(寸法を測る前後の違い) ──────────────────────
def fig_shuunou_before_after():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '収納は「多めに」ではなく、寸法を測ってから計画する', 18))

    # 左: 多めに(失敗)
    s.append(card(30, 64, 380, 190, SURF, accent=CRIT))
    s.append(txt(220, 100, '「多めに」で決めた収納', 16, INK, '700', 'middle'))
    s.append(cross_badge(70, 140, 11, CRIT))
    s.append(txt(90, 145, '持ち物の寸法を測っていない', 14, INK2, '400'))
    s.append(cross_badge(70, 172, 11, CRIT))
    s.append(txt(90, 177, '「収納は多めに」という感覚だけで広さを決めた', 14, INK2, '400'))
    s.append(txt(220, 230, '結果：住み始めてから入らないものが出る', 14, CRIT_D, '700', 'middle'))

    # 右: 寸法を測る(対策)
    s.append(card(470, 64, 380, 190, SURF, accent=GOOD))
    s.append(txt(660, 100, '寸法を測って決めた収納', 16, INK, '700', 'middle'))
    s.append(check_badge(510, 140, 11, GOOD))
    s.append(txt(530, 145, '持ち物を縦・横・高さで測って書き出す', 14, INK2, '400'))
    s.append(check_badge(510, 172, 11, GOOD))
    s.append(txt(530, 177, '入れたい収納ボックスの寸法も先に測る', 14, INK2, '400'))
    s.append(txt(660, 230, '結果：計画した通りに収まる', 14, GOOD_D, '700', 'middle'))

    s.append(txt(0, 280, 'この一手間があるかどうかで、住み始めてからの後悔が大きく変わります', 14, INK2, '700'))
    return wrap(''.join(s), W, H,
                '収納計画の失敗例と対策を比較する図',
                '「多めに」という感覚だけで決めた収納は、持ち物の寸法を測っていないため住み始めてから入らないものが出やすい。持ち物を縦・横・高さで測り、入れたい収納ボックスの寸法も先に測って計画すると、計画通りに収まりやすい。')


FIGURES = {
    'koukai-ranking':      (fig_koukai_ranking,      '図1：間取りの後悔ランキング(個別相談18件の集計)'),
    'chokkaritsu':          (fig_chokkaritsu,          '図2：直下率の考え方を示すイメージ図'),
    'shuunou-before-after': (fig_shuunou_before_after, '図3：収納計画の失敗例と対策を比較する図'),
}
