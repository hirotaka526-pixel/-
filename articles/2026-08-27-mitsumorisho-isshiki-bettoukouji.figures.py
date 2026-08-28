# -*- coding: utf-8 -*-
"""「見積書の一式は危険信号」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross, dash, arrow, pill, chip)


# ── 図1: 「一式」は中身が見えない箱 ──────────────────────
def fig_isshiki():
    W, H = 880, 360
    s = []
    s.append(txt(0, 28, '「一式」は、中身が見えない箱です', 17, INK, '700'))

    # 左: 封をされた箱(一式)
    s.append(box(0, 56, 400, 240, '#fdf2f2', CRIT, 1.5, 10))
    s.append(f'<rect x="40" y="96" width="320" height="150" rx="8" fill="#f6d9d9" stroke="{CRIT}" stroke-width="2"/>')
    s.append(f'<path d="M40 150 h320 M200 96 v150" stroke="{CRIT}" stroke-width="2" stroke-dasharray="6 5"/>')
    s.append(txt(200, 128, '？', 34, CRIT, '700', 'middle'))
    s.append(txt(200, 180, '？', 34, CRIT, '700', 'middle'))
    s.append(txt(200, 232, '？', 34, CRIT, '700', 'middle'))
    s.append(txt(20, 322, '電気工事　一式　800,000円', 15, INK, '700'))

    # 右: 開いた内訳明細
    s.append(box(480, 56, 400, 240, '#f1faf3', GOOD, 1.5, 10))
    rows = [('コンセント 24か所', '96,000'), ('スイッチ 18か所', '72,000'),
            ('照明器具取付 16台', '80,000'), ('分電盤 1面', '85,000'),
            ('幹線・配線工事', '467,000')]
    for i, (a, c) in enumerate(rows):
        y = 92 + i * 34
        s.append(check(500, y - 12, GOOD))
        s.append(txt(524, y, a, 14, INK))
        s.append(txt(858, y, c, 14, INK, '600', 'end'))
    s.append(txt(500, 322, '数量と単価が入った内訳明細', 15, GOOD_D, '700'))

    return wrap(''.join(s), W, H,
                '一式表記と内訳明細の違い',
                '一式表記の見積書は数量も単価も分からず中身が見えない箱の状態。内訳明細では数量と単価が1行ずつ分かり、他社との比較や減額の相談ができる。')


# ── 図2: 別途工事で総額が積み上がる ──────────────────────
def fig_bettouzumiage():
    W, H = 880, 450
    s = []
    s.append(txt(0, 28, '「本体価格」だけで判断すると、総額はこれだけ変わります', 17, INK, '700'))

    items = [
        ('本体価格', 2800, BLUE),
        ('地盤改良', 60, WARN),
        ('外構工事', 200, WARN),
        ('照明・カーテン', 80, WARN),
        ('エアコン', 60, WARN),
        ('給排水引込', 70, WARN),
    ]
    total = sum(v for _, v, _ in items)
    scale = 620 / total  # 幅の最大を620pxに
    x = 40
    y = 70
    bar_h = 60
    for label, val, color in items:
        w = val * scale
        s.append(box(x, y, w, bar_h, color, color, 1, 3))
        x += w
    s.append(txt(40, y - 12, '本体価格', 13, BLUE_M, '700'))
    s.append(txt(40 + (2800*scale)/2, y + bar_h/2 + 5, '2,800万円', 14, SURF, '700', 'middle'))

    # 積み上げ部分のラベル(引き出し線)。区間が狭いとラベルが重なるので
    # x位置は均等配置にし、実際のバー中心へ引き出し線で結ぶ
    lx = 40 + 2800 * scale
    labels = ['地盤改良\n60万円', '外構工事\n200万円', '照明等\n80万円', 'エアコン\n60万円', '給排水\n70万円']
    bar_centers = []
    xx = lx
    for _, val, _ in items[1:]:
        bar_centers.append(xx + val * scale / 2)
        xx += val * scale
    n = len(bar_centers)
    label_span = 880 - lx - 10
    label_xs = [lx + label_span * (i + 0.5) / n for i in range(n)]
    for i, (lbl, bx, tx) in enumerate(zip(labels, bar_centers, label_xs)):
        ty = y + bar_h + 46
        s.append(f'<line x1="{bx}" y1="{y+bar_h}" x2="{bx}" y2="{y+bar_h+14}" '
                 f'stroke="{MUTE}" stroke-width="1.2"/>')
        s.append(f'<line x1="{bx}" y1="{y+bar_h+14}" x2="{tx}" y2="{ty-28}" '
                 f'stroke="{MUTE}" stroke-width="1.2"/>')
        name, yen = lbl.split('\n')
        s.append(txt(tx, ty - 16, name, 12, INK2, '600', 'middle'))
        s.append(txt(tx, ty, yen, 12, INK2, '700', 'middle'))

    s.append(box(0, 330, 880, 90, '#fff8e6', WARN, 1.5))
    s.append(txt(20, 360, '本体価格だけで比較すると', 14, WARN_D, '700'))
    s.append(txt(20, 386, '「2,800万円の家」のはずが、別途工事を足すと総額は約3,270万円に。', 16, INK, '700'))
    s.append(txt(20, 410, 'これは一例です。実際の金額は建てる場所や仕様で変わります。', 13, INK2))
    return wrap(''.join(s), W, H,
                '本体価格に別途工事を足すと総額はどう変わるか',
                '本体価格2800万円に地盤改良・外構・照明・エアコン・給排水引込などの別途工事を積み上げると総額は約3270万円になる例。数字は一例で実際は現場ごとに変わる。')


# ── 図3: 地盤改良工法別の費用相場 ──────────────────────
def fig_jibankaikou():
    W, H = 880, 260
    s = []
    s.append(txt(0, 28, '地盤改良費の目安（30坪程度）', 17, INK, '700'))
    bars = [
        ('表層改良', 30, 50, BLUE_L, INK),
        ('柱状改良', 50, 100, BLUE, SURF),
    ]
    y0 = 60
    maxv = 110
    track_w = 640
    for i, (label, lo, hi, color, tcol) in enumerate(bars):
        y = y0 + i * 70
        s.append(txt(0, y + 28, label, 15, INK, '700'))
        s.append(box(140, y, track_w, 44, TINT, LINE, 1, 6))
        lo_x = 140 + lo / maxv * track_w
        hi_x = 140 + hi / maxv * track_w
        s.append(box(lo_x, y, hi_x - lo_x, 44, color, color, 1, 6))
        s.append(txt((lo_x + hi_x) / 2, y + 29, f'{lo}〜{hi}万円', 14, tcol, '700', 'middle'))
    s.append(txt(0, y0 + 160, '※ 一般的な相場の目安です。実際の金額は地盤調査の結果と施工会社によって変わります', 13, INK2))
    return wrap(''.join(s), W, H,
                '表層改良と柱状改良の費用相場比較',
                '30坪程度の場合、表層改良は30万〜50万円、柱状改良は50万〜100万円が一般的な相場の目安。実際の金額は地盤調査の結果と施工会社による。')


FIGURES = {
    'isshiki':      (fig_isshiki,      '図1：一式表記と、数量・単価が入った内訳明細の違い'),
    'bettouzumiage':(fig_bettouzumiage,'図2：本体価格に別途工事を積み上げると総額はどう変わるか'),
    'jibankaikou':  (fig_jibankaikou,  '図3：地盤改良費（表層改良・柱状改良）の費用相場'),
}
