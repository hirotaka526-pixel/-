# -*- coding: utf-8 -*-
"""「収納は『量』より『位置』で考える、洗濯動線の作り方」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。

内容はリール台本(「SNSで人気の回遊動線・大容量収納が後悔の理由になる盲点」
「キッチン・洗面脱衣・ファミリークローゼットを一直線につなげる家事動線の注意点」
「土間収納のルール」)を参考に、記事向けに再構成。リール内の「8割」等の煽り数値は
裏取りできないため使わず、コスト目安(2坪コンパクトで150〜200万円)は
「ケースもある」という控えめな表現にしている。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge, cross_badge)


# ── 図1: 通路ありとなしで、同じ2畳でも収納力が変わる ──────────────────────
def fig_shuunou_tsuuro():
    W, H = 880, 300
    s = []
    s.append(heading(0, 34, '同じ2畳でも、通路の有無で収納力は大きく変わります', 18))

    s.append(card(30, 64, 380, 180, SURF, accent=WARN))
    s.append(txt(220, 96, 'ウォークスルー型(通り抜け)', 15, INK, '700', 'middle'))
    s.append(box(70, 118, 300, 90, TINT, LINE, 1, 6))
    s.append(box(70, 118, 300, 24, WARN, WARN, 0, 0))
    s.append(txt(220, 134, '通路スペース', 13, SURF, '700', 'middle'))
    s.append(txt(220, 178, '棚にできるのは一部だけ', 14, INK2, '400', 'middle'))
    s.append(txt(220, 228, '→ 実質の収納力は2畳以下', 14, WARN_D, '700', 'middle'))

    s.append(card(470, 64, 380, 180, SURF, accent=NAVY))
    s.append(txt(660, 96, 'ウォークイン型(行き止まり)', 15, INK, '700', 'middle'))
    s.append(box(510, 118, 300, 90, TINT, LINE, 1, 6))
    s.append(box(510, 118, 40, 90, NAVY, NAVY, 0, 0))
    s.append(txt(660, 178, '壁一面をすべて棚にできる', 14, INK2, '400', 'middle'))
    s.append(txt(660, 228, '→ 同じ面積でも収納力は2倍近くに', 14, NAVY, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '通路の有無による収納力の違いを示す図',
                '通り抜けできるウォークスルー型の収納は、人が歩く通路スペースが必要になるため棚にできるのは一部だけで、実質の収納力は面積より小さくなる。行き止まりのウォークイン型は壁一面をすべて棚にできるため、同じ面積でも収納力は大きく変わる。')


# ── 図2: 収納は「量」ではなく「位置」と「立体」で考える ──────────────────────
def fig_shuunou_ichi_rittai():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '収納は「量」ではなく「位置」と「立体」で考えます', 18))

    s.append(card(30, 64, 380, 160, SURF, accent=WARN))
    s.append(txt(220, 98, '「量」で考える', 16, INK, '700', 'middle'))
    s.append(cross_badge(220, 136, 12, WARN))
    s.append(txt(220, 170, '広い部屋をとりあえず確保', 14, INK2, '400', 'middle'))
    s.append(txt(220, 192, '→ 使う場所と合わず物置化', 14, WARN_D, '700', 'middle'))

    s.append(card(470, 64, 380, 160, SURF, accent=NAVY))
    s.append(txt(660, 98, '「位置」と「立体」で考える', 15, INK, '700', 'middle'))
    s.append(check_badge(660, 136, 12, NAVY))
    s.append(txt(660, 170, '使う場所に、床から天井まで', 14, INK2, '400', 'middle'))
    s.append(txt(660, 192, '→ 壁面収納だけですっきり片付く', 14, NAVY, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '収納は量ではなく位置と立体で考えることを示す図',
                '広い部屋をとりあえず確保する「量」で考える収納は、使う場所と合わずに物置化しやすい。使う場所に床から天井まで立体的に仕切って片付ける「位置」と「立体」で考える収納は、壁面収納だけですっきり片付けられる。')


# ── 図3: 洗濯動線は、無理に一直線にしなくていい ──────────────────────
def fig_sentaku_dousen():
    W, H = 880, 320
    s = []
    s.append(heading(0, 34, '一直線の家事動線は、3つの注意点を確認してから', 18))

    items = [
        ('① キッチン⇔洗面の入口', '同時に使う頻度は意外と少ない。入口が増えるとコストアップ'),
        ('② 洗面⇔ファミクロの接続', '湯気・湿度対策が必要。あまり着ない服の収納には不向き'),
        ('③ 室内物干しを足す', 'どこに置くかで動線がどんどん伸びていく'),
    ]
    y0 = 70
    row_h = 66
    for i, (title, note) in enumerate(items):
        y = y0 + i * row_h
        s.append(card(20, y, 840, row_h - 10, SURF, accent=WARN, shadow=False))
        s.append(badge(56, y + (row_h - 10) / 2, 15, str(i + 1), WARN, SURF, 15))
        s.append(txt(90, y + 24, title, 15, INK, '700'))
        s.append(txt(90, y + 44, note, 14, INK2, '400'))

    s.append(txt(0, H - 18, '※ 無理に一直線にせず、暮らし方に合わせて組み合わせを選ぶ方が間取りの自由度は上がる', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                '一直線の家事動線を採用する前に確認したい3つの注意点',
                'キッチンと洗面を直接つなぐ入口は同時に使う頻度が意外と少なく入口が増えるとコストアップにつながる。洗面とファミリークローゼットを接続すると湯気や湿度対策が必要になる。室内物干しを足すとどこに置くかで動線がどんどん伸びていく。無理に一直線にせず暮らし方に合わせて組み合わせを選ぶ方が間取りの自由度は上がる。')


FIGURES = {
    'shuunou-tsuuro':       (fig_shuunou_tsuuro,       '図1：通路の有無による収納力の違い'),
    'shuunou-ichi-rittai':  (fig_shuunou_ichi_rittai,  '図2：収納は量ではなく位置と立体で考える'),
    'sentaku-dousen':        (fig_sentaku_dousen,        '図3：一直線の家事動線を採用する前の3つの注意点'),
}
