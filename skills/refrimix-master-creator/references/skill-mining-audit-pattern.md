# Skill Mining — Audit Pattern

## O que é
Análise sistemática de uma categoria de skills para identificar redundância, gaps, e oportunidades de consolidação. Produz um relatório de ações recomendados.

## Quando usar
- Mais de 3 skills em uma categoria (ex: 6 skills de carrossel/story/post)
- Sobreposição funcional clara entre skills
- Nova skill proposta já coberta por existente
- Manutenção periódica (a cada 3-6 meses)

## Formato do relatório

```markdown
| Skill | Versão | Status | Veredito |
|-------|--------|--------|----------|
| skill-name | v1.0.0 | ✅ KEEP | razão curta |
| skill-name | v1.2.0 | ⚠️ LEGACY | superseded por X — delete |
| skill-name | — | ❓ CONFUSO | sobrepõe com Y — merge ou clarify |
```

## Status classificação

| Status | Significado | Ação |
|--------|-------------|------|
| ✅ OFICIAL | skill principal ativa | manter |
| ✅ KEEP | mantém função diferente | não mexer |
| ⚙️ INFRA | backend/validador, não orquestrador | manter como apoio |
| ⚠️ LEGACY | absorvida ou superada | delete |
| ❓ CONFUSO | sobrepõe ou duplica | merge ou deprecate |
| ❌ ABSORBED | conteúdo migrado | delete |

## Checklist de audit

1. **Versão + descrição** — extrair do frontmatter SKILL.md
2. **linked_files** — listar references/, scripts/, templates/ com contagem
3. **trigger conditions** — quando cada skill é chamada
4. **Sobreposição** — duas skills fazem a mesma coisa?
5. **Lacunas** — funcionalidade sem skill?
6. **Ancestors** — skills absorvidas que ainda existem文件系统?

## Ações recomendadas

### Delete (absorvedoras)
Skills absorvidas em outra não precisam mais — conteúdo já foi migrado.

### Merge
Skills que fazem a mesma coisa mas com nomes diferentes. Criar skill nova com conteúdo fundido.

### Deprecate
Skills que ainda existem mas não são mais recomendadas. Redirecionar para a nova oficial.

### Keep as infra
Skills que validam, formatam, ou executam contratos — não orquestram mas são úteis como backend.

## Exemplo real (Refrimix Instagram 2026-05)

```
CLASSIFICAÇÃO:
✅ refrimix-master-creator v2.0.0 — ORQUESTRADOR TOP1 (faz carousel E stories)
⚙️ chatgpt-plus-image2-carousel-studio v1.0.0 — INFRA (validators, YAML, 12 references)
❓ refrimix-premium-carousel-workflow v1.0.0 — wrapper redundante do mesmo que master-creator faz
⚠️ refrimix-carousel-generator v1.2.0 — LEGACY (absorbed)
⚠️ refrimix-story-generator-v2 v1.2.0 — LEGACY (absorbed)
⚠️ refrimix-story-generator v1.0.0 — LEGACY (superseded)

AÇÕES:
1. Copiar visual-identity-refrimix.md do premium → master-creator/references/
2. Delete 3 legacy skills (carousel-generator, story-generator v1+v2)
3. Deprecate premium-carousel-workflow → redirecionar para master-creator
4. Consolidar versão master-creator → v2.1.0
```

## Comandos de auditoria

```bash
# Listar todas skills de uma categoria
ls ~/.hermes/skills/social-media/

# Extrair frontmatter de todas skills (Python)
for skill in ~/.hermes/skills/social-media/*/SKILL.md; do
  echo "=== $(dirname $skill) ==="
  head -10 "$skill"
done

# Verificar referências
for skill in ~/.hermes/skills/social-media/*; do
  if [ -d "$skill/references" ]; then
    echo "$(basename $skill): $(ls $skill/references/ | wc -l) refs"
  fi
done
```

## Output esperado
- Relatório em markdown com tabela de classificação
- Lista de ações (delete, merge, deprecate, keep)
- Skill atualizada com consolidation notes