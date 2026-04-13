import React from 'react';
import maheshLogo from '../maheshLogo.svg';
import heroPortrait from '../maheshBgRemoved02.png';
import nessLogo from '../ness.png';
import moonraftLogo from '../moonraft.png';
import ustLogo from '../UST.png';
import ciscoLogo from '../cisco.png';
import thoughtfocusLogo from '../thoughtfocusbig.png';
import caeLogo from '../cae.png';
import linkedinLogo from '../logo-linkedin.svg';
import facebookLogo from '../logo-facebook.svg';

const portfolioThemes = [
  {
    title: 'Prototype to Product',
    summary:
      'Early-stage product shaping, interaction design, and frontends that help teams validate ideas before overinvesting in process.',
    bullets: ['UI direction', 'working prototypes', 'MVP delivery'],
  },
  {
    title: 'Frontend Architecture',
    summary:
      'React and component-driven application foundations that support scale, maintainability, and faster team execution.',
    bullets: ['design systems', 'component patterns', 'delivery flow'],
  },
  {
    title: 'Modernization Work',
    summary:
      'Refreshing legacy product experiences with clearer UX, cleaner structure, and practical implementation decisions.',
    bullets: ['UX cleanup', 'refactoring strategy', 'release readiness'],
  },
];

const services = [
  {
    title: 'UI/UX Consulting',
    text: 'Product structure, interaction design, and clearer decision-making during fast-moving delivery cycles.',
  },
  {
    title: 'Rapid Prototyping',
    text: 'Clickable interfaces and working app layers that align teams earlier and reduce rework later.',
  },
  {
    title: 'Frontend Leadership',
    text: 'Architecture, implementation guidance, and hands-on execution across modern JavaScript frameworks.',
  },
  {
    title: 'Design-to-Code Systems',
    text: 'Reusable UI building blocks that keep product quality high without slowing teams down.',
  },
];

const skillGroups = [
  {
    title: 'Product and UX craft',
    text:
      'UI/UX consulting, interaction design, human interface thinking, rapid prototyping, and design systems shaped for real delivery teams.',
    items: ['UI/UX consulting', 'interaction design', 'rapid prototyping', 'design systems'],
  },
  {
    title: 'Frontend delivery stack',
    text:
      'Hands-on execution across modern JavaScript application work, from component architecture to production-ready interface builds.',
    items: ['React', 'Next.js', 'Redux', 'Angular', 'Ionic', 'Tailwind CSS', 'Node.js'],
  },
  {
    title: 'Visual and interface tooling',
    text:
      'Interface exploration and production support using established design and visualization tools from earlier product and consulting work.',
    items: ['Adobe Photoshop', 'Illustrator', 'Adobe XD', '3DS Max'],
  },
  {
    title: 'Leadership and architecture',
    text:
      'The resume thread is consistent: Technology Consultant, Tech Lead, and Software Architect roles focused on making product quality and engineering practicality work together.',
    items: ['frontend architecture', 'technical leadership', 'software architecture', 'product delivery'],
  },
];

const skillSignals = [
  '14+ years across IT, UX, and frontend product delivery',
  'Postgraduate specialization in Human Interface Design and Development',
  'Bridges consulting, design thinking, and hands-on implementation',
];

const companies = [
  ['Ness', nessLogo],
  ['Moonraft', moonraftLogo],
  ['UST', ustLogo],
  ['Cisco', ciscoLogo],
  ['ThoughtFocus', thoughtfocusLogo],
  ['CAE', caeLogo],
];

const highlights = [
  'UI/UX consulting grounded in delivery realities',
  'Rapid prototyping that helps teams move with confidence',
  'Frontend architecture for production-ready product experiences',
];

const process = [
  {
    step: '01',
    title: 'Clarify the product direction',
    text: 'Reduce ambiguity around flows, priorities, and user journeys before engineering effort spreads too thin.',
  },
  {
    step: '02',
    title: 'Turn intent into working interfaces',
    text: 'Move quickly from concept to interface prototypes and implementation-ready frontend structure.',
  },
  {
    step: '03',
    title: 'Ship with a stronger foundation',
    text: 'Keep quality, maintainability, and team velocity aligned instead of treating them as tradeoffs.',
  },
];

const experienceSignals = [
  '14+ years in IT, product delivery, and software architecture',
  'Roles spanning Technology Consultant, Tech Lead, and Software Architect',
  'Experience working with enterprise and product-focused teams across multiple industries',
];

export default function App() {
  return (
    <div className="page-shell">
      <div className="background-orb background-orb-left" />
      <div className="background-orb background-orb-right" />

      <header className="topbar">
        <a className="brand" href="#home" aria-label="Maheshchandra Hegde home">
          <img src={maheshLogo} alt="Maheshchandra Hegde logo" />
          <div>
            <strong>Maheshchandra Hegde</strong>
            <span>UI/UX Consultant</span>
          </div>
        </a>

        <nav className="nav-links" aria-label="Primary">
          <a href="#work">Work</a>
          <a href="#services">Services</a>
          <a href="#stack">Stack</a>
          <a href="#experience">Experience</a>
          <a href="#contact">Contact</a>
        </nav>
      </header>

      <main>
        <section className="hero" id="home">
          <div className="hero-copy">
            <p className="eyebrow">Portfolio</p>
            <h1>I help teams ship better product experiences, faster.</h1>
            <p className="hero-text">
              Maheshchandra Hegde is a UI/UX consultant and frontend leader focused on turning
              product ideas into usable, production-ready interfaces. The work sits at the
              intersection of design thinking, rapid prototyping, and modern frontend execution.
            </p>

            <div className="hero-actions">
              <a className="button button-primary" href="#work">
                View Portfolio Focus
              </a>
              <a className="button button-secondary" href="#contact">
                Discuss a Project
              </a>
            </div>

            <ul className="highlight-list" aria-label="Key strengths">
              {highlights.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>

          <div className="hero-visual">
            <div className="portrait-card">
              <img src={heroPortrait} alt="Maheshchandra Hegde portrait" />
            </div>
            <div className="stat-card stat-card-top">
              <span>14+ years</span>
              <p>across consulting, UI delivery, frontend architecture, and product execution</p>
            </div>
            <div className="stat-card stat-card-bottom">
              <span>Core value</span>
              <p>move from concept to working product without losing design quality</p>
            </div>
          </div>
        </section>

        <section className="portfolio-section" id="work">
          <div className="section-heading">
            <p className="eyebrow">Selected Focus</p>
            <h2>A stronger portfolio starts by showing the kind of work I help teams ship.</h2>
          </div>

          <div className="portfolio-grid">
            {portfolioThemes.map((theme) => (
              <article key={theme.title} className="portfolio-card">
                <p className="card-kicker">Portfolio theme</p>
                <h3>{theme.title}</h3>
                <p>{theme.summary}</p>
                <ul className="tag-list" aria-label={`${theme.title} topics`}>
                  {theme.bullets.map((bullet) => (
                    <li key={bullet}>{bullet}</li>
                  ))}
                </ul>
              </article>
            ))}
          </div>
        </section>

        <section className="services-section" id="services">
          <div className="section-heading section-heading-wide">
            <p className="eyebrow">Services</p>
            <h2>What teams typically bring me in for.</h2>
            <p className="section-intro">
              The value is not only visual design or code delivery in isolation. It is the ability
              to connect product thinking, interface quality, and implementation speed in one flow.
            </p>
          </div>

          <div className="service-grid">
            {services.map((service) => (
              <article key={service.title} className="service-card">
                <h3>{service.title}</h3>
                <p>{service.text}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="process-section" id="process">
          <div className="section-heading section-heading-wide">
            <p className="eyebrow">Process</p>
            <h2>Fast delivery works best when the process stays focused.</h2>
          </div>

          <div className="process-grid">
            {process.map((item) => (
              <article key={item.step} className="process-card">
                <span>{item.step}</span>
                <h3>{item.title}</h3>
                <p>{item.text}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="stack-section" id="stack">
          <div className="section-heading section-heading-wide">
            <p className="eyebrow">Skillset</p>
            <h2>Less logo wallpaper, more proof of what I can bring into the room.</h2>
            <p className="section-intro">
              My recent skillset combines product design thinking, modern frontend execution, and
              the consulting depth reflected throughout my resume and delivery experience.
            </p>
          </div>

          <div className="skillset-panel">
            <div className="skillset-intro-card">
              <p className="card-kicker">Current focus</p>
              <h3>Designing useful products and building the interfaces that make them real.</h3>
              <p>
                The strongest value sits in the overlap: UI/UX consulting, frontend architecture,
                rapid prototyping, and implementation leadership that keeps teams moving from idea
                to shipped experience.
              </p>

              <ul className="signal-list" aria-label="Skillset highlights">
                {skillSignals.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>

            <div className="skillset-grid">
              {skillGroups.map((group) => (
                <article key={group.title} className="skill-card">
                  <p className="card-kicker">Skill area</p>
                  <h3>{group.title}</h3>
                  <p>{group.text}</p>
                  <ul className="tag-list" aria-label={`${group.title} skills`}>
                    {group.items.map((item) => (
                      <li key={item}>{item}</li>
                    ))}
                  </ul>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="experience-section" id="experience">
          <div className="section-heading section-heading-wide">
            <p className="eyebrow">Experience</p>
            <h2>Built across consulting, team leadership, and hands-on product execution.</h2>
            <p className="section-intro">
              Experience spans enterprise environments, fast-moving delivery teams, and product
              roles where design quality and engineering practicality had to work together.
            </p>
          </div>

          <div className="logo-grid company-grid">
            {companies.map(([name, src]) => (
              <figure key={name} className="logo-tile company-tile">
                <img src={src} alt={name} />
                <figcaption>{name}</figcaption>
              </figure>
            ))}
          </div>

          <div className="experience-grid">
            <div className="about-card">
              <p className="eyebrow">About Mahesh</p>
              <p>
                Maheshchandra Hegde is a postgraduate from RGU, Scotland, specializing in Human
                Interface Design and Development. He has spent more than 14 years delivering work
                across consulting, technical leadership, and software architecture, with a clear
                emphasis on usable product experiences.
              </p>
            </div>

            <div className="signal-card">
              <p className="eyebrow">Experience Signals</p>
              <ul className="signal-list">
                {experienceSignals.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
          </div>
        </section>

        <section className="contact-section" id="contact">
          <div className="contact-panel">
            <div>
              <p className="eyebrow">Contact</p>
              <h2>Looking for someone who can bridge product thinking and frontend execution?</h2>
              <p>
                This redesigned home page is the first stronger portfolio pass. The next evolution
                can add detailed case studies, project stories, testimonials, and a sharper
                services page if needed.
              </p>
            </div>

            <div className="contact-details">
              <a href="mailto:hid.mahesh@gmail.com">hid.mahesh@gmail.com</a>
              <a href="tel:+919535253329">+91 9535253329</a>
              <div className="social-links">
                <a href="https://www.linkedin.com/in/maheshchandrahegde/" target="_blank" rel="noreferrer">
                  <img src={linkedinLogo} alt="LinkedIn" />{' '}
                  LinkedIn
                </a>
                <a href="https://www.facebook.com/maheshchandra.hegde" target="_blank" rel="noreferrer">
                  <img src={facebookLogo} alt="Facebook" />{' '}
                  Facebook
                </a>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <span>© 2026 Maheshchandra Hegde</span>
        <span>React rebuild foundation deployed on Firebase Hosting</span>
      </footer>
    </div>
  );
}