# -*- coding: utf-8 -*-
"""図解SVGを2倍解像度のPNGに書き出す（WordPressがSVGを除去する環境向けの控え）。

    python3 export_png.py <figures.py> <出力ディレクトリ>
"""
import sys, os, re, glob, subprocess, importlib.util

CHROME = next(iter(glob.glob('/opt/pw-browsers/*/chrome-linux/headless_shell')
                   + glob.glob('/opt/pw-browsers/*/chrome-linux/chrome')), None)

if __name__ == '__main__':
    if not CHROME:
        raise SystemExit('Chromiumが見つかりません（/opt/pw-browsers を確認）')
    figpath, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    spec = importlib.util.spec_from_file_location('article_figures', figpath)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

    for key, (fn, cap) in mod.FIGURES.items():
        svg = fn()
        w, h = map(int, re.search(r'viewBox="0 0 (\d+) (\d+)"', svg).groups())
        svg = re.sub(r'width:100%;min-width:\d+px;height:auto', f'width:{w}px;height:{h}px', svg)
        tmp = os.path.join(outdir, f'_{key}.html')
        open(tmp, 'w', encoding='utf-8').write(
            f'<html><head><meta charset="utf-8"></head>'
            f'<body style="margin:0;background:#fff">{svg}</body></html>')
        out = os.path.join(outdir, f'fig-{key}.png')
        subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-sandbox',
                        '--hide-scrollbars', '--force-device-scale-factor=2',
                        f'--window-size={w},{h}', f'--screenshot={out}',
                        f'file://{os.path.abspath(tmp)}'], capture_output=True)
        os.remove(tmp)
        print(f'  {out}  ({w*2}x{h*2})  {cap}')
