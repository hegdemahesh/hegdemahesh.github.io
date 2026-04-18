import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import maheshLogo from '../maheshLogo.svg';
import heroPortrait from '../maheshBgRemoved02.png';

const resumeSections = [
  { id: 'summary', label: 'Summary' },
  { id: 'experience', label: 'Experience' },
  { id: 'awards', label: 'Awards' },
  { id: 'education', label: 'Education' },
];

function stripBoldMarkers(value) {
  return value.replace(/^\*\*/, '').replace(/\*\*$/, '').trim();
}

function isBoldLine(line) {
  return /^\*\*.*\*\*$/.test(line);
}

function normalizeSection(heading) {
  const normalized = heading.trim().toLowerCase();

  if (normalized === 'skills summary') {
    return 'skills';
  }

  if (normalized === 'awards and acknowledgements') {
    return 'awards';
  }

  return normalized;
}

function splitExperienceHeading(heading) {
  const parts = heading.split(' — ');

  return {
    company: parts[0] || '',
    role: parts.slice(1).join(' — '),
  };
}

function createEmptyResume() {
  return {
    name: '',
    title: '',
    contact: [],
    skills: [],
    awards: [],
    experience: [],
    education: [],
  };
}

function createExperienceEntry(heading) {
  return {
    heading,
    period: '',
    paragraphs: [],
    bullets: [],
  };
}

function appendSectionItem(resume, section, item) {
  const targetMap = {
    contact: 'contact',
    skills: 'skills',
    awards: 'awards',
    education: 'education',
  };

  const target = targetMap[section];

  if (target) {
    resume[target].push(item);
  }
}

function finalizeExperience(resume, currentExperience) {
  if (!currentExperience) {
    return;
  }

  const details = splitExperienceHeading(currentExperience.heading);
  resume.experience.push({
    company: details.company,
    role: details.role,
    period: currentExperience.period,
    paragraphs: currentExperience.paragraphs,
    bullets: currentExperience.bullets,
  });
}

function handleTopLevelLine(line, resume, state) {
  if (line.startsWith('# ')) {
    resume.name = line.slice(2).trim();
    return true;
  }

  if (!state.currentSection && isBoldLine(line)) {
    resume.title = stripBoldMarkers(line);
    return true;
  }

  if (line === '**Contact**') {
    state.currentSection = 'contact';
    return true;
  }

  if (line.startsWith('## ')) {
    finalizeExperience(resume, state.currentExperience);
    state.currentExperience = null;
    state.currentSection = normalizeSection(line.slice(3));
    return true;
  }

  return false;
}

function handleExperienceLine(line, resume, currentExperience) {
  if (line.startsWith('### ')) {
    finalizeExperience(resume, currentExperience);
    return createExperienceEntry(line.slice(4).trim());
  }

  if (isBoldLine(line) && currentExperience && !currentExperience.period) {
    currentExperience.period = stripBoldMarkers(line);
    return currentExperience;
  }

  if (line.startsWith('- ') && currentExperience) {
    currentExperience.bullets.push(line.slice(2).trim());
    return currentExperience;
  }

  if (currentExperience) {
    currentExperience.paragraphs.push(line);
  }

  return currentExperience;
}

function parseResumeMarkdown(markdown) {
  const resume = createEmptyResume();
  const state = {
    currentSection: '',
    currentExperience: null,
  };

  for (const rawLine of markdown.split(/\r?\n/)) {
    const line = rawLine.trim();

    if (!line) {
      continue;
    }

    if (handleTopLevelLine(line, resume, state)) {
      continue;
    }

    if (state.currentSection === 'experience') {
      state.currentExperience = handleExperienceLine(line, resume, state.currentExperience);
      continue;
    }

    if (line.startsWith('- ')) {
      appendSectionItem(resume, state.currentSection, line.slice(2).trim());
    }
  }

  finalizeExperience(resume, state.currentExperience);
  return resume;
}

function getContactHref(item) {
  if (typeof item !== 'string' || !item.trim()) {
    return null;
  }

  const normalized = item.replaceAll(/[()\s-]/g, '');

  if (item.includes('@')) {
    return `mailto:${item}`;
  }

  if (/^\+?\d+$/.test(normalized)) {
    return `tel:+${normalized.replace(/^\+/, '')}`;
  }

  return null;
}

function getCareerSpan(experience) {
  const years = experience
    .flatMap((entry) => entry.period.match(/\b\d{4}\b/g) || [])
    .map((value) => Number.parseInt(value, 10))
    .filter((value) => Number.isFinite(value));

  if (!years.length) {
    return '';
  }

  return `${Math.max(...years) - Math.min(...years) + 1} years documented`;
}

export default function ResumePage() {
  const [resume, setResume] = useState(createEmptyResume());
  const [status, setStatus] = useState('loading');

  useEffect(() => {
    let isMounted = true;

    fetch('/RESUME.md')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Unable to load resume content.');
        }

        return response.text();
      })
      .then((markdown) => {
        if (!isMounted) {
          return;
        }

        setResume(parseResumeMarkdown(markdown));
        setStatus('ready');
      })
      .catch(() => {
        if (!isMounted) {
          return;
        }

        setStatus('error');
      });

    return () => {
      isMounted = false;
    };
  }, []);

  if (status === 'loading') {
    return (
      <div className="resume-page-shell resume-loading-state">
        <p>Loading resume...</p>
      </div>
    );
  }

  if (status === 'error') {
    return (
      <div className="resume-page-shell resume-loading-state">
        <p>Resume content could not be loaded.</p>
        <Link className="button button-secondary" to="/">
          Back to home
        </Link>
      </div>
    );
  }

  const leadSkills = resume.skills.slice(0, 3);
  const extraSkills = resume.skills.slice(3);
  const careerSpan = getCareerSpan(resume.experience);
  const emailHref = resume.contact.find((item) => item.includes('@'));
  const primaryContactHref = getContactHref(emailHref);

  return (
    <div className="resume-page-shell">
      <div className="resume-backdrop resume-backdrop-left" />
      <div className="resume-backdrop resume-backdrop-right" />

      <header className="resume-topbar">
        <Link className="brand" to="/" aria-label="Back to portfolio home">
          <img src={maheshLogo} alt="Maheshchandra Hegde logo" />
          <div>
            <strong>{resume.name}</strong>
            <span>Resume</span>
          </div>
        </Link>

        <nav className="resume-nav" aria-label="Resume navigation">
          <Link to="/">Home</Link>
          {resumeSections.map((section) => (
            <a key={section.id} href={`#${section.id}`}>
              {section.label}
            </a>
          ))}
        </nav>
      </header>

      <main>
        <section className="resume-hero">
          <div className="resume-hero-copy">
            <p className="eyebrow">Resume</p>
            <h1>{resume.name}</h1>
            <p className="resume-hero-title">{resume.title}</p>
            <p className="resume-hero-text">{resume.skills[0] || resume.title}</p>

            <div className="resume-hero-actions">
              <a className="button button-primary" href={primaryContactHref || '#contact'}>
                Contact by email
              </a>
              <a className="button button-secondary" href="#experience">
                View experience
              </a>
            </div>

            <div className="resume-stat-grid">
              <article className="resume-stat-card resume-stat-card-accent">
                <span>{careerSpan || 'Career timeline'}</span>
                <p>{resume.experience.length} documented roles across consulting, leadership, and frontend delivery.</p>
              </article>
              <article className="resume-stat-card">
                <span>{resume.awards.length} recognitions</span>
                <p>Acknowledgements captured from enterprise and consulting work.</p>
              </article>
              <article className="resume-stat-card">
                <span>{resume.education.length} academic milestones</span>
                <p>Computing, interface design, and engineering foundations.</p>
              </article>
            </div>
          </div>

          <aside className="resume-profile-panel" id="contact">
            <div className="resume-portrait-frame">
              <img src={heroPortrait} alt="Maheshchandra Hegde portrait" />
            </div>

            <div className="resume-contact-card">
              <p className="card-kicker">Contact</p>
              <ul className="resume-contact-list">
                {resume.contact.map((item) => {
                  const href = getContactHref(item);

                  return (
                    <li key={item}>
                      {href ? <a href={href}>{item}</a> : <span>{item}</span>}
                    </li>
                  );
                })}
              </ul>
            </div>
          </aside>
        </section>

        <section className="resume-section-block" id="summary">
          <div className="section-heading resume-section-heading-wide">
            <p className="eyebrow">Skills Summary</p>
            <h2>The markdown resume, presented as a structured design page.</h2>
            <p className="section-intro">
              This page reads from the existing resume source and turns it into a dedicated web experience instead of opening the raw markdown file.
            </p>
          </div>

          <div className="resume-summary-grid">
            {leadSkills.map((item, index) => (
              <article key={item} className="resume-summary-card">
                <p className="card-kicker">Focus 0{index + 1}</p>
                <p>{item}</p>
              </article>
            ))}
          </div>

          <div className="resume-detail-panel">
            <p className="card-kicker">Additional strengths</p>
            <div className="resume-detail-columns">
              {extraSkills.map((item) => (
                <p key={item}>{item}</p>
              ))}
            </div>
          </div>
        </section>

        <section className="resume-section-block" id="experience">
          <div className="section-heading resume-section-heading-wide">
            <p className="eyebrow">Experience</p>
            <h2>Product delivery, UX strategy, and frontend architecture across multiple roles.</h2>
          </div>

          <div className="resume-timeline">
            {resume.experience.map((entry) => (
              <article key={`${entry.company}-${entry.period}`} className="resume-timeline-card">
                <div className="resume-timeline-meta">
                  <span>{entry.period}</span>
                  <p>{entry.company}</p>
                </div>

                <div className="resume-timeline-content">
                  <h3>{entry.role || entry.company}</h3>
                  {entry.paragraphs.map((paragraph) => (
                    <p key={paragraph}>{paragraph}</p>
                  ))}
                  {!!entry.bullets.length && (
                    <ul className="resume-bullet-list">
                      {entry.bullets.map((bullet) => (
                        <li key={bullet}>{bullet}</li>
                      ))}
                    </ul>
                  )}
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="resume-section-block resume-split-section" id="awards">
          <article className="resume-panel-card">
            <div className="section-heading resume-compact-heading">
              <p className="eyebrow">Awards</p>
              <h2>Recognition for delivery, contribution, and leadership.</h2>
            </div>

            <ul className="resume-bullet-list resume-bullet-list-spacious">
              {resume.awards.map((award) => (
                <li key={award}>{award}</li>
              ))}
            </ul>
          </article>

          <article className="resume-panel-card" id="education">
            <div className="section-heading resume-compact-heading">
              <p className="eyebrow">Education</p>
              <h2>Academic background that supports both design and engineering practice.</h2>
            </div>

            <ul className="resume-education-list">
              {resume.education.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </article>
        </section>
      </main>
    </div>
  );
}