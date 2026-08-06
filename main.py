#!/usr/bin/env python3
"""把資料夾內圖片批次轉成 WebP 的清單預覽 CLI（只列不轉也可） — 列出可轉 WebP 的圖片（不依賴外部套件）。"""
from __future__ import annotations
import argparse
from pathlib import Path

EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".gif"}

def main() -> None:
    p = argparse.ArgumentParser(description='把資料夾內圖片批次轉成 WebP 的清單預覽 CLI（只列不轉也可）')
    p.add_argument("dir", type=Path)
    args = p.parse_args()
    for f in sorted(args.dir.rglob("*")):
        if f.is_file() and f.suffix.lower() in EXTS:
            out = f.with_suffix(".webp")
            print(f"{f} -> {out.name}")

if __name__ == "__main__":
    main()
