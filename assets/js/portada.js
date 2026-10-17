// Video de portada: elige la versión según la pantalla (horizontal o vertical) y la reproduce muda y en loop.
// Si el visitante pidió menos movimiento o ahorro de datos, queda solo la imagen fija (poster). main.js no se toca.
(() => {
  const video = document.querySelector('.hero-video');
  if (!video) return;
  const celular = window.matchMedia('(max-width: 720px)').matches;
  video.poster = celular ? video.dataset.posterCelular : video.dataset.posterCompu;
  const calmo = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const ahorro = navigator.connection && navigator.connection.saveData;
  if (calmo || ahorro) return;
  video.src = celular ? video.dataset.celular : video.dataset.compu;
  video.play().catch(() => {});
})();
