"""Arma la maqueta del rediseño (index.html) con los mismos textos, secciones y ganchos de main.js que la web actual.
Uso: python construir.py  →  index.html
Las fotos están en assets/img/<nombre>-800.webp y -1600.webp (ver ../exportar_fotos.py).
"""
from pathlib import Path

AQUI = Path(__file__).resolve().parent
# DEMO: la copia de prueba (GitHub Pages) no se indexa en Google, para no competir con itinere-rooms.com.
# Poner False al publicar en el dominio real.
DEMO = True
VERSION = int((AQUI / "assets" / "css" / "styles.css").stat().st_mtime)  # evita que el navegador use el CSS viejo
WA = "https://wa.me/34683222264"
MAPS = "https://www.google.com/maps/search/?api=1&amp;query=Itinere+Rooms+Natalio+Rivas+1+Granada"
BOOKING = "https://www.booking.com/hotel/es/itinere-rooms.es.html"

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


def ampliar(nombre, alt, clase=""):
    c = f' class="{clase}"' if clase else ""
    return (f'<button type="button"{c} data-lightbox data-full="assets/img/{nombre}-1600.webp" data-alt="{alt}" '
            f'aria-label="Ampliar: {alt}">{img(nombre, alt)}</button>')


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
      <a class="text-link" href="{WA}" target="_blank" rel="noopener">Consultar por WhatsApp{ICON["flecha"]}</a>
    </div>
  </div>
</article>"""


def servicio(icono, titulo, texto, nota):
    return (f'<article class="service-card reveal"><span class="feature-icon">{ICON[icono]}</span><h3>{titulo}</h3>'
            f'<p>{texto}</p><small>{nota}</small></article>')


def lugar(icono, titulo, sub, dist):
    return (f'<div class="location-item"><span class="feature-icon">{ICON[icono]}</span><div><strong>{titulo}</strong>'
            f'<span>{sub}</span></div><span class="location-distance">{dist}</span></div>')


def html():
    vistas = [("vista-arco", "Vista desde una ventana en arco", "tall"), ("vista-cupulas", "Tejados y cúpulas del centro histórico", ""),
              ("vista-panoramica", "La ciudad desde la 4.ª planta", ""), ("vista-balcon", "Balcón sobre los tejados", ""),
              ("vista-fachada", "Luz de Granada a media mañana", "")]
    # 4 columnas x 2 filas: baño y espejo ocupan dos filas, la cocina dos columnas
    detalles = [("bano", "Baños cuidados", "h2"), ("cocina", "Cocina compartida", "w2"), ("espejo", "Pasillos con carácter", "h2"),
                ("cafe", "Rincón del café", ""), ("armario", "Madera natural", "")]
    galeria = [("hab-toallas", "Habitación con ventana en arco"), ("room-private-1", "Doble con baño privado"),
               ("vista-cupulas", "Vistas a los tejados"), ("hab-dos-ventanas", "Habitación con dos ventanas"),
               ("room-flex-1", "Habitación con cama extra"), ("bano-2", "Baño"), ("balcony", "Balcón con mesa"),
               ("hab-escritorio", "Escritorio junto al balcón"), ("parking", "Parking privado"), ("pasillo", "Pasillo de la 4.ª planta"), ("puerta-403", "Acceso con código"),
               ("room-private-2", "Doble con escritorio"), ("hab-balcon", "Habitación con balcón")]
    preguntas = [
        ("¿Dispone de parking privado?", "Sí. Contamos con parking privado en pleno centro, con plazas limitadas y bajo reserva previa. Debido a las restricciones de tráfico del centro, es importante avisar antes de la llegada para recibir instrucciones."),
        ("¿A qué hora se puede hacer el check-in?", "El check-in comienza a las 14:00. Si necesitas entrar tarde, podemos coordinar el acceso autónomo. El check-out es a las 12:00."),
        ("¿Puedo dejar el equipaje antes o después de la estancia?", "Sí, podemos ayudarte a guardar las maletas para que aproveches mejor el día. Conviene coordinarlo con antelación."),
        ("¿Las habitaciones tienen baño privado?", "Disponemos de habitaciones con baño privado y también de una opción con baño compartido. Revisa el nombre de la habitación antes de reservar."),
        ("¿Hay cocina?", "Hay una pequeña cocina compartida con microondas, nevera, cafetera, fregadero y utensilios básicos, ideal para desayunos y comidas ligeras."),
        ("¿Cómo llego desde el aeropuerto?", "La línea de autobús del aeropuerto conecta con el centro y realiza parada en Gran Vía. También podemos orientarte sobre taxi o traslado privado."),
    ]
    puntajes = [("WiFi", 9.7), ("Ubicación", 9.6), ("Personal", 9.5), ("Calidad-precio", 9.3), ("Limpieza", 9.2), ("Confort", 9.1)]
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Itinere Rooms | Habitaciones en el centro de Granada con parking</title>
<meta name="description" content="Habitaciones cómodas en el corazón de Granada, junto a Gran Vía, Calle Elvira y el Albaicín. Parking privado bajo reserva, WiFi y valoración 9,0 en Booking.com.">
<meta name="theme-color" content="#1E2622">{"<meta name=\"robots\" content=\"noindex, nofollow\">" if DEMO else ""}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..600,50;1,9..144,300..500,50&family=Manrope:wght@400;500;600;700&display=swap">
<link rel="preload" as="image" href="assets/video/portada-compu.webp" media="(min-width: 721px)" fetchpriority="high">
<link rel="preload" as="image" href="assets/video/portada-celular.webp" media="(max-width: 720px)" fetchpriority="high">
<link rel="stylesheet" href="assets/css/styles.css?v={VERSION}">
</head>
<body>
<a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="#inicio" aria-label="Itinere Rooms - Inicio">{MARCA}<span class="brand-copy"><strong>Itinere Rooms</strong><small>Granada · Centro</small></span></a>
    <nav class="site-nav" id="main-nav" aria-label="Navegación principal"><a href="#habitaciones">Habitaciones</a><a href="#vistas">Vistas</a><a href="#servicios">Servicios</a><a href="#ubicacion">Ubicación</a><a href="#opiniones">Opiniones</a><a href="#galeria">Galería</a></nav>
    <div class="nav-actions">
      <a class="lang-link" href="en.html" hreflang="en" aria-label="View in English">EN</a>
      <a class="button" data-direct-booking="true" href="#reservar">Reservar</a>
      <button class="menu-toggle" type="button" aria-controls="main-nav" aria-expanded="false" aria-label="Abrir menú"><span></span><span></span><span></span></button>
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
        <p class="hero-eyebrow">Calle Natalio Rivas 1 · Centro de Granada</p>
        <h1>Granada<br>empieza <em>aquí.</em></h1>
        <p class="hero-lead">Habitaciones cómodas y luminosas junto a Gran Vía, a un paso de Calle Elvira y el Albaicín. Llega, aparca y descubre la ciudad caminando.</p>
        <div class="hero-actions"><a class="button button-light" href="#habitaciones">Ver habitaciones{ICON["flecha"]}</a><a class="button button-ghost" data-direct-booking="true" href="#reservar">Reservar directamente</a></div>
      </div>
      <aside class="hero-score" aria-label="Puntuación de huéspedes"><span class="score-number">9,0</span><p class="score-title">Fantástico</p><p class="score-sub">Más de 1.100 opiniones</p><span class="booking-chip">Booking.com</span></aside>
    </div>
  </div>
</section>

<section class="reservation" id="reservar" aria-labelledby="direct-booking-title">
  <div class="container">
    <div class="reservation-card">
      <div>
        <p class="kicker">Directamente con nosotros</p>
        <h2 id="direct-booking-title">Tu próxima escapada, a un paso.</h2>
        <p class="copy">Elige tus fechas y consulta las habitaciones disponibles.</p>
        <p class="stay-times">{ICON["reloj"]} Check-in desde las 14:00 · Check-out a las 12:00</p>
      </div>
      <div class="reservation-engine">
        <form class="availability-form" data-availability-form data-lang="es" novalidate>
          <div class="availability-dates">
            <label class="availability-field"><span><strong>Check-in</strong><small>Entrada</small></span><input type="date" name="checkin" required aria-label="Check-in, entrada"></label>
            <label class="availability-field"><span><strong>Check-out</strong><small>Salida</small></span><input type="date" name="checkout" required aria-label="Check-out, salida"></label>
          </div>
          <button class="availability-submit" type="submit">Ver habitaciones disponibles</button>
          <p class="availability-error" role="alert" hidden>Selecciona una fecha de salida posterior a la entrada.</p>
        </form>
        <section class="availability-results" data-availability-results aria-live="polite" hidden></section>
      </div>
    </div>
  </div>
</section>

<section class="trust" aria-label="Puntuaciones destacadas">
  <div class="container trust-grid">
    <div class="trust-item"><strong>9,0</strong><span>Booking.com</span></div>
    <div class="trust-item"><strong>9,6</strong><span>Ubicación</span></div>
    <div class="trust-item"><strong>9,2</strong><span>Limpieza</span></div>
    <div class="trust-item"><strong>9,3</strong><span>Calidad-precio</span></div>
    <div class="trust-item"><strong>250 m</strong><span>de Calle Elvira</span></div>
  </div>
</section>

<section class="section" aria-labelledby="intro-title">
  <div class="container intro-grid">
    <div class="intro-visual reveal">
      <div class="intro-photo-main arco">{img("vista-arco", "Vista de Granada desde una ventana en arco")}</div>
      <div class="intro-photo-small">{img("cocina", "Cocina compartida")}</div>
      <div class="intro-badge"><div><strong>9,6</strong><span>Ubicación</span></div></div>
    </div>
    <div class="reveal">
      <p class="kicker">Todo cerca. Todo fácil.</p>
      <h2 class="titulo" id="intro-title">Dormir en el centro cambia la forma de vivir <em>Granada.</em></h2>
      <p class="copy">Itinere Rooms es un alojamiento de gestión familiar pensado para viajeros que valoran una habitación cómoda, una atención directa y, sobre todo, una ubicación excepcional. Aquí puedes dejar el coche, salir por la puerta y empezar a caminar.</p>
      <div class="feature-list">
        <div class="feature-row"><span class="feature-icon">{ICON["pin"]}</span><div><strong>En el corazón de Granada</strong><p>Junto a Gran Vía, cerca de la Catedral, Calle Elvira y la entrada al Albaicín.</p></div></div>
        <div class="feature-row"><span class="feature-icon">{ICON["auto"]}</span><div><strong>Parking privado bajo reserva</strong><p>Una ventaja poco habitual en pleno centro. Te enviamos las indicaciones de acceso antes de llegar.</p></div></div>
        <div class="feature-row"><span class="feature-icon">{ICON["chat"]}</span><div><strong>Atención directa y cercana</strong><p>Consultas rápidas por WhatsApp, recomendaciones locales y ayuda para organizar tu llegada.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section rooms-section" id="habitaciones">
  <div class="container">
    <div class="section-head reveal"><div><p class="kicker">Habitaciones</p><h2 class="titulo">Elige tu forma de <em>descansar.</em></h2></div><p class="copy">Opciones para parejas, amigos y familias pequeñas, con baño privado o compartido y distintas configuraciones de cama.</p></div>
    <div class="room-stack">
      {habitacion([("room-flex-1", "Habitación triple o twin con baño privado"), ("room-flex-2", "Ambiente luminoso con tres camas"), ("balcony", "Balcón y vistas en algunas habitaciones")],
                  ["Hasta 3 huéspedes", "Cama extra +15 €", "Baño privado"], "Doble o twin con baño privado y cama extra",
                  "Las habitaciones 301 y 302 son dobles —con cama doble o dos individuales— y permiten añadir una cama supletoria para un tercer huésped por 15 €, sujeta a disponibilidad.",
                  ["Baño privado", "Aire acondicionado", "TV de pantalla plana", "Minibar y café", "WiFi gratis", "Ropa de cama y toallas"], "Consultar disponibilidad")}
      {habitacion([("room-private-1", "Habitación doble con baño privado"), ("room-private-2", "Habitación doble con escritorio"), ("balcony", "Balcón disponible en algunas unidades")],
                  ["2 huéspedes", "Doble o 2 camas", "Baño privado"], "Doble o twin con baño privado",
                  "Una habitación cómoda para escapadas en pareja, viajes con amigos o estancias de trabajo. Elige cama doble o dos individuales; algunas unidades disponen de balcón, sujeto a disponibilidad.",
                  ["Baño privado", "Aire acondicionado", "TV de pantalla plana", "Minibar y cafetera", "WiFi gratis", "Algunas con balcón"], "Ver disponibilidad")}
      {habitacion([("hab-arco", "Habitación doble o twin con baño compartido"), ("hab-toallas", "Ventana en arco con vistas"), ("bano", "Baño compartido")],
                  ["Hasta 3 huéspedes", "Cama extra +15 €", "Baño compartido"], "Doble o twin con baño compartido",
                  "Una alternativa sencilla y conveniente para quienes priorizan ubicación y presupuesto. Disponible con cama doble o dos camas individuales y acceso a un baño compartido cuidado. La habitación 404 es doble y permite añadir una cama supletoria para un tercer huésped por 15 €, sujeta a disponibilidad.",
                  ["Baño compartido", "Aire acondicionado", "TV de pantalla plana", "WiFi gratis", "Doble o twin", "Minibar"], "Consultar esta opción")}
    </div>
  </div>
</section>

<section class="section views" id="vistas">
  <div class="container">
    <div class="section-head reveal"><div><p class="kicker">Granada desde tu ventana</p><h2 class="titulo">Despierta entre <em>tejados y cúpulas.</em></h2></div><p class="copy">Ventanas en arco, balcones y la luz del centro histórico. Desde las plantas altas, Granada entra por la ventana.</p></div>
    <div class="views-grid">
      {"".join(f'<figure class="view-card {c} reveal">{ampliar(n, a)}<figcaption>{a}</figcaption></figure>' for n, a, c in vistas)}
    </div>
    <p class="views-note">Las vistas y los balcones dependen de cada habitación.</p>
  </div>
</section>

<section class="section details" id="detalles">
  <div class="container">
    <div class="section-head reveal"><div><p class="kicker">Los detalles</p><h2 class="titulo">Pensado para que <em>no te falte nada.</em></h2></div><p class="copy">Baños cuidados, cafetera y minibar, cocina para desayunos y comidas ligeras, y acceso autónomo con código para llegar a tu ritmo.</p></div>
    <div class="details-grid">
      {"".join(f'<figure class="detail {c} reveal">{ampliar(n, a)}<figcaption>{a}</figcaption></figure>' for n, a, c in detalles)}
    </div>
  </div>
</section>

<section class="section" id="servicios">
  <div class="container">
    <div class="section-head reveal"><div><p class="kicker">Servicios</p><h2 class="titulo">Comodidad sin <em>complicaciones.</em></h2></div><p class="copy">Todo lo necesario para aprovechar la ciudad desde el primer minuto: llegar con facilidad, descansar bien y contar con ayuda real cuando la necesites.</p></div>
    <div class="services-grid">
      <article class="service-card featured reveal">
        <div class="service-copy"><span class="feature-icon">{ICON["auto"]}</span><h3>Parking privado en pleno centro</h3><p>Plazas limitadas y bajo reserva previa. Contacta antes de llegar para recibir indicaciones de acceso.</p><small>Una ventaja poco habitual en Granada.</small></div>
        <div class="service-image">{img("parking", "Parking privado de Itinere Rooms")}</div>
      </article>
      {servicio("llave", "Check-in autónomo", "Si llegas tarde, podemos organizar un acceso autónomo para que tu llegada sea sencilla.", "Disponible previa coordinación.")}
      {servicio("wifi", "WiFi gratuito", "Conexión disponible en todo el alojamiento, con una valoración de 9,7 entre los huéspedes.", "Ideal para ocio o trabajo.")}
      {servicio("cama", "Confort en la habitación", "Aire acondicionado, calefacción, TV de pantalla plana y minibar para descansar a tu ritmo.", "Comodidad todo el año.")}
      {servicio("taza", "Cocina compartida", "Microondas, nevera, cafetera, fregadero y utensilios básicos para desayunos o comidas ligeras.", "Práctica y accesible.")}
      {servicio("maleta", "Equipaje y recomendaciones", "Posibilidad de dejar maletas y atención directa para orientarte sobre Granada, flamenco y visitas.", "Hablas con personas, no con un call center.")}
      {servicio("ascensor", "Ascensor y lavandería", "Acceso cómodo mediante ascensor y servicio de lavandería disponible para estancias más largas.", "Pensado también para varios días.")}
    </div>
  </div>
</section>

<section class="section" id="ubicacion" style="padding-top:0">
  <div class="container location-grid">
    <div class="reveal">
      <p class="kicker">La mejor base para explorar</p>
      <h2 class="titulo">Aparca una vez. Granada se recorre <em>a pie.</em></h2>
      <p class="copy">La ubicación es una de las grandes razones por las que los huéspedes eligen Itinere Rooms. Estás junto a Gran Vía, rodeado de restaurantes, tiendas, tapas y conexiones de transporte.</p>
      <div class="location-list">
        {lugar("pin", "Gran Vía de Colón", "Eje principal del centro", "a unos pasos")}
        {lugar("pin", "Calle Elvira", "Teterías, tapas y comercios tradicionales", "250 m")}
        {lugar("pin", "Catedral y centro histórico", "Monumentos y plazas principales", "a pocos minutos")}
        {lugar("pin", "Albaicín", "Barrio Patrimonio Mundial de la UNESCO", "muy cerca")}
        {lugar("bus", "Bus urbano y aeropuerto", "Conexiones desde Gran Vía", "junto al alojamiento")}
      </div>
    </div>
    <div class="map-card reveal">
      <iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Itinere%20Rooms%2C%20Natalio%20Rivas%201%2C%20Granada&amp;output=embed" title="Mapa de Itinere Rooms"></iframe>
      <div class="map-footer"><div><strong>Itinere Rooms</strong><span>Calle Natalio Rivas 1, 3º derecha · Granada</span></div><a class="text-link" href="{MAPS}" target="_blank" rel="noopener">Abrir en Google Maps{ICON["flecha"]}</a></div>
    </div>
  </div>
</section>

<section class="section details" id="opiniones">
  <div class="container">
    <div class="section-head reveal"><div><p class="kicker">Opiniones verificadas</p><h2 class="titulo">Una puntuación que se gana <em>estancia a estancia.</em></h2></div><p class="copy">Los huéspedes destacan especialmente la ubicación, la atención, la limpieza, la comodidad y la relación calidad-precio.</p></div>
    <div class="reviews-grid">
      <div class="review-score-card reveal"><span class="score-number">9,0</span><h3>Fantástico en Booking.com</h3><p>Más de 1.100 opiniones de huéspedes</p><a class="button button-light" href="{BOOKING}" target="_blank" rel="noopener">Leer opiniones{ICON["flecha"]}</a></div>
      <div class="reveal">
        <div class="rating-list">{"".join(f'<div class="rating-row"><span>{n}</span><div class="rating-track" aria-hidden="true"><div class="rating-fill" style="width:{v * 10:.0f}%"></div></div><span class="rating-value">{str(v).replace(".", ",")}</span></div>' for n, v in puntajes)}</div>
        <div class="review-tags">{"".join(f'<span class="review-tag">{t}</span>' for t in ["Ubicación perfecta", "Habitaciones limpias", "Camas cómodas", "Atención cercana", "Excelente relación calidad-precio"])}</div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="galeria">
  <div class="container">
    <div class="section-head reveal"><div><p class="kicker">Galería</p><h2 class="titulo">Descubre tu próxima <em>estancia.</em></h2></div><p class="copy">Habitaciones luminosas, baños cuidados, balcones con vistas y servicios que hacen más fácil visitar Granada.</p></div>
    <div class="gallery-grid">{"".join(f'<div class="gallery-item reveal">{ampliar(n, a, "gallery-button")}</div>' for n, a in galeria)}</div>
  </div>
</section>

<section class="section details" id="preguntas">
  <div class="container faq-grid">
    <div class="reveal"><p class="kicker">Preguntas frecuentes</p><h2 class="titulo">Antes de <em>llegar.</em></h2><p class="copy">Respuestas rápidas a las preguntas más habituales. Para cualquier situación especial, escríbenos directamente.</p></div>
    <div class="faq-list reveal">{"".join(f"<details><summary>{q}</summary><p>{r}</p></details>" for q, r in preguntas)}</div>
  </div>
</section>

<section class="section contact" id="contacto">
  <div class="container contact-grid">
    <div class="reveal">
      <p class="kicker">Reserva y contacto</p>
      <h2 class="titulo">Tu viaje puede empezar <em>con un mensaje.</em></h2>
      <p class="copy">Consulta disponibilidad, parking o cualquier detalle de la estancia. Te atendemos directamente y te ayudamos a organizar la llegada.</p>
      <div class="contact-details">
        <div class="contact-line"><span class="feature-icon">{ICON["tel"]}</span><div><small>Teléfono y WhatsApp</small><br><a href="tel:+34683222264">+34 683 22 22 64</a></div></div>
        <div class="contact-line"><span class="feature-icon">{ICON["pin"]}</span><div><small>Dirección</small><br><a href="{MAPS}" target="_blank" rel="noopener">Calle Natalio Rivas 1, 3º derecha · Granada</a></div></div>
      </div>
    </div>
    <div class="contact-card reveal">
      <h3>Consultar disponibilidad</h3>
      <p>Completa los datos y se abrirá WhatsApp con el mensaje preparado.</p>
      <form class="contact-form">
        <div><label for="name-es">Nombre</label><input id="name-es" name="name" type="text" autocomplete="name" required></div>
        <div><label for="dates-es">Fechas aproximadas</label><input id="dates-es" name="dates" type="text" placeholder="Ej. 12–15 octubre"></div>
        <div><label for="guests-contact-es">Huéspedes</label><input id="guests-contact-es" name="guests" type="number" min="1" max="3" value="2"></div>
        <div class="full"><label for="message-es">Mensaje</label><textarea id="message-es" name="message" placeholder="Parking, tipo de cama, hora de llegada…"></textarea></div>
        <button class="button full" type="submit">{ICON["wa"]}Enviar por WhatsApp</button>
        <p class="contact-privacy">Este formulario no almacena datos: prepara un mensaje y abre WhatsApp.</p>
      </form>
    </div>
  </div>
</section>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand"><a class="brand" href="#inicio">{MARCA}<span class="brand-copy"><strong>Itinere Rooms</strong><small>Granada · Centro</small></span></a><p>Habitaciones cómodas, parking privado y una ubicación excepcional para descubrir Granada caminando.</p></div>
      <div><p class="footer-title">Explorar</p><div class="footer-links"><a href="#habitaciones">Habitaciones</a><a href="#vistas">Vistas</a><a href="#servicios">Servicios</a><a href="#ubicacion">Ubicación</a><a href="#galeria">Galería</a></div></div>
      <div><p class="footer-title">Reserva</p><div class="footer-links"><a data-direct-booking="true" href="#reservar">Reservar directo</a><a href="{BOOKING}" target="_blank" rel="noopener">Booking.com</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="tel:+34683222264">+34 683 22 22 64</a><a href="{MAPS}" target="_blank" rel="noopener">Google Maps</a></div></div>
    </div>
    <div class="footer-bottom"><span>© <span data-year>2026</span> Itinere Rooms. Todos los derechos reservados.</span><span>Calle Natalio Rivas 1, 3º derecha · Granada</span></div>
  </div>
</footer>
<div class="mobile-booking-bar"><a class="button button-outline" href="{WA}" target="_blank" rel="noopener">{ICON["wa"]}WhatsApp</a><a class="button" data-direct-booking="true" href="#reservar">Reservar directo</a></div>
<dialog class="lightbox" aria-label="Galería de imágenes"><div class="lightbox-wrap"><button class="lightbox-control lightbox-close" type="button" aria-label="Cerrar">×</button><button class="lightbox-control lightbox-prev" type="button" aria-label="Anterior">‹</button><div class="lightbox-image-wrap"><img src="" alt=""></div><button class="lightbox-control lightbox-next" type="button" aria-label="Siguiente">›</button><div class="lightbox-caption"></div></div></dialog>
<script defer src="assets/js/main.js"></script>
<script defer src="assets/js/portada.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    (AQUI / "index.html").write_text(html(), encoding="utf-8")
    print("index.html listo")
