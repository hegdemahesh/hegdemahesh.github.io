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
    title: 'VoxelForge AI - modular 3D asset pipeline consulting',
    company: 'Srushtilabs',
    period: 'Jan 2026 - Present',
    duration: '5 mos',
    location: 'Bengaluru, Karnataka, India',
    mode: 'Hybrid',
    summary:
      'Built modular 3D asset workflows for game and visualization teams to move from concept to production-ready output faster.',
    details: [
      'Integrated generative AI, retopology, and PBR texturing into repeatable production pipelines.',
      'Enabled reusable environment kits with clean LOD-ready exports for Unreal Engine and Unity teams.',
    ],
  },
  {
    title: 'Twitan.com - AI-driven sports product UX consulting',
    company: 'Twitan',
    period: 'Nov 2025 - Present',
    duration: '7 mos',
    location: 'Bengaluru, Karnataka, India',
    mode: 'Hybrid',
    summary:
      'Designed and shipped product UX for AI-assisted sports management workflows used by academies, coaches, and operations teams.',
    details: [
      'Shaped product direction for Shutlify and Twicket to streamline match operations and player performance tracking.',
      'Aligned product design, engineering execution, and automation to reduce delivery friction across releases.',
    ],
  },
];

const portfolioThemes = [
  {
    title: 'Prototype to Product',
    summary:
      'Early-stage product shaping, interaction design, and frontend execution that helps teams validate ideas before overinvesting.',
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
    text: 'Clarify product direction, reduce ambiguity, and guide teams through fast-moving delivery cycles with user-centric design decisions.',
  },
  {
    title: 'Rapid Prototyping',
    text: 'Create clickable prototypes and working app layers that align stakeholders early, cut rework costs, and validate ideas before scaling.',
  },
  {
    title: 'Frontend Architecture & Leadership',
    text: 'Provide architecture guidance and hands-on execution across React, Angular, and modern JavaScript frameworks to ensure maintainability and speed.',
  },
  {
    title: 'Design-to-Code Systems',
    text: 'Build reusable UI components and design systems that keep product quality high while enabling faster team execution.',
  },
  {
    title: 'AI-Assisted Product Development',
    text: 'Integrate generative AI workflows for 3D assets, automation, and prototyping to help teams innovate without slowing delivery.',
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
  'Scalable UI/UX systems designed for speed and clarity',
  'Rapid prototypes that align stakeholders and reduce rework',
  'Frontend leadership that connects architecture and execution',
];

const impactSignals = [
  'Earlier stakeholder alignment through prototype-first product validation',
  'Reduced rework by translating product ambiguity into clear UX and engineering decisions',
  'Reusable frontend systems that improve quality while preserving delivery velocity',
];

const consultingPackages = [
  {
    title: 'UX Audit Sprint',
    text: 'A focused short engagement to identify UX friction, clarify product priorities, and define actionable improvements.',
  },
  {
    title: 'Prototype-to-Delivery Track',
    text: 'From concept framing to interactive prototypes and implementation-ready frontend structure for faster release confidence.',
  },
  {
    title: 'Fractional Frontend Leadership',
    text: 'Ongoing architecture and execution guidance for teams scaling React and Angular products without sacrificing UX quality.',
  },
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
  '18+ years in IT, product delivery, and software architecture',
  'Roles spanning Technology Consultant, Tech Lead, and Software Architect',
  'Experience working with enterprise and product-focused teams across multiple industries',
];

const voxelForgeHighlights = [
  'Visualize 3D environments before generation.',
  'Modify, refine, or delete assets seamlessly.',
  'Download complete packages with multiple LODs, ready for integration.',
];

const personalBlend = [
  'Design, machinery, visualization, and CAD',
  'Software engineering and application development',
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
          <a href="#workproof">Work</a>
          <a href="#services">Services</a>
          <a href="#experience">Experience</a>
          <a href="#contact">Contact</a>
          <a href="#portfolio">Portfolio</a>
          <a href="#engage">Engage Me</a>
        </nav>
      </header>

      <main>
        <section className="hero" id="home">
          <div className="hero-copy">
            <p className="eyebrow">Consulting Practice</p>
            <h1>
              Helping teams accelerate product delivery with clear UX, scalable frontend systems,
              and AI-driven innovation.
            </h1>
            <p className="hero-text">
              I consult with startups and enterprises to bridge product thinking and engineering
              execution, moving from concept to production without losing design quality.
            </p>

            <div className="hero-actions">
              <a className="button button-primary" href="#portfolio">
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
              <span>18+ years</span>
              <p>across consulting, UX strategy, frontend architecture, and product execution</p>
            </div>
            <div className="stat-card stat-card-bottom">
              <span>Engagement focus</span>
              <p>short UX audits, rapid prototypes, and frontend leadership for delivery teams</p>
            </div>
          </div>
        </section>

        <section className="announcement-section" id="workproof">
          <article className="announcement-card">
            <p className="eyebrow">Consulting Proof Point</p>
            <h2>VoxelForge AI turned concept sketches into production-ready 3D systems.</h2>
            <p>
              VoxelForge AI demonstrates how AI-assisted product development can move quickly from
              idea to operational capability. The platform was shaped to help studios produce
              modular, game-ready assets with repeatable quality.
            </p>
            <ul className="announcement-list" aria-label="VoxelForge AI capabilities">
              {voxelForgeHighlights.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </article>
        </section>

        <section className="bio-section" id="about-me">
          <div className="section-heading section-heading-wide">
            <p className="eyebrow">Why teams hire me</p>
            <h2>Consulting support for teams that need speed without compromising product quality.</h2>
          </div>

          <div className="bio-grid">
            <article className="bio-card">
              <p>
                Organizations bring me in when they need to move from concept to production
                without losing design quality. I combine 18+ years of frontend architecture and
                UX consulting with hands-on product execution.
              </p>
              <p>
                The focus is practical delivery: clear product direction, implementation-ready UI
                strategy, and architecture guidance that helps teams accelerate releases while
                keeping user experience sharp.
              </p>
            </article>

            <article className="bio-card">
              <p>
                Teams value a rare cross-functional blend that connects product design, frontend
                engineering, and AI-enabled workflows into one execution path.
              </p>
              <p>
                This blend combines deep expertise across two connected domains:
              </p>
              <ul className="announcement-list" aria-label="Expertise domains">
                {personalBlend.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
              <p>
                Together, these capabilities reduce handoff friction and improve outcomes for
                product, design, and engineering teams.
              </p>
            </article>
          </div>
        </section>

        <section className="portfolio-section" id="portfolio">
          <div className="section-heading">
            <p className="eyebrow">Portfolio</p>
            <h2>Consulting-led work that translates product intent into scalable delivery.</h2>
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

          <article className="about-card impact-card">
            <p className="eyebrow">Client Impact</p>
            <ul className="announcement-list">
              {impactSignals.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </article>
        </section>

        <section className="services-section" id="services">
          <div className="section-heading section-heading-wide">
            <p className="eyebrow">Services</p>
            <h2>Consulting services designed to improve speed, quality, and delivery confidence.</h2>
            <p className="section-intro">
              Engagements are structured to help teams make better product decisions earlier,
              deliver confidently, and scale frontend quality across releases.
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

        <section className="services-section" id="engage">
          <div className="section-heading section-heading-wide">
            <p className="eyebrow">Consulting Packages</p>
            <h2>Engagement options based on scope, speed, and team needs.</h2>
          </div>

          <div className="service-grid">
            {consultingPackages.map((pkg) => (
              <article key={pkg.title} className="service-card">
                <h3>{pkg.title}</h3>
                <p>{pkg.text}</p>
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
                    <p className="card-kicker">Consulting case</p>
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
                Interface Design and Development. He has spent more than 18 years delivering work
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
              <h2>Let us discuss your project and define the right consulting engagement.</h2>
              <p>
                I offer consulting engagements ranging from short UX audits to full frontend
                architecture leadership for product teams that need speed, clarity, and execution.
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