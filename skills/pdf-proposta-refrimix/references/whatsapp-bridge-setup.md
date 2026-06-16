# References — WhatsApp Bridge Setup & Auto-Responder (Refrimix 05/2026)

## Arquitetura

```
┌─────────────────────┐     HTTP/3000      ┌─────────────────────────────┐
│  Node.js Baileys     │◄──────────────────►│  Hermes WhatsAppAdapter     │
│  Bridge (bridge.js)  │   long-poll /send  │  (Python/gateway/platforms/) │
│  WhatsApp Web session│                    │                             │
└─────────────────────┘                    └──────────────┬──────────────┘
       │ QR scan                                   gateway.run (Python)
       │                                                    │
  ┌────┴────┐                                    ┌─────────▼──────────┐
  │Phone    │                                    │ AIAgent + Secretary │
  │WhatsApp │                                    │ (auto-responder)    │
  └─────────┘                                    └────────────────────┘
```

## Caminhos Fixos

```
Bridge Node.js:  /home/will/.hermes/hermes-agent/scripts/whatsapp-bridge/bridge.js
Package.json:    /home/will/.hermes/hermes-agent/scripts/whatsapp-bridge/package.json
Session dir:    ~/.hermes/whatsapp/session/
Python bridge:  /home/will/.hermes/hermes-agent/gateway/platforms/whatsapp.py
Config YAML:    ~/.hermes/config.yaml (seção `whatsapp:`)
```

## Dependências

```bash
# 1. Verificar Node.js
node --version  # precisa ser v18+

# 2. Instalar dependências Node do bridge
cd /home/will/.hermes/hermes-agent/scripts/whatsapp-bridge
npm install

# 3. Dependências Python (geralmente já instaladas)
/home/will/.hermes/python/.venv/bin/python3 -c "import pymupdf; print('ok')"
```

## Config YAML (`~/.hermes/config.yaml`)

```yaml
whatsapp:
  dm_policy: "open"          # aceita DMs de qualquer um
  group_policy: "disabled"   # ignora mensagens de grupo (@g.us)
  free_response_channels: "*"
  allowed_chats: "*"
```

## Start do Bridge (QR Code)

```bash
cd /home/will/.hermes/hermes-agent/scripts/whatsapp-bridge
WHATSAPP_MODE=bot node bridge.js --session ~/.hermes/whatsapp/session --port 3000
```

O QR code aparece em ASCII no terminal. O usuário escaneia com WhatsApp → Linked Devices → Link a Device.

Após pareamento, o bridge mostra `Conectado` e mantém-se em foreground.

## Endpoints HTTP do Bridge (porta 3000)

| Método | Path | Descrição |
|---|---|---|
| GET | `/messages` | Long-poll de mensagens recebidas |
| POST | `/send` | Envia texto: `{chatId, message}` |
| POST | `/typing` | Typing indicator: `{chatId}` |
| GET | `/health` | Health check |

## Filtros de Auto-Responder (jarvis Refrimix)

```python
# Descarte grupos (@g.us)
if message.get("chat", "").endswith("@g.us"):
    return  # ignora silenciosamente

# Escopo HVAC-R permitido
ESCOPO_PERMITIDO = [
    "ar-condicionado", "climatização", "hvac", "manutenção",
    "split", "cassete", "vrf", "pmoc", "elétrica predial",
    "construção civil", "refrigeração"
]

# Resposta de desvio (fora do escopo)
FORA_DO_ESCOPO = (
    "Dr(a)., agradeço o contato. Na Refrimix Tecnologia, nosso foco técnico é "
    "estritamente voltado a projetos de engenharia de climatização (HVAC-R) e "
    "instalações elétricas prediais/corporativas de alto padrão."
)
```

## Logging de Leads

```python
import logging, os
from datetime import datetime

LOG_PATH = "/home/will/workspace/leads_whatsapp.log"
logging.basicConfig(filename=LOG_PATH, level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s")

def log_lead(telefone, mensagem):
    logging.info(f"Lead: {telefone} | {mensagem[:80]}")
```

## Status Atual (05/2026)

- **Estrutura**: pronta (bridge.js, adapter Python, npm deps instalados)
- **Pareamento QR**: pendente — requer escaneamento pelo usuário
- **Auto-responder**: código do webhook receptor não implementado ainda em `~/.hermes/scripts/whatsapp/`
- **Próximo passo**: após QR scan, criar `~/.hermes/scripts/whatsapp/refrimix_auto_reply.py` com filtros e chiamada ao AIAgent