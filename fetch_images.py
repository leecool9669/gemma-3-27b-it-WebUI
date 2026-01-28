# -*- coding: utf-8 -*-
"""下载模型页面相关图片到 template/images，使用代理 127.0.0.1:18081"""
import os
import sys
try:
    import requests
except ImportError:
    os.system(f'"{sys.executable}" -m pip install requests -q')
    import requests

os.makedirs("images", exist_ok=True)
proxies = {"http": "http://127.0.0.1:18081", "https": "http://127.0.0.1:18081"}

# 从页面中提取的图片URL
urls = [
    ("https://cdn-thumbnails.hf-mirror.com/social-thumbnails/models/google/gemma-3-27b-it.png", "images/gemma-3-27b-it_model_page.png"),
]

for url, path in urls:
    try:
        r = requests.get(url, timeout=30, proxies=proxies)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
        print("ok:", path)
    except Exception as e:
        print("skip", path, str(e))
