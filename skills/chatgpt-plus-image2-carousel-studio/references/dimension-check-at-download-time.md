# Dimensões efetivas vs seletor de aspect ratio — 2026-05-20

## Problema observado

O seletor de aspect ratio no ChatGPT Image-2 (opção "Portrait 3:4") NÃO garante dimensões padronizadas de 1024×1365. Imagens geradas nesse modo podem vir com dimensões efetivas completamente diferentes do esperado — o caso observado foi 2492×386 (panorâmica), o que é inutilizável para Instagram 4:5.

## Mecanismo

O ChatGPT Image-2 parece redimensionar internamente com base no contenido real da cena, não respeitando uma grade fixa de pixels. A UI mostra "3:4" mas o output efetivo pode ser qualquer coisa.

## Regra de proteção

1. **Sempre verificar dimensões efetivas imediatamente após o download**, com `file` command ou Python PIL (`Image.open(path).size`).
2. **Tolerance ±5px** na dimensão esperada (ex: 1080×1350 ou 1024×1365).
3. Se as dimensões não fecham, marcar **NEEDS_FIX** na hora — não prosseguir para o próximo slide.
4. Nunca treat o aspecto selected no dropdown como proxy para as dimensões reais do arquivo.

## Comando de verificação

```bash
file /caminho/para/slide.png
# ou
python3 -c "from PIL import Image; print(Image.open('/caminho/para/slide.png').size)"
```

## Fluxo correto

```
1. Download completo
2. file <slide.png> — verificar dimensões
3. Se 1080×1350 (±5px) ou 1024×1365 (±5px) → PASS
4. Se não → NEEDS_FIX com mensagem: "dimensões efetivas X×Y não correspondem ao contrato Z×W"
```

## Por que isso importa

Sem essa verificação, um slide com dimensões erradas pode passar despercebido até a exportação final, quando já perdeu tempo em 4-5 imagens e o usuário espera o carousel completo.