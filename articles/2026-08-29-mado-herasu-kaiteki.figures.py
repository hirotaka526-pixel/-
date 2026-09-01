# -*- coding: utf-8 -*-
"""「窓を減らすと家は快適になる理由」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross, dash, arrow, pill, chip)


# ── 図1: 冬の暖房時、熱が逃げる場所の内訳 ──────────────────────
def fig_netsuson():
    W, H = 880, 340
    s = []
    s.append(txt(0, 28, '冬、暖房の熱はどこから逃げているか（試算例）', 17, INK, '700'))

    items = [
        ('開口部（窓・ドア）', 58, NAVY),
        ('外壁', 19, BLUE),
        ('換気', 17, BLUE_L),
        ('床', 10, '#c7d9ee'),
        ('その他', 6, TINT),
    ]
    total = sum(v for _, v, _ in items)
    track_w = 700
    x = 90
    y = 70
    bar_h = 56
    for label, val, color in items:
        w = val / total * track_w
        s.append(box(x, y, w, bar_h, color, color, 1, 3))
        if val >= 15:
            tcol = SURF if color in (NAVY, BLUE) else INK
            s.append(txt(x + w / 2, y + bar_h / 2 + 6, f'{val}%', 15, tcol, '700', 'middle'))
        x += w

    # 凡例(3+2の2段組み。1段5項目だと880幅に収まらないため)
    ly = y + bar_h + 40
    row1, row2 = items[:3], items[3:]
    lx = 90
    for label, val, color in row1:
        s.append(box(lx, ly - 14, 16, 16, color, color, 0, 3))
        s.append(txt(lx + 24, ly, f'{label}　{val}%', 14, INK, '600'))
        lx += 230
    ly2 = ly + 34
    lx = 90
    for label, val, color in row2:
        s.append(box(lx, ly2 - 14, 16, 16, color, color, 0, 3))
        s.append(txt(lx + 24, ly2, f'{label}　{val}%', 14, INK, '600'))
        lx += 230
    s.append(txt(0, ly2 + 40, '※ 平成4年省エネ基準レベルの試算例（経済産業省資料より）。実際の割合は住宅の断熱仕様で変わります', 13, INK2))
    return wrap(''.join(s), W, H,
                '冬の暖房時に熱が逃げる場所の割合',
                '開口部が58%と最も大きく、外壁19%、換気17%、床10%、その他6%と続く。平成4年省エネ基準レベルの試算例。')


# ── 図2: 方角別の窓計画 ──────────────────────
def fig_hougaku():
    W, H = 880, 420
    s = []
    s.append(txt(0, 28, '窓は「数」ではなく「方角ごとの役割」で決める', 17, INK, '700'))

    cx, cy, size = 440, 240, 260
    half = size / 2
    # 建物本体(平面イメージ)
    s.append(box(cx - half, cy - half, size, size, TINT, LINE, 1.5, 6))

    # 南(下)：大きい窓
    s.append(box(cx - 90, cy + half - 14, 180, 14, NAVY, NAVY, 0, 3))
    # 北(上)：小さい窓
    s.append(box(cx - 24, cy - half, 48, 14, MUTE, MUTE, 0, 3))
    # 西(左)：最小限
    s.append(box(cx - half, cy - 24, 14, 48, CRIT, CRIT, 0, 3))
    # 東(右)：中くらい
    s.append(box(cx + half - 14, cy - 40, 14, 80, BLUE, BLUE, 0, 3))

    # ラベル(方角)
    s.append(txt(cx, cy - half - 16, '北', 16, INK, '700', 'middle'))
    s.append(txt(cx, cy + half + 24, '南', 16, INK, '700', 'middle'))
    s.append(txt(cx - half - 20, cy + 6, '西', 16, INK, '700', 'middle'))
    s.append(txt(cx + half + 20, cy + 6, '東', 16, INK, '700', 'middle'))

    # 凡例カード(右上→下に4枚)
    cards = [
        ('南', '大きめの窓で日射を取り込む。庇で夏の日射は遮る', NAVY),
        ('北', '最小限。日射のメリットがほぼなく熱損失だけ大きい', MUTE),
        ('西', '最小限。夏の西日が室温上昇の主な原因になる', CRIT),
        ('東', '朝日を取り込む程度の中くらいの窓', BLUE),
    ]
    ly = 60
    for label, desc, color in cards:
        s.append(box(0, ly, 6, 44, color, color, 0, 3))
        s.append(txt(18, ly + 18, label, 15, INK, '700'))
        s.append(txt(18, ly + 38, desc, 12, INK2))
        ly += 62
    return wrap(''.join(s), W, H,
                '方角ごとの窓の役割分担',
                '南面は大きめの窓で日射取得、北面と西面は最小限、東面は中くらい。窓は数ではなく方角ごとの役割で計画する。')


# ── 図3: サッシ・ガラスの性能グレード ──────────────────────
def fig_sassi_grade():
    W, H = 880, 330
    s = []
    s.append(txt(0, 28, 'サッシ・ガラスの組み合わせによる断熱性能のイメージ', 17, INK, '700'))
    grades = [
        ('アルミサッシ\n単板ガラス', 0.22, MUTE, INK),
        ('アルミ樹脂複合\nLow-E複層', 0.45, BLUE_L, INK),
        ('樹脂サッシ\nLow-E複層', 0.72, BLUE, SURF),
        ('樹脂サッシ\nLow-Eトリプル', 1.0, NAVY, SURF),
    ]
    track_w = 640
    x0 = 180
    y0 = 60
    bar_h = 46
    for i, (label, ratio, color, tcol) in enumerate(grades):
        y = y0 + i * 60
        name = label.split('\n')
        s.append(txt(0, y + bar_h / 2 - 6, name[0], 13, INK, '700'))
        s.append(txt(0, y + bar_h / 2 + 12, name[1], 12, INK2))
        s.append(box(x0, y, track_w, bar_h, TINT, LINE, 1, 6))
        w = ratio * track_w
        s.append(box(x0, y, w, bar_h, color, color, 1, 6))
        label_txt = ['断熱性能：低い', '断熱性能：やや低い', '断熱性能：高い', '断熱性能：最も高い'][i]
        s.append(txt(x0 + w - 12 if ratio > 0.3 else x0 + w + 12,
                      y + bar_h / 2 + 5, label_txt, 13,
                      tcol if ratio > 0.3 else INK, '700',
                      'end' if ratio > 0.3 else 'start'))
    s.append(txt(0, y0 + len(grades) * 60 + 22,
                 '※ 相対的なイメージ図です。実際の性能は製品ごとのU値・日射熱取得率で確認してください', 13, INK2))
    return wrap(''.join(s), W, H,
                'サッシとガラスの組み合わせ別の断熱性能イメージ',
                'アルミサッシ単板ガラスが最も断熱性能が低く、アルミ樹脂複合Low-E複層、樹脂サッシLow-E複層、樹脂サッシLow-Eトリプルの順に高くなる。相対的なイメージ図。')


FIGURES = {
    'netsuson':     (fig_netsuson,    '図1：冬の暖房時に熱が逃げる場所の割合（試算例）'),
    'hougaku':      (fig_hougaku,     '図2：方角ごとの窓の役割分担'),
    'sassi-grade':  (fig_sassi_grade, '図3：サッシ・ガラスの組み合わせ別の断熱性能イメージ'),
}
