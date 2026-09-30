#!/usr/bin/env python3
"""Mete los PNG de sprites/ dentro de liga-barrios-barakaldo.html.

Cada archivo sprites/<clave>.png queda disponible en el juego como SPR["<clave>"]
(y SPRI["<clave>"] ya decodificado). Se puede volver a ejecutar tras cambiar o añadir
un PNG: la línea generada se sustituye entera.

Uso: python3 tools/embed_sprites.py
"""
import base64, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = ROOT / "liga-barrios-barakaldo.html"
MARK = "// sprites/ (generado por tools/embed_sprites.py)"

pngs = sorted((ROOT / "sprites").glob("*.png"))
items = ",".join(f'{p.stem}:"{base64.b64encode(p.read_bytes()).decode()}"' for p in pngs)
line = f"Object.assign(SPR,{{{items}}}); {MARK}\n"

src = HTML.read_text(encoding="utf-8")
lines = src.splitlines(keepends=True)
lines = [l for l in lines if MARK not in l]
at = next(i for i, l in enumerate(lines) if l.startswith("const HTPL="))
lines.insert(at, line)
HTML.write_text("".join(lines), encoding="utf-8")
print(f"{len(pngs)} sprites: {', '.join(p.stem for p in pngs)}")
