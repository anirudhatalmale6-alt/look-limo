LOOK LIMO - WEBSITE FILES
=========================
Elegance. Comfort. Excellence.

WHAT'S INSIDE
-------------
This is the complete Look Limo website - plain HTML, CSS and JavaScript
(no frameworks, no build tools required). You can open it anywhere.

Pages (each is a normal .html file you can edit):
  index.html ............ Home (with autoplay video hero)
  about.html ............ About Us
  services.html ......... Services overview
  airport-transfers.html  Service page
  corporate-travel.html . Service page
  weddings-events.html .. Service page
  nights-out.html ....... Service page
  fleet.html ............ Fleet
  faq.html .............. FAQ (expandable)
  contact.html .......... Contact + quote form + map

  styles.css ............ All the styling / colours
  script.js ............. Menu, FAQ accordion, counters, form
  assets/ ............... Logo, photos, hero video, poster image
  build.py .............. Optional page generator (see below)

HOW TO PREVIEW LOCALLY
----------------------
Just double-click index.html to open it in your browser. That's it.
(The contact-page map and the video work best when the site is hosted
online, e.g. GitHub Pages, but everything opens locally too.)

MAKING EDITS
------------
- To change wording/photos on a single page, edit that page's .html file
  directly, or swap an image in the assets/ folder (keep the same filename
  to make it automatic).
- The HEADER and FOOTER are shared across every page. They are generated
  by build.py so they stay identical everywhere. If you want to change the
  menu, logo, phone number or footer site-wide, edit build.py and re-run:
        python3 build.py
  That regenerates all the .html pages at once.

SWAPPING THE HERO VIDEO
-----------------------
Replace assets/hero-video.mp4 with your own MP4 (keep the same name), and
optionally assets/hero-poster.jpg with a still frame. Done.

CONTACT DETAILS USED
--------------------
Phone: 929-213-8083   Email: looklimo@gmail.com   Area: Philadelphia, PA

Questions? Message me anytime and I'll help you make any change.
