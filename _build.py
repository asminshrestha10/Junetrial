"""
JuneTrail static site — page assembly helper.
Not deployed: run locally to stitch head/nav/footer around page bodies,
so every page shares identical markup. Re-run after editing NAV/FOOTER.
"""

HEAD = """<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,ital@9..144,400;9..144,500;9..144,600;9..144,1,500&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
{extra_head}
</head>
<body>
"""

NAV = """<header class="site-nav">
  <div class="nav-inner">
    <a href="{root}" class="wordmark">
      <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M4 30L14 12L20 22L26 10L36 30" stroke="#F4EFE3" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
        <circle cx="20" cy="22" r="1.6" fill="#B8442E"/>
      </svg>
      <span>JUNETRAIL<span class="tag">off the beaten track</span></span>
    </a>
    <nav class="links">
      <a href="{root}blog/">4x4 Guides</a>
      <a href="{root}products/">Products</a>
      <a href="{root}vehicles/">Vehicles</a>
      <a href="{root}reviews/">Reviews</a>
      <a href="{root}blog/">Blog</a>
      <a href="{root}about.html">About</a>
    </nav>
    <div class="nav-right">
      <button class="search-btn">SEARCH</button>
      <button class="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""

FOOTER = """<section class="newsletter">
  <div class="container nl-inner">
    <div class="eyebrow" style="color:var(--lava);">STAY ON TRACK</div>
    <h2>Get Better at 4WDing</h2>
    <p>Weekly 4x4 guides, gear recommendations and off-road tips delivered to your inbox.</p>
    <form class="nl-form" onsubmit="return false;">
      <input type="email" placeholder="you@email.com" required>
      <button class="btn btn-primary" type="submit">SUBSCRIBE</button>
    </form>
  </div>
</section>

<footer id="about">
  <div class="container">
    <div class="foot-grid">
      <div>
        <h5>JuneTrail</h5>
        <p style="max-width:280px; line-height:1.6;">An Australian 4x4 and off-road resource — practical guides, gear reviews and vehicle setups, written with real engineering knowledge behind them.</p>
      </div>
      <div>
        <h5>Explore</h5>
        <a href="{root}blog/">4x4 Guides</a>
        <a href="{root}products/">Products</a>
        <a href="{root}vehicles/">Vehicles</a>
        <a href="{root}blog/">Blog</a>
      </div>
      <div>
        <h5>Company</h5>
        <a href="{root}about.html">About</a>
        <a href="{root}legal/editorial-policy.html">Editorial Policy</a>
        <a href="{root}contact.html">Contact</a>
      </div>
      <div>
        <h5>Legal</h5>
        <a href="{root}legal/affiliate-disclosure.html">Affiliate Disclosure</a>
        <a href="{root}legal/privacy-policy.html">Privacy Policy</a>
        <a href="{root}legal/terms.html">Terms &amp; Conditions</a>
      </div>
    </div>
    <div class="disclosure">
      Some links on this website are affiliate links, including links to Amazon. If you purchase through these links, JuneTrail may earn a commission at no additional cost to you. Product recommendations are based on independent research; we never claim a product was personally tested unless testing actually took place. All product data shown on demo pages is placeholder content pending a live product feed. © 2026 JuneTrail.
    </div>
  </div>
</footer>
<script src="{root}assets/js/main.js"></script>
</body>
</html>
"""


def render(title, description, canonical, root, body, extra_head=""):
    return (
        HEAD.format(title=title, description=description, canonical=canonical, root=root, extra_head=extra_head)
        + NAV.format(root=root)
        + body
        + FOOTER.format(root=root)
    )
