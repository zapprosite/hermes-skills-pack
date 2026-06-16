# Visual QA rubric

Return exactly one status per slide: PASS, NEEDS_FIX, or BLOCKED.

PASS only when:

- slide number/topic is correct
- copy is correct enough to publish
- title is bold, dominant, and legible in thumbnail
- subtitle is finer/lighter and readable
- safe margins are respected
- no text is cropped
- art direction matches prior slides
- result feels premium/editorial/modern, not a cheap template
- sensitive healthcare context has no unsafe guarantee or fake patient scene
- **dimensions match the run contract** — immediately after download, verify width × height via `file` command or Python PIL. For 4:5 Instagram (1080×1350), reject any image whose raw dimensions are not close to 1080×1350 (±5px tolerance). Panoramic, square, or 3:4-only images that cannot be cropped to 4:5 cleanly are NEEDS_FIX or BLOCKED. This check must fire at download time, not after the full carousel is assembled. The aspect-ratio UI selector does NOT guarantee the output dimensions — always check the actual file.

NEEDS_FIX when the image is close but one correction can likely make it publishable.

BLOCKED when the slide is wrong, repeated, unreadable, legally risky, or the tool/session cannot proceed.
