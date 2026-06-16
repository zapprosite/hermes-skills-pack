# ChatGPT Plus image download workflow

Use this when a generated image is visible in ChatGPT Plus/Camofox and you need a local copy on disk.

Observed working path:
1. Inspect the generated image element in the page context and extract its `src`.
2. Prefer in-page `fetch(src, { credentials: 'include' })` over terminal `curl`.
   - Direct `curl` against the signed `backend-api/estuary/content` URL may return 403.
3. Convert the response to a `Blob` and trigger a browser download:
   - `const blob = await (await fetch(src, { credentials: 'include' })).blob()`
   - create an `<a>` element, set `href = URL.createObjectURL(blob)`, set `download`, click it.
4. If you need a deterministic file on the host, decode the blob/data URL outside the page only after you have the bytes from the browser context. If you use the browser download button, the file lands in the host's default Downloads folder (for this machine, `/home/will/Downloads`) unless you move it afterward.

Pitfalls:
- Signed image URLs are short-lived; do the download immediately after generation.
- If `browser_cdp` cookie access is awkward, `document.cookie` from `browser_console` is usually enough for diagnosis, but the image download itself should stay in-page.
- If the page is still thinking/generating, wait for the rendered image to appear before extracting `src`.

Verification:
- Confirm the saved file is a PNG and has the expected dimensions (the test image here was 1122x1402).
- Save to a user-visible path such as `/home/will/Desktop/<name>.png`.
