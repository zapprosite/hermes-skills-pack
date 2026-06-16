---
name: chatgpt-plus-image2-carousel-studio
description: "Use when producing final Instagram carousel images through ChatGPT Plus Image-2 in Camofox/VNC with copy-first planning, per-slide QA, real downloads, and a clean export bundle. This is the hardened no-fallback workflow. See references/camofox-background-and-first-slide.md for the background-session and first-image smoke-test notes. See references/chatgpt-image-download-workflow.md for the browser-authenticated image download workaround. See `skills/browser/chatgpt-plus/` for the complete ChatGPT Plus UI map from the May 2026 audit — all 10 use-case skills (Image Generation, Voice, Write/Edit, Web Search, Projects, GPTs/Explore, Canvas, Composer Menu, Settings, File Library) plus the root index skill."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [instagram, carousel, chatgpt-plus, image2, camofox, vnc, qa-gates, no-fallback]
    related_skills: [brand-carousel-studio, carousel-copy-and-script, carousel-visual-direction, chatgpt-plus-instagram-content-studio, vnc_chatgpt_driver, carousel-quality-export, content-generation-policy]
---

# ChatGPT Plus Image-2 carousel studio

## Overview

This is the production workflow for Instagram carousels generated in ChatGPT Plus Image-2 through Camofox/VNC.

It exists to prevent the exact failure mode where an agent skips the studio workflow and renders a carousel locally with PIL, a script, or a paid API fallback. If the user asks for ChatGPT Plus, Image-2, Camofox, VNC, premium carousel work, or "não fazer errado", load this skill and follow it as the production contract.

The core rule: Hermes drives the browser. ChatGPT Plus Image-2 generates the carousel images. Hermes may plan, validate, QA, download, and export. Hermes must not replace Image-2 with a local renderer or paid model API.

Scope note: the Refrimix 4:5 / 1080x1350 lock is a campaign specialization, not the whole class. For other brands or test runs, keep the same browser-first, one-slide-at-a-time QA flow, but derive the final aspect ratio and visual contract from the campaign brief instead of forcing the Refrimix contract.

For this user, treat the persisted, already-logged-in Camofox session as the default production bench for carousel work. Prefer one isolated ChatGPT Plus chat per carousel, keep the session persistent across slides, and only re-authenticate if the session guard proves the login is stale.

## Required skill chain

Load and follow these, in order:

1. `content-generation-policy`
2. `brand-carousel-studio`
3. `carousel-copy-and-script`
4. `carousel-visual-direction`
5. `chatgpt-plus-instagram-content-studio`
6. `vnc_chatgpt_driver`
7. `image2-carousel-contract`
8. `camofox-chatgpt-plus-session-guard`
9. `image2-sequential-slide-runner`
10. `image2-slide-visual-qa`
11. `chatgpt-image-real-download`
12. `carousel-clean-final-export`
13. `carousel-quality-export`

If any required skill is unavailable, stop with `BLOCKED` and explain which skill is missing. Do not substitute a different rendering method.

## Story Sequence — 5 Quadros para Climatização

Estrutura testada para stories que vendem climatização e convertem via WhatsApp:

| Quadro | Função | Emoção | Exemplo |
|--------|--------|--------|---------|
| 1 | **HOOK** — parar o scroll | Choque/reconhecimento | "Você chega em casa e parece que entrou numa sauna." |
| 2 | **PROBLEMA** — aprofundar a dor | Desconforto | "Conta de luz alta. Conforto zero." |
| 3 | **SOLUÇÃO** — apresentar a marca | Alívio | "A Refrimix faz em 24h o que você tentou em 3 anos." |
| 4 | **PROVA SOCIAL** — credibilidade | Confiança | "+200 famílias atendidas. Zero reclamações." |
| 5 | **CTA** — converter | Urgência | "Vagas limitadas. WhatsApp no link da bio." |

**Regras story:**
- Quadro 1 deve carregar emocionalmente em 0.5s — se não para, o resto não importa
- "swipe →" é indicador universal — usar em quadros 1-4
- Quadro final (CTA) usa cor contrastante (azul ou verde WhatsApp)
- WhatsApp direto é preferível a formulário
- "Vagas limitadas" só usar se for verdade — se não for, usar outro gancho de urgência

**Formato visual story:** 9:16 (1080x1920) — diferente do carrossel 4:5.

**Copy de story por slide:**
- Headline: 5-8 palavras, bold, 30-40px equivalente
- Body: 2-3 linhas curtas, sem parágrafo parede
- Nunca culpar o usuário — mostrar que o problema é sistêmico

## Absolute blockers

Stop immediately with `BLOCKED` if any of these appear:

- Rendering final slides with PIL/Pillow, Canvas, SVG, HTML screenshot, matplotlib, ImageMagick, or any local design script.
- Calling OpenRouter, Anthropic, Claude, Gemini, Google, OpenAI Images API, or any paid external API for carousel copy or image generation.
- Changing provider, model, base_url, API settings, Camofox backend, ports, PC1 runtime, or gateway/runtime config.
- Treating a local mockup as final artwork.
- Using `curl`/`wget` from the terminal against signed ChatGPT image URLs.
- Saving signed/backend image URLs in prompts, notes, final folders, or reports.
- Advancing to the next slide before the current slide has visual QA `PASS` in the ledger.
- Marking final PASS before every image exists locally and has valid dimensions.
- Leaving prompts, ledgers, screenshots, backups, URLs, notes, or internal YAML in the final Instagram folder.
- Using `Automático`, `Square/Quadrado`, or any aspect ratio not declared in the run contract.

Correct fallback: if ChatGPT Plus/Camofox/Image-2 is unavailable, stop. Do not replace it with API, PIL, or simulated images.

## Canonical responsive format, May 2026

Operational contract for Refrimix/marketing Image-2 carousels:

- Master format: `1080x1350` (`4:5`) for ALL slides.
- Contract rule: every ChatGPT Plus Image-2 carousel contract must declare `instagram_portrait_4_5`, `1080x1350`, and `chatgpt_option: Portrait 3:4`.
- ⚠️ ChatGPT Image-2 does NOT have a 4:5 ratio option. The UI shows `Portrait 3:4` (ratio 3:4, 1024×1365). For Instagram 4:5 (1080×1350), generate in Portrait 3:4 and crop to 4:5 externally.
- No alternate aspect-ratio exception is allowed in the contract, validator, browser ratio gate, prompts, ledger, export validation, or final bundle.
- Safe area: keep text, logo, and CTA inside a central area with at least `90–120 px` lateral margin.
- Cover rule: design slide 1 as `4:5` and check profile/grid preview readability without changing the master format.
- Title: bold/black, short, thumbnail-legible.
- Subtitle: light/regular, shorter than the title block, no paragraph wall.
- One message per slide.

Summary: `4:5 / 1080x1350` is mandatory for all Refrimix/marketing carousel operations in this workflow. Do not create, validate, prompt, select, or export any alternate-ratio carousel contract.

See `references/2026-05-19-4x5-sales-carousel-standard.md` for the session correction that established the `4:5 / 1080x1350: ALL` contract rule and the exact required fields. See `references/2026-05-19-4x5-all-hardening.md` for the later hardening pass that removed operational `3:4` exceptions from validator, prompts, browser ratio gates, and export rules.
See `references/story-9x16-image2-workflow.md` for the standalone story (9:16) generation workflow — separate from carousel 4:5 flow, with tested prompts, copy template, and download sequence.

## Required contract file

Before opening ChatGPT, create a working contract outside the final folder:

`/tmp/hermes-carousel-runs/<campaign-slug>/carousel-run-contract.yaml`

Minimum shape:

```yaml
pipeline: chatgpt-plus-image2-carousel-studio
brand_slug: refrimix
campaign_slug: refrimix_pmoc_hospitalar
slide_count: 5
format:
  canonical: instagram_portrait_4_5
  width: 1080
  height: 1350
  chatgpt_option: Portrait 3:4  # 3:4 ratio — crop to 4:5 externally for Instagram 1080x1350
  safe_margin_px: 90-120
  profile_grid_preview_safe: true
provider_lock:
  image_generation: chatgpt_plus_web_image2_only
  browser: camofox_vnc
  paid_api_allowed: false
  pil_render_allowed: false
  local_renderer_allowed: false
  openrouter_allowed: false
  model_change_allowed: false
paths:
  workbench_dir: /tmp/hermes-carousel-runs/refrimix_pmoc_hospitalar
  final_dir: /home/will/Imagens/carroceis/refrimix_pmoc_hospitalar
inputs_required:
  - carousel.yaml
  - copy.md
  - caption.txt
  - visual-direction.md
  - prompts.yaml
  - render-spec.yaml
gates:
  preflight: required
  provider_lock: required
  copy_complete: required
  visual_direction_complete: required
  aspect_ratio_selected: required
  per_slide_visual_qa: required
  real_download: required
  local_file_validation: required
  final_clean_export: required
```

Run the contract validator before generation:

```bash
python3 ~/.hermes/skills/social-media/chatgpt-plus-image2-carousel-studio/scripts/validate_image2_carousel_contract.py /tmp/hermes-carousel-runs/<slug>/carousel-run-contract.yaml
```

## Workflow

### Phase 0 — PC2 operator guard

For homelab/Hermes/PC2 work, observe the guard:

- PC2 is operator; PC1 is runtime authority.
- Do not alter PC1 runtime.
- Do not copy DSNs, tokens, cookies, or secrets.
- Do not open ports.
- Do not change provider/model/API.
- PostgreSQL read-only only; Qdrant staging only; Redis status only.

This carousel workflow normally edits only user-local skill/workbench/final asset files on PC2.

### Phase 1 — Strategy and copy

Use `brand-carousel-studio` and `carousel-copy-and-script`.

Gate before Image-2:

- Every slide has title, subtitle, purpose, and visual note.
- Caption is written.
- CTA is clear.
- Claims are safe or flagged.
- No slide has two competing ideas.
- Cover title is short and visually dominant.

No copy, no image generation.

### Phase 2 — Visual direction

Use `carousel-visual-direction`.

Gate:

- Master visual direction exists.
- Prompt exists for every slide.
- Each prompt says `SOMENTE a Página N`.
- Each prompt includes exact title/subtitle text.
- Each prompt includes continuity rules, safe area, negative constraints, and `aguarde eu escrever proximo`.
- Render spec dimensions match the run contract.

### Phase 3 — Browser selection and session guard

**Regra Chrome CDP vs BrowserOS vs Camofox para ChatGPT Plus:**

| Prioridade | Browser | Endpoint | Quando usar |
|------------|---------|----------|-------------|
| **1** | **BrowserOS VNC** (`Antigravity`) | `http://127.0.0.1:6080/vnc_lite.html` | Sessão real logada do usuário — **primeira escolha** quando o usuário diz "ja tem login persistido no VNC" |
| **2** | Chrome CDP (`127.0.0.1:9222`) | `browser_navigate` direto | Chrome real com sessão se CDP responder |
| **3** | Camofox Docker (`127.0.0.1:9377`) | REST API + VNC | Background tasks, macros — **não** para ChatGPT Plus se BrowserOS estiver disponível |

**BrowserOS/Antigravity** é o browser agentic instalado via `.deb` (`browseros` 146.0.7821.31). Roda como `/usr/share/antigravity/antigravity`, porta VNC `:6080`. Usa o mesmo profile do Chrome do usuário — sessão ChatGPT Plus já persistida. **Sem CDP exposto** — automação via VNC visual.

**Camofox Docker** tem `sessionKey` requerido para criar abas. Sessão `will-hermes-main` tem **conflito Instagram/ChatGPT** — clicar "Add files and more" redireciona para Instagram Direct. **Não usar** para ChatGPT Plus Image-2 quando BrowserOS VNC está disponível.

**Verificar login BrowserOS VNC:**
```bash
# BrowserOS VNC — testar se está acessível
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:6080/vnc_lite.html  # → 200 = OK

# Chrome CDP — verificar se está ativo e com sessão
curl -s http://127.0.0.1:9222/json/version | grep -q webkit && echo "CDP OK"
```

**Se não estiver logado:** abrir `http://127.0.0.1:6080/vnc_lite.html`, fazer login manual uma vez no ChatGPT, depois o estado persiste no profile do Chrome.

Gate:

- Browser is the existing Camofox/VNC session.
- ChatGPT Plus is logged in.
- Correct project/chat is selected or a new isolated chat is created.
- Image mode is active.
- Aspect ratio dropdown is set to the contract option before the first slide.

If aspect ratio cannot be verified, stop.

### Phase 4 — Generate slide by slide

Use `image2-sequential-slide-runner`.

Rules:

1. Send only slide 1 prompt.
2. Wait until the image is complete and controls are visible.
3. Run visual QA.
4. If `PASS`, download and validate the local file.
5. Only then send `proximo` or the next slide prompt.
6. Repeat until all slides pass.

Do not batch-generate the whole carousel unless the user explicitly overrides this gate.

### Phase 5 — Visual QA

Use `image2-slide-visual-qa` for each slide.

PASS requires:

- Correct page number/topic.
- Title/subtitle correct enough to publish.
- Portuguese spelling correct.
- Title hierarchy strong; subtitle thinner/lighter.
- Legible at thumbnail size.
- No text cropped.
- No visual drift from master direction.
- No cheap stock/template look.
- No repeated previous slide.
- Sensitive healthcare/hospital context is handled without fake guarantees or identifiable patients.
- **Dimensions match the run contract** — immediately after download, verify width × height. For 4:5 Instagram (1080×1350), reject any image whose dimensions are not close to 1080×1350 (±5px tolerance). Panoramic, square, or 3:4-only images that cannot be cropped to 4:5 cleanly are NEEDS_FIX or BLOCKED. This check must fire at download time, not after the full carousel is assembled.

If `NEEDS_FIX`, correct the current slide only. If `BLOCKED`, stop.

### Phase 6 — Real download

Use `chatgpt-image-real-download`.

Valid download means:

- Download comes from ChatGPT UI or browser-authenticated context.
- When you click the in-UI download button, the browser saves to the host's default Downloads folder (`/home/will/Downloads`) unless you explicitly move it elsewhere.
- Treat the file in Downloads as the real artifact; move/copy it to the campaign folder only after verifying it opens locally.
- Local file exists on disk after the browser download.
- Image opens locally.
- Dimensions match the contract.
- File size is plausible.
- The ledger records the local path, not a signed URL.

### Phase 7 — Clean export

Use `carousel-clean-final-export` and `carousel-quality-export`.

Final folder must contain exactly:

```text
slide_01.png
slide_02.png
slide_03.png
slide_04.png
slide_05.png
caption.txt
```

or the agreed slide count.

All working files stay in `/tmp/hermes-carousel-runs/<slug>/` or a brand-carousel-studio campaign folder, never mixed into the final Instagram folder.

## Ledger

Maintain:

`/tmp/hermes-carousel-runs/<slug>/slide-ledger.yaml`

Minimum:

```yaml
slides:
  - number: 1
    expected_title: ""
    expected_subtitle: ""
    prompt_sent: false
    generated: false
    visual_qa: PENDING
    corrections: []
    downloaded_file: null
    dimensions: null
    approved_at: null
```

Run:

```bash
python3 ~/.hermes/skills/social-media/chatgpt-plus-image2-carousel-studio/scripts/validate_slide_ledger.py /tmp/hermes-carousel-runs/<slug>/slide-ledger.yaml
```

## Final validation commands

```bash
python3 ~/.hermes/skills/social-media/chatgpt-plus-image2-carousel-studio/scripts/validate_local_image_exports.py /tmp/hermes-carousel-runs/<slug>/carousel-run-contract.yaml
python3 ~/.hermes/skills/social-media/chatgpt-plus-image2-carousel-studio/scripts/validate_final_clean_bundle.py /tmp/hermes-carousel-runs/<slug>/carousel-run-contract.yaml
```

If any validator fails, the carousel is not complete.

1. Starting Image-2 before finishing copy. Fix: block until all slide copy is complete.
2. Starting Image-2 in Camofox Docker session. Fix: use BrowserOS/Antigravity VNC at `http://127.0.0.1:6080/vnc_lite.html` for ChatGPT Plus — the Camofox Docker `will-hermes-main` session has Instagram cookies that cause session-guard redirect to Instagram Direct when you click "Add files and more" or "Create image" in ChatGPT. Camofox Docker sessions only work for unauthenticated or non-Image-2 operations.
3. Trying to create tabs without `sessionKey`. Fix: `POST /tabs` requires both `userId` AND `sessionKey`. The `sessionKey` must match a Camofox profile ID from `~/.camofox-docker/profiles/`. Example: `{"userId": "will-chatgpt-plus", "sessionKey": "f98e839", "url": "https://chatgpt.com"}` — `f98e839` is a valid profile ID.
4. Instagram redirect (session guard conflict). Fix: clear Instagram cookies from the Camofox profile storage, OR use BrowserOS VNC as the automated browser for ChatGPT Plus operations. The redirect happens because the Camofox Docker profile contains Instagram session cookies that trigger the session guard when interacting with the ChatGPT "Add files and more" dropdown.
14. Instagram redirect bug — Camofox Docker (`will-hermes-main`) conflita cookies Instagram/ChatGPT no mesmo storage. Clicar "Add files and more" → "More" ou "Create image" redireciona para Instagram Direct Messages. **Sintoma**: URL mostra `chatgpt.com/?mode=image` mas DOM real é Instagram. **Fix**: usar BrowserOS VNC (`http://127.0.0.1:6080`) para ChatGPT Plus ao invés de Camofox Docker. Session guard envenenado não tem cura via API — precisa usar browser diferente.
15. Camofox criar tab requer `sessionKey` — `POST /tabs` retorna `"userId and sessionKey required"`. Sessão `will-hermes-main` não tem `sessionKey` válido. Alternativa: usar BrowserOS VNC que não precisa de sessionKey para manipulação visual.

## Verification checklist

- [ ] Required skills loaded.
- [ ] Contract file exists and validator passes.
- [ ] Copy complete before Image-2.
- [ ] Visual direction and per-slide prompts complete.
- [ ] Camofox/VNC/ChatGPT Plus session verified.
- [ ] Aspect ratio selected and recorded.
- [ ] Each slide generated one at a time.
- [ ] Each slide has QA PASS before advancing.
- [ ] Each slide downloaded as a real local image.
- [ ] Export folder is clean.
- [ ] No paid API, local renderer, provider/model/API change, secrets, or signed URLs used.

## See also

- `references/camofox-tab-creation-sessionkey.md` — Camofox tab creation with `userId`+`sessionKey`, known profile IDs, Instagram redirect bug root cause and fixes (preferred path for ChatGPT Plus Image-2)
