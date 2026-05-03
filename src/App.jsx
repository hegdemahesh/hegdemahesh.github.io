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

const latestVentures = [
  {
    title: 'Founder & Creative Technologist',
    company: 'Srushtilabs.com',
    period: 'Jan 2026 - Present',
    duration: '5 mos',
    location: 'Bengaluru, Karnataka, India',
    mode: 'Hybrid',
    summary:
      'Building an AI-assisted modular 3D asset platform focused on game-ready, low-poly collections for Unreal Engine, Unity, and visualization workflows.',
    details: [
      'Generative AI, retopology, and PBR texturing pipelines for production-ready modular asset bundles.',
      'Cultural-heritage and modern-design libraries, including South Indian temple ruins collections and reusable environment kits.',
    ],
  },
  {
    title: 'Founder & Product Design Lead',
    company: 'Twitan.com',
    period: 'Nov 2025 - Present',
    duration: '7 mos',
    location: 'Bengaluru, Karnataka, India',
    mode: 'Hybrid',
    summary:
      'Leading an AI-driven sports product studio creating scoring, event-management, and player-tracking platforms with clear UX and modular product foundations.',
    details: [
      'Flagship products include Shutlify for badminton and Twicket for cricket, focused on match operations and performance tracking.',
      'Combines product design, software engineering, and automation to support academies, coaches, players, and audience engagement.',
    ],
  },
];

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

const resumeHighlights = [
  'Senior Technical Lead for React/Node.js healthcare UI at Cyient Limited',
  'Co-Founder and Director at Technoyana Digital Transformation Services',
  'UI Architect and frontend leader for enterprise clients including Cisco, UST Global, and Moonraft',
  '16+ years of delivery experience spanning consulting, product delivery, and interactive technology',
];

const awards = [
  'Certificate of Appreciation for Contribution towards “Inspiring People”, UST Global 2018',
  'Certificate of Appreciation for Contribution to “Putting Client First”, UST Global 2016',
  'Certificate of Appreciation for “Living the Values”, UST Global 2015',
  'Appreciation from Cisco for the facility dashboard project, 2010',
];

const education = [
  'MS in Computing, Robert Gordon University, Scotland',
  'BE in Electronics and Communication, Bapuji Institute of Engineering & Technology',
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
  '16+ years in IT, product delivery, and software architecture',
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
                Explore My Work
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
              <span>16+ years</span>
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

        <section className="resume-section" id="resume">
          <div className="section-heading section-heading-wide">
            <p className="eyebrow">Resume & awards</p>
            <h2>Career highlights, recognitions, and education captured in one place.</h2>
          </div>

          <div className="resume-grid">
            <article className="resume-card">
              <p className="card-kicker">Career snapshot</p>
              <h3>Hands-on leadership across product design, frontend architecture, and creative delivery.</h3>
              <ul className="resume-list">
                {resumeHighlights.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </article>

            <div className="resume-panel">
              <article className="award-card">
                <p className="card-kicker">Awards</p>
                <ul className="award-list">
                  {awards.map((award) => (
                    <li key={award}>{award}</li>
                  ))}
                </ul>
              </article>

              <article className="education-card">
                <p className="card-kicker">Education</p>
                <ul className="education-list">
                  {education.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
              </article>

              <a className="button button-primary resume-button" href="/RESUME.md" target="_blank" rel="noreferrer">
                View full resume
              </a>
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

          <div className="venture-grid">
            {latestVentures.map((venture) => (
              <article key={venture.company} className="venture-card">
                <div className="venture-header">
                  <div>
                    <p className="card-kicker">Latest venture</p>
                    <h3>{venture.title}</h3>
                    <p className="venture-company">{venture.company}</p>
                  </div>
                  <div className="venture-meta">
                    <span>{venture.period}</span>
                    <span>{venture.duration}</span>
                  </div>
                </div>
                <p className="venture-location">
                  {venture.location} · {venture.mode}
                </p>
                <p>{venture.summary}</p>
                <ul className="venture-list">
                  {venture.details.map((detail) => (
                    <li key={detail}>{detail}</li>
                  ))}
                </ul>
              </article>
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