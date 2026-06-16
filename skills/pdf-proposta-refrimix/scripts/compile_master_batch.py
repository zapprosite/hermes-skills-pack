#!/usr/bin/env python3
"""
compile_master_batch.py — Compila 6 PDFs Refrimix em lote único.
Uso: python3 compile_master_batch.py <cliente> <output_dir> [seed_json]
"""
import subprocess, json, os, sys, glob

PYTHON = "/home/will/.hermes/python/.venv/bin/python3"
SCRIPT  = "/home/will/.hermes/scripts/refrimix/gerar_proposta.py"

def compile(base_args, tipo, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cmd = base_args + ["--tipo", tipo, "--output", out_path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    sz = os.path.getsize(out_path) if os.path.exists(out_path) else 0
    ok = r.returncode == 0 and sz > 0
    icon = "✓" if ok else "✗"
    print(f"  {icon} [{tipo}] → {os.path.basename(out_path)} ({sz:,} bytes)")
    if not ok:
        print(f"    ERRO: {r.stderr[-300:]}")
    return ok

def main():
    if len(sys.argv) < 3:
        print("Uso: compile_master_batch.py <cliente> <output_dir> [seed_json]")
        sys.exit(1)
    cliente   = sys.argv[1]
    out_dir   = sys.argv[2]
    seed_path = sys.argv[3] if len(sys.argv) > 3 else None

    if seed_path and os.path.exists(seed_path):
        seed = json.load(open(seed_path))
    else:
        seed = {"cliente": cliente, "gestao": 0, "materiais": 0, "dutos": 0,
                "equipamentos": "[]", "extras": "[]", "data": "23/05/2026",
                "cnpj": "", "prazo": ""}

    BASE = [PYTHON, SCRIPT,
        "--cliente", seed.get("cliente", cliente),
        "--data",    seed.get("data", "23/05/2026"),
        "--cnpj_cliente", seed.get("cnpj", ""),
        "--obra_prazo",   seed.get("prazo", ""),
        "--equipamentos", seed.get("equipamentos", "[]"),
        "--dutos_extras", seed.get("extras", "[]"),
        "--gestao_valor",    str(seed.get("gestao", 0)),
        "--materiais_valor", str(seed.get("materiais", 0)),
        "--dutos_valor",     str(seed.get("dutos", 0)),
    ]

    docs = [
        ("proposta",              f"{out_dir}/proposta.pdf"),
        ("contrato",              f"{out_dir}/contrato.pdf"),
        ("os",                    f"{out_dir}/os.pdf"),
        ("contrato_prestacao",    f"{out_dir}/contrato_prestacao.pdf"),
        ("orcamento_material",    f"{out_dir}/orcamento_material.pdf"),
        ("orcamento_mao_de_obra", f"{out_dir}/orcamento_mao_de_obra.pdf"),
    ]

    results = [compile(BASE, t, o) for t, o in docs]
    print(f"\n{'SUCESSO 6/6' if all(results) else f'FALHA {sum(results)}/6'}")

    # Smoke test rápido
    print("\n[Smoke Test]")
    import pymupdf as fitz
    for _, o in docs:
        if not os.path.exists(o): continue
        with fitz.open(o) as doc:
            pages = doc.page_count
            text  = "".join(doc[i].get_text() for i in range(pages))
        ok = os.path.getsize(o) > 0 and "Pág." in text
        print(f"  {'✓' if ok else '✗'} {os.path.basename(o)} | {pages}p | {'sim' if 'Pág.' in text else 'SEM'} rodapé")

if __name__ == "__main__":
    main()