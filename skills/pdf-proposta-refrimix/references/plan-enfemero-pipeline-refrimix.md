# References — plan-enfemero Pipeline Template (Refrimix E2E)

## Template Completo de Pipeline E2E

### Estrutura de diretórios
```
~/.hermes/tmp/<slug>/
  PRD.md              # Especificação do cliente e critérios
  pipeline.json       # Tarefas e dependências
  specs/
    t001_seed.py      # Gera /tmp/<slug>_seed.json
    t002_compile.py  # Compila 6 PDFs sequencialmente
    t003_validate.py # Valida logo + GDrive sync
    t004_qa.py       # Executa rfx_agentic_qa.py
    t005_smoke.py    # Smoke test final
```

### PRD.md — Template
```markdown
# PRD — <Cliente> (<Data>)

## Cliente e Contexto
- **Cliente**: <NomeFantasia>
- **Local**: <Cidade — UF>
- **Técnico Responsável**: <Nome>
- **Veículo**: <Placa>
- **Prazo**: <N> dias úteis

## Escopo Técnico
- <descrição do projeto>

## Dados Financeiros
- Gestão e Execução SRE: R$ <valor>
- Materiais: R$ <valor>
- Rede de Dutos MPU: R$ <valor>

## Equipamentos
```json
[{"modelo": "...", "btu": "36.000", "qtd": 2, "tecnologia": "Inverter R32"}]
```

## Critérios de Aceitação
- 6 PDFs com tamanho > 0 bytes
- Todos com rodapé "Pág. X de Y"
- Logo Refrimix presente
- Shadow QA aprovado
```

### pipeline.json — Template
```json
{
  "pipeline": "<slug>",
  "version": "1.0",
  "tasks": [
    {"id": "T001", "name": "Seed", "output": "/tmp/<slug>_seed.json"},
    {"id": "T002", "name": "Compile", "depends": ["T001"], "documents": [
      {"tipo": "proposta",              "out": "/dest/cliente_proposta.pdf"},
      {"tipo": "contrato",              "out": "/dest/cliente_contrato.pdf"},
      {"tipo": "os",                    "out": "/dest/cliente_os.pdf"},
      {"tipo": "contrato_prestacao",    "out": "/dest/cliente_prestacao.pdf"},
      {"tipo": "orcamento_material",    "out": "/dest/cliente_material.pdf"},
      {"tipo": "orcamento_mao_de_obra", "out": "/dest/cliente_mao.pdf"}
    ]},
    {"id": "T003", "name": "Validate", "depends": ["T002"]},
    {"id": "T004", "name": "QA Audit", "depends": ["T003"]}
  ]
}
```

### t001_seed.py — Template
```python
#!/usr/bin/env python3
"""T001 — Seeding de dados <Cliente>"""
import json, os
PYTHON = "/home/will/.hermes/python/.venv/bin/python3"
os.makedirs("/home/will/Downloads", exist_ok=True)
EQUIPAMENTOS = json.dumps([{"modelo": "...", "btu": "36.000", "qtd": 2, "tecnologia": "Inverter R32"}])
EXTRAS = json.dumps([{"desc": "...", "valor": 4500.00}])
with open("/tmp/<slug>_seed.json", "w") as f:
    json.dump({
        "cliente":    "<Cliente> (<Local>)",
        "cnpj":       "XX.XXX.XXX/0001-XX",
        "tecnico":    "<Nome>",
        "veiculo":    "<Placa>",
        "prazo":      "<N> dias úteis",
        "gestao":     <valor>,
        "materiais":  <valor>,
        "dutos":      <valor>,
        "equipamentos": EQUIPAMENTOS,
        "extras":     EXTRAS,
        "data":       "DD/MM/AAAA",
    }, f, indent=2)
print("T001 OK")
```

### t002_compile.py — Template
```python
#!/usr/bin/env python3
"""T002 — Compilação Master (6 PDFs)"""
import subprocess, json, os
PYTHON = "/home/will/.hermes/python/.venv/bin/python3"
SCRIPT  = "/home/will/.hermes/scripts/refrimix/gerar_proposta.py"
os.makedirs("/home/will/Downloads", exist_ok=True)
seed = json.load(open("/tmp/<slug>_seed.json"))
BASE = [PYTHON, SCRIPT,
    "--cliente", seed["cliente"], "--data", seed["data"],
    "--cnpj_cliente", seed["cnpj"], "--obra_prazo", seed["prazo"],
    "--equipamentos", seed["equipamentos"], "--dutos_extras", seed["extras"],
    "--gestao_valor", str(seed["gestao"]),
    "--materiais_valor", str(seed["materiais"]),
    "--dutos_valor", str(seed["dutos"])]
def compile(tipo, out):
    r = subprocess.run(BASE + ["--tipo", tipo, "--output", out], capture_output=True, text=True)
    sz = os.path.getsize(out) if os.path.exists(out) else 0
    ok = r.returncode == 0 and sz > 0
    print(f"  [{tipo}] {'OK' if ok else 'ERRO'} ({sz:,} bytes)")
    return ok
docs = [("proposta","cliente_proposta.pdf"),("contrato","cliente_contrato.pdf"),
        ("os","cliente_os.pdf"),("contrato_prestacao","cliente_prestacao.pdf"),
        ("orcamento_material","cliente_material.pdf"),("orcamento_mao_de_obra","cliente_mao.pdf")]
results = [compile(t, f"/home/will/Downloads/{f}") for t, f in docs]
print(f"\nT002 — {'SUCESSO 6/6' if all(results) else f'FALHA {sum(results)}/6'}")
```

### t003_validate.py — Template
```python
#!/usr/bin/env python3
"""T003 — Validação Identity & SRE Sync"""
import os, glob, shutil
LOGO = "/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/logo.jpeg"
GD_TARGET = "/run/user/1000/gvfs/google-drive:host=gmail.com,user=refrimixtecnologia/0AF2hQ71kEgWWUk9PVA/15UxA-7DTRUd7LkDC7wyLXZqc9neN-TP0/"
checks = []
logo_ok = os.path.exists(LOGO)
checks.append(("Logo presente", logo_ok))
pdfs = glob.glob("/home/will/Downloads/cliente_*.pdf")
checks.append(("PDFs 6/6", len(pdfs) == 6))
gdrive_ok = os.path.exists(GD_TARGET)
checks.append(("GDrive path existe", gdrive_ok))
if gdrive_ok:
    for pdf in pdfs:
        dst = os.path.join(GD_TARGET, os.path.basename(pdf))
        shutil.copy2(pdf, dst)
        checks.append((f"GDrive sync {os.path.basename(pdf)}", os.path.getsize(dst) > 0))
all_ok = all(v for _, v in checks)
for label, ok in checks:
    print(f"  {'✓' if ok else '✗'} {label}")
print(f"\nT003 — {'TODOS OK' if all_ok else 'COM FALHAS'}")
```

### t004_qa.py — Template
```python
#!/usr/bin/env python3
"""T004 — Shadow QA Audit"""
import subprocess, os
r = subprocess.run([
    "/home/will/.hermes/python/.venv/bin/python3",
    "/home/will/.hermes/scripts/refrimix/rfx_agentic_qa.py"
] + [f"/home/will/Downloads/{p}" for p in os.listdir("/home/will/Downloads")
     if p.startswith("cliente_") and p.endswith(".pdf")],
    capture_output=True, text=True)
print(r.stdout[:2000])
print(f"\nT004 — {'APROVADO ✓' if r.returncode == 0 else 'COM FALHAS ✗'}")
```

### t005_smoke.py — Template
```python
#!/usr/bin/env python3
"""T005 — Smoke Test Final"""
import pymupdf as fitz, glob, os
all_ok = True
for pdf in glob.glob("/home/will/Downloads/cliente_*.pdf"):
    with fitz.open(pdf) as doc:
        pages = doc.page_count
        text  = "".join(doc[i].get_text() for i in range(doc.page_count))
    ok = os.path.getsize(pdf) > 0 and "Pág." in text and pages >= 1
    print(f"  {'✓' if ok else '✗'} {os.path.basename(pdf):50s} {os.path.getsize(pdf):>8,} bytes | {pages:>3} pág")
    if not ok: all_ok = False
print(f"\nSMOKE — {'APROVADO 6/6 ✓' if all_ok else 'COM FALHAS ✗'}")
```

## Notas de Execução
- Sempre executar seeds e compilações com o Python do uv: `/home/will/.hermes/python/.venv/bin/python3`
- GVFS Google Drive sync é best-effort — se mount não existir, script deve continuar sem erro
- Após smoke test OK: deletar `specs/` e `pipeline.json`, manter `PRD.md` como registro durável
- QA engine: `/home/will/.hermes/scripts/refrimix/rfx_agentic_qa.py` — laudo em `/home/will/refrimix/data/agentic_qa_report.md`