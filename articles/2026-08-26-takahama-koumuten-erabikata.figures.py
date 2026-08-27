# -*- coding: utf-8 -*-
"""「高浜市で失敗しない工務店の選び方」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py にある。
新しい記事の図解も、必ずこの形（FIGURES辞書）で書くこと。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross, dash, arrow, pill, chip)

# ── 図1: 壁量計算 vs 許容応力度計算 ──────────────────────
def fig_kouzou():
    W, H = 880, 452
    s = []
    items = ['壁の量', '柱・梁の強さ', '接合部（金物）', '基礎の設計', '建物全体のバランス']
    # 左カード
    s.append(box(0, 56, 420, 340, TINT, LINE))
    s.append(box(0, 56, 420, 46, '#e8eef7', LINE))
    s.append(txt(20, 86, '壁量計算', 20, NAVY, '700'))
    s.append(txt(180, 86, '簡易な計算', 14, INK2))
    # 右カード
    s.append(box(460, 56, 420, 340, '#eef7f0', LINE))
    s.append(box(460, 56, 420, 46, '#dff0e3', LINE))
    s.append(txt(480, 86, '許容応力度計算', 20, GOOD_D, '700'))
    s.append(txt(680, 86, '緻密な構造計算', 14, INK2))

    s.append(txt(0, 32, '同じ「耐震等級3」でも、どこまで計算しているかが違います', 17, INK, '700'))

    for i, name in enumerate(items):
        y = 140 + i * 46
        # 左: 壁の量だけ1棟ごとに計算、他は仕様の基準で判断
        if i == 0:
            s.append(check(22, y - 5)); s.append(txt(48, y, name, 15, INK, '600'))
        else:
            s.append(f'<line x1="20" y1="{y-5}" x2="34" y2="{y-5}" stroke="#a8a8a3" stroke-width="2.6" stroke-linecap="round"/>')
            s.append(txt(48, y, name, 15, MUTE))
            s.append(txt(400, y, '仕様の基準で判断', 13, MUTE, '400', 'end'))
        # 右: 全部1棟ごとに計算
        s.append(check(482, y - 5)); s.append(txt(508, y, name, 15, INK, '600'))

    s.append(txt(20, 376, '→ 1棟ごとに計算するのは壁の量だけ', 14, '#8a6100', '700'))
    s.append(txt(480, 376, '→ 5項目すべてを1棟ごとに計算する', 14, GOOD_D, '700'))
    s.append(txt(0, 420, '※ 壁量計算でも金物や基礎には仕様の基準がありますが、その建物に合わせた個別の計算はしません', 13, INK2))
    s.append(txt(0, 440, '※「耐震等級3“相当”」は第三者機関の評価を受けていないという意味です', 13, INK2))
    return wrap(''.join(s), W, H,
                '壁量計算と許容応力度計算で1棟ごとに計算する範囲の違い',
                '壁量計算で1棟ごとに計算するのは壁の量のみで、柱と梁の強さ、接合部の金物、基礎の設計、建物全体のバランスは仕様の基準で判断する。許容応力度計算はこの5項目すべてを1棟ごとに計算する。')


# ── 図2: 断熱等級のいま ──────────────────────
def fig_dannetsu():
    W, H = 880, 400
    s = []
    s.append(txt(0, 28, '断熱等級のいま　― 等級4は「最低ライン」です', 17, INK, '700'))
    bars = [
        ('等級4', 210, BLUE_L, '2025年4月から、これ未満の家は建てられません', INK),
        ('等級5', 330, BLUE,   '断熱を売りにするなら、最低でもここから', SURF),
        ('等級6', 450, NAVY,   '西三河の夏の暑さに効いてくるのはこの辺り', SURF),
        # ラベル: 断熱の高低ではなく「位置づけ」を書く
    ]
    y0 = 70
    for i, (label, w, color, note, tcol) in enumerate(bars):
        y = y0 + i * 82
        s.append(f'<rect x="120" y="{y}" width="{w}" height="52" rx="6" fill="{color}"/>')
        s.append(txt(0, y + 33, label, 19, INK, '700'))
        s.append(txt(136, y + 33, ['最低ライン','ZEH水準','推奨ライン'][i], 15, tcol, '700'))
        s.append(txt(120 + w + 16, y + 33, note, 14, INK2))
    # 2030年の注記
    s.append(f'<line x1="120" y1="{y0+82*3+4}" x2="860" y2="{y0+82*3+4}" stroke="{LINE}" stroke-width="1.5"/>')
    s.append(box(120, y0 + 82 * 3 + 22, 740, 52, '#fff8e6', WARN, 1.5))
    s.append(txt(140, y0 + 82 * 3 + 46, '⚠', 18, '#8a6100', '700'))
    s.append(txt(166, y0 + 82 * 3 + 46, '2030年には等級5が最低ラインになると言われています。', 15, '#6b4d00', '700'))
    s.append(txt(166, y0 + 82 * 3 + 66, '今ギリギリで建てた家は、10年後にはっきり見劣りします。', 14, '#6b4d00'))
    return wrap(''.join(s), W, H,
                '断熱等級4・5・6の位置づけ',
                '等級4は2025年4月から義務化された最低ライン。等級5はZEH水準。等級6はさらに上。2030年には等級5が最低ラインになる見込み。')


# ── 図3: 見積書「一式」vs 内訳明細 ──────────────────────
def fig_mitsumori():
    W, H = 880, 420
    s = []
    s.append(txt(0, 28, '同じ「電気工事 80万円」でも、書き方でこれだけ違います', 17, INK, '700'))
    # 左: 一式
    s.append(box(0, 50, 420, 330, '#fdf2f2', CRIT, 1.5))
    s.append(txt(20, 82, '✕　「一式」の見積書', 17, CRIT, '700'))
    s.append(f'<line x1="20" y1="96" x2="400" y2="96" stroke="{LINE}"/>')
    s.append(txt(20, 128, '電気工事', 16, INK, '600'))
    s.append(txt(240, 128, '一式', 16, INK))
    s.append(txt(390, 128, '800,000', 16, INK, '600', 'end'))
    s.append(txt(20, 190, 'コンセントは何個まで？', 15, CRIT))
    s.append(txt(20, 220, '照明は何台まで？', 15, CRIT))
    s.append(txt(20, 250, 'この工事はどこまで含む？', 15, CRIT))
    s.append(box(20, 280, 380, 76, '#fbe3e3', CRIT, 1.5))
    s.append(txt(38, 308, '誰にも分からない', 16, CRIT, '700'))
    s.append(txt(38, 334, '着工後、1か所追加するたびに費用が増える', 14, CRIT_D))
    # 右: 内訳明細
    s.append(box(460, 50, 420, 330, '#f1faf3', GOOD, 1.5))
    s.append(txt(480, 82, '◯　数量と単価が入った内訳明細', 17, GOOD_D, '700'))
    s.append(f'<line x1="480" y1="96" x2="860" y2="96" stroke="{LINE}"/>')
    rows = [('コンセント', '24 か所', '96,000'), ('スイッチ', '18 か所', '72,000'),
            ('照明器具取付', '16 台', '80,000'), ('分電盤', '1 面', '85,000'),
            ('幹線・配線工事', '1 式', '467,000')]
    for i, (a, b, c) in enumerate(rows):
        y = 128 + i * 30
        s.append(txt(480, y, a, 14, INK))
        s.append(txt(690, y, b, 14, INK2, '400', 'end'))
        s.append(txt(860, y, c, 14, INK, '600', 'end'))
    s.append(box(480, 290, 380, 66, '#dff0e3', GOOD, 1.5))
    s.append(txt(498, 316, '他社と1行ずつ比べられる', 16, GOOD_D, '700'))
    s.append(txt(498, 340, '要らない設備を削って減額の相談もできる', 14, '#14683a'))
    s.append(txt(0, 410, '※ 出してもらう費用は0円。頼むだけです。数量・単価は記載例です', 13, INK2))
    return wrap(''.join(s), W, H,
                '一式表記の見積書と内訳明細の違い',
                '一式表記では数量も単価も分からず着工後に費用が積み上がる。内訳明細なら他社と1行ずつ比較でき減額交渉もできる。')


# ── 図4: 2つの保証の違い ──────────────────────
def fig_hosho():
    W, H = 880, 330
    s = []
    s.append(txt(0, 28, '「保証があります」の中身は2種類。差がつくのは右です', 17, INK, '700'))
    s.append(box(0, 50, 420, 250, '#f5f5f4', LINE, 1.5))
    s.append(box(0, 50, 420, 44, '#e6e6e3', LINE, 1.5))
    s.append(txt(20, 78, '住宅瑕疵担保責任保険', 17, INK, '700'))
    s.append(box(20, 108, 76, 26, '#e0e0dc', '#b5b5b0', 1.2, 13))
    s.append(txt(58, 126, '法律で義務', 13, INK2, '700', 'middle'))
    s.append(txt(20, 166, '構造と雨漏りを10年間保証', 15, INK))
    s.append(txt(20, 194, '倒産していても保険法人が支払う', 15, INK))
    s.append(box(20, 220, 380, 60, '#e6e6e3', '#b5b5b0', 1.5))
    s.append(txt(38, 248, 'どの会社も入っている', 15, INK, '700'))
    s.append(txt(38, 270, '＝ 会社選びの判断材料にならない', 14, INK2))

    s.append(box(460, 50, 420, 250, '#f1faf3', GOOD, 2))
    s.append(box(460, 50, 420, 44, '#dff0e3', GOOD, 2))
    s.append(txt(480, 78, '住宅完成保証', 17, GOOD_D, '700'))
    s.append(box(480, 108, 60, 26, '#c9e7d1', GOOD, 1.2, 13))
    s.append(txt(510, 126, '任意', 13, GOOD_D, '700', 'middle'))
    s.append(txt(480, 166, '完成前に倒産したときに備える保証', 15, INK))
    s.append(txt(480, 194, '前払金と、引き継ぐ会社への追加費用', 15, INK))
    s.append(box(480, 220, 380, 60, '#dff0e3', GOOD, 1.5))
    s.append(txt(498, 248, '入っていない会社のほうが多い', 15, GOOD_D, '700'))
    s.append(txt(498, 270, '＝ 入っていれば強い判断材料になる', 14, '#14683a'))
    return wrap(''.join(s), W, H,
                '住宅瑕疵担保責任保険と住宅完成保証の違い',
                '瑕疵担保責任保険は法律で義務のため全社が加入しており差がつかない。完成保証は任意のため加入していれば判断材料になる。')


# ── 図5: 設計と施工の体制 ──────────────────────
def fig_taisei():
    W, H = 880, 400
    s = []
    s.append(txt(0, 28, '図面どおりに建つかは、「何人を経由するか」で決まります', 17, INK, '700'))

    def person(x, y, label, color, tcol=SURF, w=150):
        return (box(x, y, w, 56, color, color, 1.5) +
                txt(x + w / 2, y + 34, label, 15, tcol, '700', 'middle'))

    def arrow(x, y, bad=False):
        c = CRIT if bad else GOOD
        return (f'<path d="M{x} {y} l26 0" stroke="{c}" stroke-width="2.4" stroke-linecap="round"/>'
                f'<path d="M{x+20} {y-5} l6 5 l-6 5" fill="none" stroke="{c}" stroke-width="2.4" '
                f'stroke-linecap="round" stroke-linejoin="round"/>')

    # 上段: 分業
    s.append(box(0, 50, 880, 150, '#fdf2f2', CRIT, 1.5))
    s.append(txt(20, 80, '✕　営業・設計・現場が別々の会社', 16, CRIT, '700'))
    xs = [20, 216, 412]
    labels = ['営業', '設計担当', '現場監督']
    for x, lb in zip(xs, labels):
        s.append(person(x, 100, lb, '#b5b5b0'))
        if x != xs[-1]:
            s.append(arrow(x + 158, 128, bad=True))
    s.append(arrow(578, 128, bad=True))
    s.append(person(608, 100, '家', MUTE, SURF, 110))
    s.append(txt(742, 122, '要望が3回', 14, CRIT, '700'))
    s.append(txt(742, 142, '伝言される', 14, CRIT, '700'))
    s.append(txt(20, 186, '設計者の意図が現場に届かず、現場が納まりやすいやり方で処理されてしまう', 14, CRIT_D))

    # 下段: 一貫
    s.append(box(0, 222, 880, 150, '#f1faf3', GOOD, 2))
    s.append(txt(20, 252, '◯　設計した建築士が、そのまま現場も管理する', 16, GOOD_D, '700'))
    s.append(person(20, 272, '建築士', GOOD, SURF, 346))
    s.append(arrow(384, 300))
    s.append(person(414, 272, '家', '#14683a', SURF, 110))
    s.append(txt(548, 294, '伝言ゲームが', 14, GOOD_D, '700'))
    s.append(txt(548, 314, 'そもそも起きない', 14, GOOD_D, '700'))
    s.append(txt(20, 358, '「設計した人と、現場を管理する人は同じですか？」— 聞けば分かります', 14, '#14683a'))
    return wrap(''.join(s), W, H,
                '分業体制と設計施工一貫体制の違い',
                '営業・設計・現場監督が別々だと要望が3回伝言され設計意図が現場に届かない。設計した建築士がそのまま現場を管理すれば伝言ゲームが起きない。')


FIGURES = {
    'kouzou':   (fig_kouzou,   '図1：壁量計算と許容応力度計算で「1棟ごとに計算する範囲」の違い'),
    'dannetsu': (fig_dannetsu, '図2：断熱等級4・5・6の位置づけ（2025年4月時点）'),
    'mitsumori':(fig_mitsumori,'図3：「一式」の見積書と、数量・単価が入った内訳明細の違い'),
    'hosho':    (fig_hosho,    '図4：住宅瑕疵担保責任保険（義務）と住宅完成保証（任意）の違い'),
    'taisei':   (fig_taisei,   '図5：分業体制と、設計施工一貫体制の違い'),
}
