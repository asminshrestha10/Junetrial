import os
from _build import render

OUT = os.path.dirname(__file__)


def write(path, title, description, canonical, root, body, extra_head=""):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(render(title, description, canonical, root, body, extra_head))
    print("wrote", path)


# ---------------------------------------------------------------
# BLOG INDEX  →  /blog/
# ---------------------------------------------------------------
blog_index_body = """
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span>Blog</div>
  <div class="page-head">
    <div class="eyebrow">BLOG</div>
    <h1>The Trail Journal</h1>
    <p>Weekly guides, comparisons and practical advice for Australian 4WD owners — informational, commercial and comparison content, organised by category.</p>
  </div>
  <div class="filter-bar">
    <span class="filter-chip active">All</span>
    <span class="filter-chip">Recovery</span>
    <span class="filter-chip">Touring</span>
    <span class="filter-chip">Suspension</span>
    <span class="filter-chip">Maintenance</span>
    <span class="filter-chip">Off-Road Driving</span>
  </div>
</div>
<section style="padding-top:0;">
  <div class="container">
    <div class="art-grid">
      <div class="art-card">
        <div class="art-img"></div>
        <div class="art-body">
          <div class="art-cat">Recovery</div>
          <h4><a href="/blog/best-4wd-recovery-boards.html">Best Recovery Boards for 4WDing in Australia</a></h4>
          <p>Our top picks for traction boards, tested against load rating, weight and price.</p>
          <div class="art-meta">18 AUG 2026 · 9 MIN READ</div>
        </div>
      </div>
      <div class="art-card">
        <div class="art-img"></div>
        <div class="art-body">
          <div class="art-cat">Recovery</div>
          <h4><a href="#">How to Recover a Bogged 4WD Safely, Step by Step</a></h4>
          <p>Assessing the bog, rigging gear correctly, and recovering without damaging your vehicle.</p>
          <div class="art-meta">18 AUG 2026 · 7 MIN READ</div>
        </div>
      </div>
      <div class="art-card">
        <div class="art-img"></div>
        <div class="art-body">
          <div class="art-cat">Off-Road Driving</div>
          <h4><a href="#">What Tyre Pressure Should You Run Off-Road?</a></h4>
          <p>Matching tyre pressure to terrain without compromising bead safety.</p>
          <div class="art-meta">11 AUG 2026 · 6 MIN READ</div>
        </div>
      </div>
      <div class="art-card">
        <div class="art-img"></div>
        <div class="art-body">
          <div class="art-cat">Comparison</div>
          <h4><a href="#">Snatch Strap vs Winch: Which Recovery Method Wins?</a></h4>
          <p>Cost, control and risk — kinetic recovery versus winching.</p>
          <div class="art-meta">4 AUG 2026 · 8 MIN READ</div>
        </div>
      </div>
      <div class="art-card">
        <div class="art-img"></div>
        <div class="art-body">
          <div class="art-cat">Touring</div>
          <h4><a href="#">Lithium vs AGM Batteries for Your Dual Battery Setup</a></h4>
          <p>Weight, cycle life and charging behaviour compared for touring rigs.</p>
          <div class="art-meta">28 JUL 2026 · 7 MIN READ</div>
        </div>
      </div>
      <div class="art-card">
        <div class="art-img"></div>
        <div class="art-body">
          <div class="art-cat">Suspension</div>
          <h4><a href="#">33-Inch vs 35-Inch Tyres: What Actually Changes</a></h4>
          <p>Clearance, gearing and drivetrain wear — the real trade-offs of sizing up.</p>
          <div class="art-meta">21 JUL 2026 · 8 MIN READ</div>
        </div>
      </div>
    </div>
  </div>
</section>
"""
write(
    "blog/index.html",
    "4x4 Blog & Guides | JuneTrail",
    "Weekly 4x4 guides, gear comparisons and practical off-road advice for Australian 4WD owners.",
    "https://junetrail.com.au/blog/",
    "/",
    blog_index_body,
)

# ---------------------------------------------------------------
# ARTICLE TEMPLATE (worked example)  →  /blog/best-4wd-recovery-boards.html
# ---------------------------------------------------------------
article_body = """
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/blog/">Blog</a><span class="sep">/</span>Best 4WD Recovery Boards</div>
  <div class="article-head">
    <div class="eyebrow">RECOVERY · COMMERCIAL GUIDE</div>
    <h1>Best Recovery Boards for 4WDing in Australia</h1>
    <div class="article-meta">
      <span>18 AUG 2026</span><span>·</span><span>9 MIN READ</span><span>·</span><span>UPDATED FOR 2026</span>
    </div>
  </div>
</div>

<div class="article-body">
  <p>Recovery boards are the first thing that should go in your kit, not the last. This guide breaks down what actually matters when you're bogged in sand or mud, and compares the boards worth carrying.</p>

  <div class="demo-banner mono">DEMO CONTENT — the products, specs and prices below are placeholders for layout purposes only.</div>

  <div class="toc">
    <span class="eyebrow">ON THIS PAGE</span>
    <a href="#quick-answer">Quick Answer</a>
    <a href="#top-picks">Our Top Picks</a>
    <a href="#what-to-look-for">What Should You Look For?</a>
    <a href="#how-we-selected">How We Selected These Products</a>
    <a href="#faq">Frequently Asked Questions</a>
    <a href="#final-recommendation">Final Recommendation</a>
  </div>

  <div class="quick-answer" id="quick-answer">
    <div class="eyebrow">QUICK ANSWER</div>
    <ol>
      <li>Best overall — Traction Recovery Board (Pair)</li>
      <li>Best budget — Composite Traction Board (Pair)</li>
      <li>Best for heavy tourers — Reinforced Recovery Board (Pair)</li>
    </ol>
  </div>

  <h2 id="top-picks">Our Top Picks</h2>

  <h3>1. Traction Recovery Board (Pair)</h3>
  <p>Placeholder overview — strong all-round choice for sand and mud recovery, balancing weight and load rating.</p>
  <div class="pros-cons">
    <div><h5>Pros</h5>Good load rating · Compact for storage · Wide track</div>
    <div><h5>Cons</h5>Higher price point · Firm underfoot on rock</div>
  </div>
  <a href="#" class="btn btn-primary" style="display:inline-block;">CHECK PRICE</a>

  <h3>2. Composite Traction Board (Pair)</h3>
  <p>Placeholder overview — budget-friendly option, suitable for occasional touring rather than heavy-duty recovery.</p>

  <h2 id="compare">Comparison Table</h2>
  <div class="compare-wrap">
    <table class="compare">
      <thead>
        <tr><th>Product</th><th>Price</th><th>Weight</th><th>Load Rating</th><th>Material</th><th>Best For</th><th>Link</th></tr>
      </thead>
      <tbody>
        <tr><td>Traction Recovery Board</td><td>TBC</td><td>TBC</td><td>TBC</td><td>Reinforced polymer</td><td>All-round touring</td><td><a class="cell-link" href="#">Check price →</a></td></tr>
        <tr><td>Composite Traction Board</td><td>TBC</td><td>TBC</td><td>TBC</td><td>Composite</td><td>Occasional use</td><td><a class="cell-link" href="#">Check price →</a></td></tr>
        <tr><td>Reinforced Recovery Board</td><td>TBC</td><td>TBC</td><td>TBC</td><td>Reinforced polymer</td><td>Heavy tourers</td><td><a class="cell-link" href="#">Check price →</a></td></tr>
      </tbody>
    </table>
  </div>

  <h2 id="what-to-look-for">What Should You Look For?</h2>
  <p>Load rating relative to your fully-laden vehicle weight matters more than headline strength claims. Look for a rating comfortably above your GVM, tread pattern that suits your usual terrain, and a board that stacks or stores flat against your existing setup.</p>
  <ul>
    <li>Load rating vs your vehicle's actual laden weight</li>
    <li>Tread depth for your typical terrain (sand vs mud)</li>
    <li>Storage footprint — flat stacking vs bulky profiles</li>
    <li>UV resistance for boards stored on a roof rack</li>
  </ul>

  <h2 id="how-we-selected">How We Selected These Products</h2>
  <p>We shortlist based on published specifications, load ratings, and consistent patterns across verified owner feedback. We do not accept payment for placement, and we clearly flag when a product has not been physically tested.</p>

  <h2 id="faq">Frequently Asked Questions</h2>
  <div class="faq-item"><h3>Do I need two boards or four?</h3><p>Two is the minimum for most recoveries; four gives you options on soft, uneven terrain where more than one wheel is affected.</p></div>
  <div class="faq-item"><h3>Are cheaper composite boards worth it?</h3><p>For occasional use on established tracks, yes. For remote touring, the higher load rating of a reinforced board is worth the extra cost.</p></div>
  <div class="faq-item"><h3>Can recovery boards replace a winch?</h3><p>No — they solve different problems. Boards help you drive out; a winch pulls you out when driving isn't possible.</p></div>

  <h2 id="final-recommendation">Final Recommendation</h2>
  <p>For most Australian 4WD owners, a mid-weight reinforced board pair covers sand, mud and light rock recovery without adding excessive kit weight. Budget boards are a reasonable entry point if you're touring on maintained tracks only.</p>

  <p style="font-size:12px;color:var(--contour);margin-top:30px;">This article contains affiliate links. See our <a href="/legal/affiliate-disclosure.html">affiliate disclosure</a>.</p>
</div>

<section class="related">
  <div class="container">
    <div class="section-head"><div><div class="eyebrow">RELATED</div><h2>Keep reading</h2></div></div>
    <div class="art-grid">
      <div class="art-card"><div class="art-img"></div><div class="art-body"><div class="art-cat">Recovery</div><h4>How to Recover a Bogged 4WD Safely</h4></div></div>
      <div class="art-card"><div class="art-img"></div><div class="art-body"><div class="art-cat">Comparison</div><h4>Snatch Strap vs Winch</h4></div></div>
      <div class="art-card"><div class="art-img"></div><div class="art-body"><div class="art-cat">Off-Road Driving</div><h4>What Tyre Pressure Should You Run Off-Road?</h4></div></div>
    </div>
  </div>
</section>
"""
write(
    "blog/best-4wd-recovery-boards.html",
    "Best 4WD Recovery Boards in Australia (2026 Guide) | JuneTrail",
    "We compare the best recovery boards for Australian 4WD owners on load rating, weight, material and price.",
    "https://junetrail.com.au/blog/best-4wd-recovery-boards/",
    "/",
    article_body,
    extra_head='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Best Recovery Boards for 4WDing in Australia","datePublished":"2026-08-18"}</script>',
)

# ---------------------------------------------------------------
# PRODUCTS INDEX  →  /products/
# ---------------------------------------------------------------
products_index_body = """
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span>Products</div>
  <div class="page-head">
    <div class="eyebrow">PRODUCTS</div>
    <h1>Gear Catalogue</h1>
    <p>Browse by category. Every product links out to Amazon with tracked affiliate parameters.</p>
  </div>
  <div class="demo-banner mono">DEMO CONTENT — placeholder catalogue shown for layout purposes only.</div>
</div>
<section style="padding-top:0;">
  <div class="container">
    <div class="cat-grid">
      <a class="cat-card" href="/products/recovery-gear/"><div class="n">17 CATEGORIES</div><h3>Recovery Gear</h3></a>
      <a class="cat-card" href="#"><div class="n">17 CATEGORIES</div><h3>Winches</h3></a>
      <a class="cat-card" href="#"><div class="n">17 CATEGORIES</div><h3>Suspension</h3></a>
      <a class="cat-card" href="#"><div class="n">17 CATEGORIES</div><h3>Lighting</h3></a>
      <a class="cat-card" href="#"><div class="n">17 CATEGORIES</div><h3>Bull Bars</h3></a>
      <a class="cat-card" href="#"><div class="n">17 CATEGORIES</div><h3>Towing &amp; Towbars</h3></a>
      <a class="cat-card" href="#"><div class="n">17 CATEGORIES</div><h3>Camping Gear</h3></a>
      <a class="cat-card" href="#"><div class="n">17 CATEGORIES</div><h3>Fridges</h3></a>
      <a class="cat-card" href="#"><div class="n">17 CATEGORIES</div><h3>UHF Radios</h3></a>
    </div>
  </div>
</section>
"""
write(
    "products/index.html",
    "4WD Gear & Accessories Catalogue | JuneTrail",
    "Browse 4WD gear by category — recovery, suspension, lighting, camping and more.",
    "https://junetrail.com.au/products/",
    "/",
    products_index_body,
)

# ---------------------------------------------------------------
# PRODUCT CATEGORY  →  /products/recovery-gear/
# ---------------------------------------------------------------
category_body = """
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/products/">Products</a><span class="sep">/</span>Recovery Gear</div>
  <div class="page-head">
    <div class="eyebrow">CATEGORY</div>
    <h1>Recovery Gear</h1>
    <p>Traction boards, snatch straps, shackles and recovery points — everything for getting unstuck safely.</p>
  </div>
  <div class="demo-banner mono">DEMO CONTENT — placeholder products shown for layout purposes only.</div>
</div>
<section style="padding-top:0;">
  <div class="container">
    <div class="prod-grid">
      <div class="prod-card">
        <div class="prod-img">RECOVERY BOARD<br>[Placeholder]</div>
        <div class="prod-body">
          <div class="prod-cat">Recovery Gear</div>
          <h4><a href="/products/recovery-gear/traction-recovery-board.html">Traction Recovery Board (Pair)</a></h4>
          <div class="prod-rating">★★★★☆ (Demo)</div>
          <div class="prod-price">Price — TBC</div>
          <a href="/products/recovery-gear/traction-recovery-board.html" class="btn-small">VIEW PRODUCT</a>
        </div>
      </div>
      <div class="prod-card">
        <div class="prod-img">SNATCH STRAP<br>[Placeholder]</div>
        <div class="prod-body">
          <div class="prod-cat">Recovery Gear</div>
          <h4>9m Kinetic Snatch Strap</h4>
          <div class="prod-rating">★★★★★ (Demo)</div>
          <div class="prod-price">Price — TBC</div>
          <a href="#" class="btn-small">VIEW PRODUCT</a>
        </div>
      </div>
      <div class="prod-card">
        <div class="prod-img">RECOVERY POINT<br>[Placeholder]</div>
        <div class="prod-body">
          <div class="prod-cat">Recovery Gear</div>
          <h4>Rated Recovery Point (Pair)</h4>
          <div class="prod-rating">★★★★☆ (Demo)</div>
          <div class="prod-price">Price — TBC</div>
          <a href="#" class="btn-small">VIEW PRODUCT</a>
        </div>
      </div>
      <div class="prod-card">
        <div class="prod-img">BOW SHACKLE<br>[Placeholder]</div>
        <div class="prod-body">
          <div class="prod-cat">Recovery Gear</div>
          <h4>Rated Bow Shackle (Pair)</h4>
          <div class="prod-rating">★★★★☆ (Demo)</div>
          <div class="prod-price">Price — TBC</div>
          <a href="#" class="btn-small">VIEW PRODUCT</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""
write(
    "products/recovery-gear/index.html",
    "Recovery Gear for 4WDs | JuneTrail",
    "Traction boards, snatch straps, recovery points and shackles for Australian 4WD recovery.",
    "https://junetrail.com.au/products/recovery-gear/",
    "/",
    category_body,
)

# ---------------------------------------------------------------
# PRODUCT DETAIL  →  /products/recovery-gear/traction-recovery-board.html
# ---------------------------------------------------------------
product_detail_body = """
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/products/">Products</a><span class="sep">/</span><a href="/products/recovery-gear/">Recovery Gear</a><span class="sep">/</span>Traction Recovery Board</div>
  <div class="product-detail">
    <div class="product-gallery">
      <div class="prod-img" style="aspect-ratio:1/1;">RECOVERY BOARD<br>[Placeholder image]</div>
    </div>
    <div class="product-info">
      <div class="eyebrow">RECOVERY GEAR</div>
      <h1>Traction Recovery Board (Pair)</h1>
      <div class="prod-rating">★★★★☆ (Demo rating)</div>
      <div class="price-row"><span class="price">Price — TBC</span></div>
      <p>Placeholder description — reinforced polymer traction boards designed for sand, mud and snow recovery. Pending live product feed.</p>
      <table class="spec-table">
        <tr><td>Brand</td><td>TBC</td></tr>
        <tr><td>Material</td><td>Reinforced polymer</td></tr>
        <tr><td>Weight (pair)</td><td>TBC</td></tr>
        <tr><td>Load rating</td><td>TBC</td></tr>
        <tr><td>Dimensions</td><td>TBC</td></tr>
      </table>
      <div class="pros-cons">
        <div><h5>Pros</h5>Good load rating · Compact storage · Wide track width</div>
        <div><h5>Cons</h5>Premium price point · Firm underfoot on rock</div>
      </div>
      <a href="#" class="btn btn-primary" style="display:inline-block;">CHECK PRICE ON AMAZON</a>
      <p style="font-size:12px;color:var(--contour);margin-top:14px;">As an Amazon Associate, JuneTrail earns from qualifying purchases. See our <a href="/legal/affiliate-disclosure.html">affiliate disclosure</a>.</p>
    </div>
  </div>
</div>
"""
write(
    "products/recovery-gear/traction-recovery-board.html",
    "Traction Recovery Board (Pair) | JuneTrail",
    "Specs, pros and cons for reinforced traction recovery boards — demo product page.",
    "https://junetrail.com.au/products/recovery-gear/traction-recovery-board/",
    "/",
    product_detail_body,
)

# ---------------------------------------------------------------
# VEHICLES INDEX  →  /vehicles/
# ---------------------------------------------------------------
vehicles_index_body = """
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span>Vehicles</div>
  <div class="page-head">
    <div class="eyebrow">VEHICLE GUIDES</div>
    <h1>Setup Guides by Platform</h1>
    <p>Modification, recovery point and accessory guidance for the most common Australian 4WD platforms.</p>
  </div>
</div>
<section style="padding-top:0;">
  <div class="container">
    <div class="cat-grid">
      <a class="cat-card" href="/vehicles/toyota-hilux.html"><div class="n">4WD PLATFORM</div><h3>Toyota Hilux</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Toyota LandCruiser</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Toyota Prado</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Ford Ranger</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Ford Everest</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Nissan Navara</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Nissan Patrol</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Mitsubishi Triton</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Mitsubishi Pajero</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Isuzu D-Max</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Isuzu MU-X</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>Mazda BT-50</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>GWM Cannon</h3></a>
      <a class="cat-card" href="#"><div class="n">4WD PLATFORM</div><h3>LDV T60</h3></a>
    </div>
  </div>
</section>
"""
write(
    "vehicles/index.html",
    "4WD Vehicle Setup Guides | JuneTrail",
    "Modification, recovery point and accessory guides for Australia's most common 4WD platforms.",
    "https://junetrail.com.au/vehicles/",
    "/",
    vehicles_index_body,
)

# ---------------------------------------------------------------
# VEHICLE GUIDE (worked example)  →  /vehicles/toyota-hilux.html
# ---------------------------------------------------------------
vehicle_body = """
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/vehicles/">Vehicles</a><span class="sep">/</span>Toyota Hilux</div>
  <div class="article-head" style="max-width:820px;">
    <div class="eyebrow">VEHICLE GUIDE</div>
    <h1>Toyota Hilux 4WD Setup Guide</h1>
    <div class="article-meta"><span>UPDATED 18 AUG 2026</span></div>
  </div>
</div>

<div class="article-body">
  <p>The Hilux is one of the most modified 4WDs in Australia, with strong aftermarket support across suspension, recovery and touring categories. This guide covers the setup path most owners take, from recovery points to full touring builds.</p>

  <h2>Vehicle Overview</h2>
  <p>Placeholder overview — covers current-generation Hilux dimensions, GVM, and common trim-level differences relevant to accessory fitment.</p>

  <h2>Common Modifications</h2>
  <ul>
    <li>Suspension lift for tyre clearance and payload</li>
    <li>Bull bar fitment for recovery points and lighting mounts</li>
    <li>Rated recovery points front and rear</li>
    <li>Roof rack for camping and touring gear</li>
  </ul>

  <h2>Suspension</h2>
  <p>Placeholder guidance on lift height selection relative to GVM and touring load.</p>

  <h2>Tyres</h2>
  <p>Placeholder guidance on tyre sizing trade-offs for this platform.</p>

  <h2>Recovery Points</h2>
  <p>Placeholder guidance on rated recovery point fitment front and rear.</p>

  <h2>Recommended Accessories</h2>
  <div class="prod-grid" style="margin-top:16px;">
    <div class="prod-card">
      <div class="prod-img">BULL BAR<br>[Placeholder]</div>
      <div class="prod-body"><div class="prod-cat">Bull Bars</div><h4>Steel Bull Bar</h4><div class="prod-price">Price — TBC</div><a href="#" class="btn-small">CHECK PRICE</a></div>
    </div>
    <div class="prod-card">
      <div class="prod-img">SUSPENSION KIT<br>[Placeholder]</div>
      <div class="prod-body"><div class="prod-cat">Suspension</div><h4>2" Lift Suspension Kit</h4><div class="prod-price">Price — TBC</div><a href="#" class="btn-small">CHECK PRICE</a></div>
    </div>
  </div>

  <p style="font-size:12px;color:var(--contour);margin-top:30px;">This page contains affiliate links. See our <a href="/legal/affiliate-disclosure.html">affiliate disclosure</a>.</p>
</div>
"""
write(
    "vehicles/toyota-hilux.html",
    "Toyota Hilux 4WD Setup Guide | JuneTrail",
    "Suspension, recovery points, bull bars and touring accessories for the Toyota Hilux.",
    "https://junetrail.com.au/vehicles/toyota-hilux/",
    "/",
    vehicle_body,
)

# ---------------------------------------------------------------
# REVIEWS INDEX  →  /reviews/
# ---------------------------------------------------------------
reviews_body = """
<div class="container">
  <div class="breadcrumb"><a href="/">Home</a><span class="sep">/</span>Reviews</div>
  <div class="page-head">
    <div class="eyebrow">REVIEWS</div>
    <h1>Product Reviews & Comparisons</h1>
    <p>In-depth reviews and side-by-side comparisons across recovery gear, suspension, lighting and more.</p>
  </div>
  <div class="demo-banner mono">DEMO CONTENT — placeholder listing shown for layout purposes only.</div>
</div>
<section style="padding-top:0;">
  <div class="container">
    <div class="art-grid">
      <div class="art-card"><div class="art-img"></div><div class="art-body"><div class="art-cat">Comparison</div><h4><a href="/blog/best-4wd-recovery-boards.html">Best Recovery Boards for 4WDing in Australia</a></h4></div></div>
      <div class="art-card"><div class="art-img"></div><div class="art-body"><div class="art-cat">Comparison</div><h4>Snatch Strap vs Winch</h4></div></div>
      <div class="art-card"><div class="art-img"></div><div class="art-body"><div class="art-cat">Comparison</div><h4>Lithium vs AGM Batteries</h4></div></div>
    </div>
  </div>
</section>
"""
write(
    "reviews/index.html",
    "4WD Product Reviews & Comparisons | JuneTrail",
    "In-depth reviews and comparisons of 4WD gear — recovery, suspension, lighting and more.",
    "https://junetrail.com.au/reviews/",
    "/",
    reviews_body,
)

# ---------------------------------------------------------------
# ABOUT / CONTACT
# ---------------------------------------------------------------
about_body = """
<div class="prose container">
  <div class="eyebrow">ABOUT</div>
  <h1>About JuneTrail</h1>
  <p>JuneTrail is an Australian 4x4 and off-road resource built on practical, engineering-informed guidance — not marketing copy. We write for owners who want to understand why a piece of gear works, not just what it costs.</p>
  <h2>Editorial approach</h2>
  <p>Recommendations are based on published specifications, manufacturer data and consistent patterns across verified owner feedback. We disclose affiliate relationships clearly and never claim a product was personally tested unless testing actually took place.</p>
  <h2>Author profiles</h2>
  <p>Placeholder — author bio and credentials to be added.</p>
</div>
"""
write("about.html", "About JuneTrail", "Who JuneTrail is and how we research 4WD gear.", "https://junetrail.com.au/about.html", "/", about_body)

contact_body = """
<div class="prose container">
  <div class="eyebrow">CONTACT</div>
  <h1>Contact</h1>
  <p>For product suggestions, corrections or partnership enquiries, reach out below.</p>
  <p>Email — <a href="mailto:hello@junetrail.com.au">hello@junetrail.com.au</a></p>
</div>
"""
write("contact.html", "Contact JuneTrail", "Get in touch with the JuneTrail team.", "https://junetrail.com.au/contact.html", "/", contact_body)

# ---------------------------------------------------------------
# LEGAL PAGES
# ---------------------------------------------------------------
disclosure_body = """
<div class="prose container">
  <div class="eyebrow">LEGAL</div>
  <h1>Affiliate Disclosure</h1>
  <p>JuneTrail is a participant in the Amazon Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by linking to Amazon and affiliated sites.</p>
  <p>Some links on this website are affiliate links. If you purchase through these links, we may earn a commission at no additional cost to you. This does not influence which products we recommend — our editorial process is independent of affiliate relationships.</p>
</div>
"""
write("legal/affiliate-disclosure.html", "Affiliate Disclosure | JuneTrail", "How JuneTrail uses affiliate links.", "https://junetrail.com.au/legal/affiliate-disclosure/", "/", disclosure_body)

privacy_body = """
<div class="prose container">
  <div class="eyebrow">LEGAL</div>
  <h1>Privacy Policy</h1>
  <p>Placeholder privacy policy — to be finalised covering data collected via newsletter signup, analytics, and cookies.</p>
</div>
"""
write("legal/privacy-policy.html", "Privacy Policy | JuneTrail", "How JuneTrail handles your data.", "https://junetrail.com.au/legal/privacy-policy/", "/", privacy_body)

terms_body = """
<div class="prose container">
  <div class="eyebrow">LEGAL</div>
  <h1>Terms & Conditions</h1>
  <p>Placeholder terms and conditions — to be finalised prior to launch.</p>
</div>
"""
write("legal/terms.html", "Terms & Conditions | JuneTrail", "Terms of use for JuneTrail.", "https://junetrail.com.au/legal/terms/", "/", terms_body)

editorial_body = """
<div class="prose container">
  <div class="eyebrow">LEGAL</div>
  <h1>Editorial Policy</h1>
  <p>Placeholder editorial policy — outlines our research process, testing methodology (when applicable), and independence from affiliate partners.</p>
</div>
"""
write("legal/editorial-policy.html", "Editorial Policy | JuneTrail", "How JuneTrail researches and writes content.", "https://junetrail.com.au/legal/editorial-policy/", "/", editorial_body)

print("ALL PAGES BUILT")
