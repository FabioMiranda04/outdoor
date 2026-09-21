#!/usr/bin/env python3
"""Gera os QR codes da página. Trocou de domínio? Mude URL e rode de novo.

    pip install segno && python3 qr/gerar.py
"""
import segno

URL = "https://outdoor-sigma.vercel.app"
WALNUT, CREME = "#402814", "#f6f3ee"

# Maiusculas de proposito: aciona o modo alfanumerico do QR, que cabe em
# menos modulos. Sobra espaco para subir a correcao de erro de M para Q
# sem o codigo ficar mais denso. So vale enquanto a URL nao tiver caminho
# — dominio nao diferencia maiuscula de minuscula, mas /caminho diferencia.
payload = URL.upper()

for nome, ecc, dark, light in (
    ("qr-outdoor",       "Q", "black", "white"),
    ("qr-outdoor-marca", "Q", WALNUT, CREME),
    ("qr-outdoor-longe", "M", "black", "white"),
):
    q = segno.make(payload, error=ecc)
    for ext, escala in (("svg", 10), ("pdf", 10), ("eps", 10), ("png", 240)):
        q.save(f"qr/{nome}.{ext}", scale=escala, border=4, dark=dark, light=light)
    print(f"{nome}: versao {q.version}, {q.symbol_size(border=0)[0]} modulos, ecc {ecc}")
