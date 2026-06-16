# Reference: Story generation via ChatGPT Plus Image-2 (20/05/2026)

## O que foi gerado nesta sessão

- **3 Stories (9:16)** via ChatGPT Plus Image-2 + Camofox/VNC
- **5 Slides de carrossel (3:4 portrait → crop para 4:5)** no mesmo chat
- Chat URL: `https://chatgpt.com/c/6a0e1307-4238-83e9-b6a0-b110a93a1634`

## Padrão de geração que funcionou

### Stories (9:16)

1. Abrir novo chat no ChatGPT Plus (ou usar chat existente persistido)
2. Enviar prompt do Story 1
3. Aguardar ~60s (pensamento longo)
4. Visualizar imagem gerada
5. **Download:** abrir em fullscreen → `browser_vision` → cp do screenshot para `/home/will/Imagens/stories/jabN/storyN.png`
6. Repetir para Story 2 e 3

### Carrossel (3:4 portrait)

1. Enviar prompt com todos os 5 slides juntos
2. ChatGPT gera 8 imagens totais (3 stories anteriores + 5 slides novos)
3. Os slides carrossel ficam nos últimos grupos de botões com img aninhadas
4. Scroll até ver todos os botões `Generated image Generated image Generated image`
5. Click no grupo de botões para abrir o modal fullscreen
6. Dentro do modal, as imagens aparecem como `Image 1 of 8`, `Image 2 of 8`, etc.
7. Click na thumbnail correta para selecionar cada slide
8. **Download:** same pattern — `browser_vision` → cp screenshot

## Descoberta importante

O ChatGPT pode devolver **8 imagens** em uma única resposta quando você faz Stories + Carrossel no mesmo chat:
- 3 Story images (9:16)
- 5 Carousel slides (3:4 portrait)

Elas ficam em grupos separados de `Generated image Generated image Generated image` — às vezes 3 rows de 3 buttons cada. O modal fullscreen enumera todas como `Image 1 of 8`, `Image 2 of 8`, etc.

Para separar stories do carrossel:
- Stories anteriores estão nos primeiros grupos de botões (mais acima na conversa)
- Carrossel slides estão nos últimos grupos (mais recentes)

## Download via browser_vision (padrão que funcionou)

```bash
# Sempre que o download nativo não funcionar ou for lento:
cp ~/.hermes/browser_screenshots/browser_screenshot_<hash>.png /home/will/Imagens/stories/jab1/story1.png

# Verificar screenshots disponíveis
ls -la ~/.hermes/browser_screenshots/*.png | tail -10
```

Quando browser_vision roda, ele salva em `~/.hermes/browser_screenshots/browser_screenshot_<hash>.png`. O agent copia esse arquivo para o destino final.

## Checklist de download por slide

- [ ] browser_vision mostra análise da imagem
- [ ] screenshot salvo em `~/.hermes/browser_screenshots/`
- [ ] cp executado para destino final
- [ ] ls confirma arquivo no destino com tamanho > 0
- [ ] Dimensões verificadas (9:16 para stories, 3:4 para carousel)

## Problemas encontrados

### 403 em URLs assinadas
`curl`/`wget` contra URLs assinadas do ChatGPT retornam 403. O workaround é **sempre usar browser_vision + cp do screenshot**, nunca terminal para download.

### Sessão Camofox não responde
Se o browser_tab fica 404, fazer `browser_navigate` de volta para a URL do chat e continuar.

### Element ref instability
Depois de click no modal, os refs mudam. Sempre fazer `browser_snapshot` depois de abrir novo modal ou fechar dialog para obter refs atualizados.

## Arquivos gerados nesta sessão

| Arquivo | Tipo | Dimensões |
|---------|------|-----------|
| `/home/will/Imagens/stories/jab1/story1.png` | Story | ~1080×1920 |
| `/home/will/Imagens/stories/jab2/story2.png` | Story | ~1080×1920 |
| `/home/will/Imagens/stories/jab3/story3.png` | Story | ~1080×1920 |
| `/home/will/Imagens/carrocei/refrimix-right-hook/01.png` | Carrossel | ~1024×1365 (crop to 4:5) |
| `/home/will/Imagens/carrocei/refrimix-right-hook/02.png` | Carrossel | ~1024×1365 |
| `/home/will/Imagens/carrocei/refrimix-right-hook/03.png` | Carrossel | ~1024×1365 |
| `/home/will/Imagens/carrocei/refrimix-right-hook/04.png` | Carrossel | ~1024×1365 |
| `/home/will/Imagens/carrocei/refrimix-right-hook/05.png` | Carrossel | ~1024×1365 |

## Caption gerado

Ver `caption.txt` em `/home/will/Imagens/carrocei/refrimix-right-hook/`.