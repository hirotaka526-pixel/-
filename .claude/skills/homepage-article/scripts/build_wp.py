# -*- coding: utf-8 -*-
"""記事Markdown → WordPress貼り付け用の装飾つきGutenberg HTML。

    python3 build_wp.py <article.md> <out.html> [figures.py]

装飾はすべてインラインstyleで書き出す。テーマのCSSに依存しないため、
どのWordPressに貼っても見た目が変わらない。

## Markdown側で使える指示(HTMLコメント)

    <!-- toc -->                         目次ブロックのプレースホルダ
    <!-- fig: キー -->                   figures.py の該当図を挿入
    <!-- photo: 説明 | alt | ファイル名 --> 写真プレースホルダ
    <!-- sns: 導入文 -->                 中盤のYouTube導線ボックス
    <!-- box: crit|warn|good|info | ラベル -->  直後の段落を色つきボックスに
    <!-- cards -->                       直後の番号付きリストを丸数字カードに
    <!-- muted -->                       直後の箇条書きを控えめな色に

    ==テキスト==                          黄色マーカー
    **テキスト**                          太字(ブランド色)

## フロントマターで使う項目

    タイトル:      WordPressのタイトル欄に入れる文字列
    スラッグ:      URLスラッグ
    関連記事:      「表示テキスト|URL」を1行に1つ
"""
import re, sys, html, importlib.util, os

# ── ブランドカラー(ここを変えれば記事全体の色が変わる) ──────
BRAND      = '#0d366b'
BRAND_TINT = '#eef3f9'
BRAND_MID  = '#2a78d6'
CRIT, CRIT_TINT = '#d03b3b', '#fdf2f2'
WARN, WARN_TINT = '#fab219', '#fff8e6'
WARN_D          = '#8a6100'
GOOD, GOOD_TINT = '#0ca30c', '#f1faf3'
INK, INK2, LINE = '#1a1a19', '#52514e', '#d8d8d4'
MARKER = 'linear-gradient(transparent 62%, #ffe89a 62%)'
BODY   = f'font-size:17px;line-height:1.95;color:{INK};'

BOX_STYLES = {
    'crit': (CRIT,   CRIT_TINT,  '⚠'),
    'warn': (WARN_D, WARN_TINT,  '📌'),
    'good': (GOOD,   GOOD_TINT,  '✓'),
    'info': (BRAND_MID, BRAND_TINT, '✓'),
}


def esc(s):
    return html.escape(s, quote=False)


def inline(t, color=BRAND):
    t = esc(t)
    t = re.sub(r'==(.+?)==',
               rf'<strong style="font-weight:700;background:{MARKER};padding:0 2px;'
               rf'color:{INK}">\1</strong>', t)
    t = re.sub(r'\*\*(.+?)\*\*', rf'<strong style="font-weight:700;color:{color}">\1</strong>', t)
    t = re.sub(r'\[(.+?)\]\((.+?)\)',
               rf'<a href="\2" style="color:{BRAND_MID};text-decoration:underline;'
               rf'text-underline-offset:3px">\1</a>', t)
    return t


def blk(name, attrs, inner):
    a = (' ' + attrs) if attrs else ''
    return f'<!-- wp:{name}{a} -->\n{inner}\n<!-- /wp:{name} -->'


def para(t):
    return blk('paragraph', '', f'<p style="{BODY}margin:0 0 1.5em">{inline(t)}</p>')


def h2(t):
    st = (f'background:{BRAND};color:#fff;font-size:23px;font-weight:700;line-height:1.5;'
          f'margin:3em 0 1.2em;padding:.7em .9em;border-radius:6px;')
    return blk('heading', '{"level":2}', f'<h2 class="wp-block-heading" style="{st}">{esc(t)}</h2>')


def h3(t):
    """「質問N：〜」形式ならバッジつきカード、それ以外は下線つき見出し。"""
    m = re.match(r'^質問(\d+)：(.+)$', t)
    if m:
        st = (f'background:{BRAND_TINT};border-left:6px solid {BRAND};border-radius:0 6px 6px 0;'
              f'color:{BRAND};font-size:20px;font-weight:700;line-height:1.6;'
              f'margin:2.4em 0 1.1em;padding:.85em 1em;')
        badge = (f'<span style="display:inline-block;background:{BRAND};color:#fff;font-size:13px;'
                 f'font-weight:700;border-radius:4px;padding:2px 9px;margin-right:10px;'
                 f'vertical-align:2px">質問{m.group(1)}</span>')
        body = esc(m.group(2))
    else:
        st = (f'color:{BRAND};font-size:20px;font-weight:700;line-height:1.6;'
              f'margin:2.4em 0 1.1em;padding-bottom:.4em;border-bottom:2px solid {BRAND_TINT};')
        badge, body = '', esc(t)
    return blk('heading', '{"level":3}', f'<h3 class="wp-block-heading" style="{st}">{badge}{body}</h3>')


def callout(t, kind, label):
    accent, tint, icon = BOX_STYLES[kind]
    inner = (f'<div class="wp-block-group" style="background:{tint};border:1px solid {accent};'
             f'border-radius:8px;padding:1.1em 1.2em;margin:0 0 1.8em">'
             f'<p style="margin:0 0 .5em;font-size:14px;font-weight:700;color:{accent};'
             f'letter-spacing:.04em">{icon} {esc(label)}</p>'
             f'<p style="{BODY}margin:0">{inline(t, accent)}</p></div>')
    return blk('group', '{"layout":{"type":"constrained"}}', inner)


def figure(svg, cap):
    inner = (f'<figure style="margin:2.2em 0;border:1px solid {LINE};border-radius:8px;'
             f'padding:1.2em;background:#fff">'
             f'<div style="overflow-x:auto;-webkit-overflow-scrolling:touch">{svg}</div>'
             f'<figcaption style="font-size:14px;color:{INK2};margin-top:.9em;line-height:1.6">'
             f'{esc(cap)}<span style="display:block;font-size:13px;color:#8a8a86;margin-top:.3em">'
             f'※スマートフォンでは図を横にスクロールできます</span></figcaption></figure>')
    return blk('html', '', inner)


def todo(text):
    st = (f'background:#fffbe8;border:2px dashed {WARN};border-radius:6px;'
          f'padding:.9em 1em;font-size:14px;color:#6b4d00;margin:0 0 1.8em')
    return blk('paragraph', '{"className":"todo"}', f'<p class="todo" style="{st}">{text}</p>')


def photo_todo(n, desc, alt, fname):
    return todo(f'【写真{n} を挿入】{esc(desc)}<br>alt：{esc(alt)}　／　ファイル名：{esc(fname)}'
                f'<br><strong>← 写真を入れたら、この段落を削除してください</strong>')


def toc_todo():
    return todo('【ここに目次ブロックを挿入】'
                '<strong>← 挿入したら、この段落を削除してください</strong>')


def ul(items, muted=False):
    col = INK2 if muted else INK
    lis = ''.join(f'<!-- wp:list-item -->\n<li style="{BODY}color:{col};margin:0 0 .7em">'
                  f'{inline(x)}</li>\n<!-- /wp:list-item -->' for x in items)
    return blk('list', '', f'<ul class="wp-block-list" style="padding-left:1.3em;'
                           f'margin:0 0 1.8em">\n{lis}\n</ul>')


def ol(items):
    lis = ''.join(f'<!-- wp:list-item -->\n<li style="{BODY}margin:0 0 .7em">'
                  f'{inline(x)}</li>\n<!-- /wp:list-item -->' for x in items)
    return blk('list', '{"ordered":true}', f'<ol class="wp-block-list" style="padding-left:1.3em;'
                                           f'margin:0 0 1.8em">\n{lis}\n</ol>')


def cards(items):
    out = []
    for i, x in enumerate(items, 1):
        num = (f'<span style="flex:0 0 34px;height:34px;background:{BRAND};color:#fff;'
               f'border-radius:50%;display:flex;align-items:center;justify-content:center;'
               f'font-weight:700;font-size:16px">{i}</span>')
        out.append(f'<div style="display:flex;gap:14px;align-items:flex-start;'
                   f'background:{BRAND_TINT};border-radius:8px;padding:1em 1.1em;margin:0 0 .9em">'
                   f'{num}<p style="{BODY}margin:0">{inline(x)}</p></div>')
    return blk('html', '', f'<div style="margin:0 0 2em">{"".join(out)}</div>')


def sns_mid(lead):
    inner = (f'<div class="wp-block-group" style="background:#fff5f5;border:1px solid #f0b8b8;'
             f'border-left:6px solid #ff0000;border-radius:0 8px 8px 0;padding:1.1em 1.2em;'
             f'margin:0 0 1.8em">'
             f'<p style="margin:0 0 .4em;font-size:14px;font-weight:700;color:#c00">'
             f'▶ YouTubeでも解説しています</p>'
             f'<p style="{BODY}margin:0">{inline(lead)}<br>'
             f'<span style="background:#ffe89a;padding:2px 6px;border-radius:3px;font-size:15px">'
             f'［ここに該当動画のURLを貼ってください］</span></p></div>')
    return blk('group', '{"layout":{"type":"constrained"}}', inner)


def author_box():
    return blk('group', '{"layout":{"type":"constrained"}}',
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
        f'<strong style="color:{BRAND}">施工エリア</strong>：高浜市・碧南市・刈谷市・安城市・'
        f'西尾市・知立市・岡崎市・豊明市・半田市・大府市・東浦町ほか西三河／知多エリア</p></div>')


def sns_end():
    def btn(label, sub, url, bg):
        return (f'<a href="{url}" target="_blank" rel="noopener" '
                f'style="flex:1 1 240px;background:{bg};color:#fff;text-decoration:none;'
                f'border-radius:8px;padding:1em 1.2em;display:block">'
                f'<span style="display:block;font-size:13px;opacity:.85">{sub}</span>'
                f'<span style="display:block;font-size:16px;font-weight:700;margin-top:2px">'
                f'{label}</span></a>')
    return blk('html', '',
        f'<div style="margin:0 0 2.5em"><p style="{BODY}margin:0 0 1em">'
        f'家づくりの本音や現場の様子は、YouTube・Instagramでも発信しています。</p>'
        f'<div style="display:flex;flex-wrap:wrap;gap:12px">'
        + btn('1級建築士 まえちゃんの家づくり教室', 'YouTube',
              'https://www.youtube.com/@inthehome', '#c4302b')
        + btn('@in.the.home', 'Instagram',
              'https://www.instagram.com/in.the.home/', '#b4318f')
        + btn('まえちゃん｜家づくりを丸ごとサポートする建築士', 'Instagram',
              'https://www.instagram.com/maechan.no.iezukuri/', '#b4318f')
        + '</div></div>')


def related(items):
    if not items:
        return ''
    lis = ''.join(f'<li style="margin:0 0 .6em"><a href="{u}" style="color:{BRAND_MID};'
                  f'font-size:16px;text-decoration:underline;text-underline-offset:3px">'
                  f'{esc(t)}</a></li>' for t, u in items)
    return blk('html', '',
        f'<div style="border-top:2px solid {LINE};padding-top:1.4em;margin:0 0 2em">'
        f'<p style="font-size:16px;font-weight:700;color:{BRAND};margin:0 0 .8em">関連記事</p>'
        f'<ul style="padding-left:1.2em;margin:0">{lis}</ul></div>')


# ── フロントマター ────────────────────────────────
def split_front(md):
    if not md.startswith('---'):
        return {}, md
    _, fm, body = md.split('---', 2)
    meta, key = {}, None
    for line in fm.split('\n'):
        if not line.strip():
            continue
        m = re.match(r'^(\S[^:]*):\s*(.*)$', line)
        if m:
            key = m.group(1).strip()
            meta[key] = m.group(2).strip()
        elif line.startswith('  - ') and key:
            meta.setdefault(key + '__list', []).append(line[4:].strip())
    return meta, body


def load_figures(path):
    if not path or not os.path.exists(path):
        return {}
    spec = importlib.util.spec_from_file_location('article_figures', path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    spec.loader.exec_module(mod)
    return getattr(mod, 'FIGURES', {})


# ── 本文の変換 ────────────────────────────────────
def convert(md, figs):
    meta, body = split_front(md)
    lines = [l.rstrip() for l in body.split('\n')]
    out, i = [], 0
    photo_n = 0
    pending_box = None      # ('crit', 'ラベル')
    pending_cards = False
    pending_muted = False
    used_figs = []

    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1; continue

        # ── 指示コメント ──
        m = re.match(r'^<!--\s*toc\s*-->$', ln)
        if m:
            out.append(toc_todo()); i += 1; continue

        m = re.match(r'^<!--\s*fig:\s*(\S+)\s*-->$', ln)
        if m:
            key = m.group(1)
            if key not in figs:
                raise SystemExit(f'図解「{key}」が figures.py にありません')
            fn, cap = figs[key]
            out.append(figure(fn(), cap)); used_figs.append(key); i += 1; continue

        m = re.match(r'^<!--\s*photo:\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*-->$', ln)
        if m:
            photo_n += 1
            out.append(photo_todo(photo_n, m.group(1), m.group(2), m.group(3)))
            i += 1; continue

        m = re.match(r'^<!--\s*sns:\s*(.+?)\s*-->$', ln)
        if m:
            out.append(sns_mid(m.group(1))); i += 1; continue

        m = re.match(r'^<!--\s*box:\s*(crit|warn|good|info)\s*\|\s*(.+?)\s*-->$', ln)
        if m:
            pending_box = (m.group(1), m.group(2)); i += 1; continue

        if re.match(r'^<!--\s*cards\s*-->$', ln):
            pending_cards = True; i += 1; continue
        if re.match(r'^<!--\s*muted\s*-->$', ln):
            pending_muted = True; i += 1; continue
        if ln.startswith('<!--'):
            i += 1; continue          # その他のコメントは無視

        # ── 見出し ──
        if ln.startswith('# '):
            i += 1; continue          # H1はWordPressのタイトル欄が持つ
        if ln.startswith('### '):
            out.append(h3(ln[4:])); i += 1; continue
        if ln.startswith('## '):
            out.append(h2(ln[3:])); i += 1; continue
        if ln.strip() == '---':
            i += 1; continue

        # ── リスト ──
        if re.match(r'^\d+\. ', ln):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                items.append(re.sub(r'^\d+\. ', '', lines[i])); i += 1
            out.append(cards(items) if pending_cards else ol(items))
            pending_cards = False; continue

        if ln.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(lines[i][2:]); i += 1
            out.append(ul(items, muted=pending_muted))
            pending_muted = False; continue

        # ── 段落 ──
        if pending_box:
            out.append(callout(ln, *pending_box)); pending_box = None
        else:
            out.append(para(ln))
        i += 1

    unused = [k for k in figs if k not in used_figs]
    if unused:
        print(f'! 未使用の図解: {", ".join(unused)}', file=sys.stderr)

    rel = [tuple(x.split('|', 1)) for x in meta.get('関連記事__list', [])]
    out += [author_box(), sns_end(), related([(t.strip(), u.strip()) for t, u in rel])]
    return meta, '\n\n'.join(x for x in out if x)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    src = open(sys.argv[1], encoding='utf-8').read()
    figs = load_figures(sys.argv[3] if len(sys.argv) > 3 else None)
    meta, out = convert(src, figs)
    open(sys.argv[2], 'w', encoding='utf-8').write(out)
    print(f'ブロック数 : {out.count("<!-- wp:")}')
    print(f'図解       : {out.count("<svg")}')
    print(f'写真枠     : {out.count("【写真")}')
    plain = re.sub(r'<[^>]+>', '', out)
    plain = re.sub(r'\s', '', plain)
    print(f'文字数     : {len(plain):,}')
    if meta.get('タイトル'):
        print(f'タイトル欄 : {meta["タイトル"]}')
