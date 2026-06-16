# ChatGPT Image Download — Fluxo Confirmado

## Problema

O ChatGPT Plus Image-2 não baixa automaticamente quando se clica "Save" na dialog de imagem. O arquivo pode ir para pasta padrão do navegador (Downloads) mas em ambiente Hermes/VNC isso é imprevisível. Técnicas que falharam:

- `urllib` direto no URL `estuary/content` → 403 Forbidden
- Clique em "Save" na dialog → não reliable no ambiente
- Browser redirect para Instagram durante navegação → sessão perdida

## Técnica Confirmada (Captura de Tela → Clipboard → PIL)

O fluxo mais confiable é usar o browser screenshot como source para o PIL composite:

### Passo a passo:

1. **Gerar imagem no ChatGPT** com Portrait 3:4
2. **Clicar na imagem** para abrir dialog fullscreen
3. **Trocar aspect ratio** para 3:4 (se necessário)
4. **Capturar screenshot do browser** via `browser_vision(question="...")` ou
   `browser_snapshot()` para obter os refs
5. **Usar `browser_console`** para extrair URLs diretas das imagens:

```javascript
// No browser console (via browser_console tool):
(() => {
  const imgs = document.querySelectorAll('img[src*="oaidalpro"], img[src*="estuary"]');
  return Array.from(imgs).map(img => ({
    src: img.src.substring(0, 400),
    w: img.naturalWidth,
    h: img.naturalHeight
  }));
})()
```

**Resultado típico:**
```json
[
  {"src": "https://chatgpt.com/backend-api/estuary/content?id=file_00000000f92871f9b817fa240167bec2&ts=494472&p=fs&cid=1&sig=...", "w": 1086, "h": 1448},
  {"src": "https://chatgpt.com/backend-api/estuary/content?id=file_00000000ef64720eb313a35b2b692891&ts=494472&p=fs&cid=1&sig=...", "w": 1536, "h": 1024}
]
```

6. **Inspecionar dimensões** — 1086x1448 = 3:4 (carrossel), 1536x1024 = 3:2 ( landscape)

## Estratégia Alternativa: PIL Base + Crop

Se a imagem baixou em formato diferente do esperado (ex: 3:4 em vez de 4:5):

```python
from PIL import Image
img = Image.open("/home/will/Downloads/carousel-projeto-ac-slide1.png")
# Crop para 4:5 (1080x1350) a partir do centro
w, h = img.size
target_ratio = 1080/1350
current_ratio = w/h
if current_ratio > target_ratio:
    # Mais largo que 4:5 — cortar laterais
    new_w = int(h * target_ratio)
    left = (w - new_w) // 2
    img = img.crop((left, 0, left + new_w, h))
img = img.resize((1080, 1350), Image.LANCZOS)
img.save(output_path)
```

## PITFALL: Instagram Captura Browser

⚠️ Ao navegar entre abas/janelas, o browser pode redirect para Instagram (sessão ativa no Instagram). Sempre verificar `window.location.href` via `browser_console` antes de assumir que está no ChatGPT.

```python
# Verificar sessão ativa:
location = browser_console(expression="window.location.href")
# Se instagram.com — voltar para chatgpt.com imediatamente
```

## PITFALL: SessionKey Camofox

O Camofox tem `user_id` e `sessionKey` isolados. Se usar browser_native junto com Camofox, pode haver conflito de cookies/sessão. Preferir usar APENAS browser_native (ferramenta nativa Hermes) ou APENAS Camofox — nunca os dois juntos na mesma sessão.

## Dimensões de Referência

| Aspect ratio | Dimensões | ChatGPT | Uso |
|---|---|---|---|
| 4:5 | 1080×1350 | Portrait 3:4 → crop | Carrossel |
| 9:16 | 1080×1920 | Portrait 9:16 | Stories |
| 1:1 | 1080×1080 | Square | Post quadrado |
| 3:4 | 1024×1365 | Portrait 3:4 (nativo) | Fonte original |
| 16:9 | 1920×1080 | Widescreen | Reels/YouTube |