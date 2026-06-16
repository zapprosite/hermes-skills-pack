# 2026-05-19 — 4:5 / 1080x1350 ALL standard for Refrimix carousels

The user corrected the Image-2 carousel workflow: for Refrimix/marketing carousels, the operational contract is now `4:5 / 1080x1350: ALL`.

Current standard for Refrimix-style sales carousels:

- Master format: `1080x1350 px`.
- Ratio: `4:5`.
- Scope: ALL slides and ALL operational contracts for Refrimix/marketing carousels.
- ChatGPT Plus dropdown: `Retrato 4:5`.
- Safe area: keep title, subtitle, logo, CTA, and critical UI inside a central area with `90–120 px` lateral margin.
- Cover: design in 4:5 and check profile/grid preview readability without changing the contract format.
- No alternate aspect-ratio exception is allowed in the run contract, validator, browser ratio selection, prompts, ledgers, or final export.

Required contract fields:

```yaml
format:
  canonical: instagram_portrait_4_5
  width: 1080
  height: 1350
  chatgpt_option: Retrato 4:5
  safe_margin_px: 90-120
  profile_grid_preview_safe: true
```

Do not create an alternate-ratio contract.

Standalone realistic-photo ratio discussions belong outside this carousel workflow. Alternate ratios must not appear as `format.canonical`, `chatgpt_option`, validator allowlist, correction prompt, or export target for Refrimix/marketing carousels.

Do not let old Image-2 references or prompt examples override the current rule. Correction prompts, browser ratio selection, validators, and final export checks must all enforce `4:5 / 1080x1350` only. If the UI label is ambiguous, validate the downloaded file dimensions rather than guessing from the dropdown label.
