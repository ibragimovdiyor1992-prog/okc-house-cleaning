#!/usr/bin/env python3
"""Generate 10 new SEO pages for okchomecleaning.com"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PHONE = "(405) 886-2107"
PHONE_TEL = "+14058862107"
DOMAIN = "okchomecleaning.com"

PAGES = [
    {
        "slug": "eco-friendly-cleaning-okc",
        "title": "Eco-Friendly House Cleaning in Oklahoma City | Green Cleaning OKC",
        "desc": "Non-toxic, eco-friendly house cleaning in Oklahoma City. Pet-safe and child-safe products. Professional green cleaning services for OKC homes.",
        "h1": "Eco-Friendly House Cleaning in Oklahoma City",
        "content": [
            ("Green cleaning uses non-toxic, biodegradable products that are safe for your family, pets, and the environment. At okchomecleaning.com, we specialize in eco-friendly house cleaning throughout Oklahoma City — from downtown lofts to suburban homes in NW OKC.",
             "Our green cleaning solutions are just as effective as traditional products. We remove dirt, grime, and bacteria using plant-based cleaners, microfiber technology, and HEPA-filter vacuums. Your home gets sparkling clean without harsh chemical residues.",
             "Eco-friendly cleaning in OKC costs the same as standard cleaning — starting at $120 for a 2-bedroom home. You don't pay extra for green products."),
            ["Safe for pets and children — no toxic residue", "Plant-based cleaning products", "HEPA vacuuming for better indoor air quality", "Same competitive pricing as standard cleaning"],
            [("Is eco-friendly cleaning as effective as regular cleaning?", "Yes. Professional green cleaning uses advanced plant-based enzymes and microfiber technology that remove dirt and bacteria just as effectively as chemical cleaners."),
             ("Do I need to provide my own eco-friendly products?", "No. We bring all supplies. If you have a preferred brand, just let Cherie know before your visit and she'll use yours."),
             ("Is eco-friendly cleaning more expensive?", "No. Our pricing is the same regardless of product type. Standard cleaning from $120, deep from $250.")]
        ]
    },
    {
        "slug": "weekly-house-cleaning-okc",
        "title": "Weekly House Cleaning in Oklahoma City | Recurring Maid Service OKC",
        "desc": "Weekly house cleaning in Oklahoma City. Consistent, reliable maid service with 15% discount for recurring clients. Same cleaner every visit.",
        "h1": "Weekly House Cleaning in Oklahoma City",
        "content": [
            ("Weekly house cleaning keeps your OKC home consistently clean without the weekend chore rush. With recurring service, you come home to a fresh, clean space every week — and save 15% on regular visits.",
             "Our weekly cleaning includes full kitchen and bathroom sanitation, floor mopping and vacuuming, dusting all surfaces, and making beds. We customize the checklist based on your home's needs. Same cleaner, same standards, every visit.",
             "Weekly service starts at $102/visit for a 2-bedroom OKC home (15% off the standard $120 rate). Bi-weekly service is also available at 10% discount."),
            ["15% discount on recurring weekly service", "Same dedicated cleaner every visit", "Flexible scheduling — morning, afternoon, or evening", "Skip or reschedule with 24-hour notice"],
            [("What if I need to cancel a week?", "No problem. Just text Cherie 24 hours before your scheduled cleaning day and we'll skip that week with no charge."),
             ("Can I add extra services to my weekly cleaning?", "Yes. Deep cleaning of specific rooms, oven cleaning, refrigerator cleaning, and window washing can be added to any weekly visit."),
             ("How long does a weekly cleaning take?", "1-2 hours for a typical 2-bedroom home. Larger homes take 2-3 hours.")]
        ]
    },
    {
        "slug": "affordable-house-cleaning-okc",
        "title": "Affordable House Cleaning in Oklahoma City | Cheap Maid Service OKC",
        "desc": "Affordable house cleaning in Oklahoma City starting at $80 for apartments. Budget-friendly maid service without cutting corners. Free estimates.",
        "h1": "Affordable House Cleaning in Oklahoma City",
        "content": [
            ("House cleaning in Oklahoma City doesn't have to break the bank. We offer professional cleaning services starting at just $80 for a 1-bedroom apartment. Our prices are 10-15% below the national average because OKC's cost of living is lower — and we pass those savings to you.",
             "Affordable doesn't mean cutting corners. We use the same professional-grade equipment and techniques as premium services. The difference? We don't spend money on fancy offices or advertising — just on cleaning your home well.",
             "OKC cleaning prices are $17-25 per hour on average. For a 2-bedroom standard clean, expect $120-170. Compare that to Merry Maids ($160-250) or HappyCleans ($140-200) — we're consistently the budget-friendly choice."),
            ["Starting at $80 for apartments", "No hidden fees or surprise charges", "Transparent pricing with upfront quotes", "Senior and military discounts available"],
            [("Is there a minimum for affordable cleaning?", "Yes, the minimum charge is $80 for a studio apartment. Most 2-bedroom homes run $120-170."),
             ("Do you provide cleaning supplies?", "Yes, all supplies are included. If you want us to use your own products, that's fine too."),
             ("How do I get the best price?", "Weekly or bi-weekly recurring service gives you the best per-visit rates. One-time cleanings are priced slightly higher.")]
        ]
    },
    {
        "slug": "spring-cleaning-okc",
        "title": "Spring Cleaning in Oklahoma City | Deep Spring Clean OKC",
        "desc": "Professional spring cleaning in Oklahoma City. Top-to-bottom deep clean for OKC homes. Remove winter grime, allergens, and clutter. Book your spring refresh.",
        "h1": "Spring Cleaning in Oklahoma City",
        "content": [
            ("Spring in Oklahoma City means pollen, dust, and the need for a reset. Our spring cleaning service goes far beyond regular maintenance — we clean every surface, every corner, and every crevice. Baseboards, window tracks, light fixtures, inside cabinets — everything.",
             "Spring cleaning is especially important in OKC because our homes trap winter dust and allergens from heating systems. A thorough spring clean removes accumulated dust, reduces allergens, and prepares your home for the warmer months ahead.",
             "Spring cleaning typically starts at $250 for a 2-bedroom home. The exact price depends on the size and condition of your home. Book in March or April for the best availability — spring is our busiest season."),
            ["Full home deep clean — every room, every surface", "Inside cabinets, drawers, and closets", "Window tracks, blinds, and light fixtures", "Baseboards, door frames, and crown molding"],
            [("How is spring cleaning different from regular cleaning?", "Spring cleaning includes areas that regular maintenance doesn't cover: inside appliances, window tracks, baseboards, light fixtures, and organizing. It's a comprehensive reset."),
             ("How long does spring cleaning take?", "A typical 2-bedroom home takes 3-5 hours. Larger homes may take 6-8 hours. We'll give you a time estimate when you book."),
             ("Should I spring clean before or after the pollen season?", "After the peak pollen season (late April to early May) is ideal — we'll remove all the pollen that settled on surfaces.")]
        ]
    },
    {
        "slug": "end-of-lease-cleaning-okc",
        "title": "End of Lease Cleaning in Oklahoma City | Move Out Cleaning OKC",
        "desc": "End of lease cleaning in Oklahoma City. Get your full security deposit back. Landlord-approved move-out cleaning. Guaranteed or we reclean.",
        "h1": "End of Lease Cleaning in Oklahoma City",
        "content": [
            ("Moving out of an OKC rental? Landlords expect a spotless property — and they'll deduct from your deposit for any missed spots. Our end-of-lease cleaning is designed to pass even the strictest landlord inspection in Oklahoma City.",
             "We clean everything the landlord checks: kitchen (inside oven, stovetop, refrigerator, cabinets), bathrooms (tile, grout, toilet, shower), windows and tracks, baseboards, light switches, and more. We use a landlord inspection checklist to ensure nothing is missed.",
             "End-of-lease cleaning starts at $300 for a 2-bedroom apartment. Most tenants get their full deposit back after our service. We guarantee your cleaning will pass inspection — or we'll reclean for free."),
            ["Landlord inspection checklist included", "Inside appliances — oven, fridge, microwave", "Window tracks, blinds, and sills", "Free reclean if landlord isn't satisfied"],
            [("Is end-of-lease cleaning the same as move-out cleaning?", "Yes. We use both terms interchangeably. It's the comprehensive cleaning required when leaving a rental property."),
             ("Do you clean the property after I've moved furniture out?", "Yes. End-of-lease cleaning is best done after all furniture is removed for full access to walls, floors, and baseboards."),
             ("Can you provide a receipt for my landlord?", "Yes. We provide a detailed cleaning receipt you can submit to your landlord as proof of professional cleaning.")]
        ]
    },
    {
        "slug": "house-cleaning-services-near-me-okc",
        "title": "House Cleaning Services Near Me in Oklahoma City | Local OKC Cleaners",
        "desc": "Looking for house cleaning services near you in Oklahoma City? Local OKC cleaner Cherie Robinson serves all OKC neighborhoods. Fast response. Free quotes.",
        "h1": "House Cleaning Services Near You in Oklahoma City",
        "content": [
            ("Searching for 'house cleaning near me' in Oklahoma City? You've found your local cleaner. Cherie Robinson serves all OKC neighborhoods — from downtown and Bricktown to NW OKC, Edmond, and beyond.",
             "When you hire local, you get personalized service. Unlike national franchises that send different crews each time, Cherie is your dedicated cleaner. She knows your home, your preferences, and your schedule.",
             "Local OKC cleaning services start at $80 for apartments and $120 for 2-bedroom homes. Response time is typically 24-48 hours. Same-day service is available for recurring clients."),
            ["Local OKC cleaner — not a national franchise", "Same person cleaning every visit", "Fast response — typically within 24 hours", "Free, no-obligation quotes"],
            [("How fast can you come to my home?", "Most first-time clients get an appointment within 2 days. For recurring clients, same-day cleaning is often available."),
             ("Do you serve all of Oklahoma City?", "Yes. We cover downtown OKC, NW OKC, Edmond, Midwest City, Del City, Moore, Norman, and all surrounding areas."),
             ("How is local better than a franchise?", "Consistency. Cherie is the same person every visit. National franchises rotate cleaners. Local means personalized service and attention to detail.")]
        ]
    },
    {
        "slug": "one-time-deep-cleaning-okc",
        "title": "One-Time Deep Cleaning in Oklahoma City | Single Deep Clean OKC",
        "desc": "One-time deep cleaning in Oklahoma City. Perfect before a party, after renovation, or when you need a reset. Professional deep clean starting at $250.",
        "h1": "One-Time Deep Cleaning in Oklahoma City",
        "content": [
            ("Need a deep clean but don't want recurring service? Our one-time deep cleaning is perfect for special occasions, post-renovation cleanup, or when your home needs a thorough reset. No commitment, no recurring charges — just a sparkling clean home.",
             "Our deep cleaning covers what standard cleaning doesn't: baseboards and trim, window tracks and sills, inside kitchen cabinets, oven and stovetop interior, refrigerator coils and shelves, bathroom tile and grout scrubbing, light fixtures and ceiling fans, and more.",
             "One-time deep cleaning in OKC starts at $250 for a 2-bedroom home. For larger homes (3-4 bedrooms), expect $330-450. We'll give you an exact quote before starting."),
            ["No contract or recurring commitment", "Everything included — no add-on charges", "Perfect for special events and occasions", "Post-renovation and move-in ready"],
            [("Can I book a deep cleaning just once?", "Absolutely. One-time deep cleaning is our most popular service for new clients. There's no obligation to continue."),
             ("What's the difference between deep and standard cleaning?", "Deep cleaning covers more areas: inside appliances, baseboards, window tracks, light fixtures, and detailed bathroom scrubbing. Standard cleaning covers surfaces, floors, and daily maintenance."),
             ("How long does a one-time deep clean take?", "A 2-bedroom home typically takes 3-4 hours for a deep clean. Add 1-2 hours per additional bedroom.")]
        ]
    },
    {
        "slug": "senior-home-cleaning-okc",
        "title": "House Cleaning for Seniors in Oklahoma City | Senior Home Care OKC",
        "desc": "House cleaning services for seniors in Oklahoma City. Trusted, reliable cleaning for elderly homeowners. Light housekeeping, deep cleaning, and more.",
        "h1": "House Cleaning for Seniors in Oklahoma City",
        "content": [
            ("As we age, keeping up with house cleaning becomes harder. Our senior-focused cleaning services in Oklahoma City help elderly homeowners maintain a clean, safe, and healthy home. We handle the heavy cleaning so seniors can focus on what matters.",
             "Senior cleaning includes light housekeeping (dusting, vacuuming, bathroom cleaning), deep cleaning (kitchen, floors, windows), and organizational help. We're patient, respectful, and trained to work around seniors' needs and schedules.",
             "Senior cleaning rates start at $45/hour or $120 for a standard 2-bedroom home. Many OKC seniors save 10% with our weekly recurring service."),
            ["Patient, respectful service for elderly clients", "Light or deep — customized to your needs", "Background-checked and insured cleaner", "Help with reaching high places, heavy lifting"],
            [("Do you provide senior discounts?", "Yes. We offer a 10% discount for senior citizens on all recurring cleaning services."),
             ("Can you clean just a few rooms instead of the whole house?", "Yes. We customize every cleaning plan. If you only need the kitchen and bathroom cleaned, that's what we'll do."),
             ("Are your cleaners background-checked?", "Yes. Cherie is fully background-checked, insured, and has been serving OKC families for years with excellent references.")]
        ]
    },
    {
        "slug": "new-home-cleaning-okc",
        "title": "New Home Cleaning in Oklahoma City | First-Time Homeowner Clean OKC",
        "desc": "New home cleaning services in Oklahoma City. For first-time homeowners and move-ins. Deep clean before you unpack. Dust-free, move-in ready.",
        "h1": "New Home Cleaning in Oklahoma City",
        "content": [
            ("Bought a new home in Oklahoma City? Congratulations! Before you move in, let us give it a thorough deep clean. New homes often have dust from construction, debris from the previous owners, and hidden grime in corners and cabinets.",
             "Our new home cleaning covers everything: deep kitchen and bathroom cleaning, inside cabinets and closets, window tracks and blinds, floors (vacuum and mop), baseboards, and light fixtures. We make sure your new home is truly move-in ready.",
             "New home cleaning in OKC starts at $250 for a 2-bedroom home and $330 for a 3-4 bedroom home. We recommend booking 3-5 days before your move-in date."),
            ["Perfect for first-time homeowners", "Construction dust and debris removal", "Inside every cabinet and closet", "Move-in ready — unpack with peace of mind"],
            [("Should I clean before or after moving furniture in?", "Before. Cleaning is much more thorough when rooms are empty. We can access all walls, floors, and baseboards."),
             ("Do you clean new construction homes?", "Yes. New construction homes need extra attention — construction dust gets everywhere. We include extra dusting for new builds."),
             ("Can I add carpet cleaning or window washing?", "Yes. These can be added to any new home cleaning package. Just let us know when you book.")]
        ]
    },
    {
        "slug": "same-day-house-cleaning-okc",
        "title": "Same-Day House Cleaning in Oklahoma City | Emergency Cleaning OKC",
        "desc": "Same-day house cleaning in Oklahoma City. Need a clean home today? We offer same-day emergency cleaning services in OKC. Call now for same-day availability.",
        "h1": "Same-Day House Cleaning in Oklahoma City",
        "content": [
            ("Need your home cleaned today? Unexpected guests, last-minute party, or just can't wait? We offer same-day house cleaning in Oklahoma City for those situations when you need a clean home right now.",
             "Same-day service is available Monday through Saturday. Call us before 11 AM and we'll typically have a cleaner at your home by afternoon. Recurring clients get priority for same-day appointments.",
             "Same-day cleaning starts at $120 for standard cleaning and $250 for deep cleaning. Same-day pricing is the same as regular — no premium for urgency."),
            ["Available Monday-Saturday", "Call before 11 AM for afternoon cleaning", "Same price as regular service — no markup", "Priority for recurring clients"],
            [("Do you charge extra for same-day service?", "No. Same-day pricing is identical to our regular service pricing. We don't charge a premium for urgency."),
             ("What areas of OKC get same-day service?", "All of Oklahoma City metro: downtown, NW OKC, Edmond, Midwest City, Del City, Moore, Norman, and surrounding neighborhoods."),
             ("How quickly can you arrive?", "Typically within 2-4 hours of your call. For recurring clients, we can often arrive within 1-2 hours.")]
        ]
    }
]

def page_html(p):
    faq_items = "".join(
        f'<div class="faq"><h3>{q}</h3><p>{a}</p></div>\n' for q, a in p["content"][2]
    )
    checks = "".join(f"<li>✔ {c}</li>\n" for c in p["content"][1])
    paras = "".join(f"<p>{c}</p>\n" for c in p["content"][0])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">{{
"@context":"https://schema.org","@type":"Article","headline":"{p['h1']}",
"datePublished":"2026-08-22","author":{{"@type":"Organization","name":"House Cleaning Oklahoma City"}},
"publisher":{{"@type":"Organization","name":"House Cleaning Oklahoma City"}},
"mainEntityOfPage":"https://{DOMAIN}/{p['slug']}.html"
}}</script>
</head>
<body>
<div class="top">📞 Same-day cleaning available — <a href="tel:{PHONE_TEL}">Call Cherie {PHONE}</a></div>
<nav>
<a href="index.html">Home</a>
<a href="deep-cleaning.html">Deep</a>
<a href="move-out-cleaning.html">Move-Out</a>
<a href="apartment-cleaning.html">Apartments</a>
<a href="blog.html">Blog</a>
</nav>
<header><h1>{p['h1']}</h1></header>
<section>{paras}</section>
<section><h2>Why Choose Us</h2><ul class="checks">{checks}</ul></section>
<section><h2>Frequently Asked Questions</h2><div class="faq">{faq_items}</div></section>
<footer>
<div class="links">
<a href="index.html">Home</a>
<a href="deep-cleaning.html">Deep Cleaning</a>
<a href="move-out-cleaning.html">Move-Out Cleaning</a>
<a href="apartment-cleaning.html">Apartment Cleaning</a>
<a href="blog.html">Blog</a>
</div>
<p><strong>House Cleaning Oklahoma City — powered by Cherie Robinson</strong> — Serving OKC since 2018</p>
<p>📞 <a href="tel:{PHONE_TEL}">{PHONE}</a> | {DOMAIN}</p>
</footer>
</body>
</html>"""

for p in PAGES:
    path = os.path.join(BASE, f"{p['slug']}.html")
    with open(path, "w") as f:
        f.write(page_html(p))
    print(f"✅ generated {p['slug']}.html")

print(f"\n📊 Total: {len(PAGES)} new pages created")