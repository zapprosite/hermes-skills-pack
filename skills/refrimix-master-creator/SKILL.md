---
name: refrimix-master-creator
description: "Orchestrador TOP 1 — gera carrossel 5 imagens + legenda ou 5 stories conectados via ChatGPT Image-2 + PIL composite. Loop until OK. Versão 2.1.0 — consolidado, references migradas, skill consolidation documentada."
version: 2.1.0
author: Jarvis (Hermes Agent)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [refrimix, instagram, carousel, story, top1, chatgpt-image2]
    related_skills: [refrimix-instagram-kit]
---

# REFRIMIX Master Creator — TOP 1 Instagram Skills v2.0.0

## REGRA DE OURO (OBRIGATÓRIO ANTES DE USAR)
Ler SEMPRE: `/home/will/Imagens/REFRIMIX-Instagram-Kit-2026-05/.rules`

---

## COMANDO DO USUÁRIO

```
gerar carousel [tema]
gerar stories [tema]
```

---

## IDENTIDADE VISUAL EXATA (confirmada via multimodal 2026-05-21)

### Cores do Logo (NUNCA mudar)
| Elemento | HEX | RGB |
|----------|-----|-----|
| "REFRIMIX" + ícone lado esquerdo | `#003359` | (0, 51, 89) |
| "TECNOLOGIA" + ícone lado direito | `#31638D` | (49, 99, 141) |

### Paleta Expandida (do .rules)
```
Navy:        #002E51  (logo, títulos, CTA)
Cream:       #F5F0E8  (background principal)
Gold:        #C9A96E  (acentos — 5-10% do layout)
Steel:       #8B9A9E  (subtítulos, texto secundário)
White:       #FFFFFF  (contraste, texto sobre navy)
```

### Tipografia (OBRIGATÓRIO — usar fontes reais, não fallback)
| Uso | Fonte | Peso | Tamanho |
|-----|-------|------|---------|
| Título | Montserrat Black | 900 | 90-120px |
| Subtítulo | Montserrat Light | 300 | 40-50px |
| Corpo | Source Sans 3 / Work Sans | Regular | 24-32px |

**Fonts verificadas:**
```bash
ls /usr/share/fonts/truetype/montserrat/Montserrat-*.ttf 2>/dev/null || echo "NOT FOUND"
ls /usr/share/fonts/opentype/montserrat/Montserrat-*.otf 2>/dev/null || echo "NOT FOUND"
```

**Se Montserrat não instalada:**
```bash
sudo apt install fonts-montserrat
```

**Fallback SE Montserrat ausente:** NUNCA usar DejaVu. Avisar usuário para instalar fonts-montserrat.

### Logo Real (OBRIGATÓRIO — nunca inventar)
```
Logo: /home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png
```
**ATENÇÃO:** O arquivo é `.png`, não `.jpeg`. Usar sempre como overlay PIL, nunca deixar ChatGPT inventar.

---

## BENCHMARK TOP 1 (OBRIGATÓRIO — comparar após cada slide/story)

**Referência:** `/home/will/Downloads/ChatGPT Image 21 de mai. de 2026, 09_27_08.png`

### O que faz ser TOP 1
- Background: foto real arquitetura luxo (living room, mármore, móveis design)
- Layout: texto à ESQUERDA, ancorado por linha vertical fina (gold 1px) como "spine"
- Hierarquia: Hook top → descrição → value proposition bottom
- Negative space: generoso, cream domina
- Leading lines: da arquitetura guia o olhar para o produto
- Logo: bottom-right, sutil, peso airy que combina com body copy
- Cores: navy headline, cream background, earth tones na foto
- Body copy: light weight com letter-spacing (kerning) largo — elegante e sofisticado

### Checklist QA (após cada slide/story)
```
[ ] Logo REFRIMIX real presente (não inventado)
[ ] Zero links/URLs/QR codes
[ ] Max 3 cores (navy #002E51 + cream #F5F0E8 + gold #C9A96E)
[ ] Título navy bold, subtítulo steel ou soft tone
[ ] Separador gold FINO (1-2px)
[ ] Narrativa conecta com próximo slide/story
[ ] Estilo consistente com os outros 4
[ ] Linha vertical gold à esquerda como âncora (estilo benchmark)
[ ] Typography: título bold ≠ subtítulo light (peso diferente)
```

---

## ANTI-SLOP RULES (do .rules)

❌ **Nunca:** stunning, incredible, epic, masterpiece, gorgeous, ultra-detailed cinematic masterpiece
✅ **Sempre:** soft overcast light from left, matte finish, navy gradient, 50mm feel, shallow DOF

❌ **Nunca:** minimalist luxury premium design (vago)
✅ **Sempre:** cream background, heavy black condensed sans, asymmetrical type block, generous negative space

❌ **Nunca:** beautiful modern architecture (genérico)
✅ **Sempre:** white concrete facade, floor-to-ceiling glass, deep overhanging slab, soft morning light from east

---

## ASPECT RATIO — ATENÇÃO CRÍTICA (prova de buraco)

ChatGPT Plus Interface não tem opção 4:5. O mais próximo é Portrait 3:4 (ratio 3:4, aproximadamente 1024×1365). Para obter 4:5 Instagram (1080×1350), gerar em Portrait 3:4 e fazer crop externo para 4:5.

| Tipo | Dimensões | ChatGPT opção | Instagram padrão |
|------|-----------|---------------|-----------------|
| Carrossel | 1080×1350 (4:5) | Portrait 3:4 → crop para 4:5 | 4:5 |
| Story | 1080×1920 (9:16) | Portrait 9:16 | 9:16 |

---

## COPY RESEARCH (dados HVAC)

| Tema | Dados |
|------|-------|
| PMOC | Lei 13.589/2018, multas R$2k-1.5M, 180 dias |
| CO2 | 1000ppm=cefaleia, 2000ppm=sonolência, 5000ppm=risco vida |
| Estadio | 50k pessoas, CO2 nas alturas, ar viciado |
| Manutenção | Filtro sujo=ácaros, 3 meses sem troca |
| Projeto | Carga térmica, PMOC, renovação de ar |
| Padrão | Qualidade premium, diferenciação, investimento |

### Valvula 4 Vias (dado técnico)
Inverte ciclo refrigerante (não compressor). Tecnologia inverter=velocidade compressor (economia). Válvula 4 vias=mudar quente/frio. Erro comum: brasileiro associa "inverter" a quente/frio — é a válvula que faz isso, não a tecnologia.

---

## PIPELINE CARROSSEL (5 slides — 4:5)

### Sequência narrativa JAB-JAB-JAB RIGHT HOOK
| Slide | Função | Copy |
|-------|--------|------|
| 1 | HOOK | "Você sabia que [fato surpreendente]?" |
| 2 | PROBLEMA | "[Dado técnico] — isso é mais comum do que parece" |
| 3 | REVELAÇÃO | "O verdadeiro problema: [expandir]" |
| 4 | PROVA | "[Solução/dado] — é assim que funciona" |
| 5 | RIGHT HOOK | "[Insight de marca] — você está fazendo isso?" |

### Phase 1: Copy Research
1. Web search: dados técnicos relevantes ao tema
2. Gerar caption com estrutura jab-jab-jab right hook
3. Caption para carrossel (não para cada imagem — é legenda do post)

### Phase 2: Generate 5 Images (ChatGPT Image-2 via Camofox)

**GERAR UMA POR VEZ, COM QA APÓS CADA UMA.**

**Prompt base (COPIAR E VARIAR SOMENTE "Subject"):**

```
[ANEXAR LOGO: /home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png]

Create a premium architectural photography for Instagram carousel slide N of 5 (portrait 3:4 aspect ratio — will crop to 4:5 for Instagram).

Theme: [SLIDE N — THEME NAME]
Subject: [DESCRIBE SPECIFIC ROOM/ENVIRONMENT matching slide N topic — same visual style as slides 1-5 — examples: "light-filled modern living room with white marble coffee table and curved designer sofa", "minimalist hotel lobby with floor-to-ceiling glass windows and concrete accent wall", "upscale open-plan kitchen with hidden lighting under cabinets and marble countertops"]

Style: Netflix luxury house — cinematic contrast, Adobe Photoshop-level shadows, 50mm lens feel, shallow depth of field, soft overcast light from left. Clean, minimalist, high-end.

Colors: Warm neutral palette — cream walls #F5F0E8, gray marble, dark charcoal accents, bronze/gold metallic highlights. NO bright saturated colors.

Composition: Generous negative space on LEFT side (40% of frame) for text overlay. Camera angle: eye-level, slightly elevated. Strong leading lines from architecture (ceiling air vent, floor line, cabinet edges) guide the eye toward the focal point.

Technical: architectural photography, 8K resolution, natural materials (marble, wood, fabric, concrete), soft shadows, warm color grading, no people, no text, no watermark, no logo.

Constraints: no generic AI look, no cheap templates, no clutter, no watermarks.
```

**CRÍTICO:** Os 5 slides DEVEM manter estilo visual IDÊNTICO — variar SOMENTE o "Subject". Same lighting, same color grading, same composition.

### Phase 3: PIL Composite

Para cada slide (1-5):
1. Background: imagem baixada do ChatGPT Image-2 (1080×1350 após crop de 3:4)
2. Texto: Montserrat Black título, Light subtítulo, gold separator (1-2px)
3. Linha vertical gold (1px) à esquerda como âncora (estilo benchmark)
4. Logo: REFRIMIX real bottom-right (180×90px)
5. Output: `slide-{N}.png` (1080×1350px)

**FONTES CONFIRMADAS:**
```
Montserrat-Black.otf: /usr/share/fonts/opentype/montserrat/Montserrat-Black.otf
Montserrat-Light.ttf: /usr/share/fonts/truetype/montserrat/Montserrat-Light.ttf
Logo: /home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png  ← .png, não .jpeg
Benchmark: /home/will/Downloads/ChatGPT Image 21 de mai. de 2026, 09_27_08.png
```

### Phase 4: QA (após cada imagem)
Usar `mcp_minimax_search_understand_image` para comparar cada slide com o benchmark.
Se QA fail: apply corrective prompt → regenerate → re-QA (até 3x).

### Phase 5: Legenda (Caption)
Gerar caption completo para o post com estrutura jab-jab-jab right hook.

### Phase 6: Output
```
/home/will/Imagens/carrocei/[TEMA-DATA]/
├── slide-01_final.png
├── slide-02_final.png
├── slide-03_final.png
├── slide-04_final.png
├── slide-05_final.png
└── caption.md
```

---

## PIPELINE STORIES (5 stories — 9:16)

### Sequência narrativa progressiva
| Story | Função | Copy |
|-------|--------|------|
| 1 | HOOK | "Você chega em casa e parece que entrou numa sauna." |
| 2 | PROBLEMA | "Conta de luz alta. Conforto zero." |
| 3 | SOLUÇÃO | "A Refrimix faz em 24h o que você tentou em 3 anos." |
| 4 | PROVA SOCIAL | "+200 famílias atendidas. Zero reclamações." |
| 5 | CTA | "Vagas limitadas. WhatsApp no link da bio." |

### Phase 1: Copy Research
1. Web search: dados técnicos relevantes ao tema
2. Gerar copy para 5 stories com estrutura narrativa progressiva

### Phase 2: Generate 5 Backgrounds (ChatGPT Image-2 via Camofox)

**GERAR UMA POR VEZ, COM QA APÓS CADA UMA.**

**Prompt base (COPIAR E VARIAR SOMENTE "Subject"):**

```
[ANEXAR LOGO: /home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png]

Create a premium architectural photography for Instagram story background (portrait 9:16 aspect ratio, 1080x1920px).

Theme: [STORY N — THEME NAME]
Subject: [DESCRIBE SPECIFIC LUXURY ENVIRONMENT matching the story — same visual style as stories 1-5 — examples: "light-filled modern living room with white marble coffee table and curved sofa", "minimalist hotel lobby with floor-to-ceiling glass and concrete accent wall", "upscale dental office waiting area with wood paneling and designer furniture"]

Style: Netflix luxury house — cinematic contrast, Adobe Photoshop-level shadows, 50mm lens feel, shallow depth of field, soft overcast light from left. Clean, minimalist, high-end.

Colors: Warm neutral palette — cream walls #F5F0E8, gray marble, dark charcoal accents, bronze/gold metallic highlights. NO bright saturated colors.

Composition: Generous negative space on left side (40% of frame) for text overlay area. Camera angle: eye-level, slightly elevated. Leading lines from architecture guide the eye.

Technical: architectural photography, 8K resolution, natural materials (marble, wood, fabric, concrete), soft shadows, warm color grading, no people, no text, no watermark, no logo.

Constraints: no generic AI look, no cheap templates, no clutter, no watermarks.
```

**CRÍTICO:** Os 5 backgrounds DEVEM manter estilo visual IDÊNTICO — variar SOMENTE o "Subject". Same lighting, same color grading, same composition.

### Phase 3: PIL Composite

Para cada story (1-5):
1. Background: imagem baixada do ChatGPT Image-2 (1080×1920)
2. Texto: Montserrat Black título, Light subtítulo, gold separator
3. Linha vertical gold (1px) à esquerda como âncora (estilo benchmark)
4. Logo: REFRIMIX real bottom-right (180×90px)
5. Output: `story-{N}.png` (1080×1920px)

### Phase 4: QA (após cada imagem)
Usar `mcp_minimax_search_understand_image` para comparar cada story com o benchmark.
Se QA fail: apply corrective prompt → regenerate → re-QA (até 3x).

### Phase 5: Output
```
/home/will/Imagens/stories/[TEMA-DATA]/
├── story-01.png
├── story-02.png
├── story-03.png
├── story-04.png
├── story-05.png
└── copy.md
```

---

## REGRAS DE CONEXÃO (CRÍTICO para TOP 1)

1. **Mesmo prompt base** — variação só em "Subject", não em "Style/Colors/Technical"
2. **Texto posicionado no MESMO lugar** em todos os 5 — hierarquia visual consistente
3. **Mesma paleta** — navy/cream/gold em todos
4. **Mesma tipografia** — Montserrat Black/Light em todos
5. **Narrativa progressiva** — slide/story N faz sentido depois de N-1
6. **Linha vertical gold** como âncora à esquerda (estilo benchmark)

---

## LOOP UNTIL OK

```
for attempt in range(1, 4):
    generate_image()
    qa_result = qa_benchmark_check()
    if qa_result.passed:
        composite()
        save()
        break
    else:
        apply_corrective_prompt()
        attempt += 1
if attempt > 3:
    FAIL — "não atingiu qualidade após 3 tentativas"
```

---

## REGRAS DE JULGAMENTO (QA mandatory para ambos)

Executar após cada imagem gerada. Falha em qualquer item = regenerate.

1. ✅ **Logo real** — usar `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png`
2. ✅ **Copy conexão** — narrativa sequencial (não slides isolados)
3. ✅ **Engajamento** — copy gera ação (pergunta, reflexão)
4. ✅ **Qualidade benchmark** — comparável ao reference image
5. ✅ **Max 3 cores** — navy/cream/gold/steel
6. ✅ **Zero links/URLs/QR** — nenhuma imagem
7. ✅ **Formato** — carrossel 4:5 (1080×1350), stories 9:16 (1080×1920)
8. ✅ **Tipografia** — Montserrat Black título, Light subtítulo

---

## TIMER ESTIMATED

| Phase | Tempo estimado |
|-------|----------------|
| Copy research | 30s |
| Generate image (1x) | 60-90s |
| PIL composite (1x) | 10s |
| QA (1x) | 15s |
| Retry (se necessário) | +90s por tentativa |
| Legenda | 20s |
| **Total 5 slides** | ~8-12 min |
| **Total 5 stories** | ~25-40 min |

---

## FONTES CONFIRMADAS

```
Montserrat-Black.otf: /usr/share/fonts/opentype/montserrat/Montserrat-Black.otf
Montserrat-Light.ttf: /usr/share/fonts/truetype/montserrat/Montserrat-Light.ttf
Logo: /home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png  ← .png, não .jpeg
Benchmark: /home/will/Downloads/ChatGPT Image 21 de mai. de 2026, 09_27_08.png
```

---

## OUTPUT DIRECTORIES

```
/home/will/Imagens/carrocei/[TEMA-DATA]/    ← carrossel 5 slides (1080x1350)
/home/will/Imagens/01-stories/[TEMA-DATA]/ ← stories 5 units (1080x1920)
```

NOTE: A pasta `01-stories` é a pasta real de stories (não `stories/`). Criar subdiretório `[TEMA-DATA]` dentro de `01-stories` se necessário. Database do kit: `/home/will/Imagens/REFRIMIX-Instagram-Kit-2026-05/banco-de-dados/refrimix_content.db`

---

## CAMOFOX / CHATGPT PLUS — FLUXO OPERACIONAL

O fluxo `mcp_browseros_*` apresenta instabilidade com o endpoint do ChatGPT. Em caso de falha:

1. Usar `browser_navigate` (ferramenta nativa do Hermes) para abrir ChatGPT
2. Usar `browser_type` + `browser_press(Enter)` para enviar prompt
3. NÃO usar `mcp_browseros_*` em paralelo ou logo após — conflita

### Passo a passo confirmado:
1. `browser_navigate` → `https://chatgpt.com`
2. Clicar botão "Create an image" (e23 no snapshot) OU digitar "Create an image" + Enter
3. Prompt vai para área de chat
4. ChatGPT responde pedindo tema + formato
5. Digitar o prompt completo (mastigado, benchmarks)
6. Aguardar botão "Generated image" aparecer
7. Clicar para expandir → dropdown 3:4 → Save

### Aspect ratio — ATENÇÃO CRÍTICA (prova de buraco)
ChatGPT Plus Interface não tem opção 4:5. O mais próximo é Portrait 3:4 (ratio 3:4, aproximadamente 1024×1365). Para obter 4:5 Instagram (1080×1350), gerar em Portrait 3:4 e fazer crop externo para 4:5.

---

## CHATGPT IMAGE-2 — FALLBACK: PIL COMPOSITE PURO

Quando o ChatGPT Image-2 falha no download (Save não funciona, Share retorna 422), seguir este caminho alternativo:

### Script Gerador (confirmado funcionando 2026-05-29)
```
/home/will/.hermes/scripts/refrimix/gerar_carrossel_projeto.py
```

### Quando usar este caminho:
- ChatGPT Image-2 gera imagem bem (visual bom, 1080+ pixels) mas download falha
- ChatGPT Save/Share bugado neste ambiente
- Tempo gasto > 5min sem progresso no fluxo normal

### Como funciona:
1. Criar script Python com PIL + textwrap para gerar slides 1080×1350
2. Background: gradiente Navy ou Cream (sem foto luxo)
3. Texto: Montserrat (ou DejaVu fallback se Montserrat ausente)
4. Linha vertical gold à esquerda
5. Logo REFRIMIX bottom-right
6. Output: PNG 1080×1350 em `/home/will/Imagens/carrocei/[TEMA-DATA]/`

### Código reuse template:
```python
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

SLIDE_W, SLIDE_H = 1080, 1350
NAVY = (0, 46, 81)
CREAM = (245, 240, 232)
GOLD = (201, 169, 110)
LOGO_PATH = "/home/will/Imagens/02-carroceis/exemplo-carrocel/logo.jpeg"

def load_font(bold=False, size=40):
    paths = {
        True: "/usr/share/fonts/opentype/montserrat/Montserrat-Black.otf",
        False: "/usr/share/fonts/truetype/montserrat/Montserrat-Light.ttf",
    }
    try:
        return ImageFont.truetype(paths[bold], size)
    except:
        # Fallback se Montserrat ausente
        fp = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold \
             else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(fp, size)

# Gerar 5 slides com bg alternado (cream/navy) e texto centralizado
# Linha vertical gold (4px) à esquerda
# Body text com textwrap (width ~34-36)
# Logo bottom-right com white background box
```

### Verificação obrigatória após gerar:
- Slide 1 + Slide 5: usar `mcp_minimax_search_understand_image` para validar
- Critério: texto visível sem corte, cores navy/cream/gold corretas
- Se slide 5 com CTA box: garantir que CTA não ultrapasse margem inferior

### Limitações deste caminho:
- NÃO é topo de linha (sem foto luxo de background)
- Usa gradiente sólido em vez de foto arquitetônica real
- Will pode substituir background por foto real depois se quiser
- Prioridade: entregar carrossel funcional > esperar Flowery

---

## HERMES INTEGRATION

- `delegate_task` com batch ≤5 para gerar imagens em paralelo
- Timer estimated: ~2min por imagem (inclui retry)
- Progress: "gerando imagem N de 5"
- QA após cada imagem antes de prosseguir

---

## SKILL CONSOLIDATION (v2.1.0)

### Ancestors ( absorbed — do NOT use separately )
- `refrimix-carousel-generator` → ABSORBED into this skill (delete if found)
- `refrimix-story-generator-v2` → ABSORBED into this skill (delete if found)
- `refrimix-story-generator` →superseded by story-generator-v2 → absorbed (delete if found)

### Related infra skills (KEEP — different layer )
- `chatgpt-plus-image2-carousel-studio` → backend de validação/contract/YAML. Não gerar com ela; usar esta master-creator para orquestrar.
- `refrimix-premium-carousel-workflow` → DEPRECATED. Função idêntica à master-creator. Referências úteis (`visual-identity-refrimix.md`) foram migradas para `references/` desta skill. Redirecionar uso para aqui.

### references/ contents
```
references/
├── copy-research-data.md        # dados HVAC copy research
├── qa-checklist.md             # checklist QA por imagem
├── valvula-4-vias.md           # dado técnico válvulas
├── visual-identity-refrimix.md # brand guide completo (migrado do premium-carousel-workflow)
├── skill-mining-audit-pattern.md # padrão de auditoria de skills (auto-gerado)
└── chatgpt-image-download-workflow.md # fluxo confirmado de download via browser console + PIL crop
```

---

## LEGACY SUB-SKILLS (mantidas para referência)

- `refrimix-carousel-generator` — skill dedicada carrossel (v1.1.0, absorvida neste v2)
- `refrimix-story-generator-v2` — skill dedicada stories (v1.1.0, absorvida neste v2)

Esta skill master-creator v2.1.0 contém todo o conteúdo fundido e é a referência oficial.