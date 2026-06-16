#!/usr/bin/env python3
"""Lint Image-2 prompt packs for per-slide carousel production."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

REQUIRED_PHRASES = ['SOMENTE', 'Página', 'proximo']


def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail('usage: qa_prompt_pack_lint.py <prompts.yaml>')
    data = yaml.safe_load(Path(sys.argv[1]).read_text(encoding='utf-8')) or {}
    prompts = data.get('image_prompts') or data.get('slides') or []
    if not prompts:
        fail('no prompts found')
    for idx, item in enumerate(prompts, 1):
        prompt = str(item.get('prompt') or '')
        missing = [p for p in REQUIRED_PHRASES if p not in prompt]
        if missing:
            fail(f'slide {idx} prompt missing phrases: {missing}')
        if 'safe' not in prompt.lower() and 'margem' not in prompt.lower():
            fail(f'slide {idx} prompt missing safe margin instruction')
        if 'título' not in prompt.lower() and 'titulo' not in prompt.lower():
            fail(f'slide {idx} prompt missing title instruction')
    print('PASS: prompt pack lint valid')

if __name__ == '__main__':
    main()
