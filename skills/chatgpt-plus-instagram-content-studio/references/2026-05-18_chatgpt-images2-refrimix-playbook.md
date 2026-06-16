# ChatGPT Images 2.0 / Image-2 playbook for Refrimix carousels

Captured: 2026-05-18, via persisted logged-in chatgpt.com session for RefriMix Tecnologia Plus.
Sources used: OpenAI Help Center article `Images in ChatGPT` (access via More > Images, direct chat prompts, editor/select tool, aspect ratio control, save/delete behavior) and a ChatGPT Plus web workbench run titled `Fluxo Carrossel Instagram`.

## Stable operating rule

Use ChatGPT Plus web as the visual lab and Hermes as the coordinator/archive. Do not use the local API for expensive creative exploration when the user asked for ChatGPT Plus/VNC workflow.

Golden rule for Refrimix:

> Image first as premium architecture. Text later as design. Never try to solve the whole carousel inside one image-generation prompt.

## Setup block for a persistent ChatGPT project/chat

Create or reuse a chat/project named `Estúdio Refrimix — Carrosséis Premium` and paste this context at the top:

```text
Você é meu diretor de arte premium para carrosséis Instagram da Refrimix Tecnologia.

Marca:
- HVAC premium
- conforto térmico
- automação
- ar-condicionado central
- VRF/VRV
- PMOC
- hospitais, clínicas, escritórios e residências de alto padrão
- público: arquitetos, engenheiros, construtoras, empresários e clientes exigentes

Estilo visual:
- arquitetura brasileira contemporânea
- interiores sofisticados
- fotografia editorial realista
- estética de revista de arquitetura
- tons off-white, cinza claro, grafite, azul petróleo e detalhes metálicos discretos
- luz natural suave
- teto limpo
- integração invisível ou quase invisível do HVAC
- nada com aparência genérica de banco de imagem
- nada de texto dentro da imagem, exceto quando eu pedir explicitamente

Regra operacional:
Gerar uma imagem por vez.
Depois de cada imagem, avaliar composição, realismo, espaço para texto, coerência com a marca e ausência de erros.
Só continuar para a próxima após aprovação.
```

## Image-by-image workflow

1. Define theme, audience, pain, promise, slide count, tone, CTA.
2. Write copy/page roles before image generation: cover, context, error/consequence, solution, CTA.
3. Generate the first image without text.
4. Approve or correct it before moving on.
5. For the next image, start with: `Create the next image for the same Refrimix premium editorial Instagram carousel...`
6. Preserve lighting, material palette, perspective, ceiling language and negative-space logic.
7. Add final text outside Images 2.0 in Canva/Figma/Photoshop or another layout tool.
8. Save winner prompt, failed prompts, failure reason and correction as a skill/reference update.

## 4:5 cover prompt template

```text
Create a premium vertical Instagram carousel cover image, 4:5 aspect ratio, 1080x1350.

Brand context:
Refrimix Tecnologia, a premium HVAC and thermal comfort company focused on high-end residential projects, architecture, automation, central air conditioning, VRF/VRV systems, PMOC, clinics, hospitals, offices, and luxury interiors.

Visual direction:
Editorial architecture magazine cover, realistic photographed Brazilian contemporary interior, calm luxury, high-end architectural composition, no generic stock-image look.

Scene:
A sophisticated interior that could belong to a luxury residence, premium office, clinic, or architecture portfolio. The HVAC integration must feel invisible or near-invisible, with a clean architectural ceiling, refined lighting design, and a strong sense of thermal comfort.

Composition:
Vertical 4:5 frame, strong asymmetrical architectural framing, generous negative space in the upper-left or upper-third area for headline placement, refined depth, clean lines, premium materials, polished plaster ceiling, natural stone, warm wood, soft daylight, subtle technical intelligence without visible equipment.

Color palette:
Off-white, warm gray, light concrete, graphite, petroleum blue accents, discreet metallic details.

Do not include:
No text inside the image. No logos. No UI overlays. No people posing. No visible air-conditioning equipment. No exaggerated ducts. No messy ceiling. No stock photo look. No cartoon style. No AI artifacts. No distorted architecture. No unreadable signs.

Quality:
Ultra-realistic editorial photography, premium architecture portfolio mood, high-end lighting, clean composition, realistic materials, professional interior photography.
```

## Panoramic carousel chunk prompt pattern

Define the full panorama first, then request one 4:5 chunk at a time. Do not ask for a 5-slide strip in one render.

```text
We are creating a premium panoramic Instagram carousel for Refrimix Tecnologia.

Final format:
A continuous wide editorial architectural scene divided into 5 vertical slides, each slide in 4:5 ratio, 1080x1350. Each slide must work individually but also feel part of the same panoramic visual story.

Brand:
Premium HVAC, thermal comfort, automation, central air conditioning, VRF/VRV, PMOC, high-end architecture, clinics, offices, hospitals, and luxury residences.

Panoramic visual concept:
A refined Brazilian contemporary interior with invisible HVAC integration, clean ceiling design, architectural intelligence, calm luxury, and strong comfort perception.

Style:
Editorial architecture magazine, realistic photography, premium materials, soft daylight, asymmetrical composition, generous negative space for future text, no text inside the image.

Important:
Generate only one chunk at a time. Do not generate all slides at once. Maintain continuity of lighting, material palette, perspective, and architectural language across all chunks.
```

Then use per-slide roles:

- Chunk 1 / cover: left side of the interior; strong beginning; right edge visually open; generous headline space.
- Chunk 2 / context: connect to chunk 1; show continuity and more of the interior; leave text space.
- Chunk 3 / risk/error: subtle planning-risk cue only; no ugly mess; premium and realistic.
- Chunk 4 / solution: mature architectural planning, seamless HVAC integration and comfort.
- Chunk 5 / CTA: right side; completion/approval feeling; left edge connects to chunk 4; large CTA space.

## Approval checklist

Approve only if:

1. It reads as realistic editorial photography.
2. It feels like premium Brazilian architecture, not generic stock.
3. The ceiling is clean and architectural.
4. HVAC is invisible or well integrated.
5. There is clean space for title/copy.
6. The image has depth and strong composition.
7. Colors fit Refrimix.
8. There is no text/logo/sign/random typography.
9. Equipment is not overly visible.
10. No perspective errors, crooked furniture, strange luminaires or fake materials.

Rule: if the image is 80% good, correct it; if the architecture was born wrong, regenerate from scratch.

## Failure corrections

Generic stock image:
```text
Make it less like a generic stock photo and more like a famous Brazilian architect’s editorial portfolio cover. Use stronger architectural framing, more negative space, fewer decorative objects, and a more intentional composition.
```

Visible HVAC equipment:
```text
Remove visible HVAC equipment. The air-conditioning system must be invisible or architecturally integrated through a clean ceiling design, with no exposed units, no wall split units, and no visible ducts.
```

Messy ceiling:
```text
Simplify the ceiling. Make it clean, premium, architectural, with subtle linear integration only. No messy ducts, no excessive lights, no technical clutter.
```

Artificial 3D render:
```text
Make it feel like a realistic professional interior photograph, not a 3D render. Add natural material imperfections, realistic daylight, subtle lens behavior, and believable architectural proportions.
```

No copy space:
```text
Recompose with generous negative space in the upper-left area and less visual noise. Keep the main architectural interest slightly off-center.
```

Too much decorative luxury:
```text
Reduce decorative furniture and luxury objects. Prioritize architecture, ceiling integration, spatial intelligence, clean materials, and calm premium atmosphere.
```

Pretty image but weak HVAC signal:
```text
Add subtle signs of thermal comfort and HVAC planning through clean ceiling integration, balanced daylight, refined airflow logic, and architectural calm. Do not show equipment.
```

Text appeared in image:
```text
Remove all text, signs, labels, symbols, UI elements, logos, and typography from the image. This must be a clean background image for later design.
```

## Learning log schema

For each carousel, save:

```text
NOME DO CARROSSEL:
OBJETIVO:
PÚBLICO:
PROMPT QUE FUNCIONOU:
PROMPTS QUE FALHARAM:
O QUE DEU ERRADO:
CORREÇÃO QUE FUNCIONOU:
PADRÃO NOVO PARA A SKILL:
DECISÃO FINAL: [usar como novo prompt base | guardar como variação | descartar]
```

## ChatGPT Images UI facts observed / verified

- The logged-in ChatGPT account was `RefriMix Tecnologia Plus`.
- The web session showed persistent history and existing Refrimix carousel chats.
- ChatGPT Help says Images can be opened from `More > Images` or by asking in chat.
- Images can create/edit images, use selection-based edits, and use aspect-ratio controls.
- Generated images are saved under the ChatGPT Images area; to delete an image, delete the conversation where it was created.
- Generated images can be copied/saved/shared from their image controls.
