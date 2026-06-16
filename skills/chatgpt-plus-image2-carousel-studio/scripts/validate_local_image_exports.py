#!/usr/bin/env python3
"""Validate local downloaded Image-2 carousel PNGs against the run contract."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml
from PIL import Image


def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail('usage: validate_local_image_exports.py <carousel-run-contract.yaml>')
    contract = yaml.safe_load(Path(sys.argv[1]).read_text(encoding='utf-8')) or {}
    slide_count = int(contract.get('slide_count') or 0)
    fmt = contract.get('format') or {}
    expected = (int(fmt.get('width')), int(fmt.get('height')))
    workbench = Path(contract['paths']['workbench_dir']).expanduser()
    export_dir = workbench / 'downloads'
    if not export_dir.exists():
        fail(f'downloads dir missing: {export_dir}')
    for i in range(1, slide_count + 1):
        p = export_dir / f'slide_{i:02d}.png'
        if not p.exists():
            fail(f'missing {p.name}')
        if p.stat().st_size < 50_000:
            fail(f'{p.name} is too small to trust')
        try:
            with Image.open(p) as im:
                if im.size != expected:
                    fail(f'{p.name} dimensions {im.size}, expected {expected}')
                if im.format != 'PNG':
                    fail(f'{p.name} is {im.format}, expected PNG')
        except Exception as e:
            fail(f'cannot open {p.name}: {e}')
    print('PASS: local image exports valid')

if __name__ == '__main__':
    main()
