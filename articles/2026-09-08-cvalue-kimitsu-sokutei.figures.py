# -*- coding: utf-8 -*-
"""「『高気密です』は測定なしでは根拠がない」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross, dash, arrow, pill, chip)


# ── 図1: C値には国の基準がない ──────────────────────
def fig_kijun_nashi():
    W, H = 880, 300
    s = []
    s.append(txt(0, 28, 'C値には、今の建築基準法・省エネ基準の中に基準がありません', 17, INK, '700'))

    # 年表(横軸)
    axis_y = 110
    x0, x1, x2 = 60, 430, 820
    s.append(f'<line x1="{x0}" y1="{axis_y}" x2="{x2}" y2="{axis_y}" stroke="{LINE}" stroke-width="2"/>')
    for x, label in [(x0, '1999年'), (x1, '2009年'), (x2, '現在')]:
        s.append(f'<circle cx="{x}" cy="{axis_y}" r="5" fill="{INK}"/>')
        s.append(txt(x, axis_y + 26, label, 14, INK, '700', 'middle'))

    s.append(box(x0 - 20, 56, x1 - x0 + 40, 36, '#f1faf3', GOOD, 1.2, 6))
    s.append(txt(x0 + (x1 - x0) / 2, 79, '次世代省エネ基準にC値の基準あり', 13, GOOD_D, '700', 'middle'))

    s.append(box(x1 - 20, 140, x2 - x1 + 40, 36, '#fdf2f2', CRIT, 1.2, 6))
    s.append(txt(x1 + (x2 - x1) / 2, 163, '法改正で基準が削除。今もそのまま', 13, CRIT_D, '700', 'middle'))

    s.append(box(0, 210, 880, 70, '#fff8e6', WARN, 1.5))
    s.append(txt(20, 238, '基準が無い、ということは', 14, WARN_D, '700'))
    s.append(txt(20, 262, '測定していなくても「高気密です」と言えてしまう、ということです', 15, INK, '700'))
    return wrap(''.join(s), W, H,
                'C値の基準が2009年に削除された経緯',
                '1999年の次世代省エネ基準にはC値の基準があったが2009年の法改正で削除され現在も基準がない状態が続いている。基準が無いということは測定していなくても高気密と言えてしまうということ。')


# ── 図2: 全棟測定と一部測定の違い ──────────────────────
def fig_zentou_vs_ichibu():
    W, H = 880, 300
    s = []
    s.append(txt(0, 28, '「全棟測定」と「一部だけ測定」では、隠せるかどうかが違います', 17, INK, '700'))

    # 左: 一部だけ測定(モデルハウス1棟だけ緑、他はグレーの?)
    s.append(box(0, 56, 420, 200, '#fdf2f2', CRIT, 1.5, 10))
    s.append(txt(20, 86, '一部の棟だけ測定', 15, CRIT_D, '700'))
    houses1 = ['◎', '?', '?', '?', '?', '?']
    for i, mark in enumerate(houses1):
        x = 30 + (i % 3) * 120
        y = 110 + (i // 3) * 60
        color = GOOD if mark == '◎' else MUTE
        s.append(box(x, y, 90, 44, TINT, color, 1.5, 6))
        s.append(txt(x + 45, y + 29, mark, 20, color, '700', 'middle'))
    s.append(txt(20, 236, 'モデルハウスだけ良い数値、他は未測定', 13, CRIT_D, '700'))

    # 右: 全棟測定(全部数字が入っている)
    s.append(box(460, 56, 420, 200, '#f1faf3', GOOD, 1.5, 10))
    s.append(txt(480, 86, '全棟測定', 15, GOOD_D, '700'))
    vals = ['0.28', '0.31', '0.25', '0.33', '0.29', '0.30']
    for i, v in enumerate(vals):
        x = 490 + (i % 3) * 120
        y = 110 + (i // 3) * 60
        s.append(box(x, y, 90, 44, TINT, GOOD, 1.5, 6))
        s.append(txt(x + 45, y + 29, v, 16, GOOD_D, '700', 'middle'))
    s.append(txt(480, 236, '建てる家ごとに数値が残り、隠せない', 13, GOOD_D, '700'))
    s.append(txt(0, 284, '※ 右の数値は実測イメージの一例です', 12, INK2))
    return wrap(''.join(s), W, H,
                '一部の棟だけ測定する会社と全棟測定する会社の違い',
                '一部の棟だけ測定する会社はモデルハウスなど良い数値の棟だけを見せ他は未測定のことがある。全棟測定する会社は建てる家ごとに数値が残り悪い数値も隠せない。')


# ── 図3: C値の目安スケール ──────────────────────
def fig_cvalue_mokuyasu():
    W, H = 880, 260
    s = []
    s.append(txt(0, 28, 'C値の目安（値が小さいほど気密性能が高い）', 17, INK, '700'))

    track_x, track_w = 60, 760
    track_y = 90
    s.append(box(track_x, track_y, track_w, 40, TINT, LINE, 1, 8))

    # スケール: 0 ~ 3.0 を track_w にマップ(左が0=高性能)
    maxv = 3.0
    def xpos(v):
        return track_x + track_w * (1 - v / maxv)

    # ゾーン: 一般的な新築の目安 ~1.0以下, 業界上位 0.5前後, 弊社基準 0.3以下
    zones = [
        (1.0, maxv, MUTE, '基準がない中での平均的な水準'),
        (0.5, 1.0, BLUE_L, '「高気密住宅」の目安とされる水準'),
        (0.3, 0.5, BLUE, '業界内でも高い水準を公開する会社が増えている'),
        (0.0, 0.3, NAVY, '弊社の自社合格基準'),
    ]
    for lo, hi, color, label in zones:
        x1, x2 = xpos(hi), xpos(lo)
        s.append(box(x1, track_y, x2 - x1, 40, color, color, 0, 0))

    for v in [0, 0.3, 0.5, 1.0, 2.0, 3.0]:
        x = xpos(v)
        s.append(f'<line x1="{x}" y1="{track_y+40}" x2="{x}" y2="{track_y+48}" stroke="{INK2}" stroke-width="1.5"/>')
        s.append(txt(x, track_y + 66, f'{v}', 13, INK2, '600', 'middle'))

    ly = track_y + 90
    legend = [(NAVY, '0.3以下：弊社の合格基準（これまで0.4を超えたことはありません）'),
              (BLUE, '0.3〜0.5：業界内でも高い水準として公開されることがある帯'),
              (BLUE_L, '0.5〜1.0：一般に「高気密住宅」の目安とされる帯')]
    for i, (color, label) in enumerate(legend):
        y = ly + i * 24
        s.append(box(0, y - 14, 16, 16, color, color, 0, 3))
        s.append(txt(24, y, label, 13, INK, '600'))
    return wrap(''.join(s), W, H,
                'C値の目安スケール',
                '値が小さいほど気密性能が高い。0.5〜1.0が一般的な高気密住宅の目安、0.3〜0.5は業界内でも高い水準、0.3以下が自社の合格基準でこれまで0.4を超えたことはない。')


FIGURES = {
    'kijun-nashi':        (fig_kijun_nashi,        '図1：C値の基準が2009年に削除された経緯'),
    'zentou-vs-ichibu':   (fig_zentou_vs_ichibu,   '図2：一部の棟だけ測定する会社と全棟測定する会社の違い'),
    'cvalue-mokuyasu':    (fig_cvalue_mokuyasu,    '図3：C値の目安スケール'),
}
