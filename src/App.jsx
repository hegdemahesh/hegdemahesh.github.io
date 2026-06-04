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

const companies = [
  ['Ness', nessLogo],
  ['Moonraft', moonraftLogo],
  ['UST', ustLogo],
  ['Cisco', ciscoLogo],
  ['ThoughtFocus', thoughtfocusLogo],
  ['CAE', caeLogo],
];

const services = [
  'UI/UX consulting',
  'Frontend architecture (React, Angular, JavaScript)',
  'Rapid prototypes and product UI delivery',
];

export default function App() {
  return (
    <div className="page-shell">
      <header className="topbar">
        <a className="brand" href="#home" aria-label="Maheshchandra Hegde home">
          <img src={maheshLogo} alt="Maheshchandra Hegde logo" />
          <div>
            <strong>Maheshchandra Hegde</strong>
            <span>UI/UX Consultant · Frontend Architect · Product Strategist</span>
          </div>
        </a>

        <nav className="nav-links" aria-label="Primary">
          <a href="#what">What I Do</a>
          <a href="#companies">Companies</a>
        </nav>
      </header>

      <main>
        <section className="hero" id="home">
          <div className="hero-copy">
            <h1>UI/UX and Frontend Consulting</h1>
            <p className="hero-text">
              I help teams design and ship clear, usable product experiences. My work combines UI
              design, frontend architecture, and practical delivery support.
            </p>

            <div className="hero-contact" aria-label="Contact links">
              <a href="mailto:hid.mahesh@gmail.com">hid.mahesh@gmail.com</a>
              <a href="tel:+919535253329">+91 9535253329</a>
              <a href="https://www.linkedin.com/in/maheshchandrahegde/" target="_blank" rel="noreferrer">
                <img src={linkedinLogo} alt="LinkedIn" />
                {' '}
                LinkedIn
              </a>
            </div>
          </div>

          <div className="hero-visual">
            <img src={heroPortrait} alt="Maheshchandra Hegde portrait" />
          </div>
        </section>

        <section className="section" id="what">
          <h2>Simple, focused support for product teams.</h2>
          <ul className="simple-list" aria-label="Services">
            {services.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </section>

        <section className="section" id="companies">
          <h2>Experience across consulting and enterprise teams.</h2>
          <div className="logo-grid">
            {companies.map(([name, src]) => (
              <figure key={name} className="logo-tile">
                <img src={src} alt={name} />
                <figcaption>{name}</figcaption>
              </figure>
            ))}
          </div>
        </section>

      </main>

      <footer className="footer">© 2026 Maheshchandra Hegde</footer>
    </div>
  );
}
