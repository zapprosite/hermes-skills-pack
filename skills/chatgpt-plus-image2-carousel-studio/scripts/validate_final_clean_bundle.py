#!/usr/bin/env python3
"""Validate the final Instagram carousel folder is clean and publish-ready."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml
from PIL import Image

ALLOWED_CAPTION = 'caption.txt'


def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail('usage: validate_final_clean_bundle.py <carousel-run-contract.yaml>')
    contract = yaml.safe_load(Path(sys.argv[1]).read_text(encoding='utf-8')) or {}
    slide_count = int(contract.get('slide_count') or 0)
    fmt = contract.get('format') or {}
    expected = (int(fmt.get('width')), int(fmt.get('height')))
    final_dir = Path(contract['paths']['final_dir']).expanduser()
    if not final_dir.exists():
        fail(f'final_dir missing: {final_dir}')
    expected_names = {f'slide_{i:02d}.png' for i in range(1, slide_count + 1)} | {ALLOWED_CAPTION}
    actual_names = {p.name for p in final_dir.iterdir() if p.is_file()}
    extras = sorted(actual_names - expected_names)
    missing = sorted(expected_names - actual_names)
    if missing:
        fail('missing final files: ' + ', '.join(missing))
    if extras:
        fail('extra files in final folder: ' + ', '.join(extras))
    for name in sorted(expected_names - {ALLOWED_CAPTION}):
        p = final_dir / name
        if p.stat().st_size < 50_000:
            fail(f'{name} is too small to trust')
        with Image.open(p) as im:
            if im.size != expected:
                fail(f'{name} dimensions {im.size}, expected {expected}')
            if im.format != 'PNG':
                fail(f'{name} is {im.format}, expected PNG')
    caption = (final_dir / ALLOWED_CAPTION).read_text(encoding='utf-8', errors='ignore')
    if 'backend-api/' in caption or 'estuary/content' in caption or 'http' in caption and 'chatgpt' in caption.lower():
        fail('caption appears to contain a backend/signed URL')
    print('PASS: final clean bundle valid')

if __name__ == '__main__':
    main()
