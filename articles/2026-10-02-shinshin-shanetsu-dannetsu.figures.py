# -*- coding: utf-8 -*-
"""「制震装置・遮熱シート・断熱材『つければ安心』の落とし穴」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
配色はネイビー基調+ゴールドアクセント+複数色(2026年9月改訂)。建物線画アイコンのみ使用可。
文字は見出し18-20px/本文ラベル15px以上/注記14px以上を厳守。

内容はYouTube台本(まえちゃん×川下さんの対談、2026年収録)を参考に、専門的に裏付けできる
部分のみ記事化。具体的な金額(構造用合板の増額分など)は台本が自動書き起こしで数字が
不確かだったため、本文では定性的な説明にとどめている。
"""
from svg_kit import (NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     FOREST, FOREST_L, TEAL, TEAL_L, NAVY_L, GOLD,
                     wrap, txt, box, heading, card, badge, check_badge, cross_badge)


# ── 図1: 制震装置は「耐震等級3」が前提 ──────────────────────
def fig_shinshin_zentei():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '制震装置は、しっかりした構造があって初めて効果を発揮します', 18))

    s.append(card(30, 64, 380, 160, SURF, accent=WARN))
    s.append(txt(220, 98, '耐震等級1(最低基準)+制震装置', 15, INK, '700', 'middle'))
    s.append(cross_badge(220, 136, 12, WARN))
    s.append(txt(220, 170, '構造自体が揺れやすいため', 14, INK2, '400', 'middle'))
    s.append(txt(220, 192, '制震装置の効果が発揮されにくい', 14, INK2, '400', 'middle'))

    s.append(card(470, 64, 380, 160, SURF, accent=NAVY))
    s.append(txt(660, 98, '耐震等級3+制震装置', 15, INK, '700', 'middle'))
    s.append(check_badge(660, 136, 12, NAVY))
    s.append(txt(660, 170, 'しっかりした構造体の上で', 14, INK2, '400', 'middle'))
    s.append(txt(660, 192, '制震装置が効果を発揮する', 14, INK2, '400', 'middle'))

    s.append(txt(0, H - 18, '※ 耐震等級1でも合法であり「無いよりは強くなる」のは事実。ただし効果の大きさが違う', 14, INK2, '400'))
    return wrap(''.join(s), W, H,
                '制震装置の効果と構造の前提条件を示す図',
                '耐震等級1(建築基準法の最低基準)に制震装置をつけても、構造自体が揺れやすいため効果が発揮されにくい。耐震等級3のしっかりした構造体の上に制震装置をつけることで、初めて効果が発揮される。耐震等級1でも合法であり無いよりは強くなるが、効果の大きさが違う。')


# ── 図2: 遮熱シートは「手段の1つ」 ──────────────────────
def fig_shanetsu_tehazu():
    W, H = 880, 280
    s = []
    s.append(heading(0, 34, '遮熱シートは、快適さをつくる手段の一つにすぎません', 18))

    items = ['断熱', '気密', '換気', '窓の配置・方角', '遮熱シート']
    card_w = 150
    gap = 12
    for i, item in enumerate(items):
        x = 20 + i * (card_w + gap)
        color = GOLD if item == '遮熱シート' else NAVY
        s.append(card(x, 70, card_w, 110, SURF, accent=color))
        s.append(txt(x + card_w / 2, 130, item, 14, INK, '700', 'middle'))

    s.append(card(20, 210, 840, 50, TINT, shadow=False))
    s.append(txt(440, 241, '→ すべてがそろって初めて「夏も快適な家」になる', 15, NAVY, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '遮熱シートは快適さをつくる手段の一つであることを示す図',
                '快適な家をつくる要素は断熱・気密・換気・窓の配置と方角・遮熱シートなど複数ある。遮熱シートだけを採用しても、たとえば西側に大きな窓があれば夏の西日の影響を受けやすく、すべての要素がそろって初めて夏も快適な家になる。')


# ── 図3: 断熱材は「種類」より「密度と施工」 ──────────────────────
def fig_dannetsuzai_shikou():
    W, H = 880, 260
    s = []
    s.append(heading(0, 34, '断熱材は、種類そのものより密度と施工の精度が重要です', 18))

    s.append(card(30, 64, 380, 150, SURF, accent=WARN))
    s.append(txt(220, 100, '「この断熱材が一番」', 16, INK, '700', 'middle'))
    s.append(txt(220, 132, 'という断定', 14, INK2, '400', 'middle'))
    s.append(txt(220, 166, '→ 素材の種類だけでは', 14, WARN_D, '700', 'middle'))
    s.append(txt(220, 188, '性能を語れない', 14, WARN_D, '700', 'middle'))

    s.append(card(470, 64, 380, 150, SURF, accent=NAVY))
    s.append(txt(660, 100, '密度(例:16K/24K)と', 16, INK, '700', 'middle'))
    s.append(txt(660, 122, '施工精度の確認', 16, INK, '700', 'middle'))
    s.append(txt(660, 166, '→ 同じ種類でも、密度と', 14, NAVY, '700', 'middle'))
    s.append(txt(660, 188, '施工次第で性能が変わる', 14, NAVY, '700', 'middle'))

    return wrap(''.join(s), W, H,
                '断熱材は種類より密度と施工精度が重要であることを示す図',
                '「この断熱材が一番」という断定は、素材の種類だけでは性能を語れない。同じグラスウールでも密度(16Kと24Kなど)によって性能が変わり、さらに施工の精度(隙間なく充填できているか)によって実際の性能が大きく左右される。')


FIGURES = {
    'shinshin-zentei':    (fig_shinshin_zentei,    '図1：制震装置の効果と構造の前提条件'),
    'shanetsu-tehazu':     (fig_shanetsu_tehazu,     '図2：遮熱シートは快適さをつくる手段の一つ'),
    'dannetsuzai-shikou':  (fig_dannetsuzai_shikou,  '図3：断熱材は種類より密度と施工精度が重要'),
}
