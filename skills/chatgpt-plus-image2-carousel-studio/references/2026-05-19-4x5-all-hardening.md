# 2026-05-19 — 4:5 / 1080x1350 ALL hardening

## Trigger

The user corrected the carousel workflow after seeing a ChatGPT Plus/Image-2 carousel technique note: for Refrimix/marketing carousels, the operational rule is not “4:5 default with 3:4 exceptions”. It is:

```text
Contrato 4:5 / 1080x1350: ALL
```

## Durable lesson

For this workflow, `3:4` is not an operational exception. It may be true as external Instagram/photo knowledge, but it must not enter the Refrimix/marketing carousel pipeline.

The hardened contract must enforce:

```yaml
format:
  canonical: instagram_portrait_4_5
  width: 1080
  height: 1350
  chatgpt_option: Retrato 4:5
  safe_margin_px: 90-120
  profile_grid_preview_safe: true
```

## What future agents must do

- Treat `4:5 / 1080x1350` as mandatory for all slides.
- Select `Retrato 4:5` in ChatGPT Plus/Image-2 before slide 1.
- Keep profile/grid readability as a QA check, not a ratio change.
- Reject `exception_reason` in the contract.
- Reject alternate aspect ratios even when the prompt says “photo”, “camera”, “cellphone”, “profile preview”, “legacy”, or “explicit user request” inside this carousel workflow.
- Remove old prompt templates that say “em 3:4” from operational recovery flows.

## Validator expectations

Positive case:

```text
PASS: image2 carousel contract valid
```

Negative cases that must fail:

- `canonical: instagram_portrait_3_4`, even with an exception reason.
- `width: 1080`, `height: 1440`.
- `chatgpt_option: Retrato 3:4`.
- any `format.exception_reason` key.

## Pitfall

Do not preserve `3:4` wording as an “allowed exception” in SKILL.md, templates, references, browser session guard, sequential runner, visual direction, quality export, or content-generation policy. If `3:4` is mentioned at all, it must be clearly outside this Refrimix/marketing carousel contract workflow.
