# -*- coding: utf-8 -*-
"""「間取りの設計には、建築士の資格が必要です」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, icon_badge)


# ── 図1: 延べ面積による設計資格の区分(木造2階建て以下) ──────────────────────
def fig_menseki_kubun_scale():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '木造2階建て以下の住宅は、延べ面積によって必要な資格が変わります', 18))

    track_x, track_y, track_w, track_h = 40, 96, 800, 54
    # 3区分: 0-100(資格不要,比率小さめに固定表示) / 100-300(木造建築士以上) / 300+(二級・一級建築士)
    zone1_w = 140
    zone2_w = 440
    zone3_w = track_w - zone1_w - zone2_w

    s.append(box(track_x, track_y, zone1_w, track_h, TINT, LINE, 1.5, 8))
    s.append(txt(track_x + zone1_w / 2, track_y + 24, '資格は', 14, INK2, '700', 'middle'))
    s.append(txt(track_x + zone1_w / 2, track_y + 42, '不要', 15, INK2, '700', 'middle'))

    x2 = track_x + zone1_w
    s.append(box(x2, track_y, zone2_w, track_h, NAVY_L, NAVY, 1.5, 8))
    s.append(txt(x2 + zone2_w / 2, track_y + 24, '木造建築士・二級建築士・', 14, NAVY, '700', 'middle'))
    s.append(txt(x2 + zone2_w / 2, track_y + 42, '一級建築士のいずれかが必要', 14, NAVY, '700', 'middle'))

    x3 = x2 + zone2_w
    s.append(box(x3, track_y, zone3_w, track_h, NAVY, NAVY, 0, 8))
    s.append(txt(x3 + zone3_w / 2, track_y + 24, '二級建築士・', 14, SURF, '700', 'middle'))
    s.append(txt(x3 + zone3_w / 2, track_y + 42, '一級建築士が必要', 14, SURF, '700', 'middle'))

    # 目盛りラベル
    s.append(txt(track_x, track_y + track_h + 20, '0㎡', 14, MUTE, '400'))
    s.append(txt(x2, track_y + track_h + 20, '100㎡', 15, INK, '700', 'middle'))
    s.append(txt(x3, track_y + track_h + 20, '300㎡', 15, INK, '700', 'middle'))

    s.append(txt(0, track_y + track_h + 56, '※木造・階数2以下の建築物の場合(建築士法第3条の3)。延べ面積100㎡はおよそ30坪にあたります', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '木造2階建て以下の住宅における延べ面積と設計資格の区分',
                '木造2階建て以下の建築物は、延べ面積100平方メートル以下であれば法律上の資格要件はない。100平方メートルを超え300平方メートル以下は木造建築士・二級建築士・一級建築士のいずれかが必要。300平方メートルを超えると二級建築士・一級建築士に限られる。')


# ── 図2: 一般的な注文住宅の広さは、ほとんど100㎡を超える ──────────────────────
def fig_tsubosuu_hikaku():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '一般的な注文住宅の広さは、ほとんど100㎡のラインを超えています', 18))

    items = [
        ('25坪(約83㎡)', 'cross'),
        ('30坪(約99㎡)', 'dash'),
        ('35坪(約116㎡)', 'check'),
        ('40坪(約132㎡)', 'check'),
    ]
    row_h = 54
    y0 = 104
    s.append(txt(560, 74, '100㎡を超える', 15, INK, '700', 'middle'))
    for i, (label, mark) in enumerate(items):
        y = y0 + i * row_h
        s.append(txt(20, y, label, 15, INK, '700'))
        if mark == 'cross':
            s.append(cross_badge(560, y - 6, 11, MUTE))
        elif mark == 'dash':
            s.append(dash(550, y - 6, MUTE))
        else:
            s.append(check_badge(560, y - 6, 11, NAVY))

    H = y0 + 3 * row_h + 50
    return wrap(''.join(s), W, H,
                '坪数ごとの延べ面積と、100平方メートルの基準を超えるかどうかの比較',
                '25坪(約83平方メートル)は基準を超えない。30坪(約99平方メートル)はほぼ境界線上。35坪(約116平方メートル)と40坪(約132平方メートル)は基準を超える。4人家族で検討されることが多い30坪台後半以降の住宅は、ほとんどが100平方メートルの基準を超える。')


# ── 図3: 誰が最初から関わったかで、間取りの中身が変わる ──────────────────────
def fig_tantou_hikaku():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '誰が最初から間取りに関わったかで、検討の中身が変わります', 18))

    s.append(card(30, 64, 380, 170, SURF, accent=WARN))
    s.append(txt(220, 100, '営業担当者だけで決めた場合', 16, INK, '700', 'middle'))
    s.append(txt(220, 132, '構造・耐震の判断が後回しに', 14, INK2, '400', 'middle'))
    s.append(txt(220, 152, 'なりやすい', 14, INK2, '400', 'middle'))
    s.append(txt(220, 182, '規模によっては資格者が関わって', 14, INK2, '400', 'middle'))
    s.append(txt(220, 202, 'いないおそれがある', 14, INK2, '400', 'middle'))

    s.append(card(470, 64, 380, 170, SURF, accent=NAVY))
    s.append(txt(660, 100, '建築士が最初から関わった場合', 16, INK, '700', 'middle'))
    s.append(txt(660, 132, '構造・耐震を踏まえたうえで', 14, INK2, '400', 'middle'))
    s.append(txt(660, 152, '間取りを検討できる', 14, INK2, '400', 'middle'))
    s.append(txt(660, 182, '資格者が責任を持って設計する', 14, INK2, '400', 'middle'))
    s.append(txt(660, 202, '体制になっている', 14, INK2, '400', 'middle'))

    return wrap(''.join(s), W, H,
                '営業担当者だけで決めた場合と建築士が最初から関わった場合の違い',
                '営業担当者だけで間取りを決めた場合、構造や耐震の判断が後回しになりやすく、規模によっては資格者が関わっていないおそれがある。建築士が最初から関わった場合は、構造や耐震を踏まえたうえで間取りを検討でき、資格者が責任を持って設計する体制になっている。')


FIGURES = {
    'menseki-kubun-scale': (fig_menseki_kubun_scale, '図1：延べ面積による設計資格の区分(木造2階建て以下)'),
    'tsubosuu-hikaku':      (fig_tsubosuu_hikaku,      '図2：一般的な注文住宅の広さと100㎡ラインの比較'),
    'tantou-hikaku':        (fig_tantou_hikaku,        '図3：誰が最初から間取りに関わったかによる違い'),
}
