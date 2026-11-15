# -*- coding: utf-8 -*-
"""「予算オーバーしたら、次は『窓とシャッター』を見直す」の図解。

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


# ── 図1: なんとなく付けた窓、3つの見直し候補 ──────────────────────
def fig_fuyou_mado_3rei():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, '「なんとなく付けた窓」、見直し候補になりやすい3つの場所', 18))

    items = [
        ('トイレの窓', '電気代より割高。北側で冬の冷気がトイレ全体を冷やす', WARN_D, TINT),
        ('お風呂の窓', '夜入るため景色は見えず、冷気侵入と結露・カビの原因に', WARN_D, TINT),
        ('階段の窓', '外観の高さが揃いにくく、冷気が1階まで伝わり降りてくる', WARN_D, TINT),
    ]
    row_h, gap = 72, 12
    y0 = 70
    for i, (label, desc, color, tint) in enumerate(items):
        y = y0 + i * (row_h + gap)
        s.append(card(0, y, 880, row_h, tint, accent=color))
        s.append(txt(26, y + 30, label, 16, color, '700'))
        s.append(txt(26, y + 54, desc, 14, INK2, '400'))

    return wrap(''.join(s), W, H,
                'なんとなく付けた窓、3つの見直し候補',
                'トイレの窓は電気代より割高で冬の冷気がトイレ全体を冷やす。お風呂の窓は夜入るため景色は見えず冷気侵入と結露・カビの原因になる。階段の窓は外観の高さが揃いにくく冷気が1階まで伝わり降りてくる。')


# ── 図2: シャッターの2つの役割と費用感 ──────────────────────
def fig_shutter_2yakuwari():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, 'シャッターには「防災」と「日射調整」の2つの役割があります', 18))

    s.append(card(30, 70, 380, 150, TINT, accent=NAVY))
    s.append(txt(220, 102, '防災(防犯・台風対策)', 16, NAVY, '700', 'middle'))
    s.append(txt(220, 134, '防火地域以外では必須ではない', 14, INK2, '400', 'middle'))
    s.append(txt(220, 156, '最近の窓は気密性・耐久性が高い', 14, INK2, '400', 'middle'))
    s.append(txt(220, 190, '1か所減らすと約15万円のコストダウン', 14, NAVY, '700', 'middle'))

    s.append(card(470, 70, 380, 150, FOREST_L, accent=GOOD_D))
    s.append(txt(660, 102, '日射調整', 16, GOOD_D, '700', 'middle'))
    s.append(txt(660, 134, '吹き抜け上部の窓などに', 14, INK2, '400', 'middle'))
    s.append(txt(660, 156, 'スリット開閉式の電動シャッター', 14, INK2, '400', 'middle'))
    s.append(txt(660, 190, '夏は遮熱、冬は暖気の流出を抑える', 14, GOOD_D, '700', 'middle'))

    s.append(txt(0, 250, '1階の日射遮蔽はシャッター以外の方法でも可能。予算に応じて設置を判断する', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                'シャッターの2つの役割と費用感',
                'シャッターには防災(防犯・台風対策)と日射調整の2つの役割がある。防災目的は防火地域以外では必須ではなく、電動シャッターを1か所減らすと約15万円のコストダウンになる。日射調整は吹き抜け上部の窓などで夏の遮熱・冬の暖気保持に活用できる。')


# ── 図3: 残すべき窓と見直し候補の窓 ──────────────────────
def fig_mado_nokosu_minaoshi():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '窓は一律に減らすのではなく、残すべき窓と見直す窓を分けます', 18))

    s.append(card(30, 70, 380, 150, FOREST_L, accent=GOOD_D))
    s.append(txt(220, 102, '残すべき窓', 17, GOOD_D, '700', 'middle'))
    s.append(txt(220, 134, '南側の窓(冬の日射取得)', 15, INK, '400', 'middle'))
    s.append(txt(220, 158, '洗面脱衣室の窓(出入りが多い)', 15, INK, '400', 'middle'))

    s.append(card(470, 70, 380, 150, TINT, accent=WARN_D))
    s.append(txt(660, 102, '見直し候補の窓', 17, WARN_D, '700', 'middle'))
    s.append(txt(660, 134, 'トイレ・お風呂・階段の窓', 15, INK, '400', 'middle'))
    s.append(txt(660, 158, '目的が曖昧な「なんとなくの窓」', 15, INK, '400', 'middle'))

    s.append(txt(0, 250, '真南の敷地は少ないため、南西・南東寄りの日射の入り方を確認して窓を設計する', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '残すべき窓と見直し候補の窓',
                '南側の窓(冬の日射取得)や洗面脱衣室の窓は残すべき窓。トイレ・お風呂・階段の窓など目的が曖昧な窓は見直し候補になる。')


FIGURES = {
    'fuyou-mado-3rei':      (fig_fuyou_mado_3rei,      '図1：なんとなく付けた窓、3つの見直し候補'),
    'shutter-2yakuwari':    (fig_shutter_2yakuwari,    '図2：シャッターの2つの役割と費用感'),
    'mado-nokosu-minaoshi': (fig_mado_nokosu_minaoshi, '図3：残すべき窓と見直し候補の窓'),
}
