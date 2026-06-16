#!/usr/bin/env python3
"""Scan a workbench for forbidden carousel-generation fallbacks."""
from __future__ import annotations
import sys
from pathlib import Path

FORBIDDEN = [
    'openrouter', 'anthropic', 'claude', 'gemini', 'google.generative',
    'images.generate', 'openai.images', 'PIL import', 'from PIL', 'pillow',
    'ImageMagick', 'matplotlib', 'provider=', 'base_url=', 'model=',
]
EXTS = {'.py','.md','.yaml','.yml','.json','.txt'}


def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail('usage: validate_no_paid_api_fallback.py <workbench-dir>')
    root = Path(sys.argv[1]).expanduser().resolve()
    if not root.exists():
        fail(f'path not found: {root}')
    hits = []
    for p in root.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in EXTS:
            continue
        text = p.read_text(encoding='utf-8', errors='ignore')
        low = text.lower()
        for term in FORBIDDEN:
            probe = term if term == term.lower() else term.lower()
            if probe in low:
                hits.append(f'{p}: {term}')
    if hits:
        fail('forbidden fallback markers found:\n' + '\n'.join(hits[:50]))
    print('PASS: no forbidden fallback markers found')

if __name__ == '__main__':
    main()
