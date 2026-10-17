# Itinere Rooms · web rediseñada

Rediseño de https://www.itinere-rooms.com/ (habitaciones en el centro de Granada).

- `index.html` se genera con `python construir.py` (textos, secciones y fotos están en ese script).
- `assets/js/main.js` es **el mismo** de la web actual, sin tocar: buscador de disponibilidad (`POST /api/availability`),
  paso al motor de MyAllocator, formulario de WhatsApp, galería y menú.
- `assets/js/portada.js`: video de portada (versión compu o celular, con imagen fija de respaldo).
- `assets/video/`: videos de portada; `assets/img/`: fotos en WebP (800 y 1600 px).
- `capturar.py`: capturas de revisión (compu y celular), con la web servida en http://localhost:8790.

Pendiente: versión en inglés (`en.html`), y publicar en el proyecto de Vercel junto a la función `/api/availability`
(sin ella, el buscador muestra el mensaje de error).
