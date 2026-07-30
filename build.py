#!/usr/bin/env python3
"""Look Limo static site generator. Builds all pages with a shared header/footer
so the chrome stays identical everywhere. Run: python3 build.py"""
import os

PHONE = "929-213-8083"
PHONE_TEL = "+19292138083"
EMAIL = "looklimo@gmail.com"
AREA = "Philadelphia"

# ---- Navigation ----
NAV = [
    ("Home", "index.html"),
    ("About", "about.html"),
    ("Services", "services.html"),
    ("Fleet", "fleet.html"),
    ("FAQ", "faq.html"),
    ("Contact", "contact.html"),
]

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" href="assets/logo.jpg" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Great+Vibes&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="styles.css" />
</head>
<body>
"""

def header(active):
    links = ""
    for label, href in NAV:
        cls = "nav__link active" if href == active else "nav__link"
        links += f'      <a href="{href}" class="{cls}">{label}</a>\n'
    return f"""
<div class="topbar">
  <div class="container topbar__inner">
    <div class="topbar__left">
      <a href="tel:{PHONE_TEL}" class="topbar__item"><span class="ic">&#9742;</span> {PHONE}</a>
      <a href="mailto:{EMAIL}" class="topbar__item"><span class="ic">&#9993;</span> {EMAIL}</a>
    </div>
    <div class="topbar__right">
      <span class="topbar__tag">Serving Philadelphia &amp; Surrounding Areas</span>
    </div>
  </div>
</div>

<header class="header" id="header">
  <div class="container header__inner">
    <a href="index.html" class="brand">
      <img src="assets/logo.jpg" alt="Look Limo" class="brand__logo" />
    </a>
    <nav class="nav" id="nav">
{links}      <a href="contact.html" class="btn btn--gold nav__cta">Get a Quote</a>
    </nav>
    <button class="nav__toggle" id="navToggle" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
"""

CTA = f"""
<section class="ctabanner">
  <div class="container ctabanner__inner">
    <h2>Ready to ride in luxury?</h2>
    <p>Book your Look Limo experience in Philadelphia today.</p>
    <a href="tel:{PHONE_TEL}" class="btn btn--gold btn--lg">&#9742; {PHONE}</a>
  </div>
</section>
"""

FOOTER = f"""
<footer class="footer">
  <div class="container footer__inner">
    <div class="footer__col footer__brand">
      <img src="assets/logo.jpg" alt="Look Limo" class="footer__logo" />
      <p>Elegance. Comfort. Excellence. Premium chauffeured limousine service across Philadelphia and the surrounding region.</p>
    </div>
    <div class="footer__col">
      <h4>Services</h4>
      <a href="personal.html">Personal</a>
      <a href="airport-transfers.html">Airport</a>
      <a href="corporate-travel.html">Corporate</a>
      <a href="school.html">School</a>
    </div>
    <div class="footer__col">
      <h4>Company</h4>
      <a href="about.html">About Us</a>
      <a href="fleet.html">Our Fleet</a>
      <a href="faq.html">FAQ</a>
      <a href="contact.html">Get a Quote</a>
    </div>
    <div class="footer__col">
      <h4>Contact</h4>
      <a href="tel:{PHONE_TEL}">{PHONE}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <span>Philadelphia, PA</span>
      <span>Available 24/7</span>
    </div>
  </div>
  <div class="footer__bar">
    <div class="container footer__bar-inner">
      <span>&copy; <span id="year"></span> Look Limo. All rights reserved.</span>
      <span>Licensed &amp; Insured &middot; Chauffeured Transportation</span>
    </div>
  </div>
</footer>

<a href="tel:{PHONE_TEL}" class="fab" aria-label="Call Look Limo">&#9742;</a>

<script src="script.js"></script>
</body>
</html>
"""

def pagehero(title_html, sub, crumb):
    return f"""
<section class="pagehero" style="background-image:url('assets/{crumb['bg']}')">
  <div class="container pagehero__inner">
    <h1>{title_html}</h1>
    <p>{sub}</p>
    <div class="crumb"><a href="index.html">Home</a> <span>&rsaquo;</span> <span>{crumb['name']}</span></div>
  </div>
</section>
"""

def write(name, html):
    path = os.path.join(os.path.dirname(__file__), name)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", name)

# =====================================================================
# HOME
# =====================================================================
home_body = f"""
<section class="hero" id="home">
  <video class="hero__video" autoplay muted loop playsinline preload="auto" poster="assets/hero-poster.jpg">
    <source src="assets/hero-video.mp4" type="video/mp4" />
  </video>
  <div class="hero__overlay"></div>
  <div class="container hero__inner">
    <p class="hero__welcome">Welcome to</p>
    <h1 class="hero__brand">Look Limo</h1>
    <p class="hero__tag">A Smarter Way to Ride</p>
    <div class="hero__cta">
      <a href="fleet.html" class="btn btn--gold btn--lg">View Fleet</a>
      <a href="contact.html" class="btn btn--ghost btn--lg">Get a Quote</a>
    </div>
  </div>
</section>

<section class="svcshow" id="services">
  <div class="svcshow__stage">
    <a class="spanel active" data-svc="personal" href="personal.html" style="background-image:url('assets/svc-personal.jpg')">
      <span class="spanel__cap"><span class="spanel__k">Our Services</span><h3>Personal</h3><p>Convenient and reliable private transportation services.</p><span class="spanel__go">Explore Personal &rarr;</span></span>
    </a>
    <a class="spanel" data-svc="corporate" href="corporate-travel.html" style="background-image:url('assets/svc-corporate.jpg')">
      <span class="spanel__cap"><span class="spanel__k">Our Services</span><h3>Corporate</h3><p>World-class executive and business transportation service.</p><span class="spanel__go">Explore Corporate &rarr;</span></span>
    </a>
    <a class="spanel" data-svc="airport" href="airport-transfers.html" style="background-image:url('assets/svc-airport.jpg')">
      <span class="spanel__cap"><span class="spanel__k">Our Services</span><h3>Airport</h3><p>Prompt airport transportation for any business trip or vacation worldwide.</p><span class="spanel__go">Explore Airport &rarr;</span></span>
    </a>
    <a class="spanel" data-svc="school" href="school.html" style="background-image:url('assets/svc-school.jpg')">
      <span class="spanel__cap"><span class="spanel__k">Our Services</span><h3>School</h3><p>Safe and reliable student transportation service.</p><span class="spanel__go">Explore School &rarr;</span></span>
    </a>
  </div>
  <div class="svcnav">
    <button type="button" class="svcnav__btn active" data-svc="personal" aria-label="Personal">
      <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/></svg>
      <span>Personal</span>
    </button>
    <button type="button" class="svcnav__btn" data-svc="corporate" aria-label="Corporate">
      <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5.5A2.5 2.5 0 0 1 10.5 3h3A2.5 2.5 0 0 1 16 5.5V7"/><path d="M3 12h18"/></svg>
      <span>Corporate</span>
    </button>
    <button type="button" class="svcnav__btn" data-svc="airport" aria-label="Airport">
      <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15.5 13 11V4.5a1.5 1.5 0 0 0-3 0V11l-8 4.5v2l8-2.3V19l-2.2 1.6v1.4L11 22l3.2 1v-1.4L12 20v-3.8l9 2.3z"/></svg>
      <span>Airport</span>
    </button>
    <button type="button" class="svcnav__btn" data-svc="school" aria-label="School">
      <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4 2 9l10 5 10-5z"/><path d="M6 11v4.5c0 1.5 2.7 2.8 6 2.8s6-1.3 6-2.8V11"/><path d="M22 9v5"/></svg>
      <span>School</span>
    </button>
  </div>
</section>

<section class="section fleet" id="fleet">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">The Fleet</p>
      <h2 class="section__title">A Vehicle for Every Occasion</h2>
      <p class="section__lead">Immaculately maintained, chauffeur-driven and ready when you are - from the Cadillac Escalade to full-size coaches.</p>
    </div>
    __FLEETGRID__
    <div class="center mt2"><a href="fleet.html" class="btn btn--gold">View the Full Fleet</a></div>
  </div>
</section>

<section class="stats">
  <div class="container grid grid--4 stats__grid">
    <div class="stat"><strong data-count="200">0</strong><span>Vehicles in Our Fleet</span></div>
    <div class="stat"><strong data-count="15">0</strong><span>Years of Experience</span></div>
    <div class="stat"><strong data-count="50000">0</strong><span>Rides Completed</span></div>
    <div class="stat"><strong data-count="24">0</strong><span>Hours a Day, 7 Days</span></div>
  </div>
</section>

<section class="section about" id="about">
  <div class="container about__inner">
    <div class="about__media">
      <img src="assets/about.jpg" alt="Look Limo luxury chauffeured vehicle" />
    </div>
    <div class="about__text">
      <p class="eyebrow">Why Look Limo</p>
      <h2 class="section__title section__title--left">Luxury You Can Count On</h2>
      <p>At Look Limo, transportation is more than getting from A to B - it is an experience built on elegance, comfort and excellence. Our professional chauffeurs, spotless fleet and around-the-clock dispatch mean you always arrive relaxed, on time and in style.</p>
      <ul class="ticks">
        <li>Professional, background-checked chauffeurs</li>
        <li>Real-time flight tracking &amp; on-time guarantee</li>
        <li>Transparent, upfront pricing - no surprises</li>
        <li>Fully licensed, insured &amp; available 24/7</li>
      </ul>
      <a href="about.html" class="btn btn--gold">More About Us</a>
    </div>
  </div>
</section>
{CTA}
"""

# ---- Fleet data (client's exact vehicle list; Escalade first) ----
_PERSON = '<circle cx="12" cy="8" r="3.3"/><path d="M5 20c0-3.6 3-6 7-6s7 2.4 7 6"/>'
FEATURE_ICONS = {
    "Flat-Screen TV": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "Leather Seating": '<path d="M5 11V6a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v5"/><path d="M4 11h16v4a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3z"/><path d="M8 21v-3M16 21v-3"/>',
    "Stereo System": '<circle cx="7" cy="17" r="2.4"/><circle cx="17" cy="15" r="2.4"/><path d="M9.4 17V6l10-2v11"/>',
    "Privacy Panel": '<path d="M12 3l7 3v5c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6z"/>',
    "Privacy Glass": '<path d="M12 3l7 3v5c0 4.5-3 7.6-7 9-4-1.4-7-4.5-7-9V6z"/>',
    "Overhead Luggage": '<rect x="5" y="7" width="14" height="12" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M9 19v2M15 19v2"/>',
    "Power Outlets": '<path d="M9 3v5M15 3v5"/><path d="M6 8h12v2a6 6 0 0 1-12 0z"/><path d="M12 16v5"/>',
    "Reading Lamp": '<path d="M8 3h8l2.4 8h-12.8z"/><path d="M12 11v7"/><path d="M8.5 21h7"/>',
    "Premium Sound": '<rect x="5" y="3" width="14" height="18" rx="2"/><circle cx="12" cy="14" r="3.1"/><circle cx="12" cy="7" r="1"/>',
    "Climate Control": '<path d="M12 2v20M4.5 6l15 12M19.5 6l-15 12"/>',
}
# (name, passengers, [features], image, "or similar" flag)
VEHICLES = [
    ("Cadillac Escalade", 6, ["Leather Seating", "Privacy Glass", "Premium Sound"], "fleet-escalade.jpg", False),
    ("Lincoln Aviator", 3, ["Leather Seating", "Climate Control"], "fleet-aviator.jpg", True),
    ("Chevy Suburban", 6, ["Leather Seating", "Reading Lamp"], "fleet-suburban.jpg", True),
    ("Mercedes Executive Sprinter", 14, ["Flat-Screen TV", "Leather Seating", "Stereo System"], "fleet-sprinter.jpg", True),
    ("Minibus", 24, ["Overhead Luggage", "Reading Lamp"], "fleet-minibus.jpg", False),
    ("Luxury Limo Minibus", 30, ["Flat-Screen TV", "Privacy Panel", "Stereo System"], "fleet-limobus.jpg", False),
    ("Bus", 35, ["Leather Seating", "Overhead Luggage", "Power Outlets"], "fleet-bus.jpg", False),
]

def _svg(inner):
    return f'<svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">{inner}</svg>'

def fleet_cards():
    cards = ""
    for name, pax, feats, img, sim in VEHICLES:
        sim_html = '<span class="vcard__sim">or similar</span>' if sim else ''
        feat_html = ""
        for f in feats:
            feat_html += f'<li>{_svg(FEATURE_ICONS.get(f, ""))}<span>{f}</span></li>'
        cards += f"""      <article class="vcard">
        <div class="vcard__img" style="background-image:url('assets/{img}')">
          <span class="vcard__pax">{_svg(_PERSON)}{pax} Passengers</span>
          <div class="vcard__title"><h3>{name}</h3>{sim_html}</div>
        </div>
        <ul class="vcard__feats">{feat_html}</ul>
      </article>
"""
    return cards

FLEET_CARDS = fleet_cards()

# fleet.html uses a grid; home uses a swipeable carousel
FLEET_GRID = '<div class="grid grid--3 fleet__grid">\n' + FLEET_CARDS + '    </div>'
FLEET_HOME = ('<div class="fleetcarousel">\n'
              '      <button type="button" class="fleetarrow fleetarrow--prev" id="fleetPrev" aria-label="Previous vehicle">&#8249;</button>\n'
              '      <div class="fleetrail" id="fleetRail">\n' + FLEET_CARDS +
              '      </div>\n'
              '      <button type="button" class="fleetarrow fleetarrow--next" id="fleetNext" aria-label="Next vehicle">&#8250;</button>\n'
              '    </div>')

home_body = home_body.replace("__FLEETGRID__", FLEET_HOME)

write("index.html",
      head("Look Limo | Luxury Limousine &amp; Chauffeur Service in Philadelphia",
           "Look Limo - premium limousine and chauffeured car service in Philadelphia, PA. Airport transfers, corporate travel, weddings and events. Elegance. Comfort. Excellence.")
      + header("index.html") + home_body + FOOTER)

# =====================================================================
# ABOUT
# =====================================================================
about_body = pagehero("About <span>Look Limo</span>",
    "Philadelphia's trusted name in luxury chauffeured transportation.",
    {"name": "About", "bg": "fleet-vip.jpg"}) + f"""
<section class="section">
  <div class="container prose center">
    <p class="eyebrow">Our Story</p>
    <h2 class="section__title">Setting the Standard for Luxury Travel in Philadelphia</h2>
    <p>Look Limo was founded on a simple belief: that getting there should feel every bit as special as the occasion itself. From the moment you book to the moment you arrive, our mission is to deliver an experience defined by elegance, comfort and excellence.</p>
    <p>We serve Philadelphia and the surrounding region with a meticulously maintained fleet and a team of professional, background-checked chauffeurs who treat punctuality and discretion as non-negotiable. Whether it is a dawn airport run, a high-stakes client meeting, a wedding or a night on the town, Look Limo is the ride you can rely on.</p>
  </div>
</section>

<section class="section bg-panel section--tight">
  <div class="container">
    <div class="grid grid--3">
      <div class="feat"><div class="feat__ic">&#128110;</div><h3>Professional Chauffeurs</h3><p>Courteous, uniformed, background-checked drivers who know the city and value your time.</p></div>
      <div class="feat"><div class="feat__ic">&#10024;</div><h3>Immaculate Fleet</h3><p>Late-model luxury vehicles, cleaned and inspected before every single ride.</p></div>
      <div class="feat"><div class="feat__ic">&#9200;</div><h3>Always On Time</h3><p>Real-time flight tracking and 24/7 dispatch mean we are ready exactly when you need us.</p></div>
    </div>
  </div>
</section>

<section class="section about">
  <div class="container about__inner">
    <div class="about__media"><img src="assets/about.jpg" alt="Look Limo chauffeured vehicle" /></div>
    <div class="about__text">
      <p class="eyebrow">Why Choose Us</p>
      <h2 class="section__title section__title--left">The Look Limo Difference</h2>
      <p>We obsess over the details other companies overlook - the bottle of water waiting in the door, the chauffeur who steps out to greet you, the route planned around traffic before you even ask.</p>
      <ul class="ticks">
        <li>Transparent, upfront pricing with no hidden fees</li>
        <li>Fully licensed &amp; insured for your peace of mind</li>
        <li>Flexible booking and last-minute availability</li>
        <li>Personalized service for every client and occasion</li>
      </ul>
      <a href="contact.html" class="btn btn--gold">Book Your Ride</a>
    </div>
  </div>
</section>
{CTA}
""".replace("{CTA}", CTA)
write("about.html",
      head("About Us | Look Limo Philadelphia",
           "Learn about Look Limo - Philadelphia's trusted luxury limousine and chauffeured car service. Professional chauffeurs, an immaculate fleet and around-the-clock service.")
      + header("about.html") + about_body + FOOTER)

# =====================================================================
# SERVICES (overview)
# =====================================================================
services_body = pagehero("Our <span>Services</span>",
    "Chauffeured transportation for every journey and occasion in Philadelphia.",
    {"name": "Services", "bg": "svc-corporate.jpg"}) + f"""
<section class="section services">
  <div class="container">
    <div class="grid grid--4 services__grid">
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-personal.jpg')"></div>
        <div class="scard__body"><h3>Personal</h3><p>Convenient and reliable private transportation for everyday journeys and special occasions.</p><a href="personal.html" class="scard__link">Learn More &rarr;</a></div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-airport.jpg')"></div>
        <div class="scard__body"><h3>Airport</h3><p>Prompt airport transportation for any business trip or vacation, with flight tracking and meet-and-greet.</p><a href="airport-transfers.html" class="scard__link">Learn More &rarr;</a></div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-corporate.jpg')"></div>
        <div class="scard__body"><h3>Corporate</h3><p>World-class executive and business transportation handled with discretion and precision.</p><a href="corporate-travel.html" class="scard__link">Learn More &rarr;</a></div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-school.jpg')"></div>
        <div class="scard__body"><h3>School</h3><p>Safe and reliable student transportation with vetted, background-checked chauffeurs.</p><a href="school.html" class="scard__link">Learn More &rarr;</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section bg-panel">
  <div class="container">
    <div class="section__head"><p class="eyebrow">How It Works</p><h2 class="section__title">Booking Is Effortless</h2></div>
    <div class="grid grid--4 steps">
      <div class="step"><div class="step__num"></div><h3>Request</h3><p>Call, email or fill out our quick quote form with your trip details.</p></div>
      <div class="step"><div class="step__num"></div><h3>Confirm</h3><p>We reply fast with availability, the right vehicle and an upfront price.</p></div>
      <div class="step"><div class="step__num"></div><h3>Relax</h3><p>Your chauffeur arrives early, dressed and ready, tracking your schedule.</p></div>
      <div class="step"><div class="step__num"></div><h3>Arrive</h3><p>Sit back and enjoy a smooth, first-class ride to your destination.</p></div>
    </div>
  </div>
</section>
{CTA}
""".replace("{CTA}", CTA)
write("services.html",
      head("Services | Look Limo Philadelphia",
           "Explore Look Limo services in Philadelphia: airport transfers, corporate travel, weddings, events and nights out. Luxury chauffeured transportation for every occasion.")
      + header("services.html") + services_body + FOOTER)

# =====================================================================
# SERVICE DETAIL PAGES
# =====================================================================
def service_page(fname, active_title, hero_title, hero_sub, bg, crumb, intro_h, intro_p, img, feats, price_block=""):
    feat_html = ""
    for ic, h, p in feats:
        feat_html += f'      <div class="feat"><div class="feat__ic">{ic}</div><h3>{h}</h3><p>{p}</p></div>\n'
    body = pagehero(hero_title, hero_sub, {"name": crumb, "bg": bg}) + f"""
<section class="section">
  <div class="container split">
    <div class="split__media"><img src="assets/{img}" alt="{crumb}" /></div>
    <div class="split__text">
      <p class="eyebrow">Look Limo</p>
      <h2 class="section__title section__title--left">{intro_h}</h2>
      {intro_p}
      <a href="contact.html" class="btn btn--gold">Get a Quote</a>
    </div>
  </div>
</section>

<section class="section bg-panel section--tight">
  <div class="container">
    <div class="grid grid--3">
{feat_html}    </div>
  </div>
</section>
{price_block}{CTA}
""".replace("{CTA}", CTA)
    write(fname,
          head(f"{active_title} | Look Limo Philadelphia", hero_sub)
          + header("services.html") + body + FOOTER)

service_page(
    "airport-transfers.html", "Airport Transfers",
    "Airport <span>Transfers</span>",
    "Stress-free rides to and from Philadelphia International (PHL) and beyond.",
    "svc-airport.jpg", "Airport Transfers",
    "On-Time Airport Service, Every Time",
    "<p>Never watch the clock again. Look Limo monitors your flight in real time, adjusts for delays automatically and has your chauffeur waiting when you land - luggage assistance included.</p><p>We serve Philadelphia International (PHL), Newark Liberty (EWR), Trenton-Mercer and other regional airports, with meet-and-greet arrivals and curbside departures.</p>",
    "fleet-sedan.jpg",
    [("&#9992;", "Flight Tracking", "We watch your flight and adjust pickup automatically for early or delayed arrivals."),
     ("&#129309;", "Meet &amp; Greet", "Your chauffeur greets you at arrivals and helps with your luggage."),
     ("&#128176;", "Flat-Rate Pricing", "Know your fare upfront - no surge pricing, no surprises.")])

service_page(
    "corporate-travel.html", "Corporate & Business Travel",
    "Corporate <span>Travel</span>",
    "Executive transportation that reflects your professional standards.",
    "svc-corporate.jpg", "Corporate Travel",
    "Impeccable Travel for Business",
    "<p>From airport pickups for visiting executives to full-day roadshows and client entertainment, Look Limo delivers discreet, dependable corporate transportation across Philadelphia.</p><p>Set up a business account for simplified billing, priority booking and consistent service your whole team can rely on.</p>",
    "fleet-exec.jpg",
    [("&#128188;", "Executive Fleet", "Luxury sedans and SUVs that make the right impression on clients."),
     ("&#128274;", "Discreet &amp; Reliable", "Professional chauffeurs trained in privacy and punctuality."),
     ("&#129534;", "Corporate Accounts", "Simplified billing, priority booking and dedicated support.")])

service_page(
    "personal.html", "Personal Transportation",
    "Personal <span>Transportation</span>",
    "Convenient, reliable private car service for everyday journeys and special occasions.",
    "svc-personal.jpg", "Personal",
    "Private Transportation, On Your Schedule",
    "<p>Whether it's a dinner reservation, a night out, a special celebration or simply getting across town in comfort, Look Limo gives you a professional chauffeur and a spotless luxury vehicle whenever you need one.</p><p>No parking, no ride-share roulette - just a dependable, private ride that arrives on time and treats you like the guest of honor.</p>",
    "svc-personal.jpg",
    [("&#128663;", "Door-to-Door", "Private pickups and drop-offs anywhere in the Philadelphia region."),
     ("&#9200;", "On Your Time", "Available 24/7 for planned trips or last-minute rides."),
     ("&#10024;", "First-Class Comfort", "Immaculate vehicles and courteous, professional chauffeurs.")])

service_page(
    "school.html", "School Transportation",
    "School <span>Transportation</span>",
    "Safe, reliable student transportation families and schools can count on.",
    "svc-school.jpg", "School",
    "Safe, Reliable Student Transportation",
    "<p>Look Limo provides dependable school and student transportation with vetted, background-checked chauffeurs and well-maintained vehicles - so parents and schools have complete peace of mind.</p><p>From daily school runs to field trips and activity transport, we get students where they need to be safely and on time, every time.</p>",
    "svc-school.jpg",
    [("&#128274;", "Safety First", "Background-checked chauffeurs and thoroughly inspected vehicles."),
     ("&#9200;", "Always On Time", "Punctual daily runs and reliable schedules parents can trust."),
     ("&#128652;", "Groups &amp; Trips", "From individual students to field trips and activity transport.")])

# =====================================================================
# FLEET
# =====================================================================
fleet_body = pagehero("Our <span>Fleet</span>",
    "Immaculately maintained luxury vehicles for parties of three to thirty-five.",
    {"name": "Fleet", "bg": "hero.jpg"}) + f"""
<section class="section fleet">
  <div class="container">
    <div class="section__head"><p class="eyebrow">The Fleet</p><h2 class="section__title">A Vehicle for Every Occasion</h2><p class="section__lead">Whatever the trip, we have the right vehicle - all chauffeur-driven and spotless.</p></div>
    {FLEET_GRID}
    <p class="center section__lead mt2">Looking for something specific? <a href="contact.html" style="color:var(--gold-2)">Ask us</a> - our fleet also includes stretch limousines and specialty vehicles on request.</p>
  </div>
</section>
{CTA}
""".replace("{FLEET_GRID}", FLEET_GRID).replace("{CTA}", CTA)
write("fleet.html",
      head("Our Fleet | Look Limo Philadelphia",
           "Explore the Look Limo fleet: luxury sedans, premium SUVs, executive coupes, VIP Rolls-Royce, executive coaches and motor coaches. Chauffeured luxury for every group size.")
      + header("fleet.html") + fleet_body + FOOTER)

# =====================================================================
# FAQ
# =====================================================================
faqs = [
    ("What areas do you serve?", "Look Limo serves Philadelphia and the surrounding region, including all major airports (PHL, Newark, Trenton-Mercer) and destinations throughout Pennsylvania, New Jersey and Delaware. Travelling further? Just ask."),
    ("How do I book a ride?", "You can book by phone at " + PHONE + ", by email at " + EMAIL + ", or by filling out the quick quote form on our Contact page. We confirm availability and pricing fast."),
    ("How far in advance should I reserve?", "We recommend booking as early as possible for weddings and large groups, but we also handle last-minute and same-day requests whenever a vehicle is available - we operate 24/7."),
    ("What does it cost?", "Pricing depends on the vehicle, distance and duration. We provide clear, upfront quotes with no hidden fees or surge pricing. Contact us for a personalized quote."),
    ("Are your chauffeurs licensed and insured?", "Absolutely. Every chauffeur is professionally licensed, background-checked and fully insured, and our vehicles are inspected and maintained to the highest standards."),
    ("Do you offer airport meet-and-greet?", "Yes. For airport arrivals, your chauffeur tracks your flight and meets you at the terminal, ready to help with luggage - all included in the service."),
    ("How many passengers can you accommodate?", "From a single traveller in a luxury sedan to 55 guests in a motor coach. Tell us your group size and occasion and we'll recommend the ideal vehicle."),
    ("What is your cancellation policy?", "We keep it fair and flexible. Reach out as soon as your plans change and we'll work with you - full details are shared at the time of booking."),
]
faq_items = ""
for q, a in faqs:
    faq_items += f"""    <div class="faq__item">
      <button class="faq__q">{q} <span class="pm">+</span></button>
      <div class="faq__a"><p>{a}</p></div>
    </div>
"""
faq_body = pagehero("Frequently Asked <span>Questions</span>",
    "Everything you need to know about riding with Look Limo.",
    {"name": "FAQ", "bg": "svc-events.jpg"}) + f"""
<section class="section">
  <div class="container">
    <div class="faq">
{faq_items}    </div>
  </div>
</section>
{CTA}
""".replace("{CTA}", CTA)
write("faq.html",
      head("FAQ | Look Limo Philadelphia",
           "Frequently asked questions about Look Limo's luxury limousine and chauffeured car service in Philadelphia - booking, pricing, service areas, airport pickups and more.")
      + header("faq.html") + faq_body + FOOTER)

# =====================================================================
# CONTACT
# =====================================================================
contact_body = pagehero("Contact <span>Look Limo</span>",
    "Request a quote or book your ride - we reply fast, 24/7.",
    {"name": "Contact", "bg": "fleet-exec.jpg"}) + f"""
<section class="section quote" id="quote">
  <div class="container contactgrid">
    <div class="quote__info">
      <p class="eyebrow">Get In Touch</p>
      <h2 class="section__title section__title--left">Request a Quote</h2>
      <p style="color:var(--muted);font-weight:300;margin-bottom:2rem">Tell us where you are going and we will get right back to you with availability and a price. Prefer to talk? Call or email us anytime - we are available around the clock.</p>
      <div class="infoblock"><span class="ic">&#9742;</span><div><h4>Call Us</h4><a href="tel:{PHONE_TEL}">{PHONE}</a></div></div>
      <div class="infoblock"><span class="ic">&#9993;</span><div><h4>Email Us</h4><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
      <div class="infoblock"><span class="ic">&#128205;</span><div><h4>Service Area</h4><p>Philadelphia, PA &amp; surrounding region</p></div></div>
      <div class="infoblock"><span class="ic">&#9200;</span><div><h4>Hours</h4><p>24 hours a day, 7 days a week</p></div></div>
    </div>
    <form class="quote__form" id="quoteForm" onsubmit="return handleQuote(event)">
      <div class="frow">
        <input type="text" name="name" placeholder="Full Name" required />
        <input type="tel" name="phone" placeholder="Phone Number" required />
      </div>
      <input type="email" name="email" placeholder="Email Address" required />
      <div class="frow">
        <select name="service" required>
          <option value="" disabled selected>Service Type</option>
          <option>Personal</option>
          <option>Airport</option>
          <option>Corporate / Business</option>
          <option>School / Student</option>
          <option>Other</option>
        </select>
        <input type="text" name="date" placeholder="Date &amp; Time" onfocus="(this.type='datetime-local')" onblur="if(!this.value)this.type='text'" required />
      </div>
      <div class="frow">
        <input type="text" name="pickup" placeholder="Pickup Location" required />
        <input type="text" name="dropoff" placeholder="Drop-off Location" required />
      </div>
      <textarea name="notes" placeholder="Passengers, special requests, etc." rows="3"></textarea>
      <button type="submit" class="btn btn--gold btn--block btn--lg">Request My Quote</button>
      <p class="formnote" id="formNote"></p>
    </form>
  </div>
</section>

<section class="section--tight" style="padding-bottom:5rem">
  <div class="container">
    <div class="mapwrap">
      <iframe title="Philadelphia service area" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=-75.28%2C39.87%2C-74.96%2C40.14&amp;layer=mapnik&amp;marker=39.9526%2C-75.1652"></iframe>
    </div>
  </div>
</section>
{CTA}
""".replace("{CTA}", CTA)
write("contact.html",
      head("Contact | Look Limo Philadelphia",
           "Contact Look Limo for luxury limousine and chauffeured car service in Philadelphia. Call " + PHONE + ", email " + EMAIL + ", or request a quote online. Available 24/7.")
      + header("contact.html") + contact_body + FOOTER)

print("\nAll pages generated.")
