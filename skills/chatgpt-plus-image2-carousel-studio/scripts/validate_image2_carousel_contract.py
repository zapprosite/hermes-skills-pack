#!/usr/bin/env python3
"""Validate the hardened ChatGPT Plus Image-2 carousel run contract."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

REQUIRED_LOCK = {
    'image_generation': 'chatgpt_plus_web_image2_only',
    'browser': 'camofox_vnc',
    'paid_api_allowed': False,
    'pil_render_allowed': False,
    'local_renderer_allowed': False,
    'openrouter_allowed': False,
    'model_change_allowed': False,
}
REQUIRED_GATES = {
    'preflight','provider_lock','copy_complete','visual_direction_complete',
    'aspect_ratio_selected','per_slide_visual_qa','real_download',
    'local_file_validation','final_clean_export'
}
def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail('usage: validate_image2_carousel_contract.py <carousel-run-contract.yaml>')
    path = Path(sys.argv[1]).expanduser().resolve()
    if not path.exists():
        fail(f'contract not found: {path}')
    data = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    if data.get('pipeline') != 'chatgpt-plus-image2-carousel-studio':
        fail('pipeline must be chatgpt-plus-image2-carousel-studio')
    slide_count = data.get('slide_count')
    if not isinstance(slide_count, int) or slide_count < 1 or slide_count > 10:
        fail('slide_count must be an int from 1 to 10')
    fmt = data.get('format') or {}
    canonical = fmt.get('canonical')
    dims = (fmt.get('width'), fmt.get('height'))
    if canonical != 'instagram_portrait_4_5':
        fail('format.canonical must be instagram_portrait_4_5; alternate aspect ratios are not permitted in Image-2 carousel contracts')
    if dims != (1080, 1350):
        fail('instagram_portrait_4_5 must be exactly 1080x1350')
    if str(fmt.get('chatgpt_option') or '') != 'Retrato 4:5':
        fail('format.chatgpt_option must be exactly "Retrato 4:5"')
    if 'exception_reason' in fmt:
        fail('format.exception_reason is not allowed; the contract is 4:5 / 1080x1350 only')
    safe = str(fmt.get('safe_margin_px', '90-120'))
    if '90' not in safe and '120' not in safe:
        fail('4:5 sales carousel should declare safe_margin_px around 90-120')
    lock = data.get('provider_lock') or {}
    for k, v in REQUIRED_LOCK.items():
        if lock.get(k) != v:
            fail(f'provider_lock.{k} must be {v!r}')
    paths = data.get('paths') or {}
    workbench = Path(str(paths.get('workbench_dir',''))).expanduser()
    final_dir = Path(str(paths.get('final_dir',''))).expanduser()
    if not str(workbench).startswith('/tmp/hermes-carousel-runs/'):
        fail('workbench_dir must be under /tmp/hermes-carousel-runs/')
    if not str(final_dir).startswith('/home/will/Imagens/carroceis/'):
        fail('final_dir must be under /home/will/Imagens/carroceis/')
    if workbench.resolve() == final_dir.resolve():
        fail('workbench_dir and final_dir must differ')
    missing_inputs = []
    for rel in data.get('inputs_required') or []:
        if not (workbench / rel).exists():
            missing_inputs.append(rel)
    if missing_inputs:
        fail('missing required inputs in workbench: ' + ', '.join(missing_inputs))
    gates = data.get('gates') or {}
    missing_gates = sorted(g for g in REQUIRED_GATES if gates.get(g) != 'required')
    if missing_gates:
        fail('missing required gates: ' + ', '.join(missing_gates))
    print('PASS: image2 carousel contract valid')

if __name__ == '__main__':
    main()
