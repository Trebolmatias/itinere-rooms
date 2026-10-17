"""Arma la web rediseñada en español (index.html) e inglés (en.html), con los mismos textos, secciones y ganchos
de main.js que la web actual. Todos los textos están en textos.py.
Uso: python construir.py  →  index.html y en.html
Las fotos están en assets/img/<nombre>-800.webp y -1600.webp (ver ../03 Diseño/exportar_fotos.py).
"""
from pathlib import Path

from textos import EN, ES

AQUI = Path(__file__).resolve().parent
# DEMO: la copia de prueba (GitHub Pages) no se indexa en Google, para no competir con itinere-rooms.com.
# Poner False al publicar en el dominio real.
DEMO = True
VERSION = int((AQUI / "assets" / "css" / "styles.css").stat().st_mtime)  # evita que el navegador use el CSS viejo
WA = "https://wa.me/34683222264"
MAPS = "https://www.google.com/maps/search/?api=1&amp;query=Itinere+Rooms+Natalio+Rivas+1+Granada"
IDS = ["habitaciones", "vistas", "servicios", "ubicacion", "opiniones", "galeria"]

ICON = {
    "flecha": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.2z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M12 21s-7-6-7-11.5a7 7 0 0 1 14 0C19 15 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "auto": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 16V11l2-5h12l2 5v5M4 16h16M4 16v2h3v-2M17 16v2h3v-2M4 11h16"/><circle cx="7.5" cy="13.5" r=".8"/><circle cx="16.5" cy="13.5" r=".8"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.6A8 8 0 1 1 21 12z"/></svg>',
    "reloj": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "llave": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l2 2M15 8l2 2"/></svg>',
    "wifi": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19" r="1" fill="currentColor"/></svg>',
    "cama": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M3 18V7M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="2"/></svg>',
    "taza": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM17 10h1.5a2.5 2.5 0 0 1 0 5H17M8 3v3M12 3v3"/></svg>',
    "maleta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="4" y="7" width="16" height="13" rx="2"/><path d="M9 7V4h6v3"/></svg>',
    "ascensor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 9l3-3 3 3M9 15l3 3 3-3"/></svg>',
    "bus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="5" y="3" width="14" height="15" rx="3"/><path d="M5 11h14M8 18v2M16 18v2"/></svg>',
    "tel": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
}
# el arco de la casa, como marca
MARCA = ('<svg class="brand-mark" viewBox="0 0 30 38" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">'
         '<path d="M2 37V15a13 13 0 0 1 26 0v22z"/><path d="M8 37V16a7 7 0 0 1 14 0v21"/><path d="M15 9v28"/></svg>')


def img(nombre, alt, sizes="(max-width: 720px) 100vw, 50vw", carga="lazy", extra=""):
    return (f'<img src="assets/img/{nombre}-800.webp" srcset="assets/img/{nombre}-800.webp 800w, assets/img/{nombre}-1600.webp 1600w" '
            f'sizes="{sizes}" alt="{alt}" loading="{carga}" decoding="async"{extra}>')


def html(t):
    def ampliar(nombre, alt, clase=""):
        c = f' class="{clase}"' if clase else ""
        return (f'<button type="button"{c} data-lightbox data-full="assets/img/{nombre}-1600.webp" data-alt="{alt}" '
                f'aria-label="{t["ampliar"]}: {alt}">{img(nombre, alt)}</button>')

    def habitacion(fotos, pills, titulo, texto, servicios, cta):
        media = "".join(ampliar(n, a, "media-main" if i == 0 else "") for i, (n, a) in enumerate(fotos))
        return f"""<article class="room-card reveal">
  <div class="room-media">{media}</div>
  <div class="room-content">
    <div class="room-meta">{"".join(f'<span class="pill">{p}</span>' for p in pills)}</div>
    <h3>{titulo}</h3>
    <p>{texto}</p>
    <ul class="amenity-list">{"".join(f"<li>{s}</li>" for s in servicios)}</ul>
    <div class="room-actions">
      <a class="button" data-direct-booking="true" href="#reservar">{cta}{ICON["flecha"]}</a>
      <a class="text-link" href="{WA}" target="_blank" rel="noopener">{t["whatsapp_consulta"]}{ICON["flecha"]}</a>
    </div>
  </div>
</article>"""

    def cabeza(k, h2, copy):
        return (f'<div class="section-head reveal"><div><p class="kicker">{t[k]}</p><h2 class="titulo">{t[h2]}</h2></div>'
                f'<p class="copy">{t[copy]}</p></div>')

    l = t["lang"]
    nav = "".join(f'<a href="#{i}">{n}</a>' for i, n in zip(IDS, t["nav"]))
    nav_pie = "".join(f'<a href="#{i}">{n}</a>' for i, n in zip(IDS, t["nav"]) if i != "opiniones")
    trust = "".join(f'<div class="trust-item"><strong>{a}</strong><span>{b}</span></div>' for a, b in t["trust"])
    features = "".join(f'<div class="feature-row"><span class="feature-icon">{ICON[i]}</span><div><strong>{a}</strong><p>{b}</p></div></div>'
                       for i, a, b in t["features"])
    habitaciones = "".join(habitacion(*h) for h in t["habitaciones"])
    vistas = "".join(f'<figure class="view-card {c} reveal">{ampliar(n, a)}<figcaption>{a}</figcaption></figure>' for n, a, c in t["vistas"])
    detalles = "".join(f'<figure class="detail {c} reveal">{ampliar(n, a)}<figcaption>{a}</figcaption></figure>' for n, a, c in t["detalles"])
    servicios = "".join(f'<article class="service-card reveal"><span class="feature-icon">{ICON[i]}</span><h3>{a}</h3><p>{b}</p><small>{c}</small></article>'
                        for i, a, b, c in t["servicios"])
    lugares = "".join(f'<div class="location-item"><span class="feature-icon">{ICON[i]}</span><div><strong>{a}</strong><span>{b}</span></div>'
                      f'<span class="location-distance">{c}</span></div>' for i, a, b, c in t["lugares"])
    puntajes = "".join(f'<div class="rating-row"><span>{n}</span><div class="rating-track" aria-hidden="true"><div class="rating-fill" style="width:{v * 10:.0f}%"></div></div>'
                       f'<span class="rating-value">{str(v).replace(".", t["decimal"])}</span></div>' for n, v in t["puntajes"])
    tags = "".join(f'<span class="review-tag">{x}</span>' for x in t["tags"])
    galeria = "".join(f'<div class="gallery-item reveal">{ampliar(n, a, "gallery-button")}</div>' for n, a in t["galeria"])
    preguntas = "".join(f"<details><summary>{q}</summary><p>{r}</p></details>" for q, r in t["preguntas"])
    robots = '<meta name="robots" content="noindex, nofollow">' if DEMO else ""
    f, pk, oc, lb = t["form"], t["parking"], t["op_card"], t["lightbox"]
    return f"""<!DOCTYPE html>
<html lang="{l}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["description"]}">
<meta name="theme-color" content="#1E2622">{robots}
<link rel="alternate" hreflang="es" href="https://itinererooms.com/"><link rel="alternate" hreflang="en" href="https://itinererooms.com/en.html"><link rel="alternate" hreflang="x-default" href="https://itinererooms.com/">
<meta property="og:type" content="website"><meta property="og:title" content="{t["title"]}"><meta property="og:description" content="{t["description"]}"><meta property="og:locale" content="{t["og_locale"]}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..600,50;1,9..144,300..500,50&family=Manrope:wght@400;500;600;700&display=swap">
<link rel="preload" as="image" href="assets/video/portada-compu.webp" media="(min-width: 721px)" fetchpriority="high">
<link rel="preload" as="image" href="assets/video/portada-celular.webp" media="(max-width: 720px)" fetchpriority="high">
<link rel="stylesheet" href="assets/css/styles.css?v={VERSION}">
</head>
<body>
<a class="skip-link" href="#contenido">{t["saltar"]}</a>
<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="#inicio" aria-label="{t["inicio_aria"]}">{MARCA}<span class="brand-copy"><strong>Itinere Rooms</strong><small>Granada · Centro</small></span></a>
    <nav class="site-nav" id="main-nav" aria-label="{t["nav_aria"]}">{nav}</nav>
    <div class="nav-actions">
      <a class="lang-link" href="{t["otro"]}" hreflang="{t["otro_lang"]}" aria-label="{t["otro_aria"]}">{t["otro_label"]}</a>
      <a class="button" data-direct-booking="true" href="#reservar">{t["reservar"]}</a>
      <button class="menu-toggle" type="button" aria-controls="main-nav" aria-expanded="false" aria-label="{t["menu_aria"]}"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="contenido">
<section class="hero" id="inicio">
  <video class="hero-video" muted loop playsinline preload="none" aria-hidden="true"
    data-compu="assets/video/portada-compu.mp4" data-celular="assets/video/portada-celular.mp4"
    data-poster-compu="assets/video/portada-compu.webp" data-poster-celular="assets/video/portada-celular.webp"
    poster="assets/video/portada-compu.webp"></video>
  <div class="container hero-content">
    <div class="hero-grid">
      <div>
        <p class="hero-eyebrow">{t["hero_eyebrow"]}</p>
        <h1>{t["hero_h1"]}</h1>
        <p class="hero-lead">{t["hero_lead"]}</p>
        <div class="hero-actions"><a class="button button-light" href="#habitaciones">{t["ver_habitaciones"]}{ICON["flecha"]}</a><a class="button button-ghost" data-direct-booking="true" href="#reservar">{t["reservar_directo"]}</a></div>
      </div>
      <aside class="hero-score" aria-label="{t["puntuacion_aria"]}"><span class="score-number">{t["nota"]}</span><p class="score-title">{t["fantastico"]}</p><p class="score-sub">{t["mas_opiniones"]}</p><span class="booking-chip">Booking.com</span></aside>
    </div>
  </div>
</section>

<section class="reservation" id="reservar" aria-labelledby="direct-booking-title">
  <div class="container">
    <div class="reservation-card">
      <div>
        <p class="kicker">{t["res_kicker"]}</p>
        <h2 id="direct-booking-title">{t["res_h2"]}</h2>
        <p class="copy">{t["res_copy"]}</p>
        <p class="stay-times">{ICON["reloj"]} {t["res_horas"]}</p>
      </div>
      <div class="reservation-engine">
        <form class="availability-form" data-availability-form data-lang="{l}" novalidate>
          <div class="availability-dates">
            <label class="availability-field"><span><strong>Check-in</strong><small>{t["entrada"]}</small></span><input type="date" name="checkin" required aria-label="{t["ci_aria"]}"></label>
            <label class="availability-field"><span><strong>Check-out</strong><small>{t["salida"]}</small></span><input type="date" name="checkout" required aria-label="{t["co_aria"]}"></label>
          </div>
          <button class="availability-submit" type="submit">{t["ver_disponibles"]}</button>
          <p class="availability-error" role="alert" hidden>{t["error_fechas"]}</p>
        </form>
        <section class="availability-results" data-availability-results aria-live="polite" hidden></section>
      </div>
    </div>
  </div>
</section>

<section class="trust" aria-label="{t["trust_aria"]}">
  <div class="container trust-grid">{trust}</div>
</section>

<section class="section" aria-labelledby="intro-title">
  <div class="container intro-grid">
    <div class="intro-visual reveal">
      <div class="intro-photo-main arco">{img("vista-arco", t["intro_alt"])}</div>
      <div class="intro-photo-small">{img("cocina", t["cocina_alt"])}</div>
      <div class="intro-badge"><div><strong>{t["badge"][0]}</strong><span>{t["badge"][1]}</span></div></div>
    </div>
    <div class="reveal">
      <p class="kicker">{t["intro_kicker"]}</p>
      <h2 class="titulo" id="intro-title">{t["intro_h2"]}</h2>
      <p class="copy">{t["intro_copy"]}</p>
      <div class="feature-list">{features}</div>
    </div>
  </div>
</section>

<section class="section rooms-section" id="habitaciones">
  <div class="container">
    {cabeza("hab_kicker", "hab_h2", "hab_copy")}
    <div class="room-stack">{habitaciones}</div>
  </div>
</section>

<section class="section views" id="vistas">
  <div class="container">
    {cabeza("vis_kicker", "vis_h2", "vis_copy")}
    <div class="views-grid">{vistas}</div>
    <p class="views-note">{t["vis_nota"]}</p>
  </div>
</section>

<section class="section details" id="detalles">
  <div class="container">
    {cabeza("det_kicker", "det_h2", "det_copy")}
    <div class="details-grid">{detalles}</div>
  </div>
</section>

<section class="section" id="servicios">
  <div class="container">
    {cabeza("ser_kicker", "ser_h2", "ser_copy")}
    <div class="services-grid">
      <article class="service-card featured reveal">
        <div class="service-copy"><span class="feature-icon">{ICON["auto"]}</span><h3>{pk[0]}</h3><p>{pk[1]}</p><small>{pk[2]}</small></div>
        <div class="service-image">{img("parking", pk[3])}</div>
      </article>
      {servicios}
    </div>
  </div>
</section>

<section class="section" id="ubicacion" style="padding-top:0">
  <div class="container location-grid">
    <div class="reveal">
      <p class="kicker">{t["ubi_kicker"]}</p>
      <h2 class="titulo">{t["ubi_h2"]}</h2>
      <p class="copy">{t["ubi_copy"]}</p>
      <div class="location-list">{lugares}</div>
    </div>
    <div class="map-card reveal">
      <iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Itinere%20Rooms%2C%20Natalio%20Rivas%201%2C%20Granada&amp;hl={l}&amp;output=embed" title="{t["mapa_title"]}"></iframe>
      <div class="map-footer"><div><strong>Itinere Rooms</strong><span>{t["direccion"]}</span></div><a class="text-link" href="{MAPS}" target="_blank" rel="noopener">{t["abrir_maps"]}{ICON["flecha"]}</a></div>
    </div>
  </div>
</section>

<section class="section details" id="opiniones">
  <div class="container">
    {cabeza("op_kicker", "op_h2", "op_copy")}
    <div class="reviews-grid">
      <div class="review-score-card reveal"><span class="score-number">{t["nota"]}</span><h3>{oc[0]}</h3><p>{oc[1]}</p><a class="button button-light" href="{t["booking_url"]}" target="_blank" rel="noopener">{oc[2]}{ICON["flecha"]}</a></div>
      <div class="reveal">
        <div class="rating-list">{puntajes}</div>
        <div class="review-tags">{tags}</div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="galeria">
  <div class="container">
    {cabeza("gal_kicker", "gal_h2", "gal_copy")}
    <div class="gallery-grid">{galeria}</div>
  </div>
</section>

<section class="section details" id="preguntas">
  <div class="container faq-grid">
    <div class="reveal"><p class="kicker">{t["faq_kicker"]}</p><h2 class="titulo">{t["faq_h2"]}</h2><p class="copy">{t["faq_copy"]}</p></div>
    <div class="faq-list reveal">{preguntas}</div>
  </div>
</section>

<section class="section contact" id="contacto">
  <div class="container contact-grid">
    <div class="reveal">
      <p class="kicker">{t["con_kicker"]}</p>
      <h2 class="titulo">{t["con_h2"]}</h2>
      <p class="copy">{t["con_copy"]}</p>
      <div class="contact-details">
        <div class="contact-line"><span class="feature-icon">{ICON["tel"]}</span><div><small>{t["tel_label"]}</small><br><a href="tel:+34683222264">+34 683 22 22 64</a></div></div>
        <div class="contact-line"><span class="feature-icon">{ICON["pin"]}</span><div><small>{t["dir_label"]}</small><br><a href="{MAPS}" target="_blank" rel="noopener">{t["direccion"]}</a></div></div>
      </div>
    </div>
    <div class="contact-card reveal">
      <h3>{t["form_h3"]}</h3>
      <p>{t["form_p"]}</p>
      <form class="contact-form">
        <div><label for="name-{l}">{f[0]}</label><input id="name-{l}" name="name" type="text" autocomplete="name" required></div>
        <div><label for="dates-{l}">{f[1]}</label><input id="dates-{l}" name="dates" type="text" placeholder="{f[2]}"></div>
        <div><label for="guests-contact-{l}">{f[3]}</label><input id="guests-contact-{l}" name="guests" type="number" min="1" max="3" value="2"></div>
        <div class="full"><label for="message-{l}">{f[4]}</label><textarea id="message-{l}" name="message" placeholder="{f[5]}"></textarea></div>
        <button class="button full" type="submit">{ICON["wa"]}{f[6]}</button>
        <p class="contact-privacy">{f[7]}</p>
      </form>
    </div>
  </div>
</section>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand"><a class="brand" href="#inicio">{MARCA}<span class="brand-copy"><strong>Itinere Rooms</strong><small>Granada · Centro</small></span></a><p>{t["pie_desc"]}</p></div>
      <div><p class="footer-title">{t["pie_explorar"]}</p><div class="footer-links">{nav_pie}</div></div>
      <div><p class="footer-title">{t["pie_reserva"]}</p><div class="footer-links"><a data-direct-booking="true" href="#reservar">{t["pie_reservar"]}</a><a href="{t["booking_url"]}" target="_blank" rel="noopener">Booking.com</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="tel:+34683222264">+34 683 22 22 64</a><a href="{MAPS}" target="_blank" rel="noopener">Google Maps</a></div></div>
    </div>
    <div class="footer-bottom"><span>© <span data-year>2026</span> Itinere Rooms. {t["derechos"]}</span><span>{t["direccion"]}</span></div>
  </div>
</footer>
<div class="mobile-booking-bar"><a class="button button-outline" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}{t["barra"][0]}</a><a class="button" data-direct-booking="true" href="#reservar">{t["barra"][1]}</a></div>
<dialog class="lightbox" aria-label="{lb[0]}"><div class="lightbox-wrap"><button class="lightbox-control lightbox-close" type="button" aria-label="{lb[1]}">×</button><button class="lightbox-control lightbox-prev" type="button" aria-label="{lb[2]}">‹</button><div class="lightbox-image-wrap"><img src="" alt=""></div><button class="lightbox-control lightbox-next" type="button" aria-label="{lb[3]}">›</button><div class="lightbox-caption"></div></div></dialog>
<script defer src="assets/js/main.js"></script>
<script defer src="assets/js/portada.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    for textos in (ES, EN):
        (AQUI / textos["archivo"]).write_text(html(textos), encoding="utf-8")
    print("index.html y en.html listos")
