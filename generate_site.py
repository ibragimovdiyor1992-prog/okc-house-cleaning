#!/usr/bin/env python3
"""Generate OKC House Cleaning site: index + 9 city pages + 3 service pages."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PHONE_DISPLAY = "(405) 555-0100"
PHONE_TEL = "+14055550100"
DOMAIN = "ibragimovdiyor1992-prog.github.io/okc-house-cleaning"

CITIES = [
    {
        "slug": "edmond",
        "name": "Edmond",
        "h1": "House Cleaning in Edmond, OK",
        "desc": "Professional house cleaning in Edmond, OK. Standard, deep and move-out cleaning with upfront pricing. Local Edmond cleaners trusted by families since 2018.",
        "sqft": "2,000-3,500 sq ft",
        "std": "$170-280", "deep": "$280-450", "move": "$300-500",
        "premium": "10-15% pricier than OKC core due to larger homes — still below the national average.",
        "areas": ["Central Edmond", "East Edmond", "West Edmond", "Edmond Highlands", "Kelly Pointe", "Oak Tree", "Gaillardia", "Spring Creek", "Mitch Park area"],
        "why": ["Same cleaners every visit — consistency you can trust", "Pet-friendly, eco-friendly supplies on request", "Flexible scheduling around school hours", "Background-checked, insured professionals"],
        "faq": [
            ("Do you clean Edmond apartments too?", "Yes. Edmond apartment cleaning starts at $90 for 1-bedroom units. Recurring discounts apply."),
            ("How far in advance should I book?", "1-3 days is typical. Same-day is often available for recurring clients."),
        ],
    },
    {
        "slug": "norman",
        "name": "Norman",
        "h1": "House Cleaning in Norman, OK",
        "desc": "House cleaning in Norman, OK for homes and apartments. Standard, deep, move-out and post-construction cleaning. Upfront pricing, insured cleaners.",
        "sqft": "1,400-2,400 sq ft",
        "std": "$140-230", "deep": "$240-380", "move": "$260-420",
        "premium": "Norman prices sit right at the OKC metro average. Student-area apartments book move-out cleaning year-round.",
        "areas": ["Campus Corner", "Sooner Heights", "Brookhaven", "Westwood", "The Trails", "East Norman", "Alameda Street area", "UNP District", "Downtown Norman"],
        "why": ["Move-out specialists for student rentals near OU", "Same-day move-out service during end-of-lease rush", "Insured and background-checked cleaners", "Transparent flat-rate quotes — no hourly surprises"],
        "faq": [
            ("Do you handle move-out cleaning for OU student rentals?", "Yes, that's one of our busiest services in Norman. We get deposits back for tenants every semester."),
            ("Can I book a one-time deep clean?", "Absolutely. One-time deep cleaning in Norman runs $240-380 depending on home size."),
        ],
    },
    {
        "slug": "moore",
        "name": "Moore",
        "h1": "House Cleaning in Moore, OK",
        "desc": "Professional house cleaning in Moore, OK. Standard, deep and move-out cleaning for Moore family homes. Upfront pricing, insured local cleaners.",
        "sqft": "1,500-2,500 sq ft",
        "std": "$150-240", "deep": "$250-400", "move": "$280-450",
        "premium": "Moore homes are mostly 3-bedroom layouts — most clients pay $160-220 for a standard visit.",
        "areas": ["Central Moore", "East Moore", "South Moore", "Moore West", "Santa Fe area", "NW 12th Street", "Broadway Terrace", "Little River area"],
        "why": ["Fast-growing family neighborhoods, weekly and bi-weekly plans", "Post-storm cleanup experience — Moore residents know us", "Background-checked, fully insured team", "Kids- and pet-safe cleaning products available"],
        "faq": [
            ("Is cleaning available right after storms or renovations?", "Yes, we offer post-construction and heavy debris cleaning across Moore and Cleveland County."),
            ("What does a standard clean include?", "Kitchen, bathrooms, floors, dusting and trash removal — typically $150-240 for a 3-bedroom Moore home."),
        ],
    },
    {
        "slug": "yukon",
        "name": "Yukon",
        "h1": "House Cleaning in Yukon, OK",
        "desc": "House cleaning in Yukon, OK — standard, deep and move-out cleaning for Yukon family homes. Upfront pricing, insured local cleaners, weekly plans.",
        "sqft": "1,800-2,800 sq ft",
        "std": "$160-260", "deep": "$260-420", "move": "$290-470",
        "premium": "New construction in Yukon means high demand for first-clean and post-construction service.",
        "areas": ["Chisholm Trail", "Mustang Creek", "West Yukon", "Village on the Park", "Grey Stone", "Sundance", "Downtown Yukon", "Canadian River area"],
        "why": ["New-home first cleans handled with extra care", "Weekly and bi-weekly family plans with discounts", "Insured, background-checked cleaners", "Supplies and equipment always included"],
        "faq": [
            ("Do you clean brand-new homes in Yukon?", "Yes — first cleans and post-construction dust removal are very common here with all the new builds."),
            ("How much is a standard cleaning in Yukon?", "Most Yukon homes pay $160-260 for standard cleaning, depending on size and condition."),
        ],
    },
    {
        "slug": "midwest-city",
        "name": "Midwest City",
        "h1": "House Cleaning in Midwest City, OK",
        "desc": "Affordable house cleaning in Midwest City, OK. Standard, deep and move-out cleaning near Tinker AFB. Upfront pricing, insured local cleaners.",
        "sqft": "1,200-2,000 sq ft",
        "std": "$120-200", "deep": "$210-340", "move": "$230-380",
        "premium": "Prices in Midwest City run 10-15% below the OKC average — great value for military families.",
        "areas": ["Tinker AFB area", "Del Park", "Heritage Park", "Country Estates", "Air Depot area", "Eastwood", "Parkview Terrace", "North Midwest City"],
        "why": ["Military-friendly scheduling around deployments", "Move-out cleaning for PCS and rental turnover", "Discounts for weekly service on base-adjacent homes", "Insured, background-checked team"],
        "faq": [
            ("Do you serve Tinker AFB families?", "Yes, we work with many military families in Midwest City and Del City, including PCS move-out cleans."),
            ("Why are Midwest City prices lower?", "Smaller average home sizes — most cleans here run $120-200, among the best value in the metro."),
        ],
    },
    {
        "slug": "del-city",
        "name": "Del City",
        "h1": "House Cleaning in Del City, OK",
        "desc": "Budget-friendly house cleaning in Del City, OK. Standard, deep and move-out cleaning for smaller homes. Upfront pricing, insured cleaners.",
        "sqft": "1,000-1,600 sq ft",
        "std": "$100-170", "deep": "$180-290", "move": "$200-330",
        "premium": "Del City's compact homes make it the most affordable cleaning market in the metro.",
        "areas": ["Central Del City", "East Del City", "North Del City", "Southeast Del City", "Overholser area", "SE 15th Street", "Vandenberg Drive area"],
        "why": ["Most affordable standard cleans in the metro", "Quick turnaround — many homes cleaned in under 90 minutes", "Friendly, consistent local team", "Fully insured and background-checked"],
        "faq": [
            ("What's the minimum cleaning in Del City?", "Standard clean for a 1-2 bedroom home starts at $100 — perfect for smaller houses and rentals."),
            ("Do you do weekly service in Del City?", "Yes, weekly and bi-weekly plans are popular here and come with 10-15% off."),
        ],
    },
    {
        "slug": "bethany",
        "name": "Bethany",
        "h1": "House Cleaning in Bethany, OK",
        "desc": "House cleaning in Bethany, OK for homes and apartments. Standard, deep and move-out cleaning. Upfront pricing, insured local cleaners.",
        "sqft": "1,200-1,800 sq ft",
        "std": "$115-185", "deep": "$195-310", "move": "$215-350",
        "premium": "Bethany sits between OKC and Yukon — prices reflect the smaller, older home stock.",
        "areas": ["Central Bethany", "West Bethany", "Northwest Bethany", "Bethany College area", "NW 39th Expressway", "Rockwell Avenue area"],
        "why": ["Attentive service for older homes and character properties", "Apartment cleaning specialists near Bethany College", "Consistent weekly teams you know by name", "Insured, background-checked cleaners"],
        "faq": [
            ("Do you clean older homes carefully?", "Yes — we're experienced with older Bethany homes and handle surfaces and fixtures with extra care."),
            ("Can I get a one-time clean before guests arrive?", "Definitely. One-time cleans are bookable 1-3 days ahead in most cases."),
        ],
    },
    {
        "slug": "mustang",
        "name": "Mustang",
        "h1": "House Cleaning in Mustang, OK",
        "desc": "Professional house cleaning in Mustang, OK. Standard, deep and move-out cleaning for growing Mustang neighborhoods. Upfront pricing, insured cleaners.",
        "sqft": "1,800-2,800 sq ft",
        "std": "$160-260", "deep": "$260-420", "move": "$290-470",
        "premium": "Mustang is one of the fastest-growing suburbs — new homes drive steady demand for first cleans.",
        "areas": ["Central Mustang", "East Mustang", "West Mustang", "Mustang Road corridor", "Canadian Hills", "Wild Horse Park area", "Prairie West"],
        "why": ["New-construction first cleans and post-build dust removal", "Growing weekly plan list for busy families", "Fully insured and background-checked", "Eco-friendly product options on request"],
        "faq": [
            ("Do you handle post-construction cleaning in Mustang?", "Yes — with all the new builds in Mustang, it's one of our most requested services."),
            ("How much is deep cleaning in Mustang?", "Deep cleaning runs $260-420 depending on home size and condition."),
        ],
    },
    {
        "slug": "choctaw",
        "name": "Choctaw",
        "h1": "House Cleaning in Choctaw, OK",
        "desc": "House cleaning in Choctaw, OK — standard, deep and move-out cleaning for larger lots and country homes. Upfront pricing, insured local cleaners.",
        "sqft": "1,600-2,600 sq ft",
        "std": "$150-240", "deep": "$250-400", "move": "$280-450",
        "premium": "Choctaw homes often combine larger square footage with country living — we bring supplies and handle the rest.",
        "areas": ["Central Choctaw", "East Choctaw", "North Choctaw", "Lake Choctaw area", "NE 23rd Street", "Harrah Road area", "Country Estates"],
        "why": ["Comfortable with acreage homes and ranch layouts", "Same-day quotes for large-property cleans", "Insured, background-checked team", "Flexible scheduling for rural routes"],
        "faq": [
            ("Do you travel to rural properties around Choctaw?", "Yes, we cover all of Choctaw and the surrounding unincorporated areas of eastern Oklahoma County."),
            ("What does standard cleaning cost in Choctaw?", "Most homes pay $150-240 for standard cleaning, similar to the OKC average."),
        ],
    },
]

SERVICES = [
    {
        "slug": "deep-cleaning",
        "name": "Deep Cleaning",
        "h1": "Deep Cleaning in Oklahoma City",
        "desc": "Deep house cleaning in Oklahoma City, OK. Baseboards, inside appliances, every corner. Upfront pricing from $250. Insured local cleaners.",
        "body": [
            ("What's included", "Deep cleaning covers everything in a standard clean plus: inside oven and refrigerator, inside cabinets, baseboards, window tracks, door frames, light fixtures and switch plates, and detailed scrubbing of grout and tile."),
            ("How long it takes", "A deep clean takes 3-6 hours depending on home size. A 2-bedroom home runs 3-4 hours with a two-person crew."),
            ("When you need it", "Spring reset, before selling, after long tenants, post-renovation dust, or simply as a quarterly refresh between regular cleanings."),
        ],
        "price": "from $250 (2-bedroom homes average $280-400)",
        "faq": [
            ("Is deep cleaning more expensive than standard?", "Yes — roughly 60-80% more, because it covers areas standard cleaning doesn't touch: inside appliances, baseboards, window tracks."),
            ("Can I combine deep cleaning with recurring service?", "Many clients book one deep clean, then switch to bi-weekly standard — ask about our transition plan."),
        ],
    },
    {
        "slug": "move-out-cleaning",
        "name": "Move-Out Cleaning",
        "h1": "Move-Out Cleaning in Oklahoma City",
        "desc": "Move-out and move-in cleaning in Oklahoma City, OK. Landlord-ready shine guaranteed, deposit back. From $300. Insured local cleaners.",
        "body": [
            ("What's included", "Full interior clean to landlord standards: kitchen degrease, bathroom descaling, inside appliances and cabinets, baseboards, walls spot-cleaned, carpets vacuumed, and a final walkthrough checklist."),
            ("Why it pays for itself", "A $300-500 move-out clean routinely saves the full security deposit — typically $800-1,500 on OKC rentals. Landlords deduct for exactly the dirt we remove."),
            ("For landlords too", "We also work directly with OKC property managers and landlords for turnover cleaning between tenants, on schedule."),
        ],
        "price": "from $300 (average $300-500 by home size)",
        "faq": [
            ("Do you guarantee my deposit back?", "We clean to landlord standards and will return to touch up anything a walkthrough flags — that's the guarantee."),
            ("How fast can you schedule a move-out clean?", "Same-day or next-day in most of the OKC metro, especially during end-of-month turnover."),
        ],
    },
    {
        "slug": "apartment-cleaning",
        "name": "Apartment Cleaning",
        "h1": "Apartment Cleaning in Oklahoma City",
        "desc": "Apartment cleaning in Oklahoma City, OK. Studio, 1 and 2-bedroom units from $80. Standard, deep and move-out options. Insured cleaners.",
        "body": [
            ("Perfect for renters", "Studio and 1-bedroom apartments clean from $80-140. Weekly, bi-weekly and monthly plans available with 10-15% discounts."),
            ("What's included", "Kitchen surfaces and sink, bathrooms, floors, dusting, and trash removal. Deep add-ons for ovens, fridges and baseboards."),
            ("Student friendly", "Popular with students and young professionals — flexible scheduling around work and class hours, no long-term commitment required."),
        ],
        "price": "from $80 (studio/1-bed, standard)",
        "faq": [
            ("Do you need building access?", "Just a key fob, garage code or a concierge arrangement — we handle the rest and lock up on the way out."),
            ("Is there a minimum contract?", "No. One-time, weekly or bi-weekly — you choose. Cancel anytime with 48 hours' notice."),
        ],
    },
]


def nav_html(current):
    links = [("index.html", "Home")]
    links.append(("deep-cleaning.html", "Deep"))
    links.append(("move-out-cleaning.html", "Move-Out"))
    links.append(("apartment-cleaning.html", "Apartments"))
    links.append(("blog.html", "Blog"))
    out = ['<nav>']
    for href, label in links:
        cls = ' class="current"' if href == current else ''
        out.append(f'<a href="{href}"{cls}>{label}</a>')
    out.append('</nav>')
    return "\n".join(out)


def footer_html():
    return f"""<footer>
  <div class="links">
    <a href="index.html">Home</a>
    <a href="deep-cleaning.html">Deep Cleaning</a>
    <a href="move-out-cleaning.html">Move-Out Cleaning</a>
    <a href="apartment-cleaning.html">Apartment Cleaning</a>
    <a href="blog.html">Blog</a>
  </div>
  <p><strong>House Cleaning Oklahoma City</strong> — Serving Oklahoma City since 2018</p>
  <p>📞 <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> | {DOMAIN}</p>
  <p style="opacity:0.7">Hours: Mon-Sat 8am-6pm · Licensed &amp; Insured</p>
</footer>"""


def schema_local(city=None, name="House Cleaning Oklahoma City"):
    address = f'"{city["name"]}, OK", "addressRegion": "OK", "addressCountry": "US"' if city else '"addressLocality": "Oklahoma City", "addressRegion": "OK", "addressCountry": "US"'
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HouseCleaner",
  "name": "{name}",
  "telephone": "{PHONE_TEL}",
  "url": "https://{DOMAIN}/",
  "address": {{ "@type": "PostalAddress", {address} }},
  "areaServed": "Oklahoma City metro",
  "priceRange": "$$",
  "openingHours": "Mo-Sa 08:00-18:00"
}}
</script>"""


def city_page(c):
    schema = schema_local(city=c, name=f"House Cleaning {c['name']}, OK")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{c['h1']}</title>
<meta name="description" content="{c['desc']}">
<link rel="stylesheet" href="style.css">
{schema}
</head>
<body>
<div class="top">📞 {c['name']} &amp; OKC Metro — <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
{nav_html(f"house-cleaning-{c['slug']}.html")}
<header>
  <h1>{c['h1']}</h1>
  <p>Reliable, insured cleaners serving {c['name']} families since 2018.</p>
  <a class="btn" href="tel:{PHONE_TEL}">Get a Free Quote</a>
</header>

<section>
  <h2>{c['name']} Cleaning Services &amp; Prices</h2>
  <p>{c['name']} homes are typically {c['sqft']}. Most clients pay:</p>
  <ul>
    <li>Standard cleaning (2-3 bed): <strong>${c['std'].replace('$','')}</strong></li>
    <li>Deep cleaning: <strong>${c['deep'].replace('$','')}</strong></li>
    <li>Move-out cleaning: <strong>${c['move'].replace('$','')}</strong></li>
    <li>Recurring weekly/bi-weekly: <strong>10-15% discount</strong></li>
  </ul>
  <p><em>{c['premium']}</em></p>
  <p><strong>Note:</strong> Prices above are estimates. The final price depends on the scope of work — we assess each home and agree on the exact price before starting.</p>
</section>

<section>
  <h2>Areas We Serve in {c['name']}</h2>
  <div class="areas">
    {''.join(f'<span>{a}</span>' for a in c['areas'])}
  </div>
</section>

<section>
  <h2>Why {c['name']} Families Choose Us</h2>
  <ul class="checks">
    {''.join(f'<li>✔ {w}</li>' for w in c['why'])}
  </ul>
  <p><a class="btn" href="tel:{PHONE_TEL}">Call for {c['name']} Pricing</a></p>
</section>

<section>
  <h2>FAQ — House Cleaning in {c['name']}</h2>
  {''.join(f'<div class="faq"><h3>{q}</h3><p>{a}</p></div>' for q, a in c['faq'])}
</section>

{footer_html()}
</body>
</html>"""


def service_page(s):
    schema = schema_local(name=f"{s['name']} Oklahoma City")
    body = "".join(
        f"<section><h2>{h}</h2><p>{p}</p></section>" for h, p in s["body"]
    )
    faq = "".join(
        f'<div class="faq"><h3>{q}</h3><p>{a}</p></div>' for q, a in s["faq"]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{s['h1']}</title>
<meta name="description" content="{s['desc']}">
<link rel="stylesheet" href="style.css">
{schema}
</head>
<body>
<div class="top">📞 OKC Metro — <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
{nav_html(f"{s['slug']}.html")}
<header>
  <h1>{s['h1']}</h1>
  <p>Upfront pricing · Insured &amp; background-checked cleaners · Since 2018</p>
  <a class="btn" href="tel:{PHONE_TEL}">Get a Free Estimate</a>
</header>

{body}

<section>
  <h2>Pricing</h2>
  <p><span class="price">{s['price']}</span></p>
  <p>This is an estimate. The final price depends on the scope of work — we'll assess your home and agree on the exact price before starting.</p>
</section>

<section>
  <h2>FAQ</h2>
  {faq}
</section>

{footer_html()}
</body>
</html>"""


def index_page():
    services_cards = ""
    schema = schema_local()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>House Cleaning Oklahoma City | Top-Rated Cleaning Services OKC</title>
<meta name="description" content="Professional house cleaning in Oklahoma City. Standard, deep and move-out cleaning with upfront pricing. Local OKC cleaners trusted by 500+ homes. Call now.">
<link rel="stylesheet" href="style.css">
{schema}
</head>
<body>
<div class="top">📞 Same-day cleaning available in OKC — <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
{nav_html("index.html")}

<header>
  <h1>House Cleaning in Oklahoma City</h1>
  <p>Trusted local cleaners. Upfront pricing. 500+ OKC homes cleaned.</p>
  <a class="btn" href="tel:{PHONE_TEL}">Get Your Free Estimate</a>
</header>

<section>
  <h2>Our Cleaning Services in OKC</h2>
  <div class="grid">
    <div class="card"><h3>🧹 Standard Cleaning</h3><p>Kitchen, bathrooms, floors, dusting — weekly or bi-weekly maintenance.</p><div class="price">from $120</div></div>
    <div class="card"><h3>✨ Deep Cleaning</h3><p>Detailed clean of every corner, baseboards, inside appliances.</p><div class="price">from $250</div><p><a href="deep-cleaning.html">Details →</a></p></div>
    <div class="card"><h3>📦 Move-Out Cleaning</h3><p>Get your deposit back. Landlord-ready shine guaranteed.</p><div class="price">from $300</div><p><a href="move-out-cleaning.html">Details →</a></p></div>
    <div class="card"><h3>🏚 Post-Construction</h3><p>Dust and debris removal after renovation or remodeling.</p><div class="price">from $350</div></div>
    <div class="card"><h3>🏢 Apartment Cleaning</h3><p>Studio and 1-2 bedroom units from $80. Perfect for renters.</p><div class="price">from $80</div><p><a href="apartment-cleaning.html">Details →</a></p></div>
  </div>
</section>

<section>
  <h2>Cleaning Prices in Oklahoma City (2026)</h2>
  <table>
    <tr><td>Studio / 1-bedroom apartment</td><td>$80-160</td></tr>
    <tr><td>2-bedroom home</td><td>$170-220</td></tr>
    <tr><td>3-bedroom home</td><td>$220-330</td></tr>
    <tr><td>4+ bedroom home</td><td>$330-450</td></tr>
    <tr><td>Hourly rate</td><td>$45-75</td></tr>
  </table>
  <p><em>OKC prices are 10-15% below the national average. Final quote depends on size and condition.</em></p>
  <p><strong>Note:</strong> Prices shown are estimates. The final price depends on the scope of work — we assess each home and agree on the exact price before starting.</p>
</section>

<section>
  <h2>House Cleaning Cost Calculator</h2>
  <div class="calc">
    <label for="beds">Number of bedrooms</label>
    <select id="beds"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select>
    <label for="type">Cleaning type</label>
    <select id="type">
      <option value="standard">Standard</option>
      <option value="deep">Deep (+$100)</option>
      <option value="moveout">Move-out (+$150)</option>
    </select>
    <label for="freq">Frequency</label>
    <select id="freq">
      <option value="once">One-time</option>
      <option value="weekly">Weekly (-15%)</option>
      <option value="biweekly">Bi-weekly (-10%)</option>
    </select>
    <button class="btn" onclick="calc()" style="border:none;cursor:pointer;width:100%;">Calculate My Price</button>
    <div class="result" id="res"></div>
    <p style="font-size:0.85em;color:#666;">Estimate only — not a final price. The final price depends on the scope of work; we'll assess your home and agree on the exact price before starting.</p>
  </div>
</section>

<section>
  <h2>Why Oklahoma City Trusts Us</h2>
  <ul class="checks">
    <li>✔ Fully insured &amp; background-checked cleaners</li>
    <li>✔ Upfront pricing — no surprises</li>
    <li>✔ Same-day &amp; emergency cleaning available</li>
    <li>✔ Eco-friendly products on request</li>
    <li>✔ Serving Oklahoma City and nearby neighborhoods</li>
  </ul>
</section>

<section>
  <h2>FAQ</h2>
  <div class="faq"><h3>How much does house cleaning cost in Oklahoma City?</h3><p>Most OKC homes pay $120-330 per visit. A 2-bedroom home averages $170-220 for standard cleaning.</p></div>
  <div class="faq"><h3>Do I need to be home during cleaning?</h3><p>No. Many clients provide a key or garage code. We're insured and bonded.</p></div>
  <div class="faq"><h3>How long does a cleaning take?</h3><p>1-2 hours for a 2-bedroom standard clean, up to 4-5 hours for deep or move-out cleaning.</p></div>
  <div class="faq"><h3>Do you bring your own supplies?</h3><p>Yes, all supplies and equipment included. Eco-friendly options available.</p></div>
</section>

{footer_html()}

<script>
function calc() {{
  const beds = parseInt(document.getElementById('beds').value);
  const type = document.getElementById('type').value;
  const freq = document.getElementById('freq').value;
  let base = 80 + (beds - 1) * 70;
  if (type === 'deep') base += 100;
  if (type === 'moveout') base += 150;
  if (freq === 'weekly') base *= 0.85;
  if (freq === 'biweekly') base *= 0.9;
  const res = document.getElementById('res');
  res.style.display = 'block';
  res.textContent = 'Estimated price: $' + Math.round(base) + ' (' + freq + ', ' + beds + ' bed)';
}}
</script>
</body>
</html>"""


def article_page(art):
    body = "\n".join(f"<section><h2>{h2}</h2>{html}</section>" for h2, html in art["body"])
    faq = "".join(
        f'<div class="faq"><h3>{q}</h3><p>{a}</p></div>' for q, a in art["faq"]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{art['title']}</title>
<meta name="description" content="{art['meta']}">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{art['title']}","datePublished":"{art['date']}","author":{{"@type":"Organization","name":"House Cleaning Oklahoma City"}},"publisher":{{"@type":"Organization","name":"House Cleaning Oklahoma City"}},"mainEntityOfPage":"https://{DOMAIN}/{art['slug']}.html"}}
</script>
</head>
<body>
<div class="top">📞 Same-day cleaning available in OKC — <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
{nav_html(art['slug'] + '.html')}

<header>
  <h1>{art['h1']}</h1>
  <p>{art['sub']}</p>
  <a class="btn" href="tel:{PHONE_TEL}">Get Your Free Estimate</a>
</header>

{body}

<section>
  <h2>Frequently Asked Questions</h2>
  <div class="faq">{faq}</div>
</section>

<section style="background:#eef4ff;padding:2rem;border-radius:12px;text-align:center;">
  <h2>Ready for a Spotless Home?</h2>
  <p>Call us today for a free estimate — no obligations, honest pricing.</p>
  <a class="btn" href="tel:{PHONE_TEL}">📞 {PHONE_DISPLAY}</a>
</section>

{footer_html()}
</body>
</html>"""


def blog_page():
    cards = "\n".join(
        f'<div class="card"><h3><a href="{a["slug"]}.html" style="color:inherit">{a["title"]}</a></h3><p>{a["meta"]}</p><p style="opacity:0.6">📅 {a["date"]}</p></div>'
        for a in ARTICLES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>House Cleaning Tips & Prices in Oklahoma City | Blog</title>
<meta name="description" content="Useful guides: cleaning prices in Oklahoma City, deep cleaning checklists, move-out tips. Read before you book.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="top">📞 Same-day cleaning available in OKC — <a href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
{nav_html("blog.html")}

<header>
  <h1>House Cleaning Guides & Prices</h1>
  <p>Honest answers about cleaning costs, checklists and tips for Oklahoma City homeowners.</p>
</header>

<section>
  <div class="grid">
    {cards}
  </div>
</section>

{footer_html()}
</body>
</html>"""


ARTICLES = [
    {
        "slug": "house-cleaning-cost-okc",
        "title": "How Much Does House Cleaning Cost in Oklahoma City? (2026 Guide)",
        "h1": "How Much Does House Cleaning Cost in Oklahoma City?",
        "sub": "Real prices for standard, deep and move-out cleaning in OKC — updated for 2026.",
        "meta": "House cleaning cost in Oklahoma City 2026: $120-330 per visit on average. See prices by home size, cleaning type and frequency.",
        "date": "2026-08-04",
        "body": [
            ("Average House Cleaning Prices in Oklahoma City",
             "<p>Most Oklahoma City homeowners pay <strong>$120-330 per visit</strong> for professional house cleaning. A typical 2-bedroom home costs <strong>$170-220</strong> for a standard clean, while a deep cleaning of the same home runs <strong>$280-380</strong>.</p><p>OKC prices run about 10-15% below the national average — you get the same quality of service for less than in Dallas or Denver.</p>"),
            ("Prices by Home Size",
             "<table><tr><td>Studio / 1-bedroom apartment</td><td>$80-160</td></tr><tr><td>2-bedroom home</td><td>$170-220</td></tr><tr><td>3-bedroom home</td><td>$220-330</td></tr><tr><td>4+ bedroom home</td><td>$330-450</td></tr><tr><td>Hourly rate</td><td>$45-75</td></tr></table><p><em>Prices are estimates. The final price depends on the scope of work — we assess each home and agree on the exact price before starting.</em></p>"),
            ("Prices by Cleaning Type",
             "<ul class='checks'><li>✔ <strong>Standard cleaning</strong> — $120-220: kitchen, bathrooms, floors, dusting. Weekly or bi-weekly visits get a 10-15% discount.</li><li>✔ <strong>Deep cleaning</strong> — $250-450: every corner, baseboards, inside appliances, detailed <a href='deep-cleaning.html'>deep clean</a>.</li><li>✔ <strong>Move-out cleaning</strong> — $300-500: landlord-ready <a href='move-out-cleaning.html'>move-out clean</a> to get your deposit back.</li><li>✔ <strong>Apartment cleaning</strong> — from $80 for studios, from $90 for 1-bedroom <a href='apartment-cleaning.html'>units</a>.</li></ul>"),
            ("What Affects the Price",
             "<h3>Home size and layout</h3><p>More bedrooms and bathrooms mean more time — and a higher price. Open-plan homes are cheaper to clean than homes with many small rooms.</p><h3>Condition of the home</h3><p>A home that hasn't been cleaned in months needs more work than one on a weekly schedule. That's why we always look at the actual scope of work before quoting.</p><h3>Frequency</h3><p>Weekly and bi-weekly clients save 10-15% — regular cleaning keeps the home from getting dirty in the first place.</p><h3>Pets</h3><p>Homes with pets need extra vacuuming and lint removal. It's a small surcharge, but we always agree on it upfront.</p>"),
            ("Why Our Prices Are Fair",
             "<p>We don't hide prices behind a booking form. You see our rates on this page, we discuss your home over the phone, and the final price is agreed <em>before</em> we start — no surprises at the end. If the scope changes, we tell you immediately and ask before doing extra work.</p>"),
        ],
        "faq": [
            ("How often should I get my house cleaned?", "Most OKC families book weekly or bi-weekly. Monthly visits are fine for maintenance if the home is kept tidy in between."),
            ("Do I need to be home during the cleaning?", "No. Many clients give us a key or garage code. We're insured and bonded."),
            ("Are your prices really final?", "The price we agree on the phone or after the first visit is the price you pay — as long as the scope of work doesn't change."),
        ],
    },
    {
        "slug": "deep-cleaning-checklist",
        "title": "Deep Cleaning Checklist: What's Included in a Professional Deep Clean",
        "h1": "Deep Cleaning Checklist: What's Included",
        "sub": "Room-by-room breakdown of a professional deep cleaning in Oklahoma City.",
        "meta": "What does a professional deep cleaning include? Room-by-room checklist: kitchen, bathrooms, baseboards, inside appliances. OKC prices from $250.",
        "date": "2026-08-04",
        "body": [
            ("Deep Cleaning vs Standard Cleaning",
             "<p>A standard cleaning keeps an already-clean home tidy. A <a href='deep-cleaning.html'>deep cleaning</a> resets the home: every corner, every surface, everything you skip during a normal week. Most OKC homeowners do one deep clean every 6-12 months — and always before moving in or out.</p>"),
            ("Kitchen",
             "<ul class='checks'><li>✔ Inside and outside of appliances (oven, fridge, microwave)</li><li>✔ Cabinet fronts, handles and kickboards</li><li>✔ Countertops scrubbed and sanitized</li><li>✔ Sink descaled and polished</li><li>✔ Backsplash degreased</li></ul>"),
            ("Bathrooms",
             "<ul class='checks'><li>✔ Shower, tub and tiles scrubbed and descaled</li><li>✔ Toilets sanitized inside and out</li><li>✔ Vanity, mirror and fixtures polished</li><li>✔ Grout spot-cleaned</li><li>✔ Exhaust fan dusted</li></ul>"),
            ("Living Areas and Bedrooms",
             "<ul class='checks'><li>✔ Baseboards and door frames wiped</li><li>✔ Light switches and outlets cleaned</li><li>✔ Ceiling fans and light fixtures dusted</li><li>✔ Windowsills and window tracks</li><li>✔ Furniture dusted top to bottom</li><li>✔ Floors vacuumed, then mopped or hard-floored cleaned</li></ul>"),
            ("How Much Does a Deep Clean Cost in OKC?",
             "<p>Expect <strong>$250-450</strong> depending on home size. A 2-bedroom home averages <strong>$280-380</strong>. Add $50-100 if the home has heavy buildup or hasn't been cleaned in months. Prices are estimates — the final price depends on the scope of work.</p>"),
        ],
        "faq": [
            ("How long does a deep cleaning take?", "A 2-bedroom home takes 3-5 hours with a team of two. Larger homes or heavy buildup can take longer."),
            ("How often should I deep clean?", "Every 6-12 months, plus before moving in or out, after renovations, or when allergies act up."),
            ("Should I be home?", "No — we work with keys and garage codes. You'll come home to a reset house."),
        ],
    },
    {
        "slug": "move-out-cleaning-checklist",
        "title": "Move-Out Cleaning Checklist: Get Your Security Deposit Back",
        "h1": "Move-Out Cleaning Checklist",
        "sub": "What landlords check before returning your deposit — and how to pass every time.",
        "meta": "Move-out cleaning checklist for OKC renters: kitchen, bathrooms, walls, floors. Professional move-out cleaning from $300. Get your deposit back.",
        "date": "2026-08-04",
        "body": [
            ("Why Move-Out Cleaning Matters",
             "<p>Most landlords walk the property with a checklist and photograph every room. A <a href='move-out-cleaning.html'>professional move-out clean</a> removes the biggest reasons deposits get withheld: grease, soap scum, dust on baseboards, and marks on walls.</p>"),
            ("Kitchen — The #1 Inspection Point",
             "<ul class='checks'><li>✔ Oven degreased inside and out, racks scrubbed</li><li>✔ Fridge emptied, defrosted and sanitized</li><li>✔ Microwave, dishwasher and range hood cleaned</li><li>✔ Cabinets wiped inside and out, shelves lined if needed</li><li>✔ Sink descaled, counters spotless</li><li>✔ Floors mopped behind appliances</li></ul>"),
            ("Bathrooms",
             "<ul class='checks'><li>✔ Toilet sanitized, no limescale</li><li>✔ Shower and tub scrubbed, glass doors streak-free</li><li>✔ Vanity, mirror and fixtures polished</li><li>✔ Grout and caulk spot-cleaned</li></ul>"),
            ("Walls, Floors and Extras",
             "<ul class='checks'><li>✔ Walls spot-cleaned (marks, scuffs, cobwebs)</li><li>✔ Baseboards wiped</li><li>✔ Windows cleaned inside</li><li>✔ Closets vacuumed and wiped</li><li>✔ Carpet vacuumed or steam-cleaned if required by lease</li><li>✔ Light fixtures and ceiling fans dusted</li></ul>"),
            ("DIY or Hire a Pro?",
             "<p>If you have the time, the DIY route works — but it takes a full day and landlords still find things you missed. A professional move-out clean in OKC costs <strong>$300-500</strong>, and it's usually cheaper than losing a $1,000+ deposit. Most of our clients book a move-out clean on moving day and hand the keys over the same afternoon.</p>"),
        ],
        "faq": [
            ("When should I schedule the move-out clean?", "The day you move out, or the day before if the landlord hands the keys over to new tenants quickly."),
            ("Will the cleaning guarantee my deposit?", "Nothing can guarantee it, but a professional clean covers every inspection point landlords check. We also clean behind appliances — the usual hidden culprit."),
            ("Do you clean carpets?", "We can add carpet steam cleaning to the move-out service — ask when you book."),
        ],
    },
]


def main():
    files = {
        "index.html": index_page(),
        "blog.html": blog_page(),
    }
    for s in SERVICES:
        files[f"{s['slug']}.html"] = service_page(s)
    for a in ARTICLES:
        files[f"{a['slug']}.html"] = article_page(a)

    for name, content in files.items():
        path = os.path.join(BASE, name)
        with open(path, "w") as f:
            f.write(content)
        print(f"OK  {name}  ({len(content)} bytes)")


if __name__ == "__main__":
    main()
