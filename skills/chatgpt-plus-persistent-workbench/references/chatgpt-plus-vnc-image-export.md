# ChatGPT Plus VNC image-export notes

Session-derived workflow notes for generating Instagram carousels inside the persisted ChatGPT Plus VNC session.

## What was confirmed
- Generated images appear in the DOM as `<img>` elements with `alt` values like `Generated image: ...`.
- The matching `src` is a signed ChatGPT backend URL (`chatgpt.com/backend-api/estuary/content?...`).
- That signed `src` is the traceable origin for the generated asset; use it to identify the exact image before any export attempt.

## Reliable workflow
1. Stay inside the persisted ChatGPT Plus workspace.
2. Generate one slide/image at a time instead of assuming a batch already exists.
3. After each generation, inspect the DOM for the newest `Generated image:` alt text.
4. Verify the image identity before moving to the next slide.
5. Treat export as a separate step from generation; generation success does not imply the file already exists locally.

## Pitfall to avoid
- Do not assume a reference Instagram post is itself a multi-slide carousel. Confirm whether the source is a single post, a gallery, or a true carousel before mirroring the structure.

## Buyer-first content direction used in this session
- Focus the visual brief and captions on final buyers, not installers.
- Prefer phrases around project, comfort, high-end residence, office, clinic, restaurant, condo, and integrated climatization.
- Avoid installer-centric keywords unless the user explicitly wants technical audience targeting.

## Session artifacts
- Generated images observed in the workspace included variants such as:
  - `Generated image: Serene minimalist living room with greenery`
  - `Generated image: Modern minimalist living room with greenery`
- Local package output was organized under a dated folder in `/home/will/Imagens/carroceis/`.
