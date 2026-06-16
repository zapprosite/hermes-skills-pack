# Provider lock contract

Allowed production path:

- Browser: existing Hermes Camofox/VNC session.
- Image generation: ChatGPT Plus web UI, Image-2.
- Output: real downloaded local PNGs.

Forbidden production paths:

- local renderers
- paid image APIs
- provider/model/API changes
- terminal downloads of signed backend URLs
- screenshots used as final generated images

If the allowed path is unavailable, the run is BLOCKED. Do not substitute.
