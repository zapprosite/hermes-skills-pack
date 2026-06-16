# ChatGPT Plus — UI Map, May 2026

## Account & Billing

- **Plan:** Plus — R$99.90/mês
- **Renewal:** June 5, 2026
- **Account type:** Tecnologia Plus (logged in during session)

## Sidebar

| Elemento | Descrição |
|---|---|
| New chat | `Ctrl+Shift+O` — novo chat isolado |
| Search chats | `Ctrl+K` |
| Seção: ChatGPT | New chat, Recent, (expandir) |
| Projects | Filtros: All, Created by you, Shared with you |
| Codex | Landing page, 3 planos (Plus/Pro/Business), integrações |
| More | Menu lateral adicional |
| Temporary chat | Banner destacado no topo |
| Profile button | Dropdown: Upgrade plan, Personalization, Profile, Settings, Help, Log out |

## Composer — Menu "Add files and more" (clique no +)

### Radio modes (exclusivos)

| Modo | Placeholder | Status |
|---|---|---|
| Create image | "Describe or edit an image" | ✅ funcional |
| Deep research | — | não testado |
| Web search | "Search the web" | ✅ funcional |

### Submenu "More"

- Agent mode
- Add sources
- Canvas
- Create task
- OpenAI Platform

### Recent files

Lista de arquivos recente do usuário.

## Image Mode Composer (Create image)

- Placeholder: `Describe or edit an image`
- Submit: `Enter`
- Aspect ratios disponíveis (dropdown, em **inglês**):

| Label | Formato | Recomendação |
|---|---|---|
| `Auto` | default | ❌ não usar para carousel |
| `Square 1:1` | 1:1 | ❌ |
| `Portrait 3:4` | **3:4 / 1024×1365** | ⚠️ não é 4:5 — usar e cropar para 4:5 |
| `Story 9:16` | 9:16 | ❌ Reels/Story |
| `Landscape 4:3` | 4:3 | ❌ |
| `Widescreen 16:9` | 16:9 | ❌ |

> ⚠️ **NÃO existe "Portrait 4:5" nem "Retrato 4:5" no ChatGPT Image-2.** A opção "Portrait 3:4" é ratio 3:4, não 4:5. Para Instagram carrossel 4:5 (1080×1350): gerar em Portrait 3:4 e cropar para 4:5 externamente.

- Botão inferior: `Start Voice` → Advanced Voice Mode
- Explore ideas: carrossel de sugestões com paginação
- Upload a photo (link discreto abaixo das sugestões)

## Write or Edit Mode

- Placeholder: `Write anything`
- Sugestões automáticas: Rewrite for clarity, Proofread, Summarize, Turn ideas into outline

## Web Search Mode

- Placeholder: `Search the web`
- Sugestões de exemplo (4 items): Barney Frank, Oregon Election Results, Thomas Massie, Ebola Outbreak Congo 2026
- Results show in the chat as regular ChatGPT responses

## Chat Area

- Share button (top-right of each message)
- Open conversation options menu
- Anexos visíveis na mensagem (ex: logo.jpeg)
- Disclaimer footer: `ChatGPT can make mistakes. Check important info.`

## Settings — Tabs (14 tabs)

| Tab | Conteúdo |
|---|---|
| General | — |
| Notifications | — |
| Personalization | — |
| Apps | — |
| Schedules | — |
| **Billing** | Plus R$99.90/mês, renews Jun 5 2026 |
| Data controls | — |
| Storage | — |
| Security | — |
| Parental controls | — |
| Account | — |
| Keyboard | — |

## Projects

- Filtros: All / Created by you / Shared with you
- Empty state: vazio, pronto para criar

## Codex

- Landing page: "Your AI assistant for work"
- 3 planos: Plus, Pro, Business
- Integrações disponíveis

## Web Search — Features, May 2026

- **GPT-5.3 Instant** = default para todos os tiers (Free incluso)
- **GPT-5.4 Thinking** = raciocínio profundo (paid tiers)
- **GPT-5.4 Pro** = capability máxima (Pro/Business/Enterprise)
- **ChatGPT Images 2.0** = lançado 21/Abr/2026 — renderização de texto melhorada, multilingual
- **DALL-E 2 e DALL-E 3** = aposentados em 12/Mai/2026 (migrar para gpt-image-2)
- **Codex** = remote access via mobile app (iOS/Android)
- **File library** expandida: Free (500MB) / Go (4GB) / Plus (20GB)
- **Personal finances** = Pro, US only, dashboard via Plaid
- **Trusted contact** feature em rollout

## Not Yet Explored

- [ ] Advanced Voice Mode / Start Voice button
- [ ] Canvas completo
- [ ] Agent mode
- [ ] Deep research mode
- [ ] Settings tabs 4-14 (Apps, Schedules, Storage, Security, Parental, Account, Keyboard)
- [ ] GPTs/Explore page
- [ ] Menu "More" completo (só texto visível, não interagido)
- [ ] Mensagens da conversa real (scroll/load)
- [ ] Codex Pro/Business features
- [ ] Projects collaborative features