#!/usr/bin/env python3
"""
smoke_test_pdf.py — Validação rápida de PDFs gerados pelo Refrimix compiler.

Uso:
  /home/will/.hermes/hermes-agent-next/venv/bin/python3 \
    /home/will/.hermes/skills/social-media/pdf-proposta-refrimix/scripts/smoke_test_pdf.py \
    /home/will/Downloads/cliente_*.pdf

Verifica (SRE gate):
  - arquivo não-vazio
  - >= 1 página
  - rodapé dinâmico "Pág." presente
  - marca "REFRIMIX" presente
  - tipo do documento (OS/proposta/contrato/orcamento) detectado

Exit code:
  0 = todos os PDFs passaram
  1 = pelo menos um falhou
"""
import glob
import os
import sys

import pymupdf as fitz  # PyMuPDF


def smoke(pdf_path: str) -> tuple[bool, str]:
    if not os.path.exists(pdf_path):
        return False, f"arquivo não existe"
    size = os.path.getsize(pdf_path)
    if size == 0:
        return False, f"PDF vazio (0 bytes)"

    try:
        with fitz.open(pdf_path) as doc:
            pages = doc.page_count
            text = "".join(doc[i].get_text() for i in range(pages))
    except Exception as e:
        return False, f"erro ao abrir PDF: {e}"

    if pages < 1:
        return False, f"pages={pages} inválido"
    if "Pág." not in text:
        return False, f"rodapé dinâmico ausente (Pág.)"
    if "REFRIMIX" not in text:
        return False, f"marca REFRIMIX ausente"

    # Tipo detectado (best effort)
    tipo = "?"
    for t in ("ORDEM DE SERVIÇO", "PROPOSTA", "CONTRATO", "ORÇAMENTO", "ORCAMENTO"):
        if t in text.upper():
            tipo = t
            break

    return True, f"OK [{tipo}] {pages}p, {size}B"


def main(patterns: list[str]) -> int:
    paths: list[str] = []
    for pat in patterns:
        paths.extend(glob.glob(pat))

    if not paths:
        print(f"[smoke] Nenhum PDF encontrado para: {patterns}")
        return 1

    failed = 0
    for pdf in paths:
        ok, msg = smoke(pdf)
        flag = "✓" if ok else "✗"
        print(f"[{flag}] {pdf}\n    {msg}")
        if not ok:
            failed += 1

    print(f"\n[smoke] {len(paths) - failed}/{len(paths)} passaram")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["/home/will/Downloads/*.pdf"]))
