# -*- coding: utf-8 -*-
"""「平屋はなぜ高い？」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross, dash, arrow, pill, chip)


# ── 図1: 同じ延床面積でも建築面積が違う ──────────────────────
def fig_heimen_hikaku():
    W, H = 880, 320
    s = []
    s.append(txt(0, 28, '延床30坪は同じでも、地面に接する面積（建築面積）が違います', 17, INK, '700'))

    # 左: 2階建て(15坪の四角を2段)
    cx1 = 150
    s.append(txt(cx1, 66, '2階建て（延床30坪）', 14, INK, '700', 'middle'))
    s.append(box(cx1 - 65, 80, 130, 60, BLUE_L, BLUE, 1.5, 6))
    s.append(txt(cx1, 116, '2階：15坪', 13, NAVY, '700', 'middle'))
    s.append(box(cx1 - 65, 150, 130, 60, BLUE_L, BLUE, 1.5, 6))
    s.append(txt(cx1, 186, '1階：15坪', 13, NAVY, '700', 'middle'))
    s.append(box(cx1 - 75, 222, 150, 24, TINT, LINE, 1, 5))
    s.append(txt(cx1, 239, '建築面積：15坪', 13, INK2, '700', 'middle'))

    # 右: 平屋(30坪を1段で)
    cx2 = 620
    s.append(txt(cx2, 66, '平屋（延床30坪）', 14, INK, '700', 'middle'))
    s.append(box(cx2 - 130, 80, 260, 130, '#fdf2f2', CRIT, 1.5, 6))
    s.append(txt(cx2, 150, '1階：30坪', 15, CRIT_D, '700', 'middle'))
    s.append(box(cx2 - 90, 222, 180, 24, TINT, LINE, 1, 5))
    s.append(txt(cx2, 239, '建築面積：30坪', 13, INK2, '700', 'middle'))

    s.append(box(0, 268, 880, 40, '#fff8e6', WARN, 1.5))
    s.append(txt(20, 293, '建築面積が広い分、基礎・屋根・外壁の工事範囲も広くなります', 14, WARN_D, '700'))
    return wrap(''.join(s), W, H,
                '延床面積が同じでも建築面積が異なる図',
                '延床30坪の2階建ては1フロア15坪ずつで建築面積15坪。同じ延床30坪の平屋は1階に全て収めるため建築面積30坪となり、基礎・屋根・外壁の工事範囲が広がる。')


# ── 図2: 必要な土地面積の目安 ──────────────────────
def fig_hitsuyou_tochi():
    W, H = 880, 300
    s = []
    s.append(txt(0, 28, '平屋（延床30坪）を建てる場合に必要な土地面積の目安', 17, INK, '700'))
    s.append(txt(0, 50, '※ 建ぺい率60%のエリアを想定した一般的な目安です。実際の数値は土地ごとに確認してください', 12, INK2))

    # 土地の外枠(50坪相当)と、建物の footprint(30坪相当)を入れ子で表示
    land_x, land_y, land_w, land_h = 240, 80, 400, 180
    s.append(box(land_x, land_y, land_w, land_h, TINT, LINE, 1.5, 8))
    s.append(txt(land_x + land_w / 2, land_y - 14, '土地：約50坪', 14, INK, '700', 'middle'))

    # 建ぺい率60%相当の建築面積を内側に(面積比60%になるよう縦横約77%ずつ)
    bld_w, bld_h = land_w * 0.77, land_h * 0.77
    bld_x = land_x + (land_w - bld_w) / 2
    bld_y = land_y + (land_h - bld_h) / 2
    s.append(box(bld_x, bld_y, bld_w, bld_h, '#fdf2f2', CRIT, 1.5, 6))
    s.append(txt(bld_x + bld_w / 2, bld_y + bld_h / 2 - 4, '建物：延床30坪', 14, CRIT_D, '700', 'middle'))
    s.append(txt(bld_x + bld_w / 2, bld_y + bld_h / 2 + 18, '（建築面積30坪）', 12, CRIT_D, '600', 'middle'))

    s.append(txt(land_x + land_w / 2, land_y + land_h + 30,
                  '外側の余白が、駐車場・庭・隣地との距離になります', 13, INK2, '600', 'middle'))
    return wrap(''.join(s), W, H,
                '平屋に必要な土地面積の目安',
                '建ぺい率60%のエリアで延床30坪の平屋を建てる場合土地は約50坪が目安。建物の周囲の余白が駐車場や庭隣地との距離になる。実際の数値は土地ごとに確認が必要。')


# ── 図3: 建物の形とコストの関係 ──────────────────────
def fig_katachi_cost():
    W, H = 880, 300
    s = []
    s.append(txt(0, 28, '建物の形がシンプルなほど、外壁・屋根の面積は小さくなります', 17, INK, '700'))

    # 左: シンプルな四角
    s.append(txt(150, 66, 'シンプルな形', 14, GOOD_D, '700', 'middle'))
    s.append(box(60, 84, 180, 140, '#f1faf3', GOOD, 2, 6))
    s.append(txt(150, 250, '外壁・屋根の線が少ない', 13, GOOD_D, '700', 'middle'))
    s.append(txt(150, 270, '→ コストを抑えやすい', 13, GOOD_D, '700', 'middle'))

    # 右: 凹凸の多い形(L字+出っ張り)
    s.append(txt(620, 66, '凹凸の多い形', 14, CRIT_D, '700', 'middle'))
    path = 'M540 90 L700 90 L700 150 L760 150 L760 230 L540 230 Z'
    s.append(f'<path d="{path}" fill="#fdf2f2" stroke="{CRIT}" stroke-width="2"/>')
    s.append(txt(650, 260, '外壁・屋根の線が多い', 13, CRIT_D, '700', 'middle'))
    s.append(txt(650, 280, '→ コストが上がりやすい', 13, CRIT_D, '700', 'middle'))
    return wrap(''.join(s), W, H,
                '建物の形とコストの関係',
                'シンプルな四角形の建物は外壁と屋根の線が少なくコストを抑えやすい。凹凸の多い形は外壁と屋根の面積が増えコストが上がりやすい。')


FIGURES = {
    'heimen-hikaku':   (fig_heimen_hikaku,   '図1：延床面積が同じでも建築面積が異なる図'),
    'hitsuyou-tochi':  (fig_hitsuyou_tochi,  '図2：平屋に必要な土地面積の目安'),
    'setsuyaku-kufuu': (fig_katachi_cost,    '図3：建物の形とコストの関係'),
}
