# -*- coding: utf-8 -*-
"""図解SVGをPNGに書き出す。

    python3 export_png.py <figures.py> <出力ディレクトリ> [--width 幅px]

`--width` を省略すると、SVGのviewBoxそのままの解像度で2倍(Retina相当)で書き出す
（大きい。印刷や高解像度表示向け）。
Googleドキュメントに貼る用途では重すぎるので、**480〜620px程度を指定する**こと。
指定した幅にアスペクト比を保って縮小し、テキストがにじまない程度の解像度で書き出す。
"""
import sys, os, re, glob, subprocess, importlib.util

CHROME = next(iter(glob.glob('/opt/pw-browsers/*/chrome-linux/headless_shell')
                   + glob.glob('/opt/pw-browsers/*/chrome-linux/chrome')), None)


def export_one(key, fn, cap, outdir, target_w=None):
    svg = fn()
    w, h = map(int, re.search(r'viewBox="0 0 (\d+) (\d+)"', svg).groups())
    if target_w:
        scale = target_w / w
        render_w, render_h = target_w, round(h * scale)
        scale_factor = 1  # 縮小先の解像度で十分。Retina倍にすると逆にファイルが重くなる
    else:
        render_w, render_h = w, h
        scale_factor = 2
    svg = re.sub(r'width:100%;min-width:\d+px;height:auto',
                 f'width:{render_w}px;height:{render_h}px', svg)
    tmp = os.path.join(outdir, f'_{key}.html')
    open(tmp, 'w', encoding='utf-8').write(
        f'<html><head><meta charset="utf-8"></head>'
        f'<body style="margin:0;background:#fff">{svg}</body></html>')
    out = os.path.join(outdir, f'fig-{key}.png')
    subprocess.run([CHROME, '--headless', '--disable-gpu', '--no-sandbox',
                    '--hide-scrollbars', f'--force-device-scale-factor={scale_factor}',
                    f'--window-size={render_w},{render_h}', f'--screenshot={out}',
                    f'file://{os.path.abspath(tmp)}'], capture_output=True)
    os.remove(tmp)
    px = f'{render_w * scale_factor}x{render_h * scale_factor}'
    print(f'  {out}  ({px})  {cap}')


if __name__ == '__main__':
    if not CHROME:
        raise SystemExit('Chromiumが見つかりません（/opt/pw-browsers を確認）')
    args = sys.argv[1:]
    target_w = None
    if '--width' in args:
        idx = args.index('--width')
        target_w = int(args[idx + 1])
        del args[idx:idx + 2]
    figpath, outdir = args[0], args[1]
    os.makedirs(outdir, exist_ok=True)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    spec = importlib.util.spec_from_file_location('article_figures', figpath)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

    for key, (fn, cap) in mod.FIGURES.items():
        export_one(key, fn, cap, outdir, target_w)
