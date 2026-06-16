# Sessão 2026-06-08 — Lições Refrimix PDF Compiler

## Problema 1: Logo não aparecia no PDF (4KB em vez de 60KB)

**Sintoma:** Gerei uma OS de teste que saiu com 3.999 bytes. Sem logo, sem identidade visual.

**Causa raiz:** O `LOGO_PATH` hardcoded em `gerar_proposta.py` apontava para
`/home/will/Imagens/Refrimix Tecnologia- Identiidade visual/Logo.png` — diretório
não existe mais. A pasta de identidade visual foi reorganizada.

**Fix:** Implementar `next((p for p in LOGO_PATHS if os.path.exists(p)), LOGO_PATHS[0])`
com fallback chain. Verificar com `find` antes de qualquer geração.

**Validação rápida:** PDF sem logo = ~4KB. PDF com logo = 60-65KB. **Sempre ler
o tamanho após gerar** — falha silenciosa do reportlab é comum quando imagem
não existe (retorna FileNotFoundError que some no stderr).

## Problema 2: Google Drive GVFS renomeia arquivos para hash

**Sintoma:** `cp arquivo.pdf /run/user/1000/gvfs/google-drive:.../Pasta/` retorna
sucesso mas o arquivo aparece com nome tipo `1xfCE8C5wNi4uiugzMWSx_QKsX_f8VkHt`.

**Causa raiz:** Google Drive FUSE/GVFS usa IDs internos. O nome original é perdido.

**Implicação:** Quando o usuário pedir "link público" de um arquivo recém-enviado,
o link aponta para o ID, não para o nome legível. O usuário precisa abrir o
drive.google.com e procurar por conteúdo, não por nome.

**Alternativa:** `rclone copy --drive-use-trash=false` preserva nomes.

**Pré-requisito:** `gio mount "google-drive://refrimixtecnologia@gmail.com"` antes
de qualquer upload — após reboot, mount cai.

## Problema 3: Venv path mudou

**Sintoma:** `ModuleNotFoundError: No module named 'reportlab'` ao rodar com
`/home/will/.hermes/python/.venv/bin/python3`.

**Causa raiz:** O venv `python/.venv` foi deletado. O venv ativo agora é
`/home/will/.hermes/hermes-agent-next/venv/bin/python3` (jun/2026).

**Fix:** Atualizar referências no SKILL.md e em todos os templates `t00X_*.py`
do `plan-enfemero-pipeline-refrimix.md` reference.

**Workaround:** Se o venv sumir, usar Python do sistema com
`pip3 install --user --break-system-packages reportlab pymupdf`.

## Problema 4: venv sem pip

**Sintoma:** `python3 -m pip install` retorna "No module named pip".

**Causa raiz:** venv criado sem `--with-pip`.

**Fix:** `python3 -m ensurepip --upgrade` antes do `pip install` para inicializar.

## Lição geral: Sempre verificar antes de usar

Antes de gerar qualquer PDF:
1. Verificar venv: `which python3 && python3 -c "import reportlab"`
2. Verificar logo: `find /home/will -type f -iname "*refrimix*logo*"`
3. Verificar Drive: `gio mount --list | grep refrimix`
