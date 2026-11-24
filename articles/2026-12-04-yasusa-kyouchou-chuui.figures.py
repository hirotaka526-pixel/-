# -*- coding: utf-8 -*-
"""「『安くします』と言われたら、まず疑ってほしい理由」の図解。

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


# ── 図1: 生コンクリート価格の仕組み ──────────────────────
def fig_namakon_kakaku_shikumi():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '生コンクリートの価格は、地域の協同組合でほぼ統一されています', 18))

    s.append(card(30, 70, 820, 90, TINT, accent=NAVY))
    s.append(txt(60, 104, '地域の生コン協同組合', 16, NAVY, '700'))
    s.append(txt(60, 132, '中小企業等協同組合法にもとづき、独占禁止法のカルテル適用除外として統一価格を設定', 14, INK2, '400'))

    s.append(card(30, 180, 380, 60, SURF, accent=GOOD))
    s.append(txt(220, 216, 'A社で購入', 15, GOOD_D, '700', 'middle'))

    s.append(card(470, 180, 380, 60, SURF, accent=GOOD))
    s.append(txt(660, 216, 'B社で購入', 15, GOOD_D, '700', 'middle'))

    s.append(txt(0, 258, '自社でプラントを持つ住宅会社はまず無く、どの会社で買っても価格はほぼ同じ', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '生コンクリート価格の仕組み',
                '生コンクリートの価格は、中小企業等協同組合法にもとづき地域の協同組合がほぼ統一して設定している。住宅会社が自社でプラントを持つことはまず無く、どの会社で購入しても価格はほぼ同じになる。')


# ── 図2: 「利益を削ってまで安くする」はなぜ怪しいか ──────────────────────
def fig_rieki_kezuru_ayashisa():
    W, H = 880, 240
    s = []
    s.append(heading(0, 34, '利益を削ってまで安くする会社は、継続できるでしょうか', 18))

    s.append(card(30, 70, 380, 130, TINT, accent=NAVY))
    s.append(txt(220, 104, '会社の利益', 16, NAVY, '700', 'middle'))
    s.append(txt(220, 132, '事業を続けるために必要な原資', 14, INK2, '400', 'middle'))
    s.append(txt(220, 154, '人件費・経費・将来への投資の元になる', 14, INK2, '400', 'middle'))

    s.append(card(470, 70, 380, 130, '#f7e9e6', accent=CRIT_D))
    s.append(txt(660, 104, '利益を大きく削る', 16, CRIT_D, '700', 'middle'))
    s.append(txt(660, 132, '特定のお客様だけ特別に安く', 14, INK2, '400', 'middle'))
    s.append(txt(660, 154, '→ 経営として無理が生じやすい', 14, CRIT_D, '700', 'middle'))

    s.append(txt(0, 226, '根拠があいまいなまま「安くします」とだけ説明される場合は、慎重に判断する', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '利益を削ってまで安くする会社への注意',
                '会社の利益は事業を続けるための原資であり、利益を大きく削って特定の客だけ安くするのは経営として無理が生じやすい。根拠があいまいな値引き説明は慎重に判断すべき。')


# ── 図3: 大工さんの日当と技術の関係 ──────────────────────
def fig_daiku_nittou_hikaku():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '日当の違いは、積み重ねてきた経験と技術の差でもあります', 18))

    s.append(card(30, 70, 380, 150, TINT, accent=WARN_D))
    s.append(txt(220, 102, '日当1万円', 20, WARN_D, '700', 'middle'))
    s.append(txt(220, 134, '経験年数が浅いことが多い', 14, INK2, '400', 'middle'))
    s.append(txt(220, 156, '道具・知識の蓄積がまだ少ない', 14, INK2, '400', 'middle'))

    s.append(card(470, 70, 380, 150, FOREST_L, accent=GOOD_D))
    s.append(txt(660, 102, '日当3万円', 20, GOOD_D, '700', 'middle'))
    s.append(txt(660, 134, '経験・知識・道具の積み重ね', 14, INK2, '400', 'middle'))
    s.append(txt(660, 156, 'その対価として評価されている', 14, INK2, '400', 'middle'))

    s.append(txt(0, 250, '安さだけを求めることは、積み重ねの少ない職人に頼むことと同じ意味になりかねない', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '大工さんの日当と技術の関係',
                '日当1万円の職人と日当3万円の職人では、積み重ねてきた経験・知識・道具への投資の差がある。安さだけを求めることは、積み重ねの少ない職人に頼むことと同じ意味になりかねない。')


FIGURES = {
    'namakon-kakaku-shikumi': (fig_namakon_kakaku_shikumi, '図1：生コンクリート価格の仕組み'),
    'rieki-kezuru-ayashisa':  (fig_rieki_kezuru_ayashisa,  '図2：「利益を削ってまで安くする」会社への注意'),
    'daiku-nittou-hikaku':    (fig_daiku_nittou_hikaku,    '図3：大工さんの日当と技術の関係'),
}
