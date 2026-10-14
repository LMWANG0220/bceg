# -*- coding: utf-8 -*-
"""
工地现场 4G 信号经常不稳，图片太大扫码会白屏等半天。
这个脚本把 img 目录里的图片批量压小，输出到 "压缩后" 目录，
你确认没问题后，把压缩后的图覆盖回 img 目录即可。

会跳过文件名里带 qr 的二维码图（二维码压糊了会识别不出来）。

用法：  python3 工具/压缩图片.py
"""
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("缺少 Pillow，请先执行： pip install pillow")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "img")
OUT = os.path.join(BASE, "压缩后")

MAX_EDGE = 1280    # 最长边像素，1080 够清楚了
QUALITY = 82       # 画质，80~85 肉眼几乎看不出差别

count = 0
for root, _, files in os.walk(SRC):
    for fn in files:
        if not fn.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        if "qr" in fn.lower():
            continue
        src = os.path.join(root, fn)
        rel = os.path.relpath(src, SRC)
        dst = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)

        im = Image.open(src)
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        w, h = im.size
        scale = min(1.0, MAX_EDGE / float(max(w, h)))
        if scale < 1.0:
            im = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
        im.save(dst, quality=QUALITY, optimize=True)

        old = os.path.getsize(src) / 1024.0
        new = os.path.getsize(dst) / 1024.0
        count += 1
        print("%-24s %7.0f KB -> %6.0f KB" % (rel, old, new))

print("-" * 46)
print("共处理 %d 张，结果在：压缩后/" % count)
print("确认无误后，把 压缩后 里的文件复制回 img/ 覆盖原图，")
print("然后把 config.js 里的 SITE_VERSION 数字 +1。")
