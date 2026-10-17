"""Capturas de página completa de la maqueta (compu y celular), para revisar y para mostrar.
Uso: python capturar.py [url]  →  capturas/compu.png, capturas/celular.png y capturas/compu_NN.jpg (por partes)
Necesita la maqueta servida (por defecto http://localhost:8790).
"""
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

AQUI = Path(__file__).resolve().parent
URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8790/"
SAL = AQUI / "capturas"
Image.MAX_IMAGE_PIXELS = None


def capturar(pag, nombre):
    pag.goto(URL, wait_until="networkidle")
    pag.evaluate("document.fonts.ready")
    # todo visible (las secciones aparecen al hacer scroll) y la portada en su primera foto
    pag.evaluate("""() => { document.querySelectorAll('.reveal').forEach(e => e.classList.add('visible'));
      document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager');
      document.getAnimations().forEach(a => { a.pause(); a.currentTime = 2500; }); }""")
    alto = pag.evaluate("document.body.scrollHeight")
    for y in range(0, alto, 700):  # recorre la página para que carguen las fotos diferidas
        pag.evaluate(f"window.scrollTo(0, {y})")
        pag.wait_for_timeout(120)
    pag.evaluate("window.scrollTo(0, 0)")
    pag.wait_for_function("[...document.images].every(i => i.complete)")
    pag.wait_for_timeout(800)
    pag.screenshot(path=str(SAL / f"{nombre}.png"), full_page=True)


def main():
    SAL.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        nav = pw.chromium.launch(channel="chrome")
        capturar(nav.new_page(viewport={"width": 1440, "height": 900}), "compu")
        capturar(nav.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True), "celular")
        nav.close()
    im = Image.open(SAL / "compu.png").convert("RGB")
    alto = 1800
    for k in range(0, im.height, alto):
        im.crop((0, k, im.width, min(k + alto, im.height))).save(SAL / f"compu_{k // alto + 1:02d}.jpg", quality=80)
    print(f"compu {im.size}, celular {Image.open(SAL / 'celular.png').size}")


if __name__ == "__main__":
    main()
