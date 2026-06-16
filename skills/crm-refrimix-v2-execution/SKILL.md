---
name: crm-refrimix-v2-execution
description: Executar CRM Refrimix v2 conforme blueprint em /home/will/workspace/crm-refrimix/PLANEJAMENTO_V2.md. Disparar agy -p em blocos de 1-2 tarefas, revisar entre blocos, fazer smoke real. Use quando Will autorizar início da v2 (previsão original 2026-06-14, 2 dias após o plano).
tags: crm, refrimix, agy, postgres, kanban, honcho, qdrant
---

# CRM Refrimix v2 — Executor

## Quando usar
Will disser "começa a v2", "executa v2", ou a data atual (validada via skill `system-date-time` + `date` no Ubuntu) ultrapassar **2026-06-17** (2 dias após 2026-06-15, data da última atualização) e o blueprint v2 ainda não foi executado.

**REGRA DE DATA:** NUNCA confiar em timestamps hardcoded deste arquivo ou de memória. SEMPRE rodar `date "+%Y-%m-%d"` antes de decidir se a v2 está atrasada. Se a data real for > 2026-06-17 e a v2 não começou, alertar o Senhor.

Quando Will autorizar início da v2, antes de despachar agy:
1. Carregar skill `system-date-time` e rodar `date` — registrar a data real
2. Reconfirmar pré-requisitos (abaixo) com a data atual
3. Despachar bloco 1

## Prerequisite check (SEMPRE rodar antes de despachar agy)
1. **v1 mergeada em main?** Verificar `cd /home/will/workspace/crm-refrimix && git log main..agent/crm-refrimix-v1`. Se tem commits não-mergeadas, PARE e peça Will merge via Gitea PR.
2. **Postgres refrimix user criado no PC1?** `ssh pc1 "sudo -u postgres psql -c '\\du' | grep refrimix"`. Se não, criar.
3. **Ollama rodando com nomic-embed-text?** `curl -s http://127.0.0.1:11434/api/tags | jq '.models[].name'`. Se não, instalar modelo.
4. **hermes-vault tem CRM vars?** `hermes-vault list | grep -i crm`. Se não, documentar e parar.
5. **Branch agent/crm-refrimix-v2 existe?** Criar de main.

## Modo de execução
- **NUNCA usar `agy-pr` (PREVC interativo trava em background)** — confirmado empiricamente
- **Usar `agy -p "{prompt}" --add-dir /home/will/workspace/crm-refrimix --dangerously-skip-permissions --print-timeout 60m`** em background com `script -qfc` pra alocar TTY
- Despachar em **blocos de 1-2 tarefas** do blueprint (não tudo de uma vez)
- Revisar + commitar entre blocos
- Smoke real entre blocos (uvicorn + curl + pytest)

## Tarefas em ordem (do blueprint)
Bloco 1: Tarefas 1-2 (setup + Postgres migration)
Bloco 2: Tarefa 3 (modelo v2 com Alembic)
Bloco 3: Tarefa 4 (auth)
Bloco 4: Tarefa 5 (integrações reais: Qdrant + Honcho + embedding queue)
Bloco 5: Tarefas 6-7 (kanban + dashboard)
Bloco 6: Tarefa 8 (detalhe v2)
Bloco 7: Tarefa 9 (PDF v2 com Montserrat)
Bloco 8: Tarefas 10-11 (testes + docs)
Bloco 9: Tarefa 12 (smoke final + PR)

## Lições da v1 (NÃO repetir)
1. Provisionar .env real ANTES de despachar agy
2. `selectinload` em todo `get_*` com relationship
3. `pool_size` incompatível com aiosqlite (ir direto pra Postgres)
4. Email validator quebrou Pydantic 2 — testar schemas no smoke
5. Agy não roda smoke visual (screenshot) — eu fecho
6. Agy não lida bem com `git push` Gitea — eu faço push + PR
7. `agy -p` é one-shot; agy-PR PREVC trava em background sem TTY
8. SQLite tem limitações — v2 já nasce em Postgres

## Comandos chave
```bash
# Despachar agy
script -qfc 'agy -p "$(cat .agy-v2-prompt-bloco-N.txt)" --add-dir /home/will/workspace/crm-refrimix --dangerously-skip-permissions --print-timeout 60m 2>&1' /home/will/workspace/crm-refrimix/.agy-v2-bloco-N.log

# Validar entre blocos
cd /home/will/workspace/crm-refrimix
git log --oneline -10
ss -tlnp | grep :8080
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://127.0.0.1:8080/
.venv/bin/pytest -x

# Verificar Postgres
ssh pc1 "sudo -u postgres psql -d hermes_core -c 'SELECT COUNT(*) FROM refrimix_crm.leads;'"
```

## Critérios de fim
- Todos os 12 blocos executados
- 20+ testes passando
- PR aberto no Gitea
- v1 migração validada (counts idênticos)
- Smoke completo: login → kanban → PDF v2 → upload → Honcho
- Will aprovou merge em main

## Referências
- Blueprint completo: `/home/will/workspace/crm-refrimix/PLANEJAMENTO_V2.md` (21KB, 16 seções)
- Blueprint v1 (histórico): `/home/will/workspace/crm-refrimix/BLUEPRINT.md`
- v1 smoke: branch `agent/crm-refrimix-v1` em `/home/will/workspace/crm-refrimix/`
- PDFs gerados v1: `~/Documents/Refrimix/CRM/PDFs/`
- Skills relacionadas: `pdf-proposta-refrimix`, `identity-manager`, `gitea-agentic-workflow`, `test-driven-development`, `prevc-autopilot`
