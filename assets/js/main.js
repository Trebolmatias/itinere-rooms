
(() => {
  const header = document.querySelector('.site-header');
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  const body = document.body;

  const setHeader = () => {
    header?.classList.toggle('scrolled', window.scrollY > 24);
  };
  setHeader();
  window.addEventListener('scroll', setHeader, { passive: true });

  menuToggle?.addEventListener('click', () => {
    const open = nav?.classList.toggle('open');
    body.classList.toggle('nav-open', Boolean(open));
    menuToggle.setAttribute('aria-expanded', String(Boolean(open)));
  });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    nav.classList.remove('open');
    body.classList.remove('nav-open');
    menuToggle?.setAttribute('aria-expanded', 'false');
  }));

  const pad = n => String(n).padStart(2, '0');
  const toISO = date => `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;
  const escapeHTML = value => String(value).replace(/[&<>'"]/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[char]));

  document.querySelectorAll('[data-availability-form]').forEach(form => {
    const checkin = form.querySelector('[name="checkin"]');
    const checkout = form.querySelector('[name="checkout"]');
    const submit = form.querySelector('[type="submit"]');
    const error = form.querySelector('.availability-error');
    const results = form.parentElement?.querySelector('[data-availability-results]');
    const lang = form.dataset.lang === 'en' ? 'en' : 'es';
    const today = new Date(); today.setHours(0, 0, 0, 0);
    const tomorrow = new Date(today); tomorrow.setDate(today.getDate() + 1);
    const nextDay = new Date(today); nextDay.setDate(today.getDate() + 2);
    checkin.min = toISO(today);
    checkout.min = toISO(tomorrow);
    if (!checkin.value) checkin.value = toISO(tomorrow);
    if (!checkout.value) checkout.value = toISO(nextDay);

    const syncCheckout = () => {
      if (!checkin.value) return;
      const minimum = new Date(`${checkin.value}T00:00:00`);
      minimum.setDate(minimum.getDate() + 1);
      checkout.min = toISO(minimum);
      if (!checkout.value || checkout.value <= checkin.value) checkout.value = toISO(minimum);
    };
    checkin.addEventListener('change', syncCheckout);

    form.addEventListener('submit', async event => {
      event.preventDefault();
      const start = checkin.value;
      const end = checkout.value;
      if (!start || !end || end <= start) {
        error.hidden = false;
        checkout.focus();
        return;
      }
      error.hidden = true;
      submit.disabled = true;
      submit.textContent = lang === 'en' ? 'Checking availability…' : 'Consultando disponibilidad…';
      if (results) {
        results.hidden = false;
        results.innerHTML = `<p class="availability-empty">${lang === 'en' ? 'Checking available rooms…' : 'Consultando habitaciones disponibles…'}</p>`;
      }
      try {
        const response = await fetch('/api/availability', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({checkin: start, checkout: end, lang})
        });
        if (!response.ok) throw new Error('availability_failed');
        const data = await response.json();
        const dateLabel = `${start.split('-').reverse().join('/')} — ${end.split('-').reverse().join('/')}`;
        const nightsLabel = lang === 'en' ? `${data.nights} ${data.nights === 1 ? 'night' : 'nights'}` : `${data.nights} ${data.nights === 1 ? 'noche' : 'noches'}`;
        const formatMoney = value => new Intl.NumberFormat(lang === 'en' ? 'en-GB' : 'es-ES', {style: 'currency', currency: 'EUR'}).format(value);
        const roomCards = data.rooms.map((room, index) => {
          const maxGuests = Math.max(2, Number(room.maxGuests) || 2);
          const maxRooms = Math.max(1, Number(room.maxRooms) || 1);
          const guestOptions = Array.from({length: maxGuests}, (_, option) => option + 1).map(guests => `<option value="${guests}"${guests === 2 ? ' selected' : ''}>${guests}</option>`).join('');
          const roomOptions = Array.from({length: maxRooms + 1}, (_, quantity) => `<option value="${quantity}">${quantity}</option>`).join('');
          return `<article class="availability-room-card" data-room-card data-room-id="${escapeHTML(room.id)}" data-base-total="${Number(room.baseTotal) || 0}" data-nights="${data.nights}" data-extra="${data.extraGuestPerNight || 15}">
            <div class="availability-room-copy"><h4>${escapeHTML(room.name)}</h4>${room.description ? `<p>${escapeHTML(room.description)}</p>` : ''}<span class="availability-base-price">${lang === 'en' ? 'Stay price per room' : 'Precio de la estancia por habitación'}: <strong>${formatMoney(Number(room.baseTotal) || 0)}</strong></span></div>
            <div class="availability-room-controls">
              <label><span>${lang === 'en' ? 'Guests' : 'Personas'}</span><select data-guests aria-label="${lang === 'en' ? 'Guests in room' : 'Personas en la habitación'}">${guestOptions}</select></label>
              <label><span>${lang === 'en' ? 'Rooms' : 'Habitaciones'}</span><select data-room-quantity aria-label="${lang === 'en' ? 'Number of rooms' : 'Cantidad de habitaciones'}">${roomOptions}</select></label>
              <div class="availability-card-total"><span>${lang === 'en' ? 'Total' : 'Total'}</span><strong data-room-total>${formatMoney(0)}</strong></div>
            </div>
          </article>`;
        }).join('');
        results.innerHTML = `<div class="availability-results-head"><div><h3>${lang === 'en' ? 'Available rooms' : 'Habitaciones disponibles'}</h3><p>${dateLabel}</p></div><span class="availability-night-count">${nightsLabel}</span></div>${roomCards ? `<div class="availability-room-list">${roomCards}</div><div class="availability-grand-total"><div><span>${lang === 'en' ? 'Total for selected stay' : 'Total de la estancia seleccionada'}</span><small>${lang === 'en' ? '1 or 2 guests: same price · 3rd guest: +€15 per night and room' : '1 o 2 personas: mismo precio · 3.ª persona: +15 € por noche y habitación'}</small></div><strong data-grand-total>${formatMoney(0)}</strong></div><button class="availability-continue" type="button" data-booking-continue disabled>${lang === 'en' ? 'Select at least one room' : 'Selecciona al menos una habitación'}</button>` : `<p class="availability-empty">${escapeHTML(data.message || (lang === 'en' ? 'No rooms are available for these dates.' : 'No hay habitaciones disponibles para estas fechas.'))}</p>`}`;
        const continueButton = results.querySelector('[data-booking-continue]');
        const updateTotals = () => {
          let grandTotal = 0;
          let selectedRooms = 0;
          results.querySelectorAll('[data-room-card]').forEach(card => {
            const guests = Number(card.querySelector('[data-guests]').value);
            const quantity = Number(card.querySelector('[data-room-quantity]').value);
            const baseTotal = Number(card.dataset.baseTotal);
            const extra = guests >= 3 ? Number(card.dataset.extra) * Number(card.dataset.nights) : 0;
            const total = (baseTotal + extra) * quantity;
            grandTotal += total;
            selectedRooms += quantity;
            card.querySelector('[data-room-total]').textContent = formatMoney(total);
          });
          const grandTotalNode = results.querySelector('[data-grand-total]');
          if (grandTotalNode) grandTotalNode.textContent = formatMoney(grandTotal);
          if (continueButton) {
            continueButton.disabled = selectedRooms === 0;
            continueButton.textContent = selectedRooms === 0
              ? (lang === 'en' ? 'Select at least one room' : 'Selecciona al menos una habitación')
              : (lang === 'en' ? `Continue booking — ${formatMoney(grandTotal)}` : `Continuar con la reserva — ${formatMoney(grandTotal)}`);
          }
        };
        results.querySelectorAll('select').forEach(select => select.addEventListener('change', updateTotals));
        continueButton?.addEventListener('click', () => {
          sessionStorage.setItem('itinere-booking-selection', JSON.stringify({checkin: start, checkout: end, nights: data.nights}));
          window.location.assign(`https://inbox.myallocator.com/${lang}/booknow/TSe_9f9sFmwdlivbMaI7sA`);
        });
        updateTotals();
        results.scrollIntoView({behavior: 'smooth', block: 'nearest'});
      } catch (requestError) {
        if (results) results.innerHTML = `<p class="availability-empty">${lang === 'en' ? 'We could not check availability right now. Please try again or open the booking engine.' : 'No hemos podido consultar la disponibilidad. Inténtalo de nuevo o abre el motor de reservas.'}</p>`;
      } finally {
        submit.disabled = false;
        submit.textContent = lang === 'en' ? 'View available rooms' : 'Ver habitaciones disponibles';
      }
    });
  });

  document.querySelectorAll('.booking-form').forEach(form => {
    const checkin = form.querySelector('[name="checkin"]');
    const checkout = form.querySelector('[name="checkout"]');
    const guests = form.querySelector('[name="guests"]');
    const note = form.parentElement?.querySelector('.form-note');
    const now = new Date();
    now.setHours(0,0,0,0);
    const tomorrow = new Date(now); tomorrow.setDate(now.getDate() + 1);
    const after = new Date(now); after.setDate(now.getDate() + 2);
    if (checkin) { checkin.min = toISO(now); if (!checkin.value) checkin.value = toISO(tomorrow); }
    if (checkout) { checkout.min = toISO(tomorrow); if (!checkout.value) checkout.value = toISO(after); }
    checkin?.addEventListener('change', () => {
      const ci = new Date(checkin.value + 'T00:00:00');
      ci.setDate(ci.getDate() + 1);
      checkout.min = toISO(ci);
      if (!checkout.value || new Date(checkout.value) <= new Date(checkin.value)) checkout.value = toISO(ci);
    });
    form.addEventListener('submit', event => {
      event.preventDefault();
      const ci = checkin?.value || '';
      const co = checkout?.value || '';
      if (!ci || !co || new Date(co) <= new Date(ci)) {
        note?.classList.add('visible');
        return;
      }
      note?.classList.remove('visible');
      const lang = document.documentElement.lang === 'en' ? 'en' : 'es';
      const msg = lang === 'en'
        ? `Hello, I would like to check availability at Itinere Rooms. Check-in: ${ci}. Check-out: ${co}. Guests: ${guests?.value || '2'}.`
        : `Hola, quisiera consultar disponibilidad en Itinere Rooms. Entrada: ${ci}. Salida: ${co}. Huéspedes: ${guests?.value || '2'}.`;
      window.open(`https://wa.me/34683222264?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
    });
  });

  document.querySelectorAll('.contact-form').forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      const data = new FormData(form);
      const lang = document.documentElement.lang === 'en' ? 'en' : 'es';
      const name = data.get('name') || '';
      const dates = data.get('dates') || '';
      const guests = data.get('guests') || '';
      const message = data.get('message') || '';
      const text = lang === 'en'
        ? `Hello, my name is ${name}. I am interested in staying at Itinere Rooms. Dates: ${dates}. Guests: ${guests}. Message: ${message}`
        : `Hola, mi nombre es ${name}. Me interesa alojarme en Itinere Rooms. Fechas: ${dates}. Huéspedes: ${guests}. Mensaje: ${message}`;
      window.open(`https://wa.me/34683222264?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
    });
  });

  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach(item => observer.observe(item));
  } else {
    revealItems.forEach(item => item.classList.add('visible'));
  }

  const dialog = document.querySelector('.lightbox');
  const lightboxImage = dialog?.querySelector('img');
  const caption = dialog?.querySelector('.lightbox-caption');
  const galleryButtons = Array.from(document.querySelectorAll('[data-lightbox]'));
  let current = 0;

  const showImage = index => {
    if (!dialog || !lightboxImage || !galleryButtons.length) return;
    current = (index + galleryButtons.length) % galleryButtons.length;
    const button = galleryButtons[current];
    lightboxImage.src = button.dataset.full || button.querySelector('img')?.src || '';
    lightboxImage.alt = button.dataset.alt || '';
    if (caption) caption.textContent = button.dataset.alt || '';
  };
  galleryButtons.forEach((button, index) => button.addEventListener('click', () => {
    showImage(index);
    if (typeof dialog.showModal === 'function') dialog.showModal();
  }));
  dialog?.querySelector('.lightbox-close')?.addEventListener('click', () => dialog.close());
  dialog?.querySelector('.lightbox-prev')?.addEventListener('click', () => showImage(current - 1));
  dialog?.querySelector('.lightbox-next')?.addEventListener('click', () => showImage(current + 1));
  dialog?.addEventListener('click', event => {
    if (event.target === dialog) dialog.close();
  });
  document.addEventListener('keydown', event => {
    if (!dialog?.open) return;
    if (event.key === 'ArrowLeft') showImage(current - 1);
    if (event.key === 'ArrowRight') showImage(current + 1);
  });



  document.querySelectorAll('[data-year]').forEach(el => el.textContent = String(new Date().getFullYear()));
})();
