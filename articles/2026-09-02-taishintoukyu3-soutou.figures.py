# -*- coding: utf-8 -*-
"""「耐震等級3『相当』は本物か」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross, dash, arrow, pill, chip)


# ── 図1: 「認定」と「相当」の証明の有無 ──────────────────────
def fig_shoumei():
    W, H = 880, 320
    s = []
    s.append(txt(0, 28, '同じ「耐震等級3」でも、証明できるかどうかが違う', 17, INK, '700'))

    # 左: 認定
    s.append(box(0, 56, 400, 220, '#f1faf3', GOOD, 1.5, 10))
    s.append(txt(20, 90, '耐震等級3（認定）', 18, GOOD_D, '700'))
    s.append(check(24, 118)); s.append(txt(50, 130, '第三者機関の審査を受けている', 14, INK))
    s.append(check(24, 148)); s.append(txt(50, 160, '住宅性能評価書を取得できる', 14, INK))
    s.append(check(24, 178)); s.append(txt(50, 190, '地震保険の割引に使える', 14, INK))
    s.append(box(20, 214, 360, 46, '#dff0e3', GOOD, 1.2, 6))
    s.append(txt(200, 242, '公的な証明書がある', 15, GOOD_D, '700', 'middle'))

    # 右: 相当
    s.append(box(480, 56, 400, 220, '#fdf2f2', CRIT, 1.5, 10))
    s.append(txt(500, 90, '耐震等級3「相当」', 18, CRIT_D, '700'))
    s.append(cross(504, 118)); s.append(txt(530, 130, '第三者機関の審査は受けていない', 14, INK))
    s.append(cross(504, 148)); s.append(txt(530, 160, '住宅性能評価書は存在しない', 14, INK))
    s.append(cross(504, 178)); s.append(txt(530, 190, '地震保険の割引に使えない可能性', 14, INK))
    s.append(box(500, 214, 360, 46, '#fbe3e3', CRIT, 1.2, 6))
    s.append(txt(680, 242, '公的な証明書がない', 15, CRIT_D, '700', 'middle'))

    s.append(txt(0, 300, '※ 性能そのものの高低ではなく、客観的に確認できる証明があるかどうかの違い', 13, INK2))
    return wrap(''.join(s), W, H,
                '耐震等級3の認定と相当の違い',
                '認定は第三者機関の審査を受け住宅性能評価書を取得でき地震保険の割引に使える。相当は審査を受けておらず証明書が存在しないため割引に使えない可能性がある。')


# ── 図2: 「相当」の2つのパターン ──────────────────────
def fig_pattern():
    W, H = 880, 300
    s = []
    s.append(txt(0, 28, '「相当」には、まったく違う2つの実態がある', 17, INK, '700'))

    s.append(box(0, 56, 420, 210, TINT, BLUE, 1.5, 10))
    s.append(txt(20, 88, 'パターンA', 14, BLUE_M, '700'))
    s.append(txt(20, 114, '計算はしているが、申請していない', 16, INK, '700'))
    s.append(txt(20, 146, '許容応力度計算まで実施済み。', 14, INK2))
    s.append(txt(20, 168, '第三者機関への申請費用と手間を', 14, INK2))
    s.append(txt(20, 190, 'かけていないだけ。', 14, INK2))
    s.append(box(20, 212, 380, 40, '#e8f0fb', BLUE, 1, 6))
    s.append(txt(210, 237, '聞けば計算書がすぐ出てくる', 14, BLUE_M, '700', 'middle'))

    s.append(box(460, 56, 420, 210, '#fdf2f2', CRIT, 1.5, 10))
    s.append(txt(480, 88, 'パターンB', 14, CRIT_D, '700'))
    s.append(txt(480, 114, 'そもそも構造計算をしていない', 16, INK, '700'))
    s.append(txt(480, 146, '「頑丈な工法だから」「経験上', 14, INK2))
    s.append(txt(480, 168, '大丈夫」といった感覚的な説明で、', 14, INK2))
    s.append(txt(480, 190, '1棟ごとの計算がない。', 14, INK2))
    s.append(box(480, 212, 380, 40, '#fbe3e3', CRIT, 1, 6))
    s.append(txt(670, 237, '根拠となる書類が存在しない', 14, CRIT_D, '700', 'middle'))

    s.append(txt(0, 280, '見分け方：「その根拠になった構造計算書を見せてもらえますか」と聞く', 14, INK, '700'))
    return wrap(''.join(s), W, H,
                '「相当」の2つのパターン',
                'パターンAは許容応力度計算まで実施済みだが申請していないだけで聞けば計算書が出てくる。パターンBはそもそも構造計算をしておらず根拠となる書類が存在しない。')


# ── 図3: 地震保険の耐震等級割引 ──────────────────────
def fig_hoken_waribiki():
    W, H = 880, 330
    s = []
    s.append(txt(0, 28, '地震保険の耐震等級割引（証明書類が必要）', 17, INK, '700'))

    bars = [
        ('耐震等級1', 10, BLUE_L, INK),
        ('耐震等級2', 30, BLUE, SURF),
        ('耐震等級3', 50, NAVY, SURF),
    ]
    x0 = 140
    track_w = 620
    maxv = 50
    y0 = 60
    bar_h = 46
    for i, (label, val, color, tcol) in enumerate(bars):
        y = y0 + i * 62
        s.append(txt(0, y + bar_h / 2 + 5, label, 15, INK, '700'))
        s.append(box(x0, y, track_w, bar_h, TINT, LINE, 1, 6))
        w = val / maxv * track_w
        s.append(box(x0, y, w, bar_h, color, color, 1, 6))
        s.append(txt(x0 + w - 14, y + bar_h / 2 + 5, f'{val}%割引', 14, tcol, '700', 'end'))

    s.append(box(0, y0 + 3 * 62 + 6, 880, 76, '#fff8e6', WARN, 1.5))
    s.append(txt(20, y0 + 3 * 62 + 30, '「相当」は証明書がないため、上記の割引が使えない可能性があります。', 14, WARN_D, '700'))
    s.append(txt(20, y0 + 3 * 62 + 56, '実際の扱いは保険会社によって異なるため、契約前に必ず直接確認してください。', 13, INK2))
    return wrap(''.join(s), W, H,
                '地震保険の耐震等級割引率',
                '地震保険の耐震等級割引は耐震等級1で10%、2で30%、3で50%。適用には建設住宅性能評価書等の証明書類が必要で、相当を自称しているだけでは割引を受けられない可能性がある。')


FIGURES = {
    'shoumei':        (fig_shoumei,        '図1：耐震等級3の「認定」と「相当」の違い'),
    'pattern':        (fig_pattern,        '図2：「相当」の2つのパターン'),
    'hoken-waribiki': (fig_hoken_waribiki, '図3：地震保険の耐震等級割引率（証明書類が必要）'),
}
