# -*- coding: utf-8 -*-
"""「基礎工事『2週間で上棟』と言われたら、確認したいこと」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD, GOLD_D,
                     wrap, txt, box, heading, card, badge, check_badge,
                     cross_badge, dash, arrow, icon_badge, pin_icon)


# ── 図1: 基礎工事の工程タイムライン ──────────────────────
def fig_kiso_koutei_timeline():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '基礎工事は、着工から完成まで大体1ヶ月程度の工程が目安です', 18))

    steps = ['着工\n(掘削・配筋)', 'コンクリート\n打設', '養生期間\n(強度の発現)', '基礎\n完成', '上棟']
    n = len(steps)
    gap = 20
    box_w = (880 - gap * (n - 1)) / n
    y = 90
    box_h = 56
    for i, label in enumerate(steps):
        x = i * (box_w + gap)
        s.append(box(x, y, box_w, box_h, TINT, NAVY, 1.2, 10))
        lines = label.split('\n')
        for j, line in enumerate(lines):
            s.append(txt(x + box_w / 2, y + 24 + j * 18, line, 14, INK, '700', 'middle'))
        if i < n - 1:
            s.append(txt(x + box_w + gap / 2, y + box_h / 2 + 5, '→', 16, MUTE, '700', 'middle'))

    s.append(txt(0, y + box_h + 50, '基礎着工から上棟まで、おおよそ1ヶ月程度を見込む工程が一般的', 15, INK2, '400'))
    s.append(txt(0, y + box_h + 76, '雨天の日はコンクリートを打てないため、余裕を持った工程が組まれているかがポイント', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                '基礎工事の工程タイムライン',
                '基礎工事は着工(掘削・配筋)からコンクリート打設、養生期間、基礎完成、上棟まで、おおよそ1ヶ月程度の工程が一般的な目安。雨天の日はコンクリートを打てないため、余裕を持った工程が組まれているかがポイントになる。')


# ── 図2: コンクリートの強度発現の推移 ──────────────────────
def fig_kyoudo_hassei_suii():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, 'コンクリートの強度は、時間をかけて発現していきます', 18))

    x0, x1 = 60, 820
    y0, y1 = 220, 90
    # 軸
    s.append(box(x0, y1, 2, y0 - y1, MUTE, MUTE, 0, 0))
    s.append(box(x0, y0, x1 - x0, 2, MUTE, MUTE, 0, 0))

    # 強度カーブ(簡易な折れ線で表現)
    pts = [(x0, y0), (x0 + (x1 - x0) * 0.25, y0 - (y0 - y1) * 0.55),
           (x0 + (x1 - x0) * 0.6, y0 - (y0 - y1) * 0.85),
           (x1, y0 - (y0 - y1) * 1.0)]
    path = f'M{pts[0][0]} {pts[0][1]} ' + ' '.join(f'L{px} {py}' for px, py in pts[1:])
    s.append(f'<path d="{path}" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')

    s.append(txt(x0, y0 + 24, '打設直後', 14, INK2, '400'))
    s.append(txt(x0 + (x1 - x0) * 0.25, y0 + 24, '7日', 14, INK2, '400', 'middle'))
    s.append(txt(x1, y0 + 24, '28日(約4週間)', 14, GOLD_D, '700', 'end'))

    s.append(box(x1 - 4, y1 + 10, 4, y0 - y1 - 10, GOLD, GOLD, 0, 0))
    s.append(txt(x1, y1 - 6, '設計基準強度の目安', 14, GOLD_D, '700', 'end'))

    s.append(txt(x0, y1 - 14, '強度 →', 14, MUTE, '400'))

    return wrap(''.join(s), W, H,
                'コンクリートの強度発現の推移',
                'コンクリートの強度は打設直後から徐々に発現し、材齢28日(約4週間)で設計基準強度に達するのが一般的な目安。打った瞬間に完成するのではなく、時間をかけて強度が上がっていく。')


# ── 図3: 工事中に確認したいポイント ──────────────────────
def fig_kiso_kakunin_point():
    W = 880
    s = []
    s.append(heading(0, 34, '基礎工事の期間について、これを確認してください', 18))

    items = [
        ('基礎着工から上棟までの工程', '1ヶ月程度を目安に、極端に短くなっていないか確認する'),
        ('コンクリート打設から上棟までの間隔', '最低でも2週間程度空いているかを確認する'),
        ('雨天・低温時の対応', '天候によって工程を調整する前提になっているか確認する'),
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
                '基礎工事の期間について確認したい3つのポイント',
                '基礎着工から上棟までの工程が1ヶ月程度を目安に極端に短くなっていないか、コンクリート打設から上棟までの間隔が最低でも2週間程度空いているか、雨天・低温時の対応が天候によって工程を調整する前提になっているかの3点。')


FIGURES = {
    'kiso-koutei-timeline':   (fig_kiso_koutei_timeline,   '図1：基礎工事の工程タイムライン'),
    'kyoudo-hassei-suii':     (fig_kyoudo_hassei_suii,     '図2：コンクリートの強度発現の推移'),
    'kiso-kakunin-point':     (fig_kiso_kakunin_point,     '図3：工事中に確認したい3つのポイント'),
}
