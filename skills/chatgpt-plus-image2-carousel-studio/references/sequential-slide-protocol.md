# Sequential slide protocol

1. Generate only slide N.
2. Wait for complete image and visible controls.
3. Run visual QA.
4. If NEEDS_FIX, correct slide N only.
5. If PASS, download and validate local file.
6. Update `slide-ledger.yaml`.
7. Only then send `proximo` or slide N+1 prompt.

Never advance on PENDING, NEEDS_FIX, BLOCKED, missing download, or missing dimensions.
