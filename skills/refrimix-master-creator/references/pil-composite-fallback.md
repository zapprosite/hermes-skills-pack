# PIL Composite Fallback — Reusable Pattern

## Contexto
ChatGPT Image-2 Save/Share bugado no ambiente Camofox. Download falha. Imagem gerada OK mas não pode ser baixada.

## Solução: PIL Composite puro

### Script disponível
```
/home/will/.hermes/scripts/refrimix/gerar_carrossel_projeto.py
```

Gera carrossel 5 slides 1080×1350 via PIL sem necessidade de baixar imagens do ChatGPT.

## Como adaptar para novo tema

1. Editar a lista `slides[]` no script — cada dict é um slide
2. Campos: `bg` ("cream"|"navy"), `title`, `subtitle` (opcional), `body`, `hook_color`, `cta` (bool)
3. Rodar: `python3 /home/will/.hermes/scripts/refrimix/gerar_carrossel_projeto.py`

## Dependências
```bash
pip install Pillow
# Fonts: sudo apt install fonts-montserrat fonts-dejavu
```

## Output
```
/home/will/Imagens/carrocei/[TEMA-DATA]/
├── slide_01_final.png
├── slide_02_final.png
├── slide_03_final.png
├── slide_04_final.png
└── slide_05_final.png
```

## Validação
Sempre rodar `mcp_minimax_search_understand_image` em slide 1 e slide 5 após gerar.
Verificar: texto sem corte, cores corretas, logo presente.

## Limitações
- Background: gradiente sólido (cream ou navy) — não foto luxo
- Will pode substituir backgrounds por fotos reais depois
- Prioridade: funcional > perfeito enquanto Flowery indisponível