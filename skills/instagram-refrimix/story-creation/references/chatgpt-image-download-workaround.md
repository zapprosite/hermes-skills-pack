# Reference: ChatGPT Image Download Workaround (20/05/2026)

## Problema

O download nativo do ChatGPT Plus pode não funcionar via Camofox/VNC, ou o arquivo vai para uma pasta temporária inacessível. `curl`/`wget` contra URLs assinadas retornam **403 Forbidden**.

## Solução padrão: browser_vision + cp

Cada vez que `browser_vision` roda, ele salva um screenshot em:

```
~/.hermes/browser_screenshots/browser_screenshot_<hash>.png
```

O agent copia esse arquivo para o destino final.

### Passo a passo

1. Gerar imagem no ChatGPT Plus
2. Clicar na miniatura ou botão da imagem para abrir modal
3. `browser_vision` → análise + screenshot salvo
4. `terminal` → `cp ~/.hermes/browser_screenshots/browser_screenshot_<hash>.png <destino>`
5. `ls -la <destino>` para confirmar

### Como identificar o screenshot correto

```bash
ls -la ~/.hermes/browser_screenshots/*.png | tail -5
```

Os mais recentes têm timestamp da sessão atual.

## Cenários

### Story 9:16 — abrir em fullscreen antes de baixar

1. Clicar no botão da imagem (e.g. `Edit image`)
2. No modal fullscreen, verificar a imagem
3. `browser_vision` → cp para destino

### Carrossel 3:4 — navegar entre slides no modal

1. Os slides aparecem como `Image 1 of N`, `Image 2 of N` etc. no modal
2. Clicar na thumbnail correta para selecionar cada slide
3. `browser_vision` → cp para cada slide

### Grupo de imagens (carousel prompt gera 5 de uma vez)

Quando o prompt gera 5 slides em uma única resposta:
- Slides aparecem como múltiplos grupos de botões `Generated image Generated image Generated image`
- Cada grupo abre um modal diferente
- Dentro do modal, navegar com as setas ou thumbnails
- Cada slide fazer `browser_vision` + cp

## Extração de URL da imagem (alternativa para debug)

```javascript
// No browser_console:
document.querySelectorAll('img[alt*="Generated image"]').forEach((img, i) => {
  console.log(i, img.src, img.getBoundingClientRect());
});
```

Isso mostra src e posição de cada imagem gerada — útil quando o modal não está respondendo.

## Limitações

- O screenshot do `browser_vision` inclui a UI do ChatGPT ao redor — não é o arquivo raw
- Para crop/trim final, usar ferramenta externa (GIMP, ImageMagick, etc.)
- Se precisar do arquivo 100% limpo, o download nativo é preferível quando disponível

## Alternativa: download button direto

Quando o botão "Save" ou "Download" aparece no modal do ChatGPT:
- Clicar nele → arquivo vai para `/home/will/Downloads/` (host)
- Depois: `cp /home/will/Downloads/<arquivo> <destino>`
- Confirmar com `ls -la /home/will/Downloads/`