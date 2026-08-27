# -*- coding: utf-8 -*-
"""記事Markdown → 装飾つきGutenberg HTML。色はすべてインラインstyleなのでテーマに依存しない。"""
import re, html, sys
import figures as F

# ── ブランドカラー(ここだけ変えれば全体が変わる) ──────────
BRAND      = '#0d366b'   # 大見出しの背景・強調文字
BRAND_TINT = '#eef3f9'   # 中見出しカードの背景
BRAND_MID  = '#2a78d6'
CRIT       = '#d03b3b'   # 危ないサイン
CRIT_TINT  = '#fdf2f2'
WARN       = '#fab219'   # 注記
WARN_TINT  = '#fff8e6'
GOOD       = '#0ca30c'
GOOD_TINT  = '#f1faf3'
INK        = '#1a1a19'
INK2       = '#52514e'
LINE       = '#d8d8d4'
MARKER     = 'linear-gradient(transparent 62%, #ffe89a 62%)'

BODY  = f'font-size:17px;line-height:1.95;color:{INK};'
FONTS = ''

# マーカーで引く重要文(太字のうちこれらはマーカー表示)
HIGHLIGHT = {
    'これが一番危ないバイアスです。', 'これが一番危ない勘違いです。',
    '安い見積書ほど、別途が多い。',
    'これでは会社の差はつきません。',
    '現在、国の基準がありません。',
    'ケンカをする必要はまったくありません。',
    'どこかで必ず伝言ゲームが起きます。',
    '設計した建築士が、そのまま現場も見る。',
    '住宅瑕疵担保責任保険は、法律で加入が義務づけられています。',
}

def esc(s): return html.escape(s, quote=False)

def inline(t, strong_color=BRAND):
    t = esc(t)
    def _strong(m):
        s = m.group(1)
        if s in HIGHLIGHT:
            return (f'<strong style="font-weight:700;background:{MARKER};'
                    f'padding:0 2px;color:{INK}">{s}</strong>')
        return f'<strong style="font-weight:700;color:{strong_color}">{s}</strong>'
    t = re.sub(r'\*\*(.+?)\*\*', _strong, t)
    t = re.sub(r'\[(.+?)\]\((.+?)\)',
               rf'<a href="\2" style="color:{BRAND_MID};text-decoration:underline;'
               r'text-underline-offset:3px">\1</a>', t)
    return t

def blk(name, attrs, inner):
    a = (' ' + attrs) if attrs else ''
    return f'<!-- wp:{name}{a} -->\n{inner}\n<!-- /wp:{name} -->'

def para(t, style='', color=BRAND):
    st = f'{BODY}margin:0 0 1.5em;{style}'
    return blk('paragraph', '', f'<p style="{st}">{inline(t, color)}</p>')

def h2(t):
    st = (f'background:{BRAND};color:#fff;font-size:23px;font-weight:700;line-height:1.5;'
          f'margin:3em 0 1.2em;padding:.7em .9em;border-radius:6px;')
    return blk('heading', '{"level":2}', f'<h2 class="wp-block-heading" style="{st}">{esc(t)}</h2>')

def h3_question(num, t):
    st = (f'background:{BRAND_TINT};border-left:6px solid {BRAND};border-radius:0 6px 6px 0;'
          f'color:{BRAND};font-size:20px;font-weight:700;line-height:1.6;'
          f'margin:2.4em 0 1.1em;padding:.85em 1em;')
    badge = (f'<span style="display:inline-block;background:{BRAND};color:#fff;font-size:13px;'
             f'font-weight:700;border-radius:4px;padding:2px 9px;margin-right:10px;'
             f'vertical-align:2px">質問{num}</span>')
    return blk('heading', '{"level":3}',
               f'<h3 class="wp-block-heading" style="{st}">{badge}{esc(t)}</h3>')

def h3_plain(t):
    st = (f'color:{BRAND};font-size:20px;font-weight:700;line-height:1.6;'
          f'margin:2.4em 0 1.1em;padding-bottom:.4em;border-bottom:2px solid {BRAND_TINT};')
    return blk('heading', '{"level":3}', f'<h3 class="wp-block-heading" style="{st}">{esc(t)}</h3>')

def callout(t, label, accent, tint, icon):
    inner = (f'<div class="wp-block-group" style="background:{tint};border:1px solid {accent};'
             f'border-radius:8px;padding:1.1em 1.2em;margin:0 0 1.8em">'
             f'<p style="margin:0 0 .5em;font-size:14px;font-weight:700;color:{accent};'
             f'letter-spacing:.04em">{icon} {label}</p>'
             f'<p style="{BODY}margin:0">{inline(t, accent)}</p></div>')
    return blk('group', '{"layout":{"type":"constrained"}}', inner)

def figure(key):
    fn, cap = F.FIGURES[key]
    inner = (f'<figure style="margin:2.2em 0;border:1px solid {LINE};border-radius:8px;'
             f'padding:1.2em;background:#fff">'
             f'<div style="overflow-x:auto;-webkit-overflow-scrolling:touch">{fn()}</div>'
             f'<figcaption style="font-size:14px;color:{INK2};margin-top:.9em;'
             f'line-height:1.6">{esc(cap)}'
             f'<span style="display:block;font-size:13px;color:#8a8a86;margin-top:.3em">'
             f'※スマートフォンでは図を横にスクロールできます</span>'
             f'</figcaption></figure>')
    return blk('html', '', inner)

def photo_todo(n, desc, alt, fn):
    st = (f'background:#fffbe8;border:2px dashed {WARN};border-radius:6px;'
          f'padding:.9em 1em;font-size:14px;color:#6b4d00;margin:0 0 1.8em')
    return blk('paragraph', '{"className":"todo-image"}',
               f'<p class="todo-image" style="{st}">【写真{n} を挿入】{esc(desc)}<br>'
               f'alt：{esc(alt)}　／　ファイル名：{fn}<br>'
               f'<strong>← 写真を入れたら、この段落を削除してください</strong></p>')

def ul(items, muted=False):
    col = INK2 if muted else INK
    lis = ''.join(
        f'<!-- wp:list-item -->\n<li style="{BODY}color:{col};margin:0 0 .7em">'
        f'{inline(x, BRAND)}</li>\n<!-- /wp:list-item -->' for x in items)
    return blk('list', '', f'<ul class="wp-block-list" style="padding-left:1.3em;margin:0 0 1.8em">\n{lis}\n</ul>')

def numbered_cards(items):
    out = []
    for i, x in enumerate(items, 1):
        num = (f'<span style="flex:0 0 34px;height:34px;background:{BRAND};color:#fff;'
               f'border-radius:50%;display:flex;align-items:center;justify-content:center;'
               f'font-weight:700;font-size:16px">{i}</span>')
        out.append(f'<div style="display:flex;gap:14px;align-items:flex-start;'
                   f'background:{BRAND_TINT};border-radius:8px;padding:1em 1.1em;margin:0 0 .9em">'
                   f'{num}<p style="{BODY}margin:0">{inline(x, BRAND)}</p></div>')
    return blk('html', '', f'<div style="margin:0 0 2em">{"".join(out)}</div>')

def sns_mid():
    inner = (f'<div class="wp-block-group" style="background:#fff5f5;border:1px solid #f0b8b8;'
             f'border-left:6px solid #ff0000;border-radius:0 8px 8px 0;padding:1.1em 1.2em;margin:0 0 1.8em">'
             f'<p style="margin:0 0 .4em;font-size:14px;font-weight:700;color:#c00">▶ YouTubeでも解説しています</p>'
             f'<p style="{BODY}margin:0">土地と地盤の話は、実際の現場を見せながら動画で解説しています。<br>'
             f'<span style="background:#ffe89a;padding:2px 6px;border-radius:3px;font-size:15px">'
             f'［ここに該当動画のURLを貼ってください］</span></p></div>')
    return blk('group', '{"layout":{"type":"constrained"}}', inner)

def author_box():
    inner = (
        f'<div class="wp-block-group" style="border:2px solid {BRAND};border-radius:10px;'
        f'padding:1.6em 1.5em;margin:3em 0 2em;background:{BRAND_TINT}">'
        f'<p style="margin:0 0 1em;font-size:14px;font-weight:700;color:#fff;background:{BRAND};'
        f'display:inline-block;padding:5px 14px;border-radius:4px">この記事を書いた人</p>'
        f'<p style="margin:0 0 .3em;font-size:20px;font-weight:700;color:{BRAND}">'
        f'前田 浩貴（まえだ ひろき）</p>'
        f'<p style="margin:0 0 1em;font-size:15px;color:{INK2}">'
        f'有限会社 IN THE HOME 代表／1級建築士・1級建築施工管理技士・2級土木施工管理技士</p>'
        f'<p style="{BODY}margin:0 0 1em">愛知県高浜市で注文住宅の設計・施工を手がける。'
        f'営業任せにせず、建築士である自身がヒアリングから設計、現場管理までを一貫して担当。'
        f'設計した人間がそのまま現場を見るため、図面通りに建てられることを何より大切にしている。'
        f'規格住宅ではなく、一邸ごとに暮らしに合わせて一から設計するスタイル。</p>'
        f'<p style="font-size:14px;color:{INK2};margin:0;line-height:1.8">'
        f'<strong style="color:{BRAND}">施工エリア</strong>：高浜市・碧南市・刈谷市・安城市・西尾市・'
        f'知立市・岡崎市・豊明市・半田市・大府市・東浦町ほか西三河／知多エリア</p></div>')
    return blk('group', '{"layout":{"type":"constrained"}}', inner)

def sns_end():
    def btn(label, sub, url, bg):
        return (f'<a href="{url}" target="_blank" rel="noopener" '
                f'style="flex:1 1 240px;background:{bg};color:#fff;text-decoration:none;'
                f'border-radius:8px;padding:1em 1.2em;display:block">'
                f'<span style="display:block;font-size:13px;opacity:.85">{sub}</span>'
                f'<span style="display:block;font-size:16px;font-weight:700;margin-top:2px">'
                f'{label}</span></a>')
    inner = (f'<div style="margin:0 0 2.5em">'
             f'<p style="{BODY}margin:0 0 1em">家づくりの本音や現場の様子は、'
             f'YouTube・Instagramでも発信しています。</p>'
             f'<div style="display:flex;flex-wrap:wrap;gap:12px">'
             + btn('1級建築士 まえちゃんの家づくり教室', 'YouTube',
                   'https://www.youtube.com/@inthehome', '#c4302b')
             + btn('@in.the.home', 'Instagram',
                   'https://www.instagram.com/in.the.home/', '#b4318f')
             + '</div></div>')
    return blk('html', '', inner)

def related():
    items = [('家づくりで失敗しないための間取りの考え方', '/column/madorinokanngaekata/'),
             ('インザホームの家づくりの想い', '/about/')]
    lis = ''.join(
        f'<li style="margin:0 0 .6em"><a href="{u}" style="color:{BRAND_MID};font-size:16px;'
        f'text-decoration:underline;text-underline-offset:3px">{esc(t)}</a></li>' for t, u in items)
    inner = (f'<div style="border-top:2px solid {LINE};padding-top:1.4em;margin:0 0 2em">'
             f'<p style="font-size:16px;font-weight:700;color:{BRAND};margin:0 0 .8em">関連記事</p>'
             f'<ul style="padding-left:1.2em;margin:0">{lis}</ul></div>')
    return blk('html', '', inner)

def toc_todo():
    st = (f'background:#fffbe8;border:2px dashed {WARN};border-radius:6px;'
          f'padding:.9em 1em;font-size:14px;color:#6b4d00;margin:0 0 2em')
    return blk('paragraph', '{"className":"todo-toc"}',
               f'<p class="todo-toc" style="{st}">【ここに目次ブロックを挿入】'
               f'<strong>← 挿入したら、この段落を削除してください</strong></p>')


# ── 本文の組み立て ──────────────────────────────────
def convert(md):
    if md.startswith('---'):
        md = md.split('---', 2)[2]
    lines = [l.rstrip() for l in md.split('\n')]
    out, i = [], 0
    # 図・写真を差し込む位置(その見出しの直前)
    FIG_BEFORE = {
        '質問2：地盤調査はいつやりますか？　地盤改良費は見積に入っていますか？': figure('kouzou'),
        '質問5：気密測定は全棟やっていますか？　C値の実測平均はいくつですか？':   figure('dannetsu'),
        '質問7：別途工事の概算も、全部出してもらえますか？':                      figure('mitsumori'),
        '【人と体制】図面通りに建つかは、現場に来る回数で決まる':                  figure('hosho'),
        '逆に、そこまで気にしなくていいこと':                                      figure('taisei'),
    }
    PHOTO_BEFORE = {
        '【断熱・気密】カタログの数字ではなく、実測を聞く':
            photo_todo(2, '地盤調査または基礎配筋の現場写真',
                       '碧南市の新築現場で地盤調査を行っている様子', 'jiban-chosa-genba.jpg'),
        '【お金・見積】契約前にしか聞けないことを、契約前に聞く':
            photo_todo(3, '気密測定の現場写真（要撮影）',
                       '気密測定器でC値を実測している新築現場', 'kimitsu-sokutei.jpg'),
    }
    in_lead = True

    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1; continue
        if ln.startswith('# '):          # H1は本文に入れない
            i += 1; continue
        if ln.startswith('<!-- 中盤SNS'):
            i += 1; continue

        if ln.startswith('<!-- ここに目次'):
            out.append(toc_todo())
            out.append(photo_todo(1, '打ち合わせで施主と図面を見ている写真',
                                  '高浜市の事務所で施主と間取り図を確認する1級建築士',
                                  'takahama-uchiawase.jpg'))
            in_lead = False
            i += 1; continue

        if ln.startswith('### '):
            t = ln[4:]
            if t in FIG_BEFORE: out.append(FIG_BEFORE.pop(t))
            m = re.match(r'^質問(\d+)：(.+)$', t)
            out.append(h3_question(m.group(1), m.group(2)) if m else h3_plain(t))
            i += 1; continue

        if ln.startswith('## '):
            t = ln[3:]
            if t in FIG_BEFORE:   out.append(FIG_BEFORE.pop(t))
            if t in PHOTO_BEFORE: out.append(PHOTO_BEFORE.pop(t))
            out.append(h2(t))
            i += 1; continue

        if ln.strip() == '---':
            i += 1; continue          # 区切り線は装飾側で持つ

        if ln.startswith('> '):
            while i < len(lines) and lines[i].startswith('> '): i += 1
            out.append(sns_mid()); continue

        if re.match(r'^\d+\. ', ln):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                items.append(re.sub(r'^\d+\. ', '', lines[i])); i += 1
            out.append(numbered_cards(items) if len(items) == 3 and '工事請負契約約款' in items[0]
                       else ul(items))
            continue

        if ln.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(lines[i][2:]); i += 1
            out.append(ul(items, muted='会社の規模' in items[0]))
            continue

        # 著者ボックス以降は自前の装飾ブロックで置き換える
        if ln.startswith('■ この記事を書いた人'):
            break

        # 特別扱いの段落
        if ln.startswith('危ないサインは'):
            out.append(callout(ln, 'こう答える会社は要注意', CRIT, CRIT_TINT, '⚠')); i += 1; continue
        if ln.startswith('**※ここは2026年度の情報です'):
            out.append(callout(re.sub(r'^\*\*|\*\*$', '', ln).replace('※', ''),
                               '制度の最新情報にご注意ください', '#8a6100', WARN_TINT, '📌'))
            i += 1; continue
        if in_lead and ln.startswith('この記事では'):
            out.append(callout(ln, 'この記事で分かること', BRAND_MID, BRAND_TINT, '✓')); i += 1; continue

        out.append(para(ln)); i += 1

    out += [author_box(), sns_end(), related()]
    return '\n\n'.join(out)


if __name__ == '__main__':
    src = open(sys.argv[1], encoding='utf-8').read()
    body = convert(src)
    open(sys.argv[2], 'w', encoding='utf-8').write(body)
    print('blocks :', body.count('<!-- wp:'))
    print('figures:', body.count('<svg'))
    print('bytes  :', len(body))
