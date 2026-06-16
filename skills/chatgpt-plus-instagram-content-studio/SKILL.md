---
name: chatgpt-plus-instagram-content-studio
references:
  - references/2026-05-18_dashboard-notes.md
description: "Gera copy e carrosséis para Instagram no ChatGPT Plus via Camofox VNC. #estudio-conteudo"
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [social-media, instagram, chatgpt-plus, gpts, projects, images, canvas]
    related_skills: [brand-carousel-studio, carousel-content-strategy, carousel-copy-and-script, carousel-visual-direction, humanizer]
---

# ChatGPT Plus Instagram Content Studio

## Overview

Use ChatGPT Plus as a creation workspace for Instagram content when the goal is to save Hermes API usage and move faster on copy, concepts, and visual drafts.

This workflow uses ChatGPT Projects to keep a brand workspace together, GPTs to generate specialist copy and angles, Images to prototype covers and visual references, and Canvas to refine the final text. The output should feel premium, editorial, and consistent with the Refrimix / architecture-driven positioning.

Reference support files:
- `references/2026-05-18_fluxo-refrimix-carrosseis-sequencial.md` — current best Refrimix workflow learned from the ChatGPT conversation `Fluxo Refrimix Carrosséis`: plan copy/title/subtitle for all 5 pages first, then generate Image-2 pages sequentially with `proximo`, waiting for completion and QA before advancing.
- `references/2026-05-18_image2-iterative-loop.md` — session-learned loop for slow Image2 iteration and approval pacing.
- `references/2026-05-18_chatgpt-images2-refrimix-playbook.md` — initial ChatGPT Images 2.0 / Image-2 Refrimix playbook: persistent logged-in chat setup, one-image-at-a-time workflow, cover and panorama prompts, approval checklist, failure corrections, and skill-learning log schema.
- `references/2026-05-18_chatgpt-signed-image-download.md` — browser-context download pattern for signed/session-bound ChatGPT generated image URLs; never preserve backend URLs.
- `../instagram-image2-carousel-prompt-engine/references/2026-05-18_image2-typography-photoshop-polish.md` — when the user explicitly wants text inside Image-2: short bold title + lighter subtitle prompt block, typography correction snippets, and Photoshop/design-tool final polish workflow.

## When to Use

Use this skill when you need to:
- turn public references into a premium Instagram carousel or story sequence;
- generate many copy variants, hooks, captions, and CTAs;
- compare specialist GPT outputs before finalizing;
- keep a reusable workspace for a brand or campaign;
- create content drafts in ChatGPT first, then save the final package locally.

Do not use this skill for:
- secrets, credentials, cookies, API keys, or private operational data;
- auto-posting, engagement automation, or platform bypasses;
- claims that need legal, medical, or regulated-domain review;
- replacing human review on factual or high-stakes content.

## Workflow

**Hardened Image-2 carousel gate:** when the user asks for final carousel images via ChatGPT Plus/Camofox/Image-2, load and follow `chatgpt-plus-image2-carousel-studio` before generating. That skill is the no-fallback production contract: copy first, visual direction second, Camofox/ChatGPT Plus third, one slide at a time, QA before `proximo`, real local download, and clean final export. Do not replace it with PIL, local renderers, screenshots, or paid API calls.

Reference update: for Image-2 carousel runs, see `references/2026-05-18-image2-sequential-qa-recovery.md` for the proven sequential QA/recovery pattern: keep an external page-state ledger, visually approve each page before `proximo`, use explicit corrective regeneration prompts when a slide repeats/drifts, and switch to a fresh chat if a later image remains stuck in `Thinking`.

1. Create or open a ChatGPT Project for the brand or campaign.
   - Keep one project per recurring content stream.
   - Store references, notes, uploaded images, and draft outputs in the same workspace.

2. Import reference imagery before prompting.
   - Save benchmark screenshots or downloaded reference images inside the project.
   - Use the reference set to anchor typography, rhythm, contrast, framing, and luxury cues.
   - Do not start image generation from a blank idea when a strong visual reference exists.

3. Use GPTs by specialty.
   - Copy GPT: generate hooks, opening lines, captions, CTAs, and alternate versions.
   - Strategy GPT: classify the angle as authority, proof, education, objection handling, or conversion.
   - Visual GPT: turn the idea into composition notes for a cover, carousel, or story.

4. Before using Images, finish the carousel brain first.
   - Define topic, audience, objective, page role, title, subtitle/bullets, CTA, caption and hashtags before generating any image.
   - For Refrimix, default to 5 pages: hook, belief shift, consequences, technical solution, premium CTA.
   - Do not start Image-2 with only a visual idea; each page needs its copy and function already locked.
   - The most common failure is generating beautiful architecture without knowing the title/subtitle/copy arc.

5. Use Images in ChatGPT as a paced sequential generator, not a one-shot batch.
   - Ask ChatGPT to generate images one page at a time.
   - Use a command pattern: `gere as imagens em sequência; eu vou falando proximo`.
   - **⚠️ TAMANHO OBRIGATÓRIO — selecionar ANTES da primeira imagem:**
     - Clique no botão **"Automático"** (dropdown de proporção) na barra inferior do ChatGPT.
     - Para carrossel Refrimix/marketing, selecione sempre o formato do contrato: **4:5 / 1080×1350**. Não use 3:4 neste workflow.
     - **NÃO use "Automático"**: gera resolução variável não-padronizada.
     - **NÃO use "Quadrado 1:1"**: perde o formato portrait que domina o feed mobile.
     - Via Camofox snapshot: achar o botão `"Choose image aspect ratio"` → clicar → encontrar `"Portrait"` ou `"Retrato"` na lista → clicar.
     - Via evaluate fallback: `[...document.querySelectorAll("span,div")].find(e=>e.textContent.trim()==="Portrait"||e.textContent.trim()==="Retrato")?.closest("button,li")?.click()`
   - Wait until the image appears and the Edit/Download controls are available before judging.
   - QA the page before typing `proximo`.
   - Type exactly `proximo` only after the current page is approved or corrected.
   - If the title/subtitle/typography is wrong, correct the current page before advancing.
   - Repeat until the whole set matches the premium reference.
   - For a difficult campaign, run 10 iterations across the same visual direction and learn the recurring failure modes before finalizing the pack.
   - Long VNC/Image-2 runs can hit Hermes's per-turn tool/API iteration budget (`agent.max_turns`, default 90; `goals.max_turns`, default 20 for `/goal`). Keep an external ledger (`notes.md` or `workflow_checklist.md`) after each slide, split the work into resumable turns before 80/90 iterations, and prefer direct browser JS extraction/download scripts for bulk download instead of spending one Hermes tool iteration per tiny UI action.

6. Use Canvas or equivalent for the final text pass.
   - Assemble the slide sequence.
   - Tighten hooks and subtitles.
   - Remove generic AI phrasing.
   - Align the CTA with the business goal.
   - If Image-2 rendered text inside images, inspect spelling and hierarchy at thumbnail size.

7. Treat ChatGPT Images as an approval loop, not blind automation.
   - Import the strongest benchmark/reference image into the project when available.
   - Generate page 1 first, then continue with `proximo` only after approval.
   - If the result misses the target, edit one variable at a time instead of restarting from scratch.
   - Keep the loop slow on purpose; no pressure, no next page until the current page is good enough.
   - Save the reference board and prompt packs alongside the campaign so future runs start from the learned standard.

8. Save the final package locally.
   - Store the approved carousel under:
     `/home/will/Imagens/carroceis/<campaign-slug>/` unless the user asks for a date-stamped folder.
   - For the final delivery folder, keep it clean by default:
     - exactly 5 final high-resolution PNG images (or the requested slide count)
     - exactly one `caption.txt` containing the ready-to-post responsive caption, CTA, and buyer-audience hashtags inline
     - no `carousel.md`, `slides.json`, `prompts.txt`, notes, checklists, reference boards, backups, or correction files in the final delivery folder unless the user explicitly asks for them
   - If operational notes, prompts, QA ledgers, or reference assets are needed, keep them outside the final delivery folder (for example under `/tmp/hermes-plan-enfemero/` or another workbench path).
   - When using ChatGPT Plus Images/Image-2, verify real local image export before finalizing: use the ChatGPT image download control when practical; if automation is required, extract the displayed generated image from the logged-in browser context and write it locally. The task is not complete until the files exist under `/home/will/Imagens/carroceis/<campaign-slug>/` and image dimensions/sizes have been checked.

9. Derive stories from the same carousel idea.
   - Convert the carousel into 3-5 story frames.
   - Keep the CTA simple: bio, WhatsApp, orçamento, ou resposta direta.
   - Aim for click behavior, not hard selling.

10. Prefer ChatGPT Plus for the visual prototype loop when the goal is premium creative iteration.
   - Use Hermes for coordination, saving, and systemization.
   - Use ChatGPT Plus Images for premium concept exploration and visual refinement.
   - Avoid defaulting to external providers when the workflow specifically benefits from native ChatGPT image iteration.

## Copy Rules

- Before image generation, complete the whole carousel copy arc: page titles, subtitles/bullets, CTA, caption and hashtags.
- Refrimix default structure is 5 pages: hook, belief shift, consequences, technical solution, premium CTA.
- Cover headline must be short, premium, and scannable.
- Each slide needs one clear job and one dominant message.
- Title should be the bold visual anchor; subtitle should be lighter, shorter, and supportive.
- Keep the tone editorial, technical, and human.
- Use proof, contrast, and specificity instead of hype.
- Match the CTA to the audience stage:
  - awareness: save or share
  - consideration: comment or DM
  - conversion: explicitly state the next action, e.g. “Agende uma reunião pelo link da BIO”; avoid a generic “Clique no link da bio” when the desired action is scheduling, orçamento, projeto, or análise técnica
- Avoid generic AI openings such as “desbloqueie”, “vamos explorar”, or “neste post”.

## Story Rules

- Stories are a conversion layer, not random posts.
- Use a three-step structure:
  - hook
  - proof or context
  - action
- Keep the language natural and premium.
- Use one clear action per story sequence.
- Point the viewer toward the bio, contact link, or direct message.

## Common Pitfalls

1. Using ChatGPT like a single generic chat.
   - Fix: separate Projects and GPTs by task.

2. Writing long, weak covers.
   - Fix: make the cover headline short and visual.

3. Letting GPT output become final without editing.
   - Fix: always pass the text through Canvas or a final human review.

4. Saving raw draft clutter instead of a clean package.
   - Fix: store the approved output in the local carousel folder.

5. Turning stories into sales spam.
   - Fix: use a soft premium CTA and make the story feel consultative.

6. Mixing regulated claims with marketing copy.
   - Fix: flag any claim that needs technical, legal, or safety review.

## Verification Checklist

- [ ] ChatGPT Project created or reused for the brand.
- [ ] GPT outputs were used for copy/angle exploration.
- [ ] Image or visual draft was created or referenced.
- [ ] Final text was refined in Canvas or equivalent.
- [ ] Carousel package saved under `/home/will/Imagens/carroceis/`.
- [ ] Proporção do contrato selecionada no dropdown do ChatGPT ANTES da primeira imagem: **4:5 / 1080×1350** para TODOS os carrosséis Refrimix/marketing deste workflow.
- [ ] The workflow used a one-image-at-a-time approval loop.
- [ ] The slow-iteration rule was followed when the reference level was hard to match.
- [ ] Story CTA points to a clear next action.
- [ ] No secrets, private data, or unsupported claims were saved.
