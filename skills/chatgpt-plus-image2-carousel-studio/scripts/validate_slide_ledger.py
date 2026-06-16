#!/usr/bin/env python3
"""Validate the one-slide-at-a-time Image-2 carousel ledger."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

VALID = {'PENDING','PASS','NEEDS_FIX','BLOCKED'}

def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail('usage: validate_slide_ledger.py <slide-ledger.yaml>')
    path = Path(sys.argv[1]).expanduser().resolve()
    data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    slides = data.get('slides') or []
    if not slides:
        fail('slides list is empty')
    seen_pending = False
    for idx, slide in enumerate(slides, 1):
        if slide.get('number') != idx:
            fail(f'slide {idx} has wrong number')
        status = slide.get('visual_qa', 'PENDING')
        if status not in VALID:
            fail(f'slide {idx} has invalid visual_qa {status!r}')
        if seen_pending and status == 'PASS':
            fail(f'slide {idx} is PASS after a prior unfinished slide')
        if status == 'PASS':
            if not slide.get('downloaded_file'):
                fail(f'slide {idx} PASS but downloaded_file is empty')
            dims = slide.get('dimensions')
            if not (isinstance(dims, list) and len(dims) == 2):
                fail(f'slide {idx} PASS but dimensions are missing')
            if not slide.get('approved_at'):
                fail(f'slide {idx} PASS but approved_at is empty')
        else:
            seen_pending = True
    print('PASS: slide ledger valid')

if __name__ == '__main__':
    main()
