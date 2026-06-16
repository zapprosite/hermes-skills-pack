# ChatGPT Plus VNC image export notes

Session note for working with a logged-in ChatGPT Plus workspace over VNC.

## Observed export pattern
- Generated images usually appear in the DOM as `<img>` elements with `alt` like `Generated image: ...`.
- The corresponding `src` is typically a signed ChatGPT asset URL under `chatgpt.com/backend-api/estuary/content?...`.
- Do not assume the visible conversation bubble is the only source of truth; inspect the DOM for the actual generated-image entries.

## Practical export fallback
- If direct navigation or programmatic fetch of the signed asset URL fails, open the image asset in the browser and capture the raw image page/screenshot.
- Treat those captures as the export source of record when direct binary download is unstable.
- Keep all campaign work in a dated local folder under `/home/will/Imagens/carroceis/<project>_<YYYY-MM-DD>/`.

## Verification rules
- Never claim a full set of images is finished until the DOM confirms every intended `Generated image:` entry.
- Before announcing delivery, verify the local files exist and have non-trivial byte sizes.
- If a reference post turns out to be a single image instead of a carousel, correct that assumption immediately to avoid false positives.
