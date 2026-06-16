# ChatGPT web image downloads when backend URLs are signed

Date learned: 2026-05-18
Applies to: ChatGPT Plus web / Images 2.0 / Image-2 production sessions, especially Instagram carousel work where generated images must be archived locally.

## Durable lesson

Images generated in ChatGPT web may appear in the DOM with backend URLs that are signed, session-bound, or otherwise not retrievable from a normal terminal HTTP client. Do not preserve or paste those URLs into notes; treat them as sensitive/transient and represent them as `[REDACTED]` if mentioned.

## Working pattern

1. Keep the logged-in browser session open on the generated image.
2. Identify the visible/generated image element in the page DOM.
3. Fetch the image from inside the browser session, not from the terminal, so the request uses the active authenticated browser context.
4. Convert the response to a Blob and trigger a download from the page.
5. Locate the downloaded file under the user's downloads directory and copy it into the campaign asset folder with a stable filename.
6. Verify the local file dimensions/type before approving it for downstream layout.

Example browser-console pattern, adapted per page structure:

```js
const imgs = [...document.querySelectorAll('img')]
  .filter(img => img.naturalWidth > 500 && img.naturalHeight > 500);
const img = imgs.at(-1);
const res = await fetch(img.src);
const blob = await res.blob();
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'cover_chatgpt_images2.png';
document.body.appendChild(a);
a.click();
a.remove();
URL.revokeObjectURL(url);
```

## Pitfalls

- Terminal-side `urllib`, `curl`, or `wget` may return 403 even when the image is visible in ChatGPT web. The fix is not to save the signed URL; the fix is to download via the authenticated browser context.
- Do not store signed backend URLs, tokens, cookies, or query strings in skills, notes, screenshots, reports, or final user messages.
- If the browser tool's first screenshot/vision pass does not show the image, scroll before rejecting it; generated images may be below the current viewport.

## Verification checklist

- Local file exists in the campaign directory.
- File command or equivalent reports an image format and expected dimensions.
- Visual QA is run on the local file, not only on the browser viewport.
- Final notes record the prompt, decision, dimensions, and local filename — not the backend URL.
