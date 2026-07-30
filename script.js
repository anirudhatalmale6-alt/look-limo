// ===== Look Limo - interactions =====
(function () {
  // year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // mobile nav
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('open'); });
    });
  }

  // sticky header shadow
  var header = document.getElementById('header');
  window.addEventListener('scroll', function () {
    if (window.scrollY > 20) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  });

  // reveal on scroll
  var revealEls = document.querySelectorAll('.scard, .fcard, .about__media, .about__text, .quote__form, .quote__info, .section__head, .stat');
  revealEls.forEach(function (el) { el.classList.add('reveal'); });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  revealEls.forEach(function (el) { io.observe(el); });

  // faq accordion
  document.querySelectorAll('.faq__q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.closest('.faq__item');
      var ans = item.querySelector('.faq__a');
      var isOpen = item.classList.contains('open');
      // close all
      document.querySelectorAll('.faq__item.open').forEach(function (o) {
        o.classList.remove('open');
        o.querySelector('.faq__a').style.maxHeight = null;
      });
      if (!isOpen) {
        item.classList.add('open');
        ans.style.maxHeight = ans.scrollHeight + 'px';
      }
    });
  });

  // service showcase switcher
  var svcBtns = document.querySelectorAll('.svcnav__btn');
  var svcPanels = document.querySelectorAll('.spanel');
  svcBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var key = btn.getAttribute('data-svc');
      svcBtns.forEach(function (b) { b.classList.toggle('active', b === btn); });
      svcPanels.forEach(function (p) { p.classList.toggle('active', p.getAttribute('data-svc') === key); });
    });
  });

  // animated counters
  function animateCount(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var dur = 1600, start = 0, t0 = null;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var val = Math.floor(p * (target - start) + start);
      el.textContent = val.toLocaleString() + (p === 1 && target >= 1000 ? '+' : (p === 1 && (target === 200 || target === 15) ? '+' : ''));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll('[data-count]');
  var cio = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { animateCount(e.target); cio.unobserve(e.target); }
    });
  }, { threshold: 0.5 });
  counters.forEach(function (el) { cio.observe(el); });
})();

// quote form (demo submit -> opens email; swap for real backend later)
function handleQuote(e) {
  e.preventDefault();
  var f = e.target;
  var note = document.getElementById('formNote');
  var name = f.name.value, phone = f.phone.value, email = f.email.value,
      service = f.service.value, date = f.date.value,
      pickup = f.pickup.value, dropoff = f.dropoff.value, notes = f.notes.value;
  var body =
    'New quote request from Look Limo website%0D%0A%0D%0A' +
    'Name: ' + name + '%0D%0A' +
    'Phone: ' + phone + '%0D%0A' +
    'Email: ' + email + '%0D%0A' +
    'Service: ' + service + '%0D%0A' +
    'Date/Time: ' + date + '%0D%0A' +
    'Pickup: ' + pickup + '%0D%0A' +
    'Drop-off: ' + dropoff + '%0D%0A' +
    'Notes: ' + notes;
  window.location.href = 'mailto:looklimo@gmail.com?subject=Quote Request - ' + encodeURIComponent(name) + '&body=' + body;
  note.textContent = 'Thank you! Your email app is opening to send the request. Or call us at 929-213-8083.';
  f.reset();
  return false;
}
