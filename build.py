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
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet" />
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
      <a href="airport-transfers.html">Airport Transfers</a>
      <a href="corporate-travel.html">Corporate &amp; Business</a>
      <a href="weddings-events.html">Weddings &amp; Events</a>
      <a href="nights-out.html">Nights Out &amp; Events</a>
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
  <div class="hero__overlay"></div>
  <div class="container hero__inner">
    <p class="hero__eyebrow">Philadelphia's Luxury Chauffeured Transportation</p>
    <h1 class="hero__title">Arrive in <span>Style.</span><br />Travel in Comfort.</h1>
    <p class="hero__sub">Look Limo delivers first-class limousine and car service across Philadelphia - airport transfers, corporate travel, weddings and every occasion that deserves to be unforgettable.</p>
    <div class="hero__cta">
      <a href="contact.html" class="btn btn--gold btn--lg">Book Your Ride</a>
      <a href="tel:{PHONE_TEL}" class="btn btn--ghost btn--lg">&#9742; Call {PHONE}</a>
    </div>
    <div class="hero__trust">
      <div class="trust"><strong>200+</strong><span>Luxury Vehicles</span></div>
      <div class="trust"><strong>24/7</strong><span>Availability</span></div>
      <div class="trust"><strong>5&#9733;</strong><span>Chauffeur Service</span></div>
    </div>
  </div>
</section>

<section class="section services" id="services">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">What We Offer</p>
      <h2 class="section__title">Our Services</h2>
      <p class="section__lead">From the runway to the red carpet, every ride with Look Limo is polished, punctual and effortless.</p>
    </div>
    <div class="grid grid--4 services__grid">
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-airport.jpg')"></div>
        <div class="scard__body">
          <h3>Airport Transfers</h3>
          <p>On-time pickups and drop-offs for PHL Philadelphia International, Newark and beyond, with flight tracking and meet-and-greet.</p>
          <a href="airport-transfers.html" class="scard__link">Learn More &rarr;</a>
        </div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-corporate.jpg')"></div>
        <div class="scard__body">
          <h3>Corporate &amp; Business</h3>
          <p>Executive travel that reflects your standards - discreet, reliable chauffeurs for meetings, roadshows and clients.</p>
          <a href="corporate-travel.html" class="scard__link">Learn More &rarr;</a>
        </div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-wedding.jpg')"></div>
        <div class="scard__body">
          <h3>Weddings &amp; Events</h3>
          <p>Make your day flawless with elegant vehicles, red-carpet arrivals and a chauffeur dedicated to the details.</p>
          <a href="weddings-events.html" class="scard__link">Learn More &rarr;</a>
        </div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-events.jpg')"></div>
        <div class="scard__body">
          <h3>Nights Out &amp; Events</h3>
          <p>Concerts, dinners, city tours or a night on the town - travel together in comfort and let us handle the driving.</p>
          <a href="nights-out.html" class="scard__link">Learn More &rarr;</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section fleet" id="fleet">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">The Fleet</p>
      <h2 class="section__title">A Vehicle for Every Occasion</h2>
      <p class="section__lead">Immaculately maintained, chauffeur-driven and ready when you are - from luxury sedans to full-size coaches.</p>
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

FLEET_GRID = """<div class="grid grid--3 fleet__grid">
      <article class="fcard">
        <div class="fcard__img" style="background-image:url('assets/fleet-sedan.jpg')"></div>
        <div class="fcard__body"><span class="fcard__cap">Up to 3 Passengers</span><h3>Luxury Sedan</h3><p>Mercedes-Benz &amp; BMW class sedans for airport runs and business travel.</p></div>
      </article>
      <article class="fcard">
        <div class="fcard__img" style="background-image:url('assets/fleet-suv.jpg')"></div>
        <div class="fcard__body"><span class="fcard__cap">Up to 6 Passengers</span><h3>Premium SUV</h3><p>Cadillac Escalade &amp; full-size SUVs - space, presence and comfort.</p></div>
      </article>
      <article class="fcard">
        <div class="fcard__img" style="background-image:url('assets/fleet-exec.jpg')"></div>
        <div class="fcard__body"><span class="fcard__cap">Up to 3 Passengers</span><h3>Executive Coupe</h3><p>Sleek performance coupes for a bold, first-class arrival.</p></div>
      </article>
      <article class="fcard">
        <div class="fcard__img" style="background-image:url('assets/fleet-vip.jpg')"></div>
        <div class="fcard__body"><span class="fcard__cap">Up to 3 Passengers</span><h3>VIP Rolls-Royce</h3><p>The ultimate statement for weddings, galas and VIP occasions.</p></div>
      </article>
      <article class="fcard">
        <div class="fcard__img" style="background-image:url('assets/fleet-coach.jpg')"></div>
        <div class="fcard__body"><span class="fcard__cap">Up to 30 Passengers</span><h3>Executive Coach</h3><p>Luxury coach with reclining seating for corporate groups and tours.</p></div>
      </article>
      <article class="fcard">
        <div class="fcard__img" style="background-image:url('assets/fleet-motorcoach.jpg')"></div>
        <div class="fcard__body"><span class="fcard__cap">Up to 55 Passengers</span><h3>Motor Coach</h3><p>Full-size motor coach for large groups, events and long-distance travel.</p></div>
      </article>
    </div>"""

home_body = home_body.replace("__FLEETGRID__", FLEET_GRID)

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
        <div class="scard__img" style="background-image:url('assets/svc-airport.jpg')"></div>
        <div class="scard__body"><h3>Airport Transfers</h3><p>Reliable rides to and from PHL, Newark and regional airports with flight tracking and meet-and-greet.</p><a href="airport-transfers.html" class="scard__link">Learn More &rarr;</a></div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-corporate.jpg')"></div>
        <div class="scard__body"><h3>Corporate &amp; Business</h3><p>Executive travel, roadshows and client transport handled with discretion and precision.</p><a href="corporate-travel.html" class="scard__link">Learn More &rarr;</a></div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-wedding.jpg')"></div>
        <div class="scard__body"><h3>Weddings &amp; Events</h3><p>Elegant wedding transportation and special-event packages built around your big day.</p><a href="weddings-events.html" class="scard__link">Learn More &rarr;</a></div>
      </article>
      <article class="scard">
        <div class="scard__img" style="background-image:url('assets/svc-events.jpg')"></div>
        <div class="scard__body"><h3>Nights Out &amp; Events</h3><p>Concerts, dinners, sporting events, city tours and nights on the town, done in style.</p><a href="nights-out.html" class="scard__link">Learn More &rarr;</a></div>
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
    "weddings-events.html", "Weddings & Events",
    "Weddings &amp; <span>Events</span>",
    "Make your special day flawless with elegant wedding transportation.",
    "svc-wedding.jpg", "Weddings & Events",
    "Your Perfect Day Deserves a Perfect Ride",
    "<p>From the first look to the last dance, Look Limo makes sure every arrival is unforgettable. Choose our VIP Rolls-Royce or a spacious coach for the whole wedding party.</p><p>We coordinate timing with your planner, decorate on request and provide a dedicated chauffeur devoted entirely to your celebration.</p>",
    "fleet-vip.jpg",
    [("&#128141;", "Wedding Packages", "Tailored packages for the couple, party and guests."),
     ("&#127881;", "Red-Carpet Arrivals", "Grand entrances and exits worthy of the occasion."),
     ("&#128197;", "Dedicated Coordination", "We sync with your schedule so everything runs on time.")])

service_page(
    "nights-out.html", "Nights Out & Events",
    "Nights Out &amp; <span>Events</span>",
    "Concerts, dinners, sporting events and nights on the town - in style.",
    "svc-events.jpg", "Nights Out",
    "Enjoy the Night - We'll Handle the Driving",
    "<p>Heading to a concert, a game, a birthday or a night out with friends? Travel together in comfort and never worry about parking, traffic or a designated driver.</p><p>From intimate dinners to full party-coach celebrations, Look Limo keeps the good times rolling safely across Philadelphia.</p>",
    "fleet-motorcoach.jpg",
    [("&#127908;", "Concerts &amp; Games", "Door-to-door service to every venue in the region."),
     ("&#127862;", "Celebrations", "Birthdays, bachelor/ette parties and nights on the town."),
     ("&#128100;", "Safe &amp; Simple", "No parking, no driving - just enjoy the evening.")])

# =====================================================================
# FLEET
# =====================================================================
fleet_body = pagehero("Our <span>Fleet</span>",
    "Immaculately maintained luxury vehicles for parties of one to fifty-five.",
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
          <option>Airport Transfer</option>
          <option>Corporate / Business</option>
          <option>Wedding / Event</option>
          <option>Night Out / Event</option>
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
