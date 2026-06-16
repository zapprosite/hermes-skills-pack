---
name: chatgpt-plus-persistent-workbench
description: "Mantém sessão persistente do ChatGPT Plus como bancada de produção de conteúdo. #bancada-chatgpt"
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [social-media, chatgpt-plus, persistence, projects, gpts, images, canvas, research]
    related_skills: [chatgpt-plus-instagram-content-studio, carousel-content-strategy, instagram-content-strategy, instagram-competitor-research]
---

# ChatGPT Plus Persistent Workbench

## Overview

Use ChatGPT Plus as a persistent working environment, not as a one-off chat. The goal is to keep a logged-in workspace alive across sessions, load references once, study what consistently works, and turn those observations into reusable content systems.

This skill is for the workflow where ChatGPT Plus becomes the place to:
- compare references side by side;
- iterate on images one at a time;
- refine copy inside Projects and Canvas;
- test specialist GPTs for angles and structure;
- capture the logic behind what performed well;
- save the learned pattern back into Hermes artifacts.

The central idea: do not only produce content in ChatGPT Plus; use it to learn a durable pattern and then encode that pattern into local files, prompts, and skills.

## When to Use

Use this skill when you need to:
- work inside a logged-in ChatGPT Plus session that stays persistent across browser runs;
- study premium Instagram references and extract the logic behind them;
- build a repeatable content workflow from Projects, GPTs, Images, and Canvas;
- keep the same brand workspace alive for slow iteration;
- train a better prompt by observing repeated failures and successes;
- move premium creative work out of ad hoc prompting and into a reusable operating system.

Do not use this skill for:
- secrets, credentials, cookies, API keys, or private operational data;
- platform bypasses, automation that violates site rules, or engagement spam;
- replacing human review on legal, medical, financial, or safety-sensitive claims;
- generic chat tasks that do not benefit from persistence or reference-driven iteration.

## Session Setup

1. Confirm the target session is actually authenticated.
   - For ChatGPT Plus, check for the profile name, project/workspace indicator, or image-capable composer.
   - For Instagram research, check that the persistent Camofox/VNC session is already logged in before reviewing posts.
   - If the page still shows login/sign-up, stop and authenticate before continuing.
   - Do not build a workflow on a logged-out session.
   - **UserId para chatgpt.com:** use `will-chatgpt-plus` conforme `hermes-browser-routing`.

2. Keep the browser context stable.
   - Use a persistent browser profile when available.
   - Avoid switching accounts mid-stream.
   - Keep one session per brand or campaign when the work is repeatable.
   - Treat ChatGPT Plus and Instagram as separate persistent workspaces when both are part of the workflow.
   - Default session: `will-chatgpt-plus` com `sessionKey` nomeado por tarefa.

3. Import a reference board.
   - Import screenshots, benchmark posts, notes, and examples before prompting.
   - Label what is being studied: layout, hierarchy, tone, realism, luxury cues, CTA, or founder presence.
   - On the ChatGPT home screen, the dedicated `Create an image` button switches the composer into image mode before prompting.
   - In image mode, the box changes to `Describe or edit an image`; pressing Enter submits the image request.

4. Open a Project per theme.
   - Use one project for one brand, niche, or campaign thread.
   - Keep prompts, versions, and exports together.

See `references/camofox-browser-persistence.md` for the compact persistent-session pattern, separation between host browser and Hermes browser backend, and the non-obvious "clicked the URL in the wrong browser" pitfall.
See `references/chatgpt-plus-ui-map-2026-05.md` for the full May 2026 UI map — composer modes, aspect ratios, Settings tabs, Projects, Codex, and not-yet-explored areas.

## Learning Loop

1. Observe the reference set.
   - Ask what makes the reference feel premium.
   - Separate visual logic from surface style.
   - Record the repeated ingredients: framing, pacing, typography, materiality, contrast, subject matter, and tone.

2. Generate one artifact at a time.
   - Start with the first slide, first cover, or first concept only.
   - Do not batch the whole carousel or the whole sequence immediately.
   - Use the first result to calibrate the rest.

3. Review before expanding.
   - Compare the output with the strongest reference.
   - Identify the mismatch: too generic, too template-like, wrong lighting, wrong composition, wrong mood, or wrong brand signal.

4. Change one variable only.
   - Adjust one thing per iteration: angle, crop, negative space, realism, light, copy density, material cues, or architectural integration.
   - Avoid restarting from scratch unless the direction is fundamentally wrong.

5. Repeat until the pattern is obvious.
   - When the target is premium and hard to hit, run multiple iterations in the same visual lane.
   - Look for the repeated failure mode.
   - Capture what finally improves the result.

6. Translate the win into a system.
   - Save the best prompt.
   - Save the failed prompt and why it failed.
   - Save the reference board.
   - Save the visual rules that emerged.
   - Turn those notes into a reusable template or skill update.

## What to Capture

Always record:
- the reference used;
- the prompt used;
- which variable changed;
- what got better;
- what still looked wrong;
- the final pattern worth reusing.

Useful categories for notes:
- premium feel
- architecture/editorial feel
- founder authority
- visual realism
- visual noise
- CTA strength
- brand consistency
- willingness to save/share/DM

## Recommended Outputs

Save final artifacts locally under a durable folder, such as:
`/home/will/Imagens/carroceis/<campaign-slug>_<YYYY-MM-DD>/`

Keep these files when relevant:
- `carousel.md`
- `caption.txt`
- `slides.json`
- `prompts.txt`
- `reference-board/`
- `failure-notes.md`
- `workflow-checklist.md`
- `pattern-notes.md`

Export note for ChatGPT Images:
- the generated image is stored in the conversation as a real `<img>` element with an `alt` like `Generated image: ...`;
- the browser DOM exposes a signed `backend-api/estuary/content?...` URL in `img.src`;
- use that src as the export handle when you need to move the generated image into a local folder;
- verify the downloaded file by checking its path, size, and image dimensions after export.

When the user is asking for a finished carousel, optimize for a ready-to-deliver bundle and a short final handoff, not a long explanation.

## Copy and Visual Rules

- Prefer premium, editorial language over hype.
- Keep one idea per slide or one intent per prompt.
- Treat founder presence as a trust asset when the brand depends on authority.
- Use ChatGPT Projects for organization, GPTs for specialized thinking, Images for visual iteration, and Canvas for final text refinement.
- Use the model outputs as raw material, not final truth.

## Common Pitfalls

1. Treating ChatGPT Plus like a normal chat.
   - Fix: use Projects and a named workspace.

2. Jumping to batch generation.
   - Fix: validate one slide or one concept first.

3. Not logging the failure mode.
   - Fix: write down what was off and why.

4. Saving only the final result.
   - Fix: save the prompt, reference, and iteration lesson too.

5. Using a logged-out or unstable browser session.
   - Fix: verify the authenticated state before work begins.

6. Confusing content quality with a single lucky prompt.
   - Fix: derive the recurring logic behind the result.

## Verification Checklist

- [ ] ChatGPT Plus session is authenticated and persistent.
- [ ] Reference board was loaded before generating.
- [ ] Work was organized into a Project or equivalent workspace.
- [ ] One artifact was generated and reviewed before expanding.
- [ ] Only one variable changed per major iteration.
- [ ] The failure mode was written down.
- [ ] The winning pattern was distilled into a reusable note or prompt.
- [ ] Final assets were saved locally with a durable name.
- [ ] No secrets or private operational data were stored.
