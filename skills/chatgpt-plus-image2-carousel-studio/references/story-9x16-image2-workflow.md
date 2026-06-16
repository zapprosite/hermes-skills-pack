# Story 9:16 via ChatGPT Image-2 — Workflow Separado

Stories usam 9:16 (1080×1920), não 4:5. Workflow separado do carrossel.

## Aspect Ratio — Instabilidade do Dropdown (2026-05-20 update)

⚠️ **Instabilidade observada:** O dropdown de aspect ratio pode fechar ao tentar selecionar dentro dele. Sintoma: ao clicar no dropdown ele abre mas ao tentar clicar na opção o dropdown colapsa.

**Workaround testado e confirmado:**
1. Clicar em "Create an image" (ícone de geração de imagem)
2. **ANTES de colar o prompt**: clicar no dropdown de aspect ratio e selecionar "Story 9:16"
3. **Manter o cursor no campo de texto** — não clicar em outra área
4. Colar o prompt (o prompt NÃO deve pedir aspect ratio — o dropdown já definiu)
5. Se o dropdown fechar durante a seleção, esperar 2s e tentar novamente — às vezes precisa de 2 tentativas

**Não fazer:** Não incluir "9:16 aspect ratio" ou "1080x1920 pixels" dentro do texto do prompt quando o dropdown já está definido — isso causa conflito e o ChatGPT às vezes ignora o dropdown.

## Workflow Completo (testado 2026-05-20)

### Abrir sessão
1. Camofox/VNC com ChatGPT Plus logado
2. Criar novo chat ou usar chat existente persistido
3. Clicar em "Create an image" (ícone ✏️)

### Selecionar ratio → prompt → gerar → baixar

```bash
# Padrao de download que funcionou:
# 1. browser_vision анализирует → screenshot salvo em ~/.hermes/browser_screenshots/
# 2. cp para destino final
cp ~/.hermes/browser_screenshots/browser_screenshot_<hash>.png /home/will/Imagens/stories/jab1/story1.png
```

### Download nativo também funciona

Quando o botão "Save" aparece no modal fullscreen:
1. Clicar em "Save" → arquivo vai para `/home/will/Downloads/`
2. `cp /home/will/Downloads/<file> <destino>`
3. `ls -la /home/will/Downloads/` para confirmar

### Session persistente — Stories + Carrossel no mesmo chat

Na mesma sessão do ChatGPT (同一 chat), você pode gerar:
- 3 Stories (9:16)
- 5 Slides de carrossel (3:4 portrait)

Total: 8 imagens na mesma conversa. ChatGPT gera todas na mesma resposta quando você faz prompt único para todos.

**Como separar stories vs carousel no chat:**
- Stories ficam nos primeiros grupos de botões `Generated image Generated image Generated image` (mais acima na conversa)
- Carrossel slides ficam nos últimos grupos de botões (mais recentes)

No modal fullscreen, todas aparecem numeradas: `Image 1 of 8`, `Image 2 of 8`, etc.

## Pasta de destino

```
/home/will/Imagens/stories/<story-slug>/
  story1.png   (ou story01.png)
  story2.png
  story3.png
  copy.txt
```

```
/home/will/Imagens/carrocei/<campaign-slug>/
  01.png
  02.png
  03.png
  04.png
  05.png
  caption.txt
```

## Prompts Story testados (Refrimix, 2026-05-20)

### Story 1 — Jab #1 (Educação)
```
Create an Instagram story image for a Brazilian HVAC/refrigeration company.
Design a clean, professional dark background (dark blue #1a2a4a) with a split
AC unit illustrated in modern minimalist style. Text overlay in white bold font:
'Você sabia que o ar-condicionado pode dividir seu ambiente em ZONAS de
temperatura?' Small technical icons showing temperature zones. Professional look.
```
*(sem mencionar 9:16 no prompt — dropdown define)*

### Story 2 — Jab #2 (Prova Social)
```
Create an Instagram story image for a Brazilian HVAC company. Show a professional
AC installation team in action — technicians installing a commercial split system
on a clean ceiling. Dark professional background with company branding visible.
Text overlay in white: 'Obra executada com precisão. Cliente satisfeito.' Team
working photo style, modern corporate.
```

### Story 3 — Jab #3 (Engajamento)
```
Create an Instagram story image for a Brazilian HVAC company. Design a
question/engagement style visual: dark background with gradient, large white
bold text: 'Qual foi o MAIOR erro que você já cometeu com ar-condicionado?'
Subtitle in Portuguese: 'Conta aqui nos comentários 👇' Engagement style with
comment bubble icon. Professional, clean.
```

## Copy para Stories (copy.txt)

Cada story precisa在旁边:
- Headline: 5-8 palavras, bold
- Body: 2-3 linhas curtas
- Nunca vender diretamente (é Jab)

## Erros comuns e fixes

| Erro | Causa | Fix |
|------|-------|-----|
| Imagem 16:9 em vez de 9:16 | Ratio não selecionado no dropdown | Selecionar Story 9:16 antes do prompt |
| Prompts longos com instrução de ratio | Conflito com dropdown | Prompt não menciona ratio — dropdown define |
| Download retorna 403 | `curl`/`wget` contra URL assinada | Sempre via `browser_vision` + cp, ou fetch+blob in-page |
| Dimensões erradas (ex: panoramic) | Ratio errado ou dropdown fechou | Re-selecionar Story 9:16 e regenerar |
| Tab 404 após scroll | Sessão Camofox desconfigurou | `browser_navigate` de volta para URL do chat |
| Element ref muda depois de click | Modal aberto alterou refs | Sempre fazer `browser_snapshot` depois de abrir modal |
| Screenshot não mostra imagem | UI do ChatGPT cobre a imagem | Abrir imagem em fullscreen antes de `browser_vision` |

## Sessão Camofox — browser_vision + cp (workaround padrão)

```bash
# Cada browser_vision salva screenshot em:
~/.hermes/browser_screenshots/browser_screenshot_<hash>.png

# Identificar o mais recente
ls -la ~/.hermes/browser_screenshots/*.png | tail -5

# Copiar para destino
cp ~/.hermes/browser_screenshots/browser_screenshot_<hash>.png <destino>

# Confirmar
ls -la <destino>
```

## Extração de URL via browser_console (para debug)

```javascript
// Encontrar todas as imagens geradas na página
document.querySelectorAll('img').forEach(img => {
  if (img.naturalWidth > 500) {
    console.log(img.alt || 'no-alt', img.naturalWidth + 'x' + img.naturalHeight, img.src.substring(0, 150));
  }
});
```

## Checkpoints salvos

Ver `/home/will/.hermes/checkpoints/jab-jab-hook-20260520.json` para estado completo da sessão.