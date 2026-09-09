#!/usr/bin/env python3
"""Look Limo city landing pages: Philadelphia, New Jersey, New York.

Imported by build.py, which calls build_city_pages() at the end.

WHY THIS FILE EXISTS SEPARATELY: these three pages are for review before they
go live, so they are written into preview/ and are NOT in the site navigation.
Everything about the chrome - head, topbar, header, footer, CTA - is reused
from build.py rather than copied, so a later change to the header reaches these
pages too. Copying it would have looked identical today and drifted by the
first edit.

The `base` argument is what makes both possible. Pages in preview/ need "../"
in front of every asset and link; the same function called with base="" writes
them at the site root once the client approves. So approving does not mean
rewriting them - it means changing one argument.

CONTACT DETAILS: the client sent looklimousine@gmail.com, (610) 638-4083 and
(484) 478-2931 with this request. The rest of the site still carries the older
looklimo@gmail.com / 929-213-8083. These pages use the NEW ones because they
are what he sent for these pages; the discrepancy is flagged to him rather than
silently applied to eleven other live pages.
"""
# NOT `import build`. build.py is the entry point, so it runs as __main__;
# importing it by name would execute the whole file a SECOND time as a separate
# module object - every page written twice, and a circular import on top. It
# hands itself in instead.
build = None

PHONE_1 = "(610) 638-4083"
PHONE_1_TEL = "+16106384083"
PHONE_2 = "(484) 478-2931"
PHONE_2_TEL = "+14844782931"
CITY_EMAIL = "looklimousine@gmail.com"


# ---------------------------------------------------------------------------
# Line icons, gold stroke, drawn to the same 24x24 grid as build.FEATURE_ICONS
# and the .svcnav buttons.
#
# NOT emoji. The first build used them and half rendered as flat monochrome
# glyphs while the other half came back as full-colour vendor emoji - a blue
# briefcase and a red alarm clock next to a gold aeroplane. It reads as cheap
# on a luxury brand page, and which ones go colour depends on the device, so
# it cannot be checked once and trusted.
# ---------------------------------------------------------------------------
def ico(inner):
    return ('<span class="feat__ic feat__ic--svg"><svg viewBox="0 0 24 24" '
            'stroke-linecap="round" stroke-linejoin="round">' + inner + '</svg></span>')


I_PLANE = '<path d="M12 2.6c.85 0 1.4.75 1.4 1.7v4.1l6.9 3.9v1.9l-6.9-2v4.2l2.3 1.7v1.6L12 18.7l-3.7 1v-1.6l2.3-1.7v-4.2l-6.9 2v-1.9l6.9-3.9V4.3c0-.95.55-1.7 1.4-1.7z"/>'
I_BRIEF = '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5.2A2 2 0 0 1 11 3.2h2a2 2 0 0 1 2 2V7"/><path d="M3 12.4h18"/>'
I_CLOCK = '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.1V12l3.3 2"/>'
I_ROUTE = '<circle cx="5.2" cy="17.4" r="2.3"/><circle cx="18.8" cy="6.6" r="2.3"/><path d="M7 15.8c1.7-3.1 4.6-5.4 9.4-6.7"/><path d="M13.4 9.2l3-.3-.5 3"/>'
I_RINGS = '<circle cx="9" cy="14.4" r="4.8"/><circle cx="15" cy="14.4" r="4.8"/><path d="M12 4.2l2 2.7h-4z"/>'
I_TICKET = '<path d="M3 9.2V6.4a1.2 1.2 0 0 1 1.2-1.2h15.6A1.2 1.2 0 0 1 21 6.4v2.8a2.9 2.9 0 0 0 0 5.6v2.8a1.2 1.2 0 0 1-1.2 1.2H4.2A1.2 1.2 0 0 1 3 17.6v-2.8a2.9 2.9 0 0 0 0-5.6z"/><path d="M14.6 5.2v13.6"/>'
I_HOTEL = '<path d="M3.2 20.6V5.2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v15.4"/><path d="M15.2 20.6V10.4h3.6a2 2 0 0 1 2 2v8.2"/><path d="M2 20.6h20"/><path d="M7 7.2h2M7 11h2M7 14.8h2"/>'
I_GROUP = '<circle cx="8.6" cy="8" r="3"/><path d="M2.8 20c0-3.2 2.6-5.4 5.8-5.4S14.4 16.8 14.4 20"/><path d="M15.6 7.3a3 3 0 0 1 0 5.5"/><path d="M17.2 14.4c2 .7 3.5 2.6 3.5 5.6"/>'

I_SHIELD = '<path d="M12 3l7.8 3.1v5.2c0 4.7-3.3 8-7.8 9.3-4.5-1.3-7.8-4.6-7.8-9.3V6.1z"/><path d="M8.8 12.1l2.2 2.2 4.4-4.4"/>'
I_TAG = '<path d="M20.6 12.6l-8 8a1.9 1.9 0 0 1-2.7 0L3.8 14.5a1.9 1.9 0 0 1-.6-1.4V4.6a1 1 0 0 1 1-1h8.5a1.9 1.9 0 0 1 1.4.6l6.5 6.5a1.9 1.9 0 0 1 0 2.9z"/><circle cx="8" cy="8" r="1.5"/>'
I_24H = '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.1V12l3.3 2"/><path d="M12 1.8v1.6M12 20.6v1.6M1.8 12h1.6M20.6 12h1.6"/>'
I_TRACK = '<path d="M21.4 3.6L2.6 10.3l7.1 2.6 2.6 7.1z"/><path d="M21.4 3.6L9.7 12.9"/>'
I_SPARK = '<path d="M11 3l2 5.4 5.4 2-5.4 2-2 5.4-2-5.4-5.4-2 5.4-2z"/><path d="M18.4 15.4l.7 1.9 1.9.7-1.9.7-.7 1.9-.7-1.9-1.9-.7 1.9-.7z"/>'
I_HEADSET = '<path d="M4.2 13.4v-1.2a7.8 7.8 0 0 1 15.6 0v1.2"/><path d="M4.2 13.4h2.4a1 1 0 0 1 1 1v3.8a1 1 0 0 1-1 1H5.7a1.5 1.5 0 0 1-1.5-1.5z"/><path d="M19.8 13.4h-2.4a1 1 0 0 0-1 1v3.8a1 1 0 0 0 1 1h.5a1.9 1.9 0 0 0 1.9-1.9z"/>'


# ---------------------------------------------------------------------------
# The eight services the client listed, verbatim from his message.
# ---------------------------------------------------------------------------
SERVICES = [
    (ico(I_PLANE), "Airport Transportation",
     "Meet-and-greet arrivals, real-time flight tracking and curbside departures "
     "at every airport we serve. Your chauffeur adjusts automatically when your "
     "flight moves."),
    (ico(I_BRIEF), "Corporate Transportation",
     "Executive travel for client visits, roadshows and board meetings, with "
     "corporate accounts, consolidated billing and priority booking for your team."),
    (ico(I_CLOCK), "Hourly Car Service",
     "Keep a chauffeur and vehicle on hand by the hour. Multiple stops, waiting "
     "time and changes of plan are all part of the booking, not extras."),
    (ico(I_ROUTE), "City-to-City Transportation",
     "Direct point-to-point travel between Philadelphia, New Jersey, New York, "
     "Washington DC and beyond - no terminals, no connections, no waiting."),
    (ico(I_RINGS), "Wedding Transportation",
     "Transport for the couple, the wedding party and guests, planned to the "
     "minute around your ceremony, photographs and reception."),
    (ico(I_TICKET), "Event Transportation",
     "Concerts, games, galas, proms and conferences - arrivals coordinated so "
     "your whole party gets there together and leaves without hunting for a ride."),
    (ico(I_HOTEL), "Hotel Transportation",
     "Guest shuttles and door-to-door hotel transfers for visiting travellers, "
     "conference attendees and hospitality partners."),
    (ico(I_GROUP), "Group Transportation",
     "From three passengers to thirty-five in a single vehicle, and larger "
     "parties across multiple vehicles moving on one schedule."),
]


# ---------------------------------------------------------------------------
# Airports. Every entry is a real, currently-operating commercial or executive
# airport in the region named. The three-letter code is the IATA code, which is
# what a passenger reads off their own ticket - it is the useful thing to show,
# not decoration.
# ---------------------------------------------------------------------------
CITIES = [
    {
        "slug": "philadelphia",
        "name": "Philadelphia",
        "title": "Philadelphia <span>Limo Service</span>",
        "state": "Philadelphia, PA",
        "sub": "Chauffeured luxury transportation across Philadelphia, the Main Line "
               "and the surrounding counties - 24 hours a day.",
        "bg": "hero-image.jpg",
        # The client asked for THIS photograph to move off the home page and
        # onto Philadelphia - it is a Philadelphia picture: his own LOOK LIMO
        # Pennsylvania plate, the PHL airport sign, the city skyline behind.
        "hero_img": "hero-image.jpg",
        "hero_alt": "Look Limo Cadillac Escalade at Philadelphia International Airport with the Philadelphia skyline",
        "split_img": "fleet-escalade.jpg",
        "meta": "Look Limo provides chauffeured limousine and car service across "
                "Philadelphia and the surrounding region - PHL airport transfers, "
                "corporate travel, hourly service, weddings, events and group "
                "transportation. Available 24/7.",
        "intro_h": "Philadelphia's Chauffeured Car Service",
        "intro_p": [
            "Look Limo is a Philadelphia-based chauffeured transportation company "
            "serving the city and the whole surrounding region. We cover Center "
            "City and every neighbourhood around it, the Main Line, and the "
            "suburban counties - and we are on the road 24 hours a day, seven "
            "days a week.",
            "Every ride is a professional chauffeur in a spotless, fully insured "
            "vehicle, quoted upfront. No surge pricing, no ride-share roulette, "
            "and no wondering whether the car will actually turn up.",
        ],
        "areas_h": "Areas We Cover in and around Philadelphia",
        "areas": [
            "Center City, Old City &amp; Rittenhouse Square",
            "University City, Fishtown &amp; Northern Liberties",
            "Manayunk, Chestnut Hill &amp; Roxborough",
            "South Philadelphia &amp; the Stadium District",
            "The Main Line - Bala Cynwyd, Ardmore, Bryn Mawr, Villanova, Wayne",
            "King of Prussia, Conshohocken &amp; Plymouth Meeting",
            "Montgomery, Bucks, Delaware &amp; Chester counties",
            "Doylestown, Media, Norristown &amp; Bensalem",
        ],
        "airports": [
            ("PHL", "Philadelphia International Airport",
             "Our home airport. Meet-and-greet at baggage claim for arrivals, "
             "curbside for departures, all terminals A through F."),
            ("PNE", "Northeast Philadelphia Airport",
             "General aviation and private charter on the north side of the city."),
            ("TTN", "Trenton-Mercer Airport",
             "Ewing, NJ - about 40 minutes from Center City, and often the "
             "quicker option for the northern suburbs."),
            ("ABE", "Lehigh Valley International",
             "Allentown, PA - serving clients heading north through Bucks and "
             "Lehigh counties."),
            ("ILG", "Wilmington / New Castle Airport",
             "Wilmington, DE - convenient for Delaware County and the "
             "I-95 corridor south of the city."),
            ("EWR", "Newark Liberty International",
             "New Jersey - regularly booked from Philadelphia for international "
             "departures and long-haul connections."),
        ],
    },
    {
        "slug": "new-jersey",
        "name": "New Jersey",
        "title": "New Jersey <span>Limo Service</span>",
        "state": "New Jersey",
        "sub": "Chauffeured transportation across North, Central and South Jersey - "
               "airports, corporate travel, weddings and the Shore.",
        "bg": "fleet-sprinter.jpg",
        # No New Jersey photograph exists yet - flagged to the client.
        "hero_img": "fleet-sprinter.jpg",
        "hero_alt": "Look Limo Mercedes Executive Sprinter",
        "split_img": "fleet-suburban.jpg",
        "meta": "Look Limo provides chauffeured limousine and car service throughout "
                "New Jersey - Newark Liberty (EWR), Teterboro, Atlantic City and "
                "Trenton-Mercer transfers, corporate travel, hourly service, "
                "weddings, events and group transportation. Available 24/7.",
        "intro_h": "Chauffeured Travel Across New Jersey",
        "intro_p": [
            "New Jersey is a state you cross constantly, and traffic on the "
            "Turnpike or the Parkway can turn a simple trip into a stressful one. "
            "Look Limo takes that off your hands: a professional chauffeur who "
            "knows the routes, watches the traffic and plans around it.",
            "We work the whole state - the North Jersey corporate corridor, the "
            "Princeton and Trenton area in the centre, and South Jersey down to "
            "Atlantic City and the Shore - as well as every crossing into "
            "Philadelphia and New York.",
        ],
        "areas_h": "Areas We Cover Across New Jersey",
        "areas": [
            "Newark, Jersey City, Hoboken &amp; the Gold Coast",
            "Paramus, Hackensack &amp; Bergen County",
            "Morristown, Short Hills, Montclair &amp; Essex County",
            "Princeton, Trenton &amp; Mercer County",
            "Edison, Woodbridge &amp; Middlesex County",
            "Cherry Hill, Camden &amp; the Philadelphia side of the river",
            "Atlantic City, Cape May &amp; the Jersey Shore",
            "Freehold, Toms River &amp; Monmouth and Ocean counties",
        ],
        "airports": [
            ("EWR", "Newark Liberty International",
             "New Jersey's main international gateway. Meet-and-greet arrivals in "
             "all three terminals, with flight tracking included."),
            ("TEB", "Teterboro Airport",
             "The region's busiest executive airport - private aviation, minutes "
             "from Manhattan and the Bergen County corporate belt."),
            ("TTN", "Trenton-Mercer Airport",
             "Ewing, NJ - the practical choice for Princeton, Trenton and "
             "Bucks County travellers."),
            ("ACY", "Atlantic City International",
             "Egg Harbor Township - serving Atlantic City, Cape May and the "
             "southern Shore."),
            ("MMU", "Morristown Municipal Airport",
             "Executive and charter traffic for the Morris County business "
             "corridor."),
            ("PHL", "Philadelphia International",
             "Regularly booked from South and Central Jersey, and often faster "
             "than heading north."),
        ],
    },
    {
        "slug": "new-york",
        "name": "New York",
        "title": "New York <span>Limo Service</span>",
        "state": "New York",
        "sub": "Chauffeured transportation in Manhattan, the boroughs, Long Island, "
               "Westchester and the Hudson Valley.",
        "bg": "fleet-aviator.jpg",
        # No New York photograph exists yet - flagged to the client.
        "hero_img": "fleet-escalade.jpg",
        "hero_alt": "Look Limo Cadillac Escalade on a city street at night",
        "split_img": "fleet-limobus.jpg",
        "meta": "Look Limo provides chauffeured limousine and car service across New "
                "York - JFK, LaGuardia, Newark, Westchester and Long Island "
                "MacArthur transfers, corporate travel, hourly service, weddings, "
                "events and group transportation. Available 24/7.",
        "intro_h": "Chauffeured Travel in New York",
        "intro_p": [
            "New York punishes anyone who is improvising. Look Limo gives you a "
            "chauffeur who knows the bridges, the tunnels and the crosstown "
            "timings, and a vehicle waiting where it said it would be - whether "
            "that is a midtown kerb, a JFK terminal or a house on Long Island.",
            "We cover all five boroughs, Long Island out to the Hamptons, "
            "Westchester and the lower Hudson Valley, and we run the "
            "New York to Philadelphia and New York to New Jersey corridors "
            "constantly.",
        ],
        "areas_h": "Areas We Cover Across New York",
        "areas": [
            "Manhattan - Midtown, Downtown, Upper East &amp; Upper West Side",
            "Brooklyn, Queens, The Bronx &amp; Staten Island",
            "Long Island - Nassau &amp; Suffolk counties",
            "The Hamptons, Montauk &amp; the East End",
            "Westchester - White Plains, Yonkers, Scarsdale &amp; Rye",
            "New Rochelle, Mount Vernon &amp; the Sound Shore",
            "Rockland County &amp; the lower Hudson Valley",
            "Direct runs to Philadelphia, New Jersey &amp; Connecticut",
        ],
        "airports": [
            ("JFK", "John F. Kennedy International",
             "Queens - meet-and-greet at arrivals in every terminal, with your "
             "flight tracked so delays do not cost you a car."),
            ("LGA", "LaGuardia Airport",
             "Queens - the closest airport to Midtown, and the one where a "
             "pre-booked chauffeur saves the most time."),
            ("EWR", "Newark Liberty International",
             "New Jersey - a New York gateway in everything but address, and "
             "one we cover from either side of the river."),
            ("HPN", "Westchester County Airport",
             "White Plains - commercial and executive traffic for Westchester "
             "and Fairfield County."),
            ("ISP", "Long Island MacArthur Airport",
             "Islip - the practical airport for Suffolk County and the East End."),
            ("SWF", "New York Stewart International",
             "Newburgh - serving the Hudson Valley and the northern suburbs."),
            ("TEB", "Teterboro Airport",
             "New Jersey - the region's main private-aviation field, minutes "
             "from Manhattan."),
        ],
    },
]


WHY = [
    (ico(I_SHIELD), "Licensed &amp; Fully Insured",
     "Every chauffeur is professionally licensed and background-checked, and "
     "every vehicle is inspected, maintained and insured."),
    (ico(I_TAG), "Upfront, Flat-Rate Pricing",
     "You are quoted a price before you book and that is the price. No surge "
     "pricing, no meter running in traffic, no surprises at the end."),
    (ico(I_24H), "Available 24 Hours a Day",
     "Early flights, late arrivals, last-minute changes and same-day requests. "
     "We answer the phone at four in the morning."),
    (ico(I_TRACK), "We Watch Your Flight",
     "Airport pickups are tracked in real time and your pickup moves "
     "automatically when your flight does - at no extra charge."),
    (ico(I_SPARK), "An Immaculate Fleet",
     "Late-model black vehicles kept spotless inside and out, from a Cadillac "
     "Escalade to a thirty-five seat coach."),
    (ico(I_HEADSET), "A Real Person Answers",
     "You deal with our team directly, not an app queue - and the same team "
     "sees your booking through from quote to drop-off."),
]

BOOK_STEPS = [
    ("Tell Us the Trip",
     "Call, email or send the quote form - where you are going, when, and how "
     "many of you there are."),
    ("Get a Firm Price",
     "We come back fast with the right vehicle and a flat, all-in price. "
     "Nothing is charged and nothing is final until you say yes."),
    ("We Confirm It",
     "You get written confirmation with your chauffeur's details, and we "
     "re-confirm ahead of the pickup."),
    ("Ride",
     "Your chauffeur arrives early. On airport pickups we are already tracking "
     "your flight before you land."),
]


def _btn_row(base, big=False):
    """Book Now / Call Now / Request a Quote - the three the client asked for.

    Reuses .hero__cta, which is the flex row already used on the home hero, so
    these wrap sensibly on a phone instead of overflowing. Rendered more than
    once per page on purpose: on a long landing page a visitor who is convinced
    at the airports section should not have to scroll back to the top.
    """
    lg = " btn--lg" if big else ""
    return f"""
      <div class="hero__cta">
        <a href="{base}booking.html" class="btn btn--gold{lg}">Book Now</a>
        <a href="tel:{PHONE_1_TEL}" class="btn btn--ghost{lg}">&#9742; Call Now</a>
        <a href="{base}contact.html" class="btn btn--ghost{lg}">Request a Quote</a>
      </div>
"""


def _topbar(base):
    """Same shape as build.header()'s topbar, with the new contact details."""
    return f"""
<div class="topbar">
  <div class="container topbar__inner">
    <div class="topbar__left">
      <a href="tel:{PHONE_1_TEL}" class="topbar__item"><span class="ic">&#9742;</span> {PHONE_1}</a>
      <a href="tel:{PHONE_2_TEL}" class="topbar__item"><span class="ic">&#9742;</span> {PHONE_2}</a>
      <a href="mailto:{CITY_EMAIL}" class="topbar__item"><span class="ic">&#9993;</span> {CITY_EMAIL}</a>
    </div>
    <div class="topbar__right">
      <span class="topbar__tag">Philadelphia &middot; New Jersey &middot; New York</span>
    </div>
  </div>
</div>
"""


def _header(base):
    links = ""
    for label, href in build.NAV:
        links += f'      <a href="{base}{href}" class="nav__link">{label}</a>\n'
    return f"""
<header class="header" id="header">
  <div class="container header__inner">
    <a href="{base}index.html" class="brand">
      <img src="{base}assets/logo.jpg" alt="Look Limo" class="brand__logo" />
    </a>
    <nav class="nav" id="nav">
{links}      <a href="{base}contact.html" class="btn btn--gold nav__cta">Get a Quote</a>
    </nav>
    <button class="nav__toggle" id="navToggle" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
"""


def _footer(base, city):
    return f"""
<footer class="footer">
  <div class="container footer__inner">
    <div class="footer__col footer__brand">
      <img src="{base}assets/logo.jpg" alt="Look Limo" class="footer__logo" />
      <p>Elegance. Comfort. Excellence. Chauffeured luxury transportation across
         Philadelphia, New Jersey and New York.</p>
    </div>
    <div class="footer__col">
      <h4>Service Areas</h4>
      <a href="philadelphia.html">Philadelphia</a>
      <a href="new-jersey.html">New Jersey</a>
      <a href="new-york.html">New York</a>
    </div>
    <div class="footer__col">
      <h4>Company</h4>
      <a href="{base}about.html">About Us</a>
      <a href="{base}fleet.html">Our Fleet</a>
      <a href="{base}booking.html">Book a Ride</a>
      <a href="{base}faq.html">FAQ</a>
      <a href="{base}contact.html">Get a Quote</a>
    </div>
    <div class="footer__col">
      <h4>Contact</h4>
      <a href="tel:{PHONE_1_TEL}">{PHONE_1}</a>
      <a href="tel:{PHONE_2_TEL}">{PHONE_2}</a>
      <a href="mailto:{CITY_EMAIL}">{CITY_EMAIL}</a>
      <span>{city['state']}</span>
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

<a href="tel:{PHONE_1_TEL}" class="fab" aria-label="Call Look Limo">&#9742;</a>

<script src="{base}script.js"></script>
</body>
</html>
"""


def city_page(city, base="../", out_dir="preview"):
    """One city landing page. base="" + out_dir="." puts it at the site root."""
    esc_name = city["name"]

    airports = ""
    for code, name, blurb in city["airports"]:
        airports += (
            f'      <div class="feat">\n'
            f'        <div class="feat__ic gold-text">{code}</div>\n'
            f'        <h3>{name}</h3>\n'
            f'        <p>{blurb}</p>\n'
            f'      </div>\n')

    services = ""
    for ic, name, blurb in SERVICES:
        services += (f'      <div class="feat">{ic}'
                     f'<h3>{name}</h3><p>{blurb}</p></div>\n')

    why = ""
    for ic, name, blurb in WHY:
        why += (f'      <div class="feat">{ic}'
                f'<h3>{name}</h3><p>{blurb}</p></div>\n')

    steps = ""
    for h, p in BOOK_STEPS:
        steps += (f'      <div class="step"><div class="step__num"></div>'
                  f'<h3>{h}</h3><p>{p}</p></div>\n')

    areas = "".join(f"        <li>{a}</li>\n" for a in city["areas"])
    intro = "".join(f"      <p>{p}</p>\n" for p in city["intro_p"])

    # The home page hero is three stacked lines - a script "Welcome to", the
    # name in big gold, then a tagline - over black, with the video band and a
    # full-width photograph beneath. These pages now use exactly that, with the
    # CITY as the big gold line so the H1 is still the thing the page is about.
    body = f"""
<section class="hero" id="home">
  <div class="container hero__inner">
    <p class="hero__welcome">Look Limo in</p>
    <h1 class="hero__brand hero__brand--city" style="--chars:{len(esc_name)}">{esc_name}</h1>
    <p class="hero__tag">{city['sub']}</p>
{_btn_row(base, big=True)}
    <div class="crumb crumb--hero"><a href="{base}index.html">Home</a> <span>&rsaquo;</span> <span>{esc_name}</span></div>
  </div>
{build.HEROVID_LOCAL.replace('src="assets/', f'src="{base}assets/').replace('poster="assets/', f'poster="{base}assets/')}
  <div class="hero__media">
    <img src="{base}assets/{city['hero_img']}" alt="{city['hero_alt']}" />
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media"><img src="{base}assets/{city['split_img']}" alt="Look Limo chauffeured vehicle in {esc_name}" /></div>
    <div class="split__text">
      <p class="eyebrow">Look Limo &middot; {esc_name}</p>
      <h2 class="section__title section__title--left">{city['intro_h']}</h2>
{intro}      <h3 style="color:#fff;font-size:1.35rem;margin:1.6rem 0 .9rem">{city['areas_h']}</h3>
      <ul class="ticks">
{areas}      </ul>
      <a href="{base}contact.html" class="btn btn--gold">Request a Quote</a>
    </div>
  </div>
</section>

<section class="section bg-panel">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">Airports</p>
      <h2 class="section__title">Airports We Serve in {esc_name}</h2>
      <p class="section__lead">Every pickup is tracked against your live flight time, and your
        chauffeur meets you inside with luggage help included - not in a car park.</p>
    </div>
    <div class="grid grid--3">
{airports}    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">Services</p>
      <h2 class="section__title">What We Do in {esc_name}</h2>
      <p class="section__lead">Every service below is available across the whole area, 24 hours a day.</p>
    </div>
    <div class="grid grid--4">
{services}    </div>
{_btn_row(base)}
  </div>
</section>

<section class="section bg-panel fleet">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">The Fleet</p>
      <h2 class="section__title">Vehicles Available in {esc_name}</h2>
      <p class="section__lead">From three passengers to thirty-five, all chauffeur-driven and spotless.</p>
    </div>
    {{FLEET}}
    <div class="center mt2"><a href="{base}fleet.html" class="btn btn--gold">View the Full Fleet</a></div>
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

<section class="section">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">Booking</p>
      <h2 class="section__title">How to Book</h2>
      <p class="section__lead">Four steps, and the first one takes about a minute.</p>
    </div>
    <div class="grid grid--4 steps">
{steps}    </div>
    <div class="grid grid--3 mt2">
      <div class="infoblock"><span class="ic">&#9742;</span><div><h4>Call Us</h4>
        <a href="tel:{PHONE_1_TEL}">{PHONE_1}</a><br />
        <a href="tel:{PHONE_2_TEL}">{PHONE_2}</a></div></div>
      <div class="infoblock"><span class="ic">&#9993;</span><div><h4>Email Us</h4>
        <a href="mailto:{CITY_EMAIL}">{CITY_EMAIL}</a></div></div>
      <div class="infoblock"><span class="ic">&#9200;</span><div><h4>Hours</h4>
        <p>24 hours a day, 7 days a week</p></div></div>
    </div>
{_btn_row(base)}
  </div>
</section>

<section class="section bg-panel">
  <div class="container">
    <div class="section__head">
      <p class="eyebrow">Why Look Limo</p>
      <h2 class="section__title">Why Choose Us in {esc_name}</h2>
    </div>
    <div class="grid grid--3">
{why}    </div>
  </div>
</section>

<section class="ctabanner">
  <div class="container ctabanner__inner">
    <h2>Ready to ride in {esc_name}?</h2>
    <p>Tell us where you are going and we will come back with a firm price.</p>
{_btn_row(base, big=True)}
  </div>
</section>
""".replace("{FLEET}", build.FLEET_HOME.replace('src="assets/', f'src="{base}assets/')
                                       .replace("url('assets/", f"url('{base}assets/"))

    # Inlined rather than added to styles.css ON PURPOSE. These pages go up
    # for review while the rest of the site stays exactly as it is, so they
    # must not depend on a stylesheet change that has not been published. When
    # the client approves, this block moves into styles.css.
    # noindex while these sit in preview/. They are unapproved copies of pages
    # that will later exist at the real URLs, and letting Google index the
    # preview first is how a site ends up competing with itself. Dropped when
    # base="" moves them to the site root.
    robots = ('<meta name="robots" content="noindex,nofollow" />\n'
              if out_dir != "." else "")

    extra_css = """<style>
.feat__ic--svg{display:block;line-height:0;margin-bottom:.9rem}
.feat__ic--svg svg{width:34px;height:34px;stroke:var(--gold-2);fill:none;stroke-width:1.5}
.feat:hover .feat__ic--svg svg{stroke:var(--gold)}
.feat__ic.gold-text{font-family:'Jost',sans-serif;font-weight:600;letter-spacing:2px;font-size:1.7rem}
.pagehero .hero__cta{margin:1.6rem 0 .4rem}
.section .hero__cta{margin-top:2.6rem}
.ctabanner .hero__cta{margin-top:1.4rem}
.hero__cta{display:flex;gap:.9rem;flex-wrap:wrap;justify-content:center}
@media(max-width:900px){.grid--4{grid-template-columns:1fr 1fr}}
@media(max-width:620px){.grid--4{grid-template-columns:1fr}}
</style>
"""

    html = (build.head(f"{esc_name} Limo Service | Look Limo", city["meta"])
            .replace('href="assets/', f'href="{base}assets/')
            .replace('href="styles.css"', f'href="{base}styles.css"')
            .replace("</head>", robots + extra_css + "</head>")
            + _topbar(base) + _header(base) + body + _footer(base, city))
    build.write(f"{out_dir}/{city['slug']}.html", html)


def build_city_pages(build_module):
    global build
    build = build_module
    import os
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview")
    os.makedirs(d, exist_ok=True)
    print("\n-- city landing pages (preview/, not in site nav) --")
    for city in CITIES:
        city_page(city)
