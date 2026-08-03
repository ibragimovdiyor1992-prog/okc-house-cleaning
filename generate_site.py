#!/usr/bin/env python3
"""Generate OKC House Cleaning site: index + 9 city pages + 3 service pages."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PHONE_DISPLAY = "(405) 555-0100"
PHONE_TEL = "+14055550100"
DOMAIN = "okchousecleaning.com"

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
    for c in CITIES[:4]:
        links.append((f"house-cleaning-{c['slug']}.html", c["name"]))
    links.append(("deep-cleaning.html", "Deep"))
    links.append(("move-out-cleaning.html", "Move-Out"))
    links.append(("apartment-cleaning.html", "Apartments"))
    out = ['<nav>']
    for href, label in links:
        cls = ' class="current"' if href == current else ''
        out.append(f'<a href="{href}"{cls}>{label}</a>')
    out.append('</nav>')
    return "\n".join(out)


def footer_html():
    city_links = "".join(
        f'<a href="house-cleaning-{c["slug"]}.html">{c["name"]} Cleaning</a>' for c in CITIES
    )
    return f"""<footer>
  <div class="links">
    {city_links}
    <a href="deep-cleaning.html">Deep Cleaning</a>
    <a href="move-out-cleaning.html">Move-Out Cleaning</a>
    <a href="apartment-cleaning.html">Apartment Cleaning</a>
  </div>
  <p><strong>House Cleaning Oklahoma City</strong> — Serving OKC Metro since 2018</p>
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
  <p>Exact quotes are confirmed by phone — call for your home's price.</p>
</section>

<section>
  <h2>FAQ</h2>
  {faq}
</section>

<section>
  <h2>Serving the Whole OKC Metro</h2>
  <p>We clean homes across Oklahoma City and surrounding suburbs:</p>
  <div class="areas">
    {''.join(f'<a href="house-cleaning-{c["slug"]}.html" style="text-decoration:none"><span>{c["name"]}</span></a>' for c in CITIES)}
  </div>
</section>

{footer_html()}
</body>
</html>"""


def index_page():
    city_cards = "".join(
        f'<a href="house-cleaning-{c["slug"]}.html" style="text-decoration:none;color:inherit">'
        f'<div class="card"><h3>🧹 {c["name"]}</h3><p>Standard from ${c["std"].split("-")[0].strip().replace("$","")} · Deep from ${c["deep"].split("-")[0].strip().replace("$","")}</p></div></a>'
        for c in CITIES
    )
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
    <p style="font-size:0.85em;color:#666;">Estimate only. Call for exact quote based on your home.</p>
  </div>
</section>

<section>
  <h2>Cleaning Services by City</h2>
  <p>We serve the entire Oklahoma City metro — choose your city for local pricing and coverage:</p>
  <div class="grid">
    {city_cards}
  </div>
</section>

<section>
  <h2>Why Oklahoma City Trusts Us</h2>
  <ul class="checks">
    <li>✔ Fully insured &amp; background-checked cleaners</li>
    <li>✔ Upfront pricing — no surprises</li>
    <li>✔ Same-day &amp; emergency cleaning available</li>
    <li>✔ Eco-friendly products on request</li>
    <li>✔ Serving OKC, Edmond, Norman, Yukon, Moore and more</li>
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


def main():
    files = {
        "index.html": index_page(),
    }
    for c in CITIES:
        files[f"house-cleaning-{c['slug']}.html"] = city_page(c)
    for s in SERVICES:
        files[f"{s['slug']}.html"] = service_page(s)

    for name, content in files.items():
        path = os.path.join(BASE, name)
        with open(path, "w") as f:
            f.write(content)
        print(f"OK  {name}  ({len(content)} bytes)")


if __name__ == "__main__":
    main()
