# -*- coding: utf-8 -*-
"""「間取りは誰が描いていますか？」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
「もっと分かりやすい内容で」という要望を受け、専門用語を減らし、視覚的な比較を中心にした。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross)


# ── 図1: 営業マンが描く間取り vs 建築士が描く間取り ──────────────────────
def fig_eigyou_vs_kenchikushi():
    W, H = 880, 320
    s = []
    s.append(txt(0, 28, '同じ間取り図でも、検討している深さが違います', 17, INK, '700'))

    # 左: 営業マンが描く間取り(浅い)
    s.append(box(30, 60, 380, 220, TINT, LINE, 1.5, 10))
    s.append(txt(220, 90, '営業担当が描く間取り', 15, INK, '700', 'middle'))
    items1 = [('部屋の配置', True), ('部屋の広さ', True), ('壁の中の構造', False), ('配管・納まり', False)]
    for i, (label, ok) in enumerate(items1):
        y = 122 + i * 34
        s.append((check if ok else cross)(60, y, GOOD if ok else CRIT))
        s.append(txt(80, y + 5, label, 14, INK, '600'))

    # 右: 建築士が描く間取り(深い)
    s.append(box(470, 60, 380, 220, '#f1faf3', GOOD, 1.5, 10))
    s.append(txt(660, 90, '建築士が描く間取り', 15, GOOD_D, '700', 'middle'))
    items2 = [('部屋の配置', True), ('部屋の広さ', True), ('壁の中の構造', True), ('配管・納まり', True)]
    for i, (label, ok) in enumerate(items2):
        y = 122 + i * 34
        s.append(check(500, y, GOOD))
        s.append(txt(520, y + 5, label, 14, INK, '600'))

    s.append(txt(0, 300, '見た目が同じ間取り図でも、想定している範囲がまったく違います', 13, INK2, '600'))
    return wrap(''.join(s), W, H,
                '営業担当が描く間取りと建築士が描く間取りの違い',
                '営業担当が描く間取りは部屋の配置と広さのみを検討することが多いのに対し、建築士が描く間取りは壁の中の構造や配管の納まりまで想定して描かれている。見た目が同じ間取り図でも検討している範囲が異なる。')


# ── 図2: 優先順位の3段階 ──────────────────────
def fig_yuusenjyuni():
    W, H = 880, 300
    s = []
    s.append(txt(0, 28, '要望を3段階に分けると、判断の基準ができます', 17, INK, '700'))

    levels = [
        ('①必ず叶えたいこと', '家事動線、生活音対策など', NAVY, 560),
        ('②できれば叶えたいこと', '対面キッチン、パントリーなど', BLUE, 380),
        ('③余裕があれば叶えたいこと', '書斎、造作家具など', BLUE_L, 200),
    ]
    cx = 440
    top = 60
    for i, (label, note, color, w) in enumerate(levels):
        y = top + i * 60
        x = cx - w / 2
        tcol = SURF if color != BLUE_L else INK
        s.append(box(x, y, w, 46, color, color, 0, 8))
        s.append(txt(cx, y + 20, label, 15, tcol, '700', 'middle'))
        s.append(txt(cx, y + 38, note, 11, tcol, '400', 'middle'))

    s.append(txt(0, top + 3 * 60 + 20, '削るときは③→②の順。①は最後まで残します', 13, INK2, '700'))
    return wrap(''.join(s), W, H,
                '間取りの要望を3段階に分けたピラミッド図',
                '要望を必ず叶えたいこと、できれば叶えたいこと、余裕があれば叶えたいことの3段階に分ける。予算オーバー時は余裕があればの層から削り、必ず叶えたいことは最後まで残す。')


# ── 図3: 予算オーバー時に削る順番 ──────────────────────
def fig_kezuru_jyunban():
    W, H = 880, 260
    s = []
    s.append(txt(0, 28, '予算オーバーになったとき、削る順番を間違えないでください', 17, INK, '700'))

    steps = [
        ('1', '③余裕があれば', 'まずここから見直す', BLUE_L, INK),
        ('2', '②できればの中の低優先度', '次にここを見直す', BLUE, SURF),
        ('3', '①必ず叶えたいこと', '最後まで残す（構造・性能など）', NAVY, SURF),
    ]
    for i, (num, label, note, color, tcol) in enumerate(steps):
        x = 40 + i * 280
        s.append(box(x, 60, 240, 130, color, color, 0, 10))
        s.append(txt(x + 120, 95, num, 26, tcol, '700', 'middle'))
        s.append(txt(x + 120, 130, label, 14, tcol, '700', 'middle'))
        s.append(txt(x + 120, 155, note, 12, tcol, '400', 'middle'))
        if i < 2:
            s.append(txt(x + 260, 125, '→', 22, INK2, '700', 'middle'))

    s.append(txt(0, 230, '①の構造・耐震性・断熱気密は、後から変更しづらく住み心地に直結します', 13, INK2, '600'))
    return wrap(''.join(s), W, H,
                '予算オーバー時に削る順番の図',
                '予算オーバー時はまず余裕があればの層、次にできればの中の低優先度のものを見直し、必ず叶えたいこと(構造・耐震性・断熱気密など)は最後まで残す。')


FIGURES = {
    'eigyou-vs-kenchikushi': (fig_eigyou_vs_kenchikushi, '図1：営業担当が描く間取りと建築士が描く間取りの違い'),
    'yuusenjyuni-3dankai':   (fig_yuusenjyuni,            '図2：間取りの要望を3段階に分けたピラミッド図'),
    'kezuru-jyunban':        (fig_kezuru_jyunban,         '図3：予算オーバー時に削る順番の図'),
}
