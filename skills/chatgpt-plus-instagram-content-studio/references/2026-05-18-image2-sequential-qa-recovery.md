# Image-2 sequential carousel QA and recovery — 2026-05-18

Session context: Refrimix PMOC hospitalar carousel produced through persisted ChatGPT Plus web/VNC using the copy-first → Image-2 one-page-at-a-time workflow.

## Durable pattern

1. Build the full copy pack first: page role, exact title, exact subtitle/bullets, visual direction, and per-page Image-2 prompt.
2. Generate only one page at a time.
3. After each image, visually QA before sending `proximo`:
   - page number/role matches the plan;
   - exact title and subtitle/bullets are present;
   - Portuguese accents and wording are correct;
   - text hierarchy is readable: title bold/semibold, supporting copy light/medium;
   - no patients/faces/identifiable people when operating in hospital/clinic context;
   - premium editorial look, not generic stock/AI template.
4. Keep an external state ledger in Hermes/local notes. Do not rely on ChatGPT's web conversation state alone to remember which page is next.
5. If a page repeats or drifts, do not continue with plain `proximo`. Send a corrective regeneration prompt naming the failure and the exact next page.

## Corrective prompt pattern

Use this shape when ChatGPT/Image-2 repeats the previous slide or generates the wrong page:

```text
A imagem mais recente [repetiu a Página X / não correspondeu à Página Y].
Gere agora SOMENTE a Página Y do carrossel [tema] no formato obrigatório 4:5 / 1080x1350.
Texto exato na imagem: título "..."
Subtítulo/bullets exatos: "..."
Visual: [scene, palette, overlays, constraints].
Tipografia: título bold/semibold, subtítulo light, margens 90px.
Depois aguarde eu escrever `proximo`.
```

## Stuck generation recovery

If ChatGPT remains in `Thinking` after several minutes on a later image turn:

- Do not keep stacking `Enter`/duplicate messages in the same stuck turn.
- Try stop once and wait briefly.
- If still stuck, open a fresh ChatGPT chat and continue from the external state ledger with only the remaining page(s), not the whole old conversation.
- Preserve approved image IDs/URLs and QA notes before switching chats.

## PMOC hospitalar carousel lesson

In this session:

- Page 1 and 2 were approved on first generation.
- Page 3 initially drifted; regeneration with exact title + bullet list fixed it.
- Page 4 initially repeated Page 3; regeneration with explicit Page 4 title/subtitle and visual constraints fixed it.
- Page 5 got stuck in `Thinking`; best next step is a fresh chat with the external ledger and only the CTA page prompt.

## Approved QA gate wording

For each image, ask the visual QA to verify:

```text
Verifique se a imagem centralizada é a Página N. Leia título/subtítulo/bullets visíveis. A página deveria conter: [...]. Verifique estética premium, legibilidade, português correto, sem pessoas/pacientes identificáveis. Aprovar ou reprovar?
```
