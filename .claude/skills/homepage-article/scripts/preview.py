# -*- coding: utf-8 -*-
"""装飾つきHTMLを実際にブラウザで描画してPNGにする。目視確認用。

    python3 preview.py <wp.html> <出力ディレクトリ> [オフセットpx...]

デスクトップ(760px幅)とスマホ(390px幅)の両方を書き出す。
**スマホ表示の確認は必須。** 図解の文字が潰れていないか、
横スクロールが本文側に出ていないかを必ず目で見ること。
"""
import re, sys, os, subprocess, glob

CHROME = next(iter(glob.glob('/opt/pw-browsers/*/chrome-linux/headless_shell')
                   + glob.glob('/opt/pw-browsers/*/chrome-linux/chrome')), None)

PAGE = """<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
 body{{margin:{off}px 0 0 0;background:#f0f0ee;
      font-family:"Hiragino Kaku Gothic ProN","Yu Gothic",Meiryo,sans-serif}}
 .wrap{{max-width:{maxw};margin:0 auto;background:#fff;padding:{pad}}}
 h1{{font-size:{h1}px;line-height:1.5;color:#1a1a19;margin:0 0 1.2em}}
</style></head><body><div class="wrap">{h1tag}{body}</div></body></html>"""


def shot(body, out, width, height, off, title):
    desktop = width > 500
    page = PAGE.format(
        off=-off, maxw='760px' if desktop else '100%',
        pad='40px 32px' if desktop else '20px 16px',
        h1=30 if desktop else 24,
        h1tag=f'<h1>{title}</h1>' if (title and off == 0) else '',
        body=body)
    tmp = out.replace('.png', '.html')
    open(tmp, 'w', encoding='utf-8').write(page)
    subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-sandbox',
                    '--hide-scrollbars', f'--window-size={width},{height}',
                    f'--screenshot={out}', f'file://{os.path.abspath(tmp)}'],
                   capture_output=True)
    os.remove(tmp)
    print('  ', out)


if __name__ == '__main__':
    if not CHROME:
        raise SystemExit('Chromiumが見つかりません（/opt/pw-browsers を確認）')
    src, outdir = sys.argv[1], sys.argv[2]
    offsets = [int(x) for x in sys.argv[3:]] or [0, 1500, 3000]
    os.makedirs(outdir, exist_ok=True)
    raw = open(src, encoding='utf-8').read()
    body = re.sub(r'<!-- /?wp:[^>]*-->', '', raw)
    title = ''
    print('デスクトップ(760px):')
    for off in offsets:
        shot(body, f'{outdir}/pc-{off}.png', 860, 1500, off, title)
    print('スマホ(390px)  ※必ず目で確認すること:')
    for off in offsets:
        shot(body, f'{outdir}/sp-{off}.png', 390, 1400, off, title)
