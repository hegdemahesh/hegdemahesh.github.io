import React from 'react';
import maheshLogo from '../maheshLogo.svg';
import nessLogo from '../ness.png';
import moonraftLogo from '../moonraft.png';
import ustLogo from '../UST.png';
import ciscoLogo from '../cisco.png';
import thoughtfocusLogo from '../thoughtfocusbig.png';
import caeLogo from '../cae.png';
import linkedinLogo from '../logo-linkedin.svg';
import TechnoyanaLogo from './TechnoyanaLogo';

const clientLogos = [
  ['Cisco', ciscoLogo],
  ['UST Global', ustLogo],
  ['Ness Digital Engineering', nessLogo],
  ['Moonraft Innovation Labs', moonraftLogo],
  ['ThoughtFocus', thoughtfocusLogo],
  ['CAE Simulators', caeLogo],
];

const flagshipDivisions = [
  {
    name: 'Technoyana Digital Transformation Services',
    subtitle: 'Private Limited (Est. 2021) · Co-Founder & Technology Leader',
    badge: 'Core Powerhouse & Incubator',
    description:
      'Directing product architecture, AI-assisted engineering, and creative technology vision. Leading distributed development of industrial software, CNC machine interfaces, microfinance platforms, and 3D architectural applications.',
    pillars: ['Scalable Cloud Architecture', 'Firebase, Node.js & React', 'Distributed Engineering Models', 'HCI Design Systems'],
    website: 'https://technoyana.in/',
    websiteLabel: 'technoyana.in',
  },
  {
    name: 'Srushtilabs',
    subtitle: 'A Technoyana Division · Founder & Creative Technologist',
    badge: 'Spatial AI & 3D Tech',
    description:
      'Pioneering AI-assisted modular 3D asset generation and spatial computing workflows. Architecting game-ready, low-poly pipelines optimized for WebGL, Unreal Engine, and Unity with automated retopology and PBR textures.',
    pillars: ['Voxelforge AI (Modular 3D Assets)', 'Generative AI Pipelines', 'Unreal Engine & Unity Optimization', 'ayam3d Exploratory R&D'],
    website: 'https://srushtilabs.com',
    websiteLabel: 'srushtilabs.com',
  },
  {
    name: 'Twitan',
    subtitle: 'A Technoyana Division · Founder & Product Design Lead',
    badge: 'Sports SaaS Studio',
    description:
      'High-reliability operational SaaS studio for tournament directors, academies, and live match scoring. Engineered Shutlify (Badminton OS) and Twicket (Cricket Engine) with multi-role permissions and offline-capable PWAs.',
    pillars: ['Shutlify (Badminton OS)', 'Twicket (Cricket Scoring)', 'Automated Bracket Generators', 'Venue-Ready Offline PWAs'],
    website: 'https://twitan.com',
    websiteLabel: 'twitan.com',
  },
];

const technoyanaPosts = [
  {
    id: 'news-1',
    date: 'August 1, 2026',
    dateTime: '2026-08-01',
    category: 'Product & R&D Update',
    author: 'SrushtiLabs Team',
    title: 'SrushtiLabs Showcases Voxelforge AI for Game-Ready 3D Asset Bundles',
    summary:
      'Technoyana Private Limited powers Voxelforge AI under SrushtiLabs, delivering low-poly modular 3D assets for Unreal Engine & Unity. Game developers and 3D artists can generate, retopologize, and export optimized assets within minutes.',
    tag: 'Voxelforge AI · ayam3d R&D',
    link: 'https://srushtilabs.com/voxelforge/',
    linkLabel: 'Explore Voxelforge AI',
  },
  {
    id: 'news-2',
    date: 'July 15, 2026',
    dateTime: '2026-07-15',
    category: 'Corporate News',
    author: 'Leadership Team',
    title: 'Technoyana Engineering Updates & Product Roadmap',
    summary:
      'Overview of recent achievements in custom product engineering, cloud infrastructure, and enterprise SaaS solutions. Expanding development and scaling core architectures across Twitan and SrushtiLabs suites.',
    tag: 'Cloud & Enterprise SaaS',
    link: 'https://technoyana.in/',
    linkLabel: 'Read on Technoyana.in',
  },
  {
    id: 'news-3',
    date: 'June 20, 2026',
    dateTime: '2026-06-20',
    category: 'Product Update',
    author: 'Sports Tech Team',
    title: 'Twitan Sports Suite Introduces Shutlify & Twicket Platforms',
    summary:
      'Engineered by Technoyana, Twitan provides operational software including Shutlify for badminton tournament management and Twicket for cricket match scoring, engineered with offline PWA reliability for low-connectivity venues.',
    tag: 'Shutlify · Twicket OS',
    link: 'https://twitan.com',
    linkLabel: 'Visit Twitan.com',
  },
];

const careerRoles = [
  {
    role: 'Senior Technology Lead',
    company: 'Cyient',
    period: 'Nov 2023 - Mar 2025 · 1 yr 5 mos',
    location: 'Bangalore Urban (Hybrid)',
    description:
      'Spearheaded the design and development of a web-based patient monitoring platform for Philips, optimized for intensive care (ICU) and critical care units (CCU), enabling real-time clinical decision support and hospital infrastructure integration.',
  },
  {
    role: 'Lead - Development',
    company: 'Ness Digital Engineering',
    period: 'Oct 2019 - Apr 2020 · 7 mos',
    location: 'Bengaluru Area',
    description:
      'Architected frontend infrastructure and led Angular enterprise applications development adhering to stringent accessibility and security standards while guiding UI engineering best practices.',
  },
  {
    role: 'User Interface Architect',
    company: 'Moonraft Innovation Labs',
    period: 'May 2019 - Jul 2019 · 3 mos',
    location: 'Bengaluru Area',
    description:
      'Led development of mobile and web applications for premier hospitality clients and engineered a cross-platform UI design system using web components (LitElement).',
  },
  {
    role: 'Associate Project Manager & Senior Systems Analyst',
    company: 'UST Global / CISCO',
    period: 'Feb 2015 - Feb 2019 · 4 yrs 1 mo',
    location: 'Bangalore & Cisco Campus',
    description:
      'Consultant at Cisco Systems designing intelligent facility dashboards, rich data visualizations, and enterprise management interfaces with high-performance real-time telemetry.',
  },
  {
    role: 'Co-Founder & Technology Leader',
    company: 'InnoBrik Software Technologies',
    period: 'Feb 2011 - Oct 2014 · 3 yrs 9 mos',
    location: 'Bangalore',
    description:
      'Co-founded and scaled startup engineering teams, architecting custom web and mobile products from initial concept to commercial launch.',
  },
  {
    role: 'Consultant : UX/UI Tech Lead & Independent Consultant',
    company: 'ThoughtFocus & Consulting Practice',
    period: 'Apr 2008 - Mar 2014',
    location: 'Bangalore',
    description:
      'Delivered creative data visualizations, rich internet applications, and dashboards for clients including Vodafone, Cisco, and DGLogik.',
  },
  {
    role: 'Visual Database Developer',
    company: 'CAE',
    period: 'Sep 2007 - Apr 2008 · 8 mos',
    location: 'Bangalore',
    description:
      'Engineered high-fidelity 3D terrain and visual databases for civil and military flight simulators.',
  },
];

const expertisePillars = [
  {
    title: 'Spatial Computing & 3D',
    skills: 'WebGL, WebGPU, Unreal Engine, Unity, Blender, 3ds Max, Modular Asset Bundles, PBR & Automated Retopology',
  },
  {
    title: 'Generative AI & Tooling',
    skills: 'AI 3D Generation Workflows, Voxelforge AI, ayam3d Generative R&D, Prompt & Asset Synthesis Pipelines',
  },
  {
    title: 'Frontend & Systems Architecture',
    skills: 'React, TypeScript, Next.js, Angular, LitElement Web Components, Design Systems, State Management',
  },
  {
    title: 'Cloud & Scalable SaaS',
    skills: 'Firebase, Node.js, Serverless, Offline PWAs, Real-Time Sync, Multi-Role Permissions, Microservices',
  },
];

export default function App() {
  return (
    <div className="page-shell">
      {/* Accessibility: Skip-to-content bypass link */}
      <a href="#main-content" className="skip-link">
        Skip to main content
      </a>

      {/* Navigation */}
      <header className="topbar">
        <a className="brand" href="#home" aria-label="Maheshchandra Hegde, home">
          <img src={maheshLogo} alt="" aria-hidden="true" width="40" height="40" />
          <div className="brand-text">
            <strong>Maheshchandra Hegde</strong>
            <span className="brand-title">Founder & CTO · Technoyana</span>
          </div>
        </a>

        <nav className="nav-links" aria-label="Primary navigation">
          <a href="#ventures">Ventures</a>
          <a href="#recent-posts">Recent Posts</a>
          <a href="#experience">Experience</a>
          <a href="#expertise">Expertise</a>
          <a href="#contact" className="nav-highlight">Get In Touch</a>
        </nav>
      </header>

      <main id="main-content" tabIndex="-1">
        {/* Hero Section */}
        <section className="hero" id="home">
          <div className="hero-copy">
            <div className="badge-wrapper">
              <span className="eyebrow-badge">Founder & CTO · Creative Technologist</span>
              <span className="pronoun-badge">He/Him</span>
            </div>

            <h1>
              Building AI-driven <span className="text-gradient">3D asset platforms</span> & spatial computing solutions.
            </h1>

            <p className="hero-text">
              Co-Founder and Technology Leader at <strong>Technoyana Digital Transformation Services</strong>.
              Overseeing flagship ventures including <strong>Srushtilabs</strong> (AI-assisted modular 3D assets & Voxelforge AI)
              and <strong>Twitan</strong> (high-reliability sports SaaS suite including Shutlify and Twicket).
            </p>

            <div className="hero-cta-group">
              <a href="#ventures" className="btn btn-primary">
                Explore Ventures
                <span className="btn-arrow" aria-hidden="true">→</span>
              </a>
              <a href="#recent-posts" className="btn btn-secondary">
                Technoyana Posts & News
              </a>
              <a
                href="https://www.linkedin.com/in/maheshchandrahegde/"
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-linkedin"
                aria-label="LinkedIn Profile (opens in new tab)"
              >
                <img src={linkedinLogo} alt="" aria-hidden="true" width="18" height="18" />
                <span>LinkedIn Profile</span>
              </a>
            </div>

            <div className="quick-contact-row" aria-label="Quick contact">
              <a href="mailto:hid.mahesh@gmail.com" className="quick-contact-link">
                <span className="icon-dot" aria-hidden="true"></span>
                hid.mahesh@gmail.com
              </a>
              <a href="tel:+919535253329" className="quick-contact-link">
                <span className="icon-dot" aria-hidden="true"></span>
                +91 9535253329
              </a>
              <span className="quick-contact-loc">Bengaluru, Karnataka, India</span>
            </div>
          </div>

          {/* Hero Right: Venture Showcase Card (Replacing previous portrait photo) */}
          <div className="hero-showcase">
            <div className="showcase-card">
              <div className="showcase-header">
                <div className="showcase-status">
                  <span className="live-indicator" aria-hidden="true"></span>
                  Active Studio Operations
                </div>
                <div className="showcase-est">Est. 2021</div>
              </div>

              <div className="showcase-technoyana">
                <TechnoyanaLogo height={28} textColor="#0f172a" />
                <p className="showcase-sub">
                  Digital Transformation Services Private Limited
                </p>
              </div>

              <div className="showcase-divisions">
                <div className="division-pill">
                  <div className="div-icon div-srushti" aria-hidden="true">3D</div>
                  <div>
                    <strong>Srushtilabs</strong>
                    <span>Spatial AI & Voxelforge AI</span>
                  </div>
                </div>
                <div className="division-pill">
                  <div className="div-icon div-twitan" aria-hidden="true">OS</div>
                  <div>
                    <strong>Twitan</strong>
                    <span>Shutlify & Twicket SaaS</span>
                  </div>
                </div>
              </div>

              <div className="showcase-metrics">
                <div className="metric-item">
                  <div className="metric-num">18+</div>
                  <div className="metric-lbl">Years Experience</div>
                </div>
                <div className="metric-item">
                  <div className="metric-num">3</div>
                  <div className="metric-lbl">Flagship Divisions</div>
                </div>
                <div className="metric-item">
                  <div className="metric-num">3D + AI</div>
                  <div className="metric-lbl">Core Architecture</div>
                </div>
              </div>

              <div className="showcase-footer">
                <span className="photo-notice">New executive portrait updating soon</span>
              </div>
            </div>
          </div>
        </section>

        {/* Flagship Ventures Section */}
        <section className="section" id="ventures" aria-labelledby="ventures-heading">
          <div className="section-header">
            <div className="section-eyebrow">TECHNOLOGY LEADERSHIP & VENTURES</div>
            <h2 id="ventures-heading">Technoyana & Flagship Divisions</h2>
            <p className="section-desc">
              Powering modern enterprise solutions, generative 3D asset engineering, and domain-specific SaaS platforms.
            </p>
          </div>

          <div className="ventures-grid">
            {flagshipDivisions.map((division) => (
              <div key={division.name} className="venture-card">
                <div className="venture-header">
                  <span className="venture-badge">{division.badge}</span>
                  <a
                    href={division.website}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="venture-ext-link"
                    title={`Visit ${division.websiteLabel} (opens in new tab)`}
                    aria-label={`Visit ${division.websiteLabel} (opens in new tab)`}
                  >
                    {division.websiteLabel} <span aria-hidden="true">↗</span>
                  </a>
                </div>

                <h3>{division.name}</h3>
                <p className="venture-subtitle">{division.subtitle}</p>
                <p className="venture-description">{division.description}</p>

                <div className="venture-pillars" aria-label="Key Pillars">
                  {division.pillars.map((pillar) => (
                    <span key={pillar} className="pillar-tag">
                      {pillar}
                    </span>
                  ))}
                </div>

                <div className="venture-action">
                  <a
                    href={division.website}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="venture-btn"
                    aria-label={`Visit ${division.websiteLabel} (opens in new tab)`}
                  >
                    Visit {division.websiteLabel} <span className="sr-only">(opens in new tab)</span>
                  </a>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Recent Posts from technoyana.in */}
        <section className="section section-highlight" id="recent-posts" aria-labelledby="posts-heading">
          <div className="section-header">
            <div className="section-eyebrow">TECHNOYANA.IN INSIGHTS & UPDATES</div>
            <div className="header-with-logo">
              <h2 id="posts-heading">Recent Posts & News</h2>
              <a
                href="https://technoyana.in/"
                target="_blank"
                rel="noopener noreferrer"
                className="logo-badge-link"
                aria-label="Visit Technoyana.in website (opens in new tab)"
              >
                <TechnoyanaLogo height={24} textColor="#0f172a" />
              </a>
            </div>
            <p className="section-desc">
              Latest product announcements, generative 3D updates, and engineering roadmaps from Technoyana.
            </p>
          </div>

          <div className="posts-grid">
            {technoyanaPosts.map((post) => (
              <article key={post.id} className="post-card">
                <div className="post-meta">
                  <span className="post-category">{post.category}</span>
                  <time className="post-date" dateTime={post.dateTime}>{post.date}</time>
                </div>

                <h3 className="post-title">{post.title}</h3>
                <p className="post-summary">{post.summary}</p>

                <div className="post-footer">
                  <span className="post-tag">{post.tag}</span>
                  <a
                    href={post.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="post-link"
                    aria-label={`${post.linkLabel}: ${post.title} (opens in new tab)`}
                  >
                    {post.linkLabel} <span aria-hidden="true">→</span>
                  </a>
                </div>
              </article>
            ))}
          </div>

          <div className="posts-banner">
            <div>
              <strong>Explore the full Technoyana innovation ecosystem</strong>
              <p>Discover client engineering case studies, spatial AI demos, and software services.</p>
            </div>
            <a
              href="https://technoyana.in/"
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-primary"
              aria-label="Visit Technoyana.in (opens in new tab)"
            >
              Visit Technoyana.in <span aria-hidden="true">↗</span>
            </a>
          </div>
        </section>

        {/* Core Expertise Section */}
        <section className="section" id="expertise" aria-labelledby="expertise-heading">
          <div className="section-header">
            <div className="section-eyebrow">COMPETENCIES & CAPABILITIES</div>
            <h2 id="expertise-heading">Pillars of Architectural Expertise</h2>
            <p className="section-desc">
              Bridging high-performance UI/UX systems with scalable full-stack pipelines and spatial technologies.
            </p>
          </div>

          <div className="expertise-grid">
            {expertisePillars.map((pillar) => (
              <div key={pillar.title} className="expertise-card">
                <h3>{pillar.title}</h3>
                <p>{pillar.skills}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Career & Consulting Experience */}
        <section className="section" id="experience" aria-labelledby="experience-heading">
          <div className="section-header">
            <div className="section-eyebrow">TRACK RECORD & LEADERSHIP</div>
            <h2 id="experience-heading">Enterprise & Consulting Experience</h2>
            <p className="section-desc">
              Proven track record across global tech enterprises, startups, and specialized engineering consultancies.
            </p>
          </div>

          <div className="experience-timeline">
            {careerRoles.map((exp) => (
              <div key={`${exp.company}-${exp.role}`} className="exp-card">
                <div className="exp-main">
                  <div className="exp-role-row">
                    <h3 className="exp-role">{exp.role}</h3>
                    <span className="exp-company-badge">{exp.company}</span>
                  </div>
                  <div className="exp-meta">
                    <span className="exp-period">{exp.period}</span>
                    {exp.location && <span className="exp-location">· {exp.location}</span>}
                  </div>
                  <p className="exp-description">{exp.description}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Client & Enterprise Recognition */}
        <section className="section" id="companies" aria-labelledby="companies-heading">
          <div className="section-header">
            <div className="section-eyebrow">TRUSTED BY GLOBAL TEAMS</div>
            <h2 id="companies-heading">Enterprise Consulting & Client History</h2>
          </div>

          <div className="logo-grid">
            {clientLogos.map(([name, src]) => (
              <figure key={name} className="logo-tile">
                <img src={src} alt="" aria-hidden="true" loading="lazy" />
                <figcaption>{name}</figcaption>
              </figure>
            ))}
          </div>
        </section>

        {/* Contact Section */}
        <section className="section contact-section" id="contact" aria-labelledby="contact-heading">
          <div className="contact-box">
            <h2 id="contact-heading">Let’s Build Something Exceptional</h2>
            <p>
              Interested in AI-driven 3D workflows, spatial computing architectures, or enterprise product engineering?
              Feel free to connect.
            </p>

            <div className="contact-actions">
              <a href="mailto:hid.mahesh@gmail.com" className="btn btn-primary">
                Email: hid.mahesh@gmail.com
              </a>
              <a href="tel:+919535253329" className="btn btn-secondary">
                Call: +91 9535253329
              </a>
              <a
                href="https://www.linkedin.com/in/maheshchandrahegde/"
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-linkedin"
                aria-label="Connect on LinkedIn (opens in new tab)"
              >
                <img src={linkedinLogo} alt="" aria-hidden="true" width="18" height="18" />
                <span>Connect on LinkedIn</span>
              </a>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="footer">
        <div className="footer-content">
          <div className="footer-left">
            <strong>Maheshchandra Hegde</strong>
            <p>Founder & CTO · Technoyana Digital Transformation Services Pvt. Ltd.</p>
          </div>
          <div className="footer-links" aria-label="Footer navigation links">
            <a href="https://technoyana.in" target="_blank" rel="noopener noreferrer">
              technoyana.in <span className="sr-only">(opens in new tab)</span>
            </a>
            <a href="https://srushtilabs.com" target="_blank" rel="noopener noreferrer">
              srushtilabs.com <span className="sr-only">(opens in new tab)</span>
            </a>
            <a href="https://twitan.com" target="_blank" rel="noopener noreferrer">
              twitan.com <span className="sr-only">(opens in new tab)</span>
            </a>
            <a href="https://www.linkedin.com/in/maheshchandrahegde/" target="_blank" rel="noopener noreferrer">
              LinkedIn <span className="sr-only">(opens in new tab)</span>
            </a>
          </div>
        </div>
        <div className="footer-bottom">
          © {new Date().getFullYear()} Maheshchandra Hegde. All rights reserved.
        </div>
      </footer>
    </div>
  );
}
