# -*- coding: utf-8 -*-
"""「住宅完成保証と瑕疵担保責任保険は別物」の図解。

共通部品は .claude/skills/homepage-article/scripts/svg_kit.py。
"""
from svg_kit import (FONT, NAVY, BLUE, BLUE_L, BLUE_M, GOOD, GOOD_D, CRIT, CRIT_D,
                     WARN, WARN_D, INK, INK2, MUTE, LINE, SURF, TINT,
                     wrap, txt, box, check, cross, dash, arrow, pill, chip)


# ── 図1: 保証している「期間」が違う ──────────────────────
def fig_kikan():
    W, H = 880, 340
    s = []
    s.append(txt(0, 28, '2つの保証は、守っている「期間」がそもそも違います', 17, INK, '700'))

    # 時系列の軸
    axis_y = 130
    x_start, x_mid, x_end = 40, 420, 840
    s.append(f'<line x1="{x_start}" y1="{axis_y}" x2="{x_end}" y2="{axis_y}" stroke="{LINE}" stroke-width="2"/>')
    for x, label in [(x_start, '契約'), (x_mid, '引き渡し'), (x_end, '10年後')]:
        s.append(f'<circle cx="{x}" cy="{axis_y}" r="5" fill="{INK}"/>')
        s.append(txt(x, axis_y + 28, label, 14, INK, '700', 'middle'))

    # 上段: 住宅完成保証(契約〜引き渡し)
    s.append(box(x_start, 50, x_mid - x_start, 40, CRIT, CRIT, 0, 6))
    s.append(txt((x_start + x_mid) / 2, 75, '住宅完成保証（工事中）', 14, SURF, '700', 'middle'))

    # 下段: 瑕疵担保責任保険(引き渡し〜10年)
    s.append(box(x_mid, 170, x_end - x_mid, 40, GOOD, GOOD, 0, 6))
    s.append(txt((x_mid + x_end) / 2, 195, '瑕疵担保責任保険（完成後10年）', 14, SURF, '700', 'middle'))

    s.append(box(0, 240, 420, 80, '#fdf2f2', CRIT, 1.2, 8))
    s.append(txt(16, 264, '住宅完成保証', 14, CRIT_D, '700'))
    s.append(txt(16, 286, '倒産による工事中断から守る', 13, INK))
    s.append(txt(16, 306, '（任意）', 13, INK2))

    s.append(box(460, 240, 420, 80, '#f1faf3', GOOD, 1.2, 8))
    s.append(txt(476, 264, '瑕疵担保責任保険', 14, GOOD_D, '700'))
    s.append(txt(476, 286, '完成後に見つかった欠陥から守る', 13, INK))
    s.append(txt(476, 306, '（法律で加入が義務）', 13, INK2))
    return wrap(''.join(s), W, H,
                '住宅完成保証と瑕疵担保責任保険が対象とする期間の違い',
                '住宅完成保証は契約から引き渡しまでの工事中の倒産に備える任意の制度。瑕疵担保責任保険は引き渡しから10年間の完成後の欠陥に備える法律で加入が義務の制度。')


# ── 図2: 会社登録と個別申込みは別 ──────────────────────
def fig_touroku_vs_koubetsu():
    W, H = 880, 300
    s = []
    s.append(txt(0, 28, '「会社が登録している」と「あなたの家が保証される」は別の話です', 17, INK, '700'))

    s.append(box(0, 56, 420, 200, TINT, LINE, 1.5, 10))
    s.append(txt(20, 88, 'STEP1：会社が保証機関に登録', 15, INK, '700'))
    s.append(check(24, 116)); s.append(txt(50, 128, '財務状況・建築実績の審査', 14, INK))
    s.append(check(24, 146)); s.append(txt(50, 158, '事業年数の審査', 14, INK))
    s.append(box(20, 180, 380, 56, '#e8f0fb', BLUE, 1.2, 6))
    s.append(txt(210, 205, 'ここまでは「会社」の話', 14, BLUE_M, '700', 'middle'))
    s.append(txt(210, 224, '個々の家にはまだ何もついていない', 13, INK2, '400', 'middle'))

    s.append(box(460, 56, 420, 200, '#f1faf3', GOOD, 1.5, 10))
    s.append(txt(480, 88, 'STEP2：住宅ごとに個別申込み', 15, GOOD_D, '700'))
    s.append(check(484, 116)); s.append(txt(510, 128, 'この工事について申込みをする', 14, INK))
    s.append(check(484, 146)); s.append(txt(510, 158, '保証証書・確認書の発行を受ける', 14, INK))
    s.append(box(480, 180, 380, 56, '#dff0e3', GOOD, 1.2, 6))
    s.append(txt(670, 205, 'ここで初めて「あなたの家」の話', 14, GOOD_D, '700', 'middle'))
    s.append(txt(670, 224, '証書がなければ保証の対象外の可能性', 13, INK2, '400', 'middle'))
    return wrap(''.join(s), W, H,
                '会社の制度登録と住宅ごとの個別申込みの違い',
                'STEP1は会社が保証機関に登録する段階で個々の家にはまだ保証がついていない。STEP2で住宅ごとに個別申込みをして保証証書の発行を受けて初めてその家が保証の対象になる。')


# ── 図3: 保証タイプ2種類の比較 ──────────────────────
def fig_type_hikaku():
    W, H = 880, 280
    s = []
    s.append(txt(0, 28, '住宅完成保証には、2つのしくみがあります', 17, INK, '700'))

    s.append(box(0, 56, 420, 190, '#eef3f9', BLUE, 1.5, 10))
    s.append(txt(20, 88, '保険タイプ', 17, BLUE_M, '700'))
    s.append(txt(20, 118, '保証機関が保険というしくみで', 14, INK))
    s.append(txt(20, 140, '保証する。', 14, INK))
    s.append(txt(20, 172, '一般的な保証のイメージに近い', 13, INK2))
    s.append(txt(20, 192, '仕組み。', 13, INK2))
    s.append(box(20, 210, 380, 24, '#dce8f8', BLUE, 0, 4))
    s.append(txt(210, 227, '保証限度額は契約額の80%程度が目安', 12, BLUE_M, '700', 'middle'))

    s.append(box(460, 56, 420, 190, '#fff3e0', WARN, 1.5, 10))
    s.append(txt(480, 88, 'エスクロー（第三者預託）タイプ', 15, WARN_D, '700'))
    s.append(txt(480, 118, '工事代金の一部を第三者機関が', 14, INK))
    s.append(txt(480, 140, '預かっておくしくみ。', 14, INK))
    s.append(txt(480, 172, '万一のとき、預けた資金から', 13, INK2))
    s.append(txt(480, 192, '費用を充てる。', 13, INK2))
    s.append(box(480, 210, 380, 24, '#ffe9c2', WARN, 0, 4))
    s.append(txt(670, 227, '限度額は機関ごとに条件が異なる', 12, WARN_D, '700', 'middle'))
    return wrap(''.join(s), W, H,
                '保険タイプとエスクロータイプの違い',
                '保険タイプは保証機関が保険のしくみで保証し限度額は契約額の80%程度が目安。エスクロータイプは工事代金の一部を第三者機関が預かるしくみで限度額は機関ごとに条件が異なる。')


FIGURES = {
    'kikan':               (fig_kikan,               '図1：住宅完成保証と瑕疵担保責任保険が対象とする期間の違い'),
    'touroku-vs-koubetsu': (fig_touroku_vs_koubetsu, '図2：会社の制度登録と住宅ごとの個別申込みの違い'),
    'type-hikaku':         (fig_type_hikaku,         '図3：保険タイプとエスクロー（第三者預託）タイプの違い'),
}
