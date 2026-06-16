# Camofox tab creation — sessionKey pattern and Instagram redirect bug

## Creating authenticated tabs

Camofox `POST /tabs` requires TWO fields:

```json
{
  "userId": "will-chatgpt-plus",
  "sessionKey": "f98e839",
  "url": "https://chatgpt.com"
}
```

- `userId`: arbitrary string identifying the session owner
- `sessionKey`: MUST match a profile ID from `~/.camofox-docker/profiles/` (these are the directory names, e.g. `f98e839`, `8d751da`, `80ca04f8`)
- `url`: optional initial navigation

Without both fields, returns `{"error":"userId and sessionKey required"}`.

## Known working profile IDs

| Profile ID | Notes |
|------------|-------|
| `f98e839` | RefriMix logged in |
| `8d751da` | Created May 27, clean |
| `80ca04f8` | Created May 23 |
| `b78010a2` | Created May 27 after restart |

## Instagram redirect bug (session guard conflict)

**Symptom**: Clicking "Add files and more" or "Create image" in ChatGPT Plus causes the tab to redirect to `https://www.instagram.com/direct/t/...`

**Root cause**: The Camofox Docker profile storage contains Instagram session cookies. When you interact with the "Add files and more" dropdown in ChatGPT, the Camofox session guard detects the Instagram cookies and redirects to Instagram.

**Fix options** (in order of reliability):

1. **Use BrowserOS VNC** — `http://127.0.0.1:6080/vnc_lite.html` — BrowserOS runs Chrome separately and doesn't have the Instagram cookie conflict. This is the preferred path for ChatGPT Plus Image-2 work.

2. **Clear Instagram cookies from Camofox profile** — remove Instagram-related cookies from the profile's storage-state.json in `~/.camofox-docker/profiles/<profileId>/`

3. **Create a new clean profile** — create a new Camofox profile that only has ChatGPT cookies, no Instagram

## API endpoints reference

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/health` | none | Browser health + memory |
| POST | `/tabs` | none | Create tab (needs userId+sessionKey) |
| GET | `/tabs` | none | List tabs |
| POST | `/tabs/{tabId}/navigate` | none | Navigate tab |
| GET | `/tabs/{tabId}/snapshot` | none | Page snapshot |
| GET | `/tabs/{tabId}/screenshot` | none | PNG screenshot |
| POST | `/tabs/{tabId}/click` | none | Click element |
| POST | `/tabs/{tabId}/type` | none | Type into element |
| DELETE | `/tabs/{tabId}` | none | Close tab |
| POST | `/sessions/{userId}/cookies` | BearerAuth | Import cookies |

## Tab creation example (verified working)

```bash
TAB=$(curl -sX POST http://127.0.0.1:9377/tabs \
  -H "Content-Type: application/json" \
  -d '{"userId":"will-chatgpt-plus","sessionKey":"f98e839","url":"https://chatgpt.com"}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['tabId'])")
echo "Tab ID: $TAB"
# Tab ID: 630488c2-e392-4e02-a723-5bb69209b3ab
```