# -*- coding: utf-8 -*-
"""
给每个工艺生成一张贴现场的二维码，输出到「二维码」目录。

  二维码/钢筋绑扎.png   ->  https://你的网址/?p=rebar

用法：
    python3 工具/生成二维码.py
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = os.path.join(BASE, "config.js")
OUT = os.path.join(BASE, "二维码")

# 想手动指定网址就填这里（https 开头）；留空则自动读 config.js 里的 SITE_URL
SITE_URL = ""

try:
    import qrcode
    from PIL import Image
except ImportError:
    sys.exit("缺少依赖，请先执行： pip install qrcode pillow")

js = open(CFG, encoding="utf-8").read()

if not SITE_URL:
    m = re.search(r"SITE_URL\s*=\s*['\"]([^'\"]+)['\"]", js)
    SITE_URL = m.group(1) if m else ""

if not SITE_URL or "你的域名" in SITE_URL or "example.com" in SITE_URL:
    sys.exit(
        "还没填真实网址。\n"
        "先部署到 EdgeOne Pages 拿到 https 开头的网址，\n"
        "填进 config.js 的 window.SITE_URL，再运行本脚本。"
    )

SITE_URL = SITE_URL.rstrip("/")

# 抓每个工艺的 id 和 name
items = re.findall(r"id:\s*['\"]([^'\"]+)['\"].*?name:\s*['\"]([^'\"]*)['\"]", js, re.S)
if not items:
    sys.exit("config.js 里没解析到工艺，请检查 id / name 两行是否完整。")


def make_qr(data, out_path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,          # 留白越大，微信越容易扫
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    logo = os.path.join(BASE, "logo.png")
    if os.path.exists(logo):
        lg = Image.open(logo).convert("RGBA")
        lw = img.size[0] // 5
        lg = lg.resize((lw, lw))
        img.paste(lg, ((img.size[0] - lw) // 2, (img.size[1] - lw) // 2), lg)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path)
    return out_path


print("=" * 58)
for pid, name in items:
    url = SITE_URL + "/?p=" + pid
    fn = (name or pid) + ".png"
    make_qr(url, os.path.join(OUT, fn))
    print("%-10s -> 二维码/%s" % (name, fn))
    print("            %s" % url)

print("=" * 58)
print("共 %d 张，全部在「二维码」目录，一个工艺贴一张，别贴混。" % len(items))
