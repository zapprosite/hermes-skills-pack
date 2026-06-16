---
name: pdf-proposta-refrimix
description: >
  Use esta skill SEMPRE que o usuário pedir para GERAR, CRIAR ou EMITIR um documento
  técnico, comercial ou contratual em PDF com a identidade visual da Refrimix
  Tecnologia. Gatilhos incluem: "gerar proposta", "criar contrato", "emitir OS",
  "fazer ordem de serviço", "gerar orçamento de material", "orçamento de mão de obra",
  "contrato de prestação de serviço", "emitir proposta Refrimix", "fazer OS para técnico".
  A skill usa o Master Compiler em Python para gerar PDFs ultra-premium com base no tipo
  especificado.
version: 3.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [proposta, contrato, ordem-de-servico, orcamento, pdf, hvac, refrimix]
    related_skills: [plan-enfemero, test-driven-development, subagent-driven-development]
    changelog:
      - "3.2.0 (jun/2026): corrige path do venv para /home/will/.hermes/hermes-agent-next/venv/; adiciona seção de bootstrap do venv (ensurepip + pip install); adiciona scripts/smoke_test_pdf.py reusável"
      - "3.1.0: flow canônico orientado por templates + compile_request.py"
---

# Skill: Master Document Compiler — Refrimix Tecnologia

Esta skill orquestra a geração automatizada de 6 tipos de documentos essenciais com a
identidade visual de luxo da Refrimix Tecnologia. O compilador ReportLab integrado garante
consistência e acabamento profissional impecável.

O fluxo canônico agora é orientado por templates estruturados em:

- `/home/will/.hermes/scripts/refrimix/templates/document_catalog.json`
- `/home/will/.hermes/scripts/refrimix/templates/identity_index.json`
- `/home/will/.hermes/scripts/refrimix/compile_request.py`

Use `compile_request.py` quando o usuário pedir "gere X, Y e Z documentos" a partir de
dados do cliente e escopo de execução. Use `gerar_proposta.py` diretamente apenas para
casos simples de um único tipo.

## ⚠️ ARMADILHAS CRÍTICAS DO COMPILADOR

### Venv correto mudou em jun/2026
- **Use:** `/home/will/.hermes/hermes-agent-next/venv/bin/python3` (NÃO `python/.venv` que não existe mais)
- Se venv sumir: `python3` do sistema + `pip3 install --user --break-system-packages reportlab pymupdf`
- `reportlab` e `pymupdf` são deps obrigatórias; `ModuleNotFoundError` → instalar antes de rodar

### Logo path tem múltiplos candidatos — usar fallback chain (jun/2026)
A skill precisa do logo mas o caminho original `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png` **NÃO EXISTE MAIS**. Caminhos reais verificados em jun/2026 (em ordem de preferência):

1. `/home/will/Imagens/brand/identity/referencias/Logo.png` — oficial atual
2. `/home/will/.hermes/scripts/refrimix/logo_white.png` — branco, melhor contraste sobre fundo cream
3. `/home/will/Refrimix-tecnologia/06_MIDIAS_E_REDES_SOCIAIS/03_identidade_visual/logo_refrimix.png`
4. `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png` — legado (não existe)
5. `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg` — legado (não existe)

**Patch recomendado em `gerar_proposta.py` (linha ~37):**
```python
LOGO_PATHS = [
    "/home/will/Imagens/brand/identity/referencias/Logo.png",
    "/home/will/.hermes/scripts/refrimix/logo_white.png",
    "/home/will/Refrimix-tecnologia/06_MIDIAS_E_REDES_SOCIAIS/03_identidade_visual/logo_refrimix.png",
    "/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png",
    "/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg",
]
LOGO_PATH = next((p for p in LOGO_PATHS if os.path.exists(p)), LOGO_PATHS[0])
```

**Como descobrir o logo em runtime:**
```bash
find /home/will -type f \( -iname "logo*.png" -o -iname "logo*.jpeg" -o -iname "logo*.jpg" -o -iname "*refrimix*logo*" \) 2>/dev/null | head -5
```

PDF sem logo = 4KB. PDF com logo = 60-65KB. Sempre validar tamanho > 30KB após gerar.

### Google Drive GVFS renomeia arquivos para hash (comportamento normal, não bug)
- `cp arquivo.pdf /run/user/1000/gvfs/google-drive:.../Pasta/` faz upload OK mas o arquivo aparece com nome hash (ex: `1xfCE8C5wNi4uiugzMWSx_QKsX_f8VkHt`)
- **Google Drive identifica por ID interno, não por filename** — comportamento esperado do FUSE/GVFS
- Se usuário pedir "link público do Drive": o link vai para o arquivo pelo ID, não pelo nome; abrir no drive.google.com e buscar por conteúdo
- Para preservar nome: usar `rclone copy --drive-use-trash=false` em vez de `cp` direto
- Antes de qualquer upload GVFS: `gio mount "google-drive://refrimixtecnologia@gmail.com"` (pode estar desmontado após reboot)

### `tipo=proposta` exige campos DIFERENTES de `orcamento_*`
CNPJ:       37.308.021/0001-89
Cidade:     Guarujá — São Paulo
Instagram:  @willrefrimix
Logo:       /home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png
Cores:      Midnight Navy (#002E51) | Burnished Gold (#C9A96E) | Cream (#F5F0E8)
Interpretador: /home/will/.hermes/hermes-agent-next/venv/bin/python3  ← ATENÇÃO: NÃO é /home/will/.hermes/python/.venv/ (esse path não existe)
Compilador: /home/will/.hermes/hermes-agent-next/venv/bin/python3 /home/will/.hermes/scripts/refrimix/gerar_proposta.py
Batch:      /home/will/.hermes/hermes-agent-next/venv/bin/python3 /home/will/.hermes/scripts/refrimix/compile_request.py

> **Python/venv correto:** o caminho legado `/home/will/.hermes/python/.venv/bin/python3` está quebrado. Venv válido: `/home/will/.hermes/hermes-agent-next/venv/bin/python3`. Se `reportlab`/`pymupdf` faltarem: `python3 -m ensurepip --upgrade && python3 -m pip install reportlab pymupdf` DENTRO do venv.

> **Logo path resolution (2026-05-25):** script tenta 5 caminhos em ordem. Antigo oficial `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png` foi REMOVIDO. Caminhos reais (em prioridade):
> 1. `/home/will/Imagens/brand/identity/referencias/Logo.png`
> 2. `/home/will/.hermes/scripts/refrimix/logo_white.png`
> 3. `/home/will/Refrimix-tecnologia/06_MIDIAS_E_REDES_SOCIAIS/03_identidade_visual/logo_refrimix.png`
> 
> PDF < 10KB = logo path quebrado. Investigar `find /home/will -iname "logo*png"`.
Catalogo:   /home/will/.hermes/scripts/refrimix/templates/document_catalog.json
Identidade: /home/will/.hermes/scripts/refrimix/templates/identity_index.json
```

---

## TIPOS DE DOCUMENTOS DISPONÍVEIS (`--tipo`)

| Tipo | Descrição | Estrutura |
|---|---|---|
| `proposta` | Proposta Técnica Executiva completa | Piso: `/home/will/Downloads/teste_skill_proposta.pdf` ou superior |
| `contrato` | Contrato de instalação e execução | Piso: quadro executivo, 10 cláusulas, aceite, anexos, assinaturas |
| `os` | Ordem de Serviço de campo | Ficha técnica, escopo, checklist operacional, assinatura |
| `contrato_prestacao` | Prestação SRE com SLAs | Escopo recorrente, SLA, garantias, relatórios, evidências |
| `orcamento_material` | Orçamento de materiais e insumos | Materiais, rastreabilidade, logística, total e aceite |
| `orcamento_mao_de_obra` | Orçamento de mão de obra e execução | Engenharia, equipe, comissionamento, segurança e condições |

---

## PARÂMETROS OBRIGATÓRIOS E OPICIONAIS

### Entrada recomendada: request JSON

Quando o usuário pedir vários PDFs de uma vez, crie um request JSON seguindo:

```bash
/home/will/.hermes/scripts/refrimix/templates/request_examples/costa_do_sol_batch.json
```

Depois compile:

```bash
/home/will/.hermes/python/.venv/bin/python3 \
  /home/will/.hermes/scripts/refrimix/compile_request.py \
  --request /home/will/.hermes/scripts/refrimix/templates/request_examples/costa_do_sol_batch.json \
  --types proposta,contrato,os
```

O request deve conter, no mínimo:

```json
{
  "cliente": {"nome": "Cliente", "cnpj_cpf": "", "local": ""},
  "execucao": {"resumo": "...", "escopo": ["..."], "equipamentos": [], "dutos_extras": []},
  "valores": {"gestao_valor": 0, "materiais_valor": 0, "dutos_valor": 0},
  "condicoes": {"validade_proposta": "30 dias", "garantia_instalacao": "12 meses", "obra_prazo": "15 dias uteis"},
  "documentos": ["proposta", "contrato"]
}
```

CPF real nunca entra em template, markdown ou log. Se precisar de CPF do Will,
usar runtime/vault conforme `identity_index.json`.

### Entrada direta legada: CLI do compilador

```bash
# Obrigatórios para todos os tipos
--cliente   "Nome do Cliente - Local"
--tipo      "proposta|contrato|os|contrato_prestacao|orcamento_material|orcamento_mao_de_obra"
--output    "/caminho/para/saida.pdf"

# Opcionais (use conforme o tipo)
--data                   "DD/MM/AAAA"
--cnpj_cliente           "XX.XXX.XXX/0001-XX"
--obra_prazo             "XX dias úteis"
--tecnico_nome           "Nome do Técnico"
--placa_veiculo          "XXX-0000"
--equipamentos           '[{"modelo":"...","btu":"36.000","qtd":2,"tecnologia":"Inverter R32"}]'
--dutos_extras           '[{"desc":"Kit Damper Belimo","valor":4500.00}]'
--gestao_valor           "48000.00"
--materiais_valor        "31500.00"
--dutos_valor            "74800.00"
--validade_proposta      "30 dias"
--garantia_instalacao     "24 meses"
--checklist_incluir       "true"
```

---

## ⚠️ ARMADILHAS CRÍTICAS DO COMPILADOR

### Venv correto mudou em jun/2026
- **Use:** `/home/will/.hermes/hermes-agent-next/venv/bin/python3` (NÃO `python/.venv` que não existe mais)
- Se venv sumir: `python3` do sistema + `pip3 install --user --break-system-packages reportlab pymupdf`
- `reportlab` e `pymupdf` são deps obrigatórias; `ModuleNotFoundError` → instalar antes de rodar

### Logo path tem múltiplos candidatos — usar fallback chain (jun/2026)
A skill precisa do logo mas o caminho original `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png` **NÃO EXISTE MAIS**. Caminhos reais verificados em jun/2026 (em ordem de preferência):

1. `/home/will/Imagens/brand/identity/referencias/Logo.png` — oficial atual
2. `/home/will/.hermes/scripts/refrimix/logo_white.png` — branco, melhor contraste sobre fundo cream
3. `/home/will/Refrimix-tecnologia/06_MIDIAS_E_REDES_SOCIAIS/03_identidade_visual/logo_refrimix.png`
4. `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png` — legado (não existe)
5. `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg` — legado (não existe)

**Patch recomendado em `gerar_proposta.py` (linha ~37):**
```python
LOGO_PATHS = [
    "/home/will/Imagens/brand/identity/referencias/Logo.png",
    "/home/will/.hermes/scripts/refrimix/logo_white.png",
    "/home/will/Refrimix-tecnologia/06_MIDIAS_E_REDES_SOCIAIS/03_identidade_visual/logo_refrimix.png",
    "/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png",
    "/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg",
]
LOGO_PATH = next((p for p in LOGO_PATHS if os.path.exists(p)), LOGO_PATHS[0])
```

**Como descobrir o logo em runtime:**
```bash
find /home/will -type f \( -iname "logo*.png" -o -iname "logo*.jpeg" -o -iname "logo*.jpg" -o -iname "*refrimix*logo*" \) 2>/dev/null | head -5
```

PDF sem logo = 4KB. PDF com logo = 60-65KB. Sempre validar tamanho > 30KB após gerar.

### Google Drive GVFS renomeia arquivos para hash (comportamento normal, não bug)
- `cp arquivo.pdf /run/user/1000/gvfs/google-drive:.../Pasta/` faz upload OK mas o arquivo aparece com nome hash (ex: `1xfCE8C5wNi4uiugzMWSx_QKsX_f8VkHt`)
- **Google Drive identifica por ID interno, não por filename** — comportamento esperado do FUSE/GVFS
- Se usuário pedir "link público do Drive": o link vai para o arquivo pelo ID, não pelo nome; abrir no drive.google.com e buscar por conteúdo
- Para preservar nome: usar `rclone copy --drive-use-trash=false` em vez de `cp` direto
- Antes de qualquer upload GVFS: `gio mount "google-drive://refrimixtecnologia@gmail.com"` (pode estar desmontado após reboot)

### `tipo=proposta` exige campos DIFERENTES de `orcamento_*`
**não existe** e falha imediatamente.

Dependências obrigatórias: `reportlab` (geração PDF) e `pymupdf` (smoke test). Se
`ModuleNotFoundError` aparecer, bootstrap do venv:

```bash
/home/will/.hermes/hermes-agent-next/venv/bin/python3 -m ensurepip --upgrade
/home/will/.hermes/hermes-agent-next/venv/bin/python3 -m pip install reportlab pymupdf
```

**Não** tentar `pip install --user --break-system-packages` no Python do sistema — vai
## ⚠️ ARMADILHAS CRÍTICAS DO COMPILADOR

### Venv correto mudou em jun/2026
- **Use:** `/home/will/.hermes/hermes-agent-next/venv/bin/python3` (NÃO `python/.venv` que não existe mais)
- Se venv sumir: `python3` do sistema + `pip3 install --user --break-system-packages reportlab pymupdf`
- `reportlab` e `pymupdf` são deps obrigatórias; `ModuleNotFoundError` → instalar antes de rodar

### Logo path tem múltiplos candidatos — usar fallback chain (jun/2026)
A skill precisa do logo mas o caminho original `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png` **NÃO EXISTE MAIS**. Caminhos reais verificados em jun/2026 (em ordem de preferência):

1. `/home/will/Imagens/brand/identity/referencias/Logo.png` — oficial atual
2. `/home/will/.hermes/scripts/refrimix/logo_white.png` — branco, melhor contraste sobre fundo cream
3. `/home/will/Refrimix-tecnologia/06_MIDIAS_E_REDES_SOCIAIS/03_identidade_visual/logo_refrimix.png`
4. `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png` — legado (não existe)
5. `/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg` — legado (não existe)

**Patch recomendado em `gerar_proposta.py` (linha ~37):**
```python
LOGO_PATHS = [
    "/home/will/Imagens/brand/identity/referencias/Logo.png",
    "/home/will/.hermes/scripts/refrimix/logo_white.png",
    "/home/will/Refrimix-tecnologia/06_MIDIAS_E_REDES_SOCIAIS/03_identidade_visual/logo_refrimix.png",
    "/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png",
    "/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg",
]
LOGO_PATH = next((p for p in LOGO_PATHS if os.path.exists(p)), LOGO_PATHS[0])
```

**Como descobrir o logo em runtime:**
```bash
find /home/will -type f \( -iname "logo*.png" -o -iname "logo*.jpeg" -o -iname "logo*.jpg" -o -iname "*refrimix*logo*" \) 2>/dev/null | head -5
```

PDF sem logo = 4KB. PDF com logo = 60-65KB. Sempre validar tamanho > 30KB após gerar.

### Google Drive GVFS renomeia arquivos para hash (comportamento normal, não bug)
- `cp arquivo.pdf /run/user/1000/gvfs/google-drive:.../Pasta/` faz upload OK mas o arquivo aparece com nome hash (ex: `1xfCE8C5wNi4uiugzMWSx_QKsX_f8VkHt`)
- **Google Drive identifica por ID interno, não por filename** — comportamento esperado do FUSE/GVFS
- Se usuário pedir "link público do Drive": o link vai para o arquivo pelo ID, não pelo nome; abrir no drive.google.com e buscar por conteúdo
- Para preservar nome: usar `rclone copy --drive-use-trash=false` em vez de `cp` direto
- Antes de qualquer upload GVFS: `gio mount "google-drive://refrimixtecnologia@gmail.com"` (pode estar desmontado após reboot)

### `tipo=proposta` exige campos DIFERENTES de `orcamento_*`
  {"modelo": "Daikin Cassete...", "btu": "36.000", "qtd": 2, "tecnologia": "Inverter Neodymium R32"}

ORCAMENTO ( usa desc/valor/qtd ):
  {"desc": "Daikin Cassete Inverter Premium 36.000 BTUs", "valor": 12500.00, "qtd": 2}
```

Nunca use `desc`/`valor` dentro do campo `--equipamentos` quando `--tipo` for `proposta`.
O compilador espera `modelo`, `btu`, `qtd`, `tecnologia` — falha silenciosa com KeyError.

### Dutos Extras sempre usa `desc` + `valor`
```json
[{"desc": "Kit Damper Motorizado Belimo", "valor": 4500.00}]
```

### Google Drive GVFS sync é best-effort
```python
GD_TARGET = "/run/user/1000/gvfs/google-drive:host=gmail.com,user=refrimixtecnologia/..."
if os.path.exists(GD_TARGET):
    shutil.copy2(pdf_path, os.path.join(GD_TARGET, os.path.basename(pdf_path)))
# Se GVFS não montado: prosseguir sem erro
```

---

## WORKFLOW DE EXECUÇÃO (PASSO A PASSO)

### PASSO 1 — IDENTIFICAR TIPO E COMPILAR

Preferir batch:

```bash
PYTHON=/home/will/.hermes/hermes-agent-next/venv/bin/python3
BATCH=/home/will/.hermes/scripts/refrimix/compile_request.py
REQ=/home/will/.hermes/scripts/refrimix/templates/request_examples/costa_do_sol_batch.json

$PYTHON $BATCH --request "$REQ" --types proposta,contrato,os
```

Uso direto para um PDF:

```bash
PYTHON=/home/will/.hermes/hermes-agent-next/venv/bin/python3
SCRIPT=/home/will/.hermes/scripts/refrimix/gerar_proposta.py

$PYTHON $SCRIPT \
  --cliente "Cliente — Cidade" \
  --tipo "proposta" \
  --equipamentos '[{"modelo":"Daikin VRF 10 TR","btu":"120.000","qtd":4,"tecnologia":"VRF Inverter R32"}]' \
  --gestao_valor "48000.00" \
  --materiais_valor "31500.00" \
  --dutos_valor "74800.00" \
  --output "/home/will/Downloads/cliente_proposta.pdf"
```

### PASSO 2 — SMOKE TEST (SRE GATE)

Atalho reusável (substitui o snippet Python inline):

```bash
/home/will/.hermes/hermes-agent-next/venv/bin/python3 \
  /home/will/.hermes/skills/social-media/pdf-proposta-refrimix/scripts/smoke_test_pdf.py \
  /home/will/Downloads/cliente_*.pdf
```

Exit 0 = todos passaram; exit 1 = pelo menos um falhou. Verifica: arquivo não-vazio,
≥1 página, rodapé "Pág.", marca "REFRIMIX", tipo detectado.

Ou inline (se preferir):

```python
import pymupdf as fitz, glob, os

for pdf in glob.glob("/home/will/Downloads/cliente_*.pdf"):
    with fitz.open(pdf) as doc:
        pages = doc.page_count
        text  = "".join(doc[i].get_text() for i in range(doc.page_count))
    assert os.path.getsize(pdf) > 0,  f"PDF vazio: {pdf}"
    assert "Pág." in text,             f"Rodapé ausente: {pdf}"
    assert pages >= 1,                  f"Páginas={pages} inválido: {pdf}"
```

### PASSO 3 — SHADOW QA AUDIT (opcional, para pipelines completos)
```bash
/home/will/.hermes/hermes-agent-next/venv/bin/python3 \
  /home/will/.hermes/scripts/refrimix/rfx_agentic_qa.py \
  /home/will/Downloads/cliente_*.pdf
# Laudo: /home/will/refrimix/data/agentic_qa_report.md
```

### PASSO 4 — NOTIFICAR E ENTREGAR
Informe ao usuário: caminho absoluto do PDF, tamanho em bytes e número de páginas.

---

## EXEMPLOS RÁPIDOS POR TIPO

```bash
# OS de campo
--tipo "os" --tecnico_nome "William Santos" --placa_veiculo "LOG-1A80" --checklist_incluir "true"

# Contrato comercial
--tipo "contrato" --cnpj_cliente "28.409.112/0001-90" --obra_prazo "20 dias úteis"

# Contrato SRE com NR-10/NR-35
--tipo "contrato_prestacao" --garantia_instalacao "24 meses"

# Orçamento material com dutos extras
--tipo "orcamento_material" \
  --dutos_extras '[{"desc":"Grelha Linear Double-Deflection","valor":3200.00}]'
```

---

## PIPELINE E2E COMPLETO (plan-enfemero)

Para simulações E2E como RFX-AUTO-ONBOARDING-E2E:

1. Criar `.hermes/tmp/<slug>/PRD.md` com dados do cliente e critérios de aceitação
2. Criar `.hermes/tmp/<slug>/pipeline.json` com sequência de tasks
3. Criar specs em `.hermes/tmp/<slug>/specs/t00X_*.py`
4. Executar em ordem: seed → compile (6 PDFs) → validate → QA → smoke → cleanup
5. Manter `PRD.md` como registro durável se smoke passar; deletar `specs/` após sucesso

Ver: `references/plan-enfemero-pipeline-refrimix.md` para template completo.

---

## ORGANIZAÇÃO DE SKILLS RECOMENDADA

Para PDF Refrimix, carregar apenas esta skill e, se houver extração/edição de PDF
existente, complementar com:

- `productivity/ocr-and-documents` para ler PDFs existentes.
- `productivity/nano-pdf` somente para microedição textual em PDF pronto.
- `software-development/plan-enfemero` para mudança de compilador com smoke.

Para imagem/carrossel ChatGPT Plus/Image-2, não usar esta skill. Usar o roteamento em
`/home/will/.hermes/skills/ROUTING_REFRIMIX.md`.
