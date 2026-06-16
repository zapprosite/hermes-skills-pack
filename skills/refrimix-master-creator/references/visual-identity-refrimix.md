# Refrimix — Identidade Visual Completa (confirmada multimodal + pesquisa)

## Logo (análise direta via mcp_minimax_search_understand_image — 2026-05-21)

**Arquivo:** `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg`
**Marca:** REFRIMIX + tagline TECNOLOGIA
**Ícone:** meio floco de neve (refrigeração) + meio circuito (tecnologia)
**Cores do logo:** Midnight Navy `#002E51` sobre branco

---

## Paleta de Cores — Luxury Architecture

| Nome | HEX | RGB | Uso |
|------|-----|-----|-----|
| Midnight Navy (base) | `#002E51` | (0, 46, 81) | Títulos, CTA, logo |
| White | `#FFFFFF` | (255, 255, 255) | Fundo, contraste |
| Warm Cream | `#F5F0E8` | (245, 240, 232) | Background slides — luxe, não flat |
| Burnished Gold | `#C9A96E` | (201, 169, 110) | Acentos premium, bordas, ícones |
| Soft Steel | `#8B9A9E` | (139, 154, 158) | Subtítulo, texto secundário |
| Deep Charcoal | `#1C1C1E` | (28, 28, 30) | Título em fundo claro |
| Copper Accent | `#B87333` | (184, 115, 51) | Highlights sparíngly |

### Regras de uso de cor

- **Máximo 3 cores por slide** — nunca mais
- **Nunca** usar a mesma cor para título e subtítulo
- **Gold/copper** como acento — sparíngly, não dominar
- **Steel/gray** para texto secundário — nunca para título
- **Cream/ivory** para background luxe — não branco puro

### Paletas prontas por contexto

**Carrossel luxo (fundo claro):**
- Background: `#F5F0E8` (warm cream)
- Título: `#002E51` (navy) ou `#1C1C1E` (charcoal)
- Subtítulo: `#8B9A9E` (steel)
- Acento: `#C9A96E` (gold) — borda fina ou detalhe

**Story noturno:**
- Background: `#002E51` (navy profundo)
- Título: `#FFFFFF` (white)
- Acento: `#C9A96E` (gold)

---

## Tipografia — Pares Confirmados

### Família 1 — TÍTULO (bold condensada, chamar atenção)

| Fonte | Peso | Estilo | Onde usar |
|--------|------|--------|-----------|
| Montserrat | Black (900) | Bold condensed, geometric | Título principal em TODO slide |
| Bebas Neue | Regular | ALL CAPS condensada | Títulos curtos, editorial |
| Gotham Ultra | Bold | Wide condensed | Autoridade, headlines |
| Syncopate | Bold | Tech/sophistication | Variação moderna |

**Regra:** TÍTULO curto (1-3 palavras), ALL CAPS ou Title Case, 90-120px equivalente em canvas

### Família 2 — SUBTÍTULO (light, contraste mandatory)

| Fonte | Peso | Estilo |
|--------|------|--------|
| Montserrat | Light (300) | Mesma família — contraste de peso |
| Lato | Light (300) | Clean, legível |

**Regra:** Subtítulo 40-50px, peso light/regular, max 2 linhas, COR DIFERENTE do título

### Família 3 — CORPO (stories, captions)

- `Source Sans 3` Regular
- `Work Sans` Regular

---

## Anti-Slop — O Que NUNCA Fazer em Prompts

### Vagas → Visuais (ser específico)

❌ "stunning, incredible, epic, masterpiece, gorgeous, ultra-detailed cinematic masterpiece"
✅ "soft overcast light from left, matte finish, navy gradient, 50mm feel, shallow DOF"

❌ "minimalist luxury premium design"
✅ "cream background, heavy black condensed sans, asymmetrical type block, generous negative space"

❌ "beautiful modern architecture"
✅ "white concreteFacade, floor-to-ceiling glass, deep overhanging slab, soft morning light from east"

### Texto em Prompts

❌ Gerar texto sem descrever fonte
✅ `"REFRIMIX" in bold condensed navy blue sans-serif, 80px, top-left with 60px padding`

❌ "use a nice font"
✅ "Montserrat Black, 100px equivalent, deep navy #002E51, center-upper third"

### Contraste Mandatory

Sempre especificar contraste entre texto e fundo:
```text
Text: "REFRIMIX" in bold condensed white with navy drop-shadow (2px offset, 40% opacity) — maximum readability on warm cream #F5F0E8 background.
```

---

## Como Construir Prompt Luxury para ChatGPT Image-2

```text
[ANEXAR LOGO: /home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg]

Create a premium editorial poster (Portrait 3:4, 1080x1350 for Instagram).

Palette: warm cream #F5F0E8 background | navy #002E51 title | gold #C9A96E accent

Logo: REFRIMIX in bold condensed navy, top-left, 60px safe margin.
Title: "TÍTULO CURTO EM ASPAS" — Montserrat Black, 100px, navy #002E51, center-upper area, massive negative space below.
Subtitle: "Subtítulo menor" — Montserrat Light, 42px, steel #8B9A9E, below title, max 2 lines.
Accent: thin gold #C9A96E horizontal rule between title and subtitle.
Background: warm cream #F5F0E8 with subtle grain texture.
Style: Netflix luxury architecture editorial — cinematic contrast, Adobe Photoshop-level shadows, deep DOF, clean aesthetic.
Constraints: no watermark, no extra logos, no generic AI look, no clutter.
```

---

## Drop Shadow — Receita Adobe Photoshop

```text
Text "TÍTULO" drop shadow: 2px right, 2px down, blur 4px, color rgba(0,46,81,0.35)
Text "REFRIMIX" on navy background: white text with 1px navy outline for pop
```