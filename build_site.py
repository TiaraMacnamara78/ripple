import re

with open(r'C:\Users\butto\ripple\logo_b64.txt', 'r') as f:
    logo_b64 = f.read().strip()

logo_img = f'<img src="data:image/gif;base64,{logo_b64}" alt="Ripple" class="logo-img">'
footer_img = f'<img src="data:image/gif;base64,{logo_b64}" alt="Ripple" class="footer-logo">'
hero_img = '<img src="hero.png" alt="5-star Google reviews" class="hero-photo">'

css = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ripple &mdash; 5-Star Google Reviews Made Easy.</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anybody:ital,wght@0,300;0,400;0,500;0,900;1,300;1,400;1,700;1,900&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --cream: #f2ede6;
  --cream-dark: #e8e1d8;
  --ink: #0d0d0d;
  --ink-mid: #3a3630;
  --ink-light: #7a736c;
  --rule: #d4cdc4;
  --orange: #e8a030;
  --orange-dark: #c8881a;
}
html { scroll-behavior: smooth; }
body { background: var(--cream); color: var(--ink); font-family: 'Anybody', sans-serif; font-weight: 300; line-height: 1.6; overflow-x: hidden; }
nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; padding: 1.25rem 3rem; background: var(--cream); border-bottom: 1px solid var(--rule); }
.nav-left { display: flex; align-items: center; }
.nav-center { display: flex; align-items: center; justify-content: center; }
.nav-right { display: flex; align-items: center; justify-content: flex-end; }
.logo-img { height: 38px; width: auto; mix-blend-mode: multiply; display: block; }
.nav-cta { background: var(--orange); color: var(--ink); padding: 0.55rem 1.5rem; border-radius: 100px; text-decoration: none; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.03em; transition: background 0.2s, transform 0.15s; }
.nav-cta:hover { background: var(--orange-dark); transform: translateY(-1px); }
.hero { min-height: 100vh; display: grid; grid-template-columns: 1fr 1fr; border-bottom: 1px solid var(--rule); padding-top: 72px; }
.hero-left { display: flex; flex-direction: column; justify-content: center; padding: 6rem 4rem 6rem 6rem; }
.hero-right { position: relative; overflow: hidden; }
.hero-photo { width: 100%; height: 100%; object-fit: cover; object-position: center; display: block; }
.hero-label { font-size: 0.7rem; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-light); margin-bottom: 2rem; }
h1 { font-family: 'Anybody', sans-serif; font-size: clamp(2.8rem, 5vw, 5.5rem); font-weight: 900; font-style: italic; line-height: 0.95; letter-spacing: -0.02em; margin-bottom: 2rem; }
.hero-sub { font-size: 1rem; color: var(--ink-light); max-width: 400px; line-height: 1.75; margin-bottom: 2.5rem; font-weight: 300; }
.btn-primary { background: var(--orange); color: var(--ink); padding: 1rem 2.5rem; border-radius: 100px; text-decoration: none; font-size: 0.9rem; font-weight: 700; letter-spacing: 0.03em; transition: all 0.2s; display: inline-block; }
.btn-primary:hover { background: var(--orange-dark); transform: translateY(-2px); }
.hero-stats { display: flex; gap: 2.5rem; margin-top: 4rem; padding-top: 2.5rem; border-top: 1px solid var(--rule); }
.stat { }
.stat-num { display: block; font-size: 2rem; font-weight: 900; font-style: italic; line-height: 1; margin-bottom: 0.25rem; }
.stat-label { font-size: 0.7rem; color: var(--ink-light); text-transform: uppercase; letter-spacing: 0.08em; font-weight: 400; line-height: 1.5; }
section { border-bottom: 1px solid var(--rule); }
.container { max-width: 1100px; margin: 0 auto; padding: 0 3rem; }
.section-inner { padding: 8rem 0; }
.eyebrow { font-size: 0.7rem; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; color: var(--ink-light); margin-bottom: 2rem; display: block; }
h2 { font-family: 'Anybody', sans-serif; font-size: clamp(2.5rem, 5vw, 5rem); font-weight: 900; font-style: italic; line-height: 0.95; letter-spacing: -0.02em; margin-bottom: 2rem; }
.pain-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--rule); border: 1px solid var(--rule); border-radius: 2px; overflow: hidden; margin-top: 5rem; }
.pain-card { background: var(--cream); padding: 3rem 2.5rem; }
.pain-num { font-size: 0.7rem; color: var(--ink-light); letter-spacing: 0.15em; font-weight: 400; margin-bottom: 2rem; display: block; }
.pain-card h3 { font-size: 1.3rem; font-weight: 700; font-style: italic; line-height: 1.2; margin-bottom: 1rem; }
.pain-card p { font-size: 0.9rem; color: var(--ink-light); line-height: 1.75; font-weight: 300; }
.how-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 8rem; align-items: center; margin-top: 5rem; }
.how-steps { display: flex; flex-direction: column; }
.how-step { padding: 2.5rem 0; border-top: 1px solid var(--rule); display: grid; grid-template-columns: 3rem 1fr; gap: 1.5rem; align-items: start; }
.how-step:last-child { border-bottom: 1px solid var(--rule); }
.step-n { font-size: 0.7rem; color: var(--ink-light); letter-spacing: 0.1em; padding-top: 0.2rem; font-weight: 400; }
.step-content h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }
.step-content p { font-size: 0.875rem; color: var(--ink-light); line-height: 1.75; font-weight: 300; }
.how-visual { background: var(--ink); border-radius: 4px; aspect-ratio: 3/4; display: flex; align-items: center; justify-content: center; }
.how-visual .placeholder-label { font-size: 0.7rem; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; text-transform: uppercase; }
.sms-section-inner { padding: 8rem 0; display: grid; grid-template-columns: 1fr 1fr; gap: 8rem; align-items: center; }
.phone { background: #1a1612; border-radius: 32px; padding: 2rem 1.5rem; max-width: 320px; border: 1px solid #2a2520; }
.phone-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.06); }
.phone-avatar { width: 38px; height: 38px; border-radius: 50%; background: #3a3530; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; color: rgba(255,255,255,0.6); flex-shrink: 0; }
.phone-name { font-size: 0.85rem; font-weight: 600; color: #f0ece6; }
.phone-time { font-size: 0.7rem; color: rgba(255,255,255,0.3); }
.bubble { background: #2a5fd6; border-radius: 18px 18px 4px 18px; padding: 1rem 1.1rem; font-size: 0.82rem; line-height: 1.65; color: #fff; margin-bottom: 0.4rem; }
.bubble-time { font-size: 0.65rem; color: rgba(255,255,255,0.25); text-align: right; }
.sms-text { max-width: 480px; }
.sms-text h2 { margin-bottom: 1.5rem; }
.sms-text p { font-size: 1rem; color: var(--ink-light); line-height: 1.8; margin-bottom: 2rem; font-weight: 300; }
.check-list { list-style: none; display: flex; flex-direction: column; gap: 1rem; }
.check-list li { font-size: 0.875rem; color: var(--ink-mid); display: flex; gap: 1rem; align-items: flex-start; line-height: 1.5; }
.check-list li::before { content: ""; width: 5px; height: 5px; border-radius: 50%; background: var(--ink); margin-top: 0.45rem; flex-shrink: 0; }
.for-section { background: var(--ink); color: var(--cream); border-bottom: none; }
.for-inner { padding: 10rem 0; text-align: center; }
.for-inner .eyebrow { color: rgba(242,237,230,0.35); }
.for-inner h2 { color: var(--cream); max-width: 900px; margin: 0 auto 2rem; }
.for-inner p { font-size: 1rem; color: rgba(242,237,230,0.5); max-width: 680px; margin: 0 auto 3rem; line-height: 1.8; font-weight: 300; }
.pricing-inner { padding: 8rem 0; max-width: 600px; margin: 0 auto; text-align: center; }
.pricing-inner h2 { margin-bottom: 1rem; }
.pricing-inner .sub { font-size: 1rem; color: var(--ink-light); margin-bottom: 4rem; font-weight: 300; }
.price-card { border: 1px solid var(--rule); border-radius: 4px; padding: 3.5rem; text-align: left; }
.price-badge { display: inline-block; font-size: 0.65rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; background: var(--ink); color: var(--cream); padding: 0.3rem 0.8rem; border-radius: 100px; margin-bottom: 2rem; }
.price-amount { font-size: 5rem; font-weight: 900; font-style: italic; line-height: 1; margin-bottom: 0.25rem; }
.price-amount sup { font-size: 2rem; vertical-align: top; margin-top: 1rem; }
.price-note { font-size: 0.8rem; color: var(--ink-light); margin-bottom: 2.5rem; }
.price-features { list-style: none; margin-bottom: 3rem; }
.price-features li { padding: 0.85rem 0; border-bottom: 1px solid var(--rule); font-size: 0.875rem; color: var(--ink-mid); display: flex; gap: 0.75rem; align-items: center; }
.price-features li::before { content: ""; width: 4px; height: 4px; border-radius: 50%; background: var(--ink); flex-shrink: 0; }
.price-cta { display: block; width: 100%; background: var(--orange); color: var(--ink); border: none; border-radius: 100px; padding: 1.1rem; font-family: 'Anybody', sans-serif; font-size: 0.9rem; font-weight: 700; letter-spacing: 0.03em; cursor: pointer; transition: all 0.2s; text-align: center; text-decoration: none; }
.price-cta:hover { background: var(--orange-dark); transform: translateY(-1px); }
.waitlist-inner { padding: 8rem 0; max-width: 560px; margin: 0 auto; text-align: center; }
.waitlist-inner h2 { margin-bottom: 1rem; }
.waitlist-inner .sub { font-size: 1rem; color: var(--ink-light); margin-bottom: 3rem; font-weight: 300; }
.form { display: flex; flex-direction: column; gap: 0.75rem; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; }
input, select { width: 100%; background: transparent; border: 1px solid var(--rule); border-radius: 4px; padding: 0.9rem 1.1rem; color: var(--ink); font-family: 'Anybody', sans-serif; font-size: 0.875rem; font-weight: 300; outline: none; transition: border-color 0.2s; -webkit-appearance: none; }
input::placeholder { color: var(--ink-light); }
input:focus, select:focus { border-color: var(--ink); }
select option { background: var(--cream); }
.submit-btn { background: var(--orange); color: var(--ink); border: none; border-radius: 4px; padding: 1rem; font-family: 'Anybody', sans-serif; font-size: 0.9rem; font-weight: 700; cursor: pointer; transition: all 0.2s; margin-top: 0.5rem; }
.submit-btn:hover { background: var(--orange-dark); transform: translateY(-1px); }
.form-note { font-size: 0.75rem; color: var(--ink-light); margin-top: 0.75rem; }
.success-msg { display: none; border: 1px solid var(--rule); border-radius: 4px; padding: 1.25rem; font-size: 0.875rem; color: var(--ink-mid); margin-top: 1rem; }
footer { padding: 3rem; display: flex; align-items: center; justify-content: space-between; font-size: 0.75rem; color: var(--ink-light); }
footer a { color: var(--ink-light); text-decoration: none; transition: color 0.2s; }
footer a:hover { color: var(--ink); }
.footer-logo { height: 22px; width: auto; mix-blend-mode: multiply; }
@media (max-width: 900px) {
  nav { padding: 1rem 1.5rem; }
  .hero { grid-template-columns: 1fr; }
  .hero-left { padding: 4rem 2rem; }
  .hero-right { height: 50vh; }
  .container { padding: 0 1.5rem; }
  .pain-grid { grid-template-columns: 1fr; }
  .how-layout { grid-template-columns: 1fr; gap: 3rem; }
  .how-visual { display: none; }
  .sms-section-inner { grid-template-columns: 1fr; gap: 3rem; }
  .form-row { grid-template-columns: 1fr; }
  footer { flex-direction: column; gap: 1rem; text-align: center; }
}
</style>
</head>
<body>'''

body = f'''
<nav>
  <div class="nav-left"></div>
  <div class="nav-center"><a href="#">{logo_img}</a></div>
  <div class="nav-right"><a href="#waitlist" class="nav-cta">Join waitlist</a></div>
</nav>

<section class="hero">
  <div class="hero-left">
    <span class="hero-label">Now accepting early access</span>
    <h1>5-Star Google Reviews Made Easy. Powered by AI.</h1>
    <p class="hero-sub">Ripple automatically sends a personalised review request the moment a job is done. No awkward asks. Just results.</p>
    <a href="#waitlist" class="btn-primary">Get early access &rarr;</a>
    <div class="hero-stats">
      <div class="stat"><span class="stat-num">73%</span><span class="stat-label">of customers review<br>when asked personally</span></div>
      <div class="stat"><span class="stat-num">4&times;</span><span class="stat-label">more reviews vs<br>asking in person</span></div>
      <div class="stat"><span class="stat-num">2 min</span><span class="stat-label">to set up.<br>Then automatic.</span></div>
    </div>
  </div>
  <div class="hero-right">{hero_img}</div>
</section>

<section>
  <div class="container"><div class="section-inner">
    <span class="eyebrow">The problem</span>
    <h2>Sound familiar?</h2>
    <div class="pain-grid">
      <div class="pain-card"><span class="pain-num">01</span><h3>It feels awkward to ask</h3><p>You just finished a great job. The last thing you want to do is stand there and ask for a favour. So you don&rsquo;t. And the moment passes.</p></div>
      <div class="pain-card"><span class="pain-num">02</span><h3>It always slips through</h3><p>You mean to follow up. But there&rsquo;s another job, another invoice, another problem. Following up on reviews never makes the list.</p></div>
      <div class="pain-card"><span class="pain-num">03</span><h3>Your competitors pull ahead</h3><p>Customers Google before they call. More reviews means higher rankings, more trust, more calls. Every missed review is a customer lost.</p></div>
    </div>
  </div></div>
</section>

<section id="how">
  <div class="container"><div class="section-inner">
    <span class="eyebrow">How it works</span>
    <h2>Set it up once.<br>Let it run.</h2>
    <div class="how-layout">
      <div class="how-steps">
        <div class="how-step"><span class="step-n">01</span><div class="step-content"><h3>Connect your tools</h3><p>Link your invoicing or booking software &mdash; Xero, Square, ServiceM8, Mindbody, and more. Takes two minutes.</p></div></div>
        <div class="how-step"><span class="step-n">02</span><div class="step-content"><h3>Job marked complete</h3><p>When a job is done or an invoice paid, Ripple picks it up automatically. No manual input from your team.</p></div></div>
        <div class="how-step"><span class="step-n">03</span><div class="step-content"><h3>Review request sent</h3><p>A personalised SMS arrives at the perfect moment. The customer taps, leaves a review, your rating grows.</p></div></div>
      </div>
      <div class="how-visual"><span class="placeholder-label">Photo</span></div>
    </div>
  </div></div>
</section>

<section>
  <div class="container">
    <div class="sms-section-inner">
      <div class="phone">
        <div class="phone-header"><div class="phone-avatar">ME</div><div><div class="phone-name">Mick&rsquo;s Electrical</div><div class="phone-time">Today, 3:42 PM</div></div></div>
        <div class="bubble">Hi Sarah! Thanks for having us out today to sort your switchboard. If you have a moment, we&rsquo;d really appreciate a quick Google review &mdash; it helps more than you know.<br><br>g.page/r/mickselectrical &mdash; Mick</div>
        <div class="bubble-time">Delivered &check;</div>
      </div>
      <div class="sms-text">
        <span class="eyebrow">The message</span>
        <h2>Human.<br>Personal.<br>Not a template.</h2>
        <p>Every review request is written by AI, tailored to the specific job. It reads like a message from the business owner &mdash; because it should.</p>
        <ul class="check-list">
          <li>Mentions the actual job completed</li>
          <li>Uses the customer&rsquo;s name</li>
          <li>Direct link to your Google Review page</li>
          <li>Sent at exactly the right moment</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="for-section">
  <div class="container"><div class="for-inner">
    <span class="eyebrow">Who it&rsquo;s for</span>
    <h2>Any business that earns<br>Google Reviews.</h2>
    <p>Tradies, restaurants, salons, dentists, gyms, vets, hotels, auto businesses, retail, studios, real estate agents, pharmacies, cafes, physios, florists, photographers &mdash; if your customers can leave a Google Review, Ripple works for you.</p>
    <a href="#waitlist" class="btn-primary">Get early access &rarr;</a>
  </div></div>
</section>

<section id="pricing">
  <div class="container"><div class="pricing-inner">
    <span class="eyebrow">Pricing</span>
    <h2>Simple<br>and fair.</h2>
    <p class="sub">Free during beta. No credit card required.</p>
    <div class="price-card">
      <span class="price-badge">Early access &mdash; Beta</span>
      <div class="price-amount"><sup>$</sup>0</div>
      <div class="price-note">Free during beta &middot; <strong>$49/month</strong> at launch</div>
      <ul class="price-features">
        <li>Unlimited review requests</li>
        <li>AI-personalised messages</li>
        <li>Connect any invoicing tool</li>
        <li>Google Review direct links</li>
        <li>SMS delivery</li>
        <li>Dashboard to track results</li>
      </ul>
      <a href="#waitlist" class="price-cta">Claim your free spot &rarr;</a>
    </div>
  </div></div>
</section>

<section id="waitlist">
  <div class="container"><div class="waitlist-inner">
    <span class="eyebrow">Early access</span>
    <h2>Be first<br>in the water.</h2>
    <p class="sub">Join the waitlist and get free access during beta. We&rsquo;re onboarding businesses one by one.</p>
    <form class="form" id="waitlist-form">
      <div class="form-row">
        <input type="text" placeholder="Your name" required>
        <input type="text" placeholder="Business name" required>
      </div>
      <input type="email" placeholder="Email address" required>
      <select required>
        <option value="" disabled selected>What type of business?</option>
        <option>Tradie / Trade services</option>
        <option>Restaurant / Cafe</option>
        <option>Hair / Beauty salon</option>
        <option>Dental / Medical</option>
        <option>Gym / Fitness studio</option>
        <option>Vet / Pet care</option>
        <option>Hotel / Accommodation</option>
        <option>Auto services</option>
        <option>Retail / Boutique</option>
        <option>Real estate</option>
        <option>Other</option>
      </select>
      <input type="text" placeholder="Google Review page URL (optional)">
      <button type="submit" class="submit-btn">Join the waitlist &rarr;</button>
      <p class="form-note">No spam. No credit card. Just early access.</p>
    </form>
    <div class="success-msg" id="success-msg">You&rsquo;re on the list! We&rsquo;ll be in touch soon.</div>
  </div></div>
</section>

<footer>
  {footer_img}
  <span>&copy; 2026 Ripple. All rights reserved.</span>
  <div style="display:flex;gap:1.5rem;"><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Contact</a></div>
</footer>

<script>
document.getElementById('waitlist-form').addEventListener('submit', function(e) {{
  e.preventDefault();
  this.style.display = 'none';
  document.getElementById('success-msg').style.display = 'block';
}});
</script>
</body>
</html>'''

full = css + body
with open(r'C:\Users\butto\ripple\index.html', 'w', encoding='utf-8') as f:
    f.write(full)
print('Done. Lines:', full.count('\n'))
