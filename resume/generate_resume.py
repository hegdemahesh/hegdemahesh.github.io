"""
Resume Generator for Maheshchandra Hegde
Generates:
1. CV_maheshchandra_hegde.pdf (Pixel-perfect vector PDF via Headless Edge/Chrome)
2. CV_maheshchandra_hegde.docx (Native Microsoft Word format via python-docx)

Target Roles: Fractional CTO / Technical Architect / Principal Consultant
Balanced Executive Profile
"""

import os
import subprocess
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, ".."))

photo_path = os.path.join(root_dir, "maheshForResume.jpg")
if not os.path.exists(photo_path):
    # fallback to original extracted image if needed
    alt_photo = os.path.join(script_dir, "original", "image1.jpg")
    if os.path.exists(alt_photo):
        photo_path = alt_photo

HTML_PATH = os.path.join(script_dir, "CV_maheshchandra_hegde.html")
PDF_PATH = os.path.join(script_dir, "CV_maheshchandra_hegde.pdf")
DOCX_PATH = os.path.join(script_dir, "CV_maheshchandra_hegde.docx")


# ==============================================================================
# 1. HTML & PDF GENERATOR
# ==============================================================================
def generate_html_and_pdf():
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Maheshchandra Hegde - Resume | Fractional CTO & Principal Architect</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 portrait;
    margin: 10mm 12mm 10mm 12mm;
    @bottom-right {{
      content: counter(page);
    }}
  }}
  * {{
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }}
  body {{
    font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #1e293b;
    line-height: 1.44;
    font-size: 9.2pt;
    font-weight: 350;
    margin: 0;
    padding: 0;
    background: #ffffff;
  }}
  a {{
    color: #0284c7;
    text-decoration: none;
    font-weight: 400;
  }}
  a:hover {{
    text-decoration: underline;
  }}

  /* HEADER */
  .header-card {{
    border-bottom: 2px solid #0284c7;
    padding-bottom: 7px;
    margin-bottom: 9px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 14px;
  }}
  .header-info {{
    flex-grow: 1;
  }}
  .header-info h1 {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 20pt;
    font-weight: 700;
    margin: 0 0 2px 0;
    color: #0f172a;
    letter-spacing: -0.4px;
  }}
  .header-headline {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 10.8pt;
    font-weight: 500;
    color: #0284c7;
    margin-bottom: 4px;
    letter-spacing: 0.1px;
  }}
  .header-meta {{
    font-size: 8.6pt;
    font-weight: 350;
    color: #475569;
    line-height: 1.48;
  }}
  .header-meta strong {{
    font-weight: 500;
    color: #1e293b;
  }}
  .photo-box {{
    width: 80px;
    height: 100px;
    border-radius: 5px;
    overflow: hidden;
    flex-shrink: 0;
    border: 2px solid #cbd5e1;
    box-shadow: 0 2px 5px rgba(0,0,0,0.06);
  }}
  .photo-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}

  /* SECTION TITLES */
  h2.section-title {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #0f172a;
    font-size: 10pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.7px;
    border-bottom: 1.5px solid #0284c7;
    padding-bottom: 2px;
    margin-top: 9px;
    margin-bottom: 5px;
    page-break-after: avoid;
  }}

  /* SUMMARY & CALLOUT */
  .summary-text {{
    font-size: 9.1pt;
    font-weight: 350;
    color: #334155;
    line-height: 1.44;
    margin-bottom: 5px;
    text-align: justify;
  }}
  .summary-text strong {{
    font-weight: 500;
    color: #0f172a;
  }}

  /* SKILLS MATRIX */
  .skills-container {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px 12px;
    margin-bottom: 7px;
  }}
  .skill-group {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3px solid #0284c7;
    border-radius: 4px;
    padding: 4.5px 7.5px;
    page-break-inside: avoid;
  }}
  .skill-group strong {{
    display: block;
    font-size: 8.7pt;
    font-weight: 600;
    color: #0f172a;
    margin-bottom: 1px;
  }}
  .skill-group span {{
    font-size: 8.2pt;
    font-weight: 350;
    color: #475569;
    line-height: 1.32;
    display: block;
  }}

  /* EXPERIENCE ITEMS */
  .exp-item {{
    margin-bottom: 6px;
    page-break-inside: avoid;
  }}
  .exp-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 1px;
  }}
  .exp-role {{
    font-size: 9.5pt;
    font-weight: 600;
    color: #0f172a;
  }}
  .exp-company {{
    font-size: 9.5pt;
    font-weight: 600;
    color: #0284c7;
  }}
  .exp-tenure {{
    font-size: 8.4pt;
    font-weight: 400;
    color: #64748b;
    white-space: nowrap;
  }}
  .exp-subhead {{
    font-size: 8.3pt;
    font-weight: 350;
    color: #64748b;
    font-style: normal;
    margin-bottom: 2px;
  }}
  ul.exp-bullets {{
    margin: 2px 0 3px 14px;
    padding: 0;
  }}
  ul.exp-bullets li {{
    font-size: 8.9pt;
    font-weight: 350;
    color: #334155;
    line-height: 1.4;
    margin-bottom: 2px;
  }}
  ul.exp-bullets li strong {{
    font-weight: 500;
    color: #0f172a;
  }}

  /* SUB-DIVISIONS (Technoyana SrushtiLabs & Twitan) */
  .sub-division {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5px 8px;
    margin: 3px 0 4px 0;
  }}
  .sub-division-title {{
    font-size: 8.8pt;
    font-weight: 600;
    color: #0369a1;
    margin-bottom: 2px;
  }}

  /* EDUCATION & AWARDS */
  .two-col-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }}
  .edu-card, .award-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 4.5px 7.5px;
    margin-bottom: 3px;
    page-break-inside: avoid;
  }}
  .edu-card h4, .award-card h4 {{
    margin: 0 0 1px 0;
    font-size: 8.8pt;
    color: #0f172a;
    font-weight: 600;
  }}
  .edu-card p, .award-card p {{
    margin: 0;
    font-size: 8.2pt;
    font-weight: 350;
    color: #475569;
  }}

  .page-break {{
    page-break-before: always;
  }}
</style>
</head>
<body>

<!-- HEADER -->
<header class="header-card">
  <div class="header-info">
    <h1>MAHESHCHANDRA HEGDE</h1>
    <div class="header-headline">Fractional CTO | Technical Architect | Creative Technologist</div>
    <div class="header-meta">
      <strong>Bangalore, India</strong> &nbsp;|&nbsp; 
      <span>+91 9535253329 / +91 7022407280</span> &nbsp;|&nbsp; 
      <a href="mailto:hid.mahesh@gmail.com">hid.mahesh@gmail.com</a><br>
      Portfolio: <a href="https://hegdemahesh.in" target="_blank">hegdemahesh.in</a> &nbsp;|&nbsp; 
      Technoyana: <a href="https://technoyana.in" target="_blank">technoyana.in</a> &nbsp;|&nbsp; 
      LinkedIn: <a href="https://www.linkedin.com/in/maheshchandrahegde/" target="_blank">linkedin.com/in/maheshchandrahegde</a>
    </div>
  </div>
  <div class="photo-box">
    <img src="{photo_path.replace(os.sep, '/')}" alt="Maheshchandra Hegde">
  </div>
</header>

<!-- EXECUTIVE SUMMARY -->
<section>
  <h2 class="section-title">Executive Profile & Summary</h2>
  <div class="summary-text">
    <strong>Versatile Technology Leader, Principal Architect, and Product Strategist</strong> with <strong>18+ years</strong> of track record architecting high-performance digital products, distributed cloud platforms, and immersive spatial 3D systems. Expert in <strong>React, Angular, TypeScript, Node.js, Web Components (LitElement), Cloud architectures (GCP/Firebase, AWS)</strong>, and resilient offline-first PWAs. Dual-disciplined background blending Human Interface Design (<strong>M.S. in Computing, UK</strong>) with Electronics & Communication Engineering (<strong>B.E.</strong>), uniquely bridging high-level executive business strategy with deep, hands-on architectural rigor.
  </div>
  <div class="summary-text">
    Currently serving as <strong>Fractional CTO at eBodhya Technologies</strong> (leading AI-assisted Academic Intelligence & school management systems) and <strong>Founder & CTO at Technoyana Digital Transformation Services</strong>, incubating deep-tech product studios including <strong>SrushtiLabs</strong> (generative 3D asset platforms, VoxelForge AI, Ayam3d) and <strong>Twitan</strong> (high-reliability sports tournament management OS, Shutlify & Twicket). Proven background executing mission-critical enterprise modernizations (4-year zero-downtime migration of Cisco Stadium Vision Director), clinical ICU software (Philips Healthcare ICCA), and cross-framework UI design systems. Available for fractional leadership, architecture governance, and technical consulting.
  </div>
</section>

<!-- CORE COMPETENCIES -->
<section>
  <h2 class="section-title">Core Competencies & Technical Mastery</h2>
  <div class="skills-container">
    <div class="skill-group">
      <strong>Executive & Technical Leadership</strong>
      <span>Fractional CTO, Technical Architecture, System Modernization, Product Strategy, Agile/Scrum, Mentorship, Engineering Roadmaps</span>
    </div>
    <div class="skill-group">
      <strong>Frontend & Web Systems</strong>
      <span>React, TypeScript, Angular, Web Components (LitElement), Next.js, Vite, Redux, Modern JavaScript (ES6+), HTML5/CSS3, WCAG 2.1 AA</span>
    </div>
    <div class="skill-group">
      <strong>AI, Spatial Computing & 3D Tech</strong>
      <span>Generative 3D Asset Creation, Mesh Synthesis, Automated Retopology, Tileable PBR Textures & Upscaling, Three.js, WebGL, 3ds Max, Blender</span>
    </div>
    <div class="skill-group">
      <strong>Cloud, Backend & Offline Architecture</strong>
      <span>Node.js, Express, Firebase / Google Cloud Platform (GCP), AWS, REST APIs, Micro-frontends, PWA (Offline-first / IndexedDB)</span>
    </div>
    <div class="skill-group">
      <strong>Enterprise Security & Reliability</strong>
      <span>Strict Healthcare Security (MFA, RBAC, XSS Prevention), HIPAA/PHI Data Protection, Zero Memory-Leak Continuous Clinical Uptime</span>
    </div>
    <div class="skill-group">
      <strong>Design Systems & UX Strategy</strong>
      <span>Enterprise UI Design Systems, Design-to-Code Automation, Interactive Prototyping, Figma, Adobe XD, Photoshop, Human-Interface Design</span>
    </div>
  </div>
</section>

<!-- PROFESSIONAL EXPERIENCE -->
<section>
  <h2 class="section-title">Professional Experience</h2>

  <!-- eBodhya -->
  <div class="exp-item">
    <div class="exp-header">
      <div>
        <span class="exp-role">Fractional Chief Technology Officer (CTO)</span> — 
        <span class="exp-company">eBodhya Technologies Private Limited</span>
      </div>
      <span class="exp-tenure">Sep 2026 – Present</span>
    </div>
    <div class="exp-subhead">Bengaluru, India · Academic Intelligence Operating System & EdTech SaaS Platform</div>
    <ul class="exp-bullets">
      <li>Drive technical leadership and architectural vision for an interconnected Academic Intelligence OS designed to streamline school operations, curriculum workflows, and assessment processes.</li>
      <li>Architect curriculum-aware AI workflows and evaluation engines linking question banks, automated grading, and real-time student analytics into a unified source of truth.</li>
      <li>Establish modular full-stack architecture, scalability guidelines, and automated deployment pipelines, empowering educators and accelerating product-market rollout.</li>
    </ul>
  </div>

  <!-- Technoyana -->
  <div class="exp-item">
    <div class="exp-header">
      <div>
        <span class="exp-role">Founder & Chief Technology Officer (CTO)</span> — 
        <span class="exp-company">Technoyana Digital Transformation Services Pvt. Ltd.</span>
      </div>
      <span class="exp-tenure">May 2021 – Present</span>
    </div>
    <div class="exp-subhead">Bengaluru, India · Enterprise Product Engineering, Spatial AI & High-Reliability SaaS Studio</div>
    <ul class="exp-bullets">
      <li>Direct end-to-end technology vision, cloud architecture, and product engineering across Technoyana's incubator portfolio and enterprise consulting initiatives.</li>
      <li>
        <strong>SrushtiLabs (Spatial AI & 3D Tech Division) | <a href="https://srushtilabs.com/voxelforge/" target="_blank">srushtilabs.com</a></strong>:
        <ul style="margin: 2px 0 2px 14px;">
          <li>Architected <strong>VoxelForge AI</strong> (<a href="https://srushtilabs.com/voxelforge/" target="_blank">srushtilabs.com/voxelforge/</a>), a generative 3D asset platform producing modular, low-poly 3D models and asset bundles optimized for real-time engines including Unreal Engine, Unity, and WebGL.</li>
          <li>Engineered <strong>Ayam3d</strong> (<a href="https://ayam3d.in/" target="_blank">ayam3d.in/</a>), a parametric AI 3D mesh synthesis engine transforming natural language prompts into production 3D assets with automated retopology and tileable PBR texture pipelines; secured early investor validation.</li>
        </ul>
      </li>
      <li>
        <strong>Twitan (Sports SaaS Studio) | <a href="https://twitan.com" target="_blank">twitan.com</a></strong>:
        <ul style="margin: 2px 0 2px 14px;">
          <li>Architected <strong>Shutlify (Badminton OS)</strong>, an end-to-end tournament management platform featuring automated knockout/round-robin fixture engines, live court arbitration, multi-court scheduling, and offline-first PWA resilience for unreliable venue networks (deployed at tournaments like HBL Sirsi).</li>
          <li>Developed <strong>Twicket</strong>, a high-fidelity real-time scoring and match statistics engine for cricket tournaments.</li>
        </ul>
      </li>
      <li><strong>Specialized Multi-Disciplinary Engineering</strong>: Designed customized CNC machine controller interfaces and automated CAD/CAM toolpath generation pipelines; delivered architectural 3D simulations and consumer IoT parking payment applications.</li>
    </ul>
  </div>

  <!-- Cyient / Philips -->
  <div class="exp-item">
    <div class="exp-header">
      <div>
        <span class="exp-role">Senior Technical Lead (React / Node.js)</span> — 
        <span class="exp-company">Cyient Limited / Philips Healthcare</span>
      </div>
      <span class="exp-tenure">Nov 2023 – Mar 2025</span>
    </div>
    <div class="exp-subhead">Bengaluru, India · Philips IntelliSpace Critical Care & Anesthesia (ICCA) · Mission-Critical ICU Software</div>
    <ul class="exp-bullets">
      <li>Led web-tier engineering and frontend architecture for Philips ICCA clinical software deployed in hospital ICUs and anesthesia departments globally.</li>
      <li>Ensured 24/7 continuous clinical reliability with zero memory leaks and sub-second UI responsiveness under dense, real-time streaming patient telemetry.</li>
      <li>Strictly enforced enterprise healthcare security policies including Multi-Factor Authentication (MFA), Cross-Site Scripting (XSS) prevention, granular Role-Based Access Control (RBAC), and strict patient data privacy compliance.</li>
      <li>Governed code quality, architectural standards, automated regression testing, and modular micro-frontends across distributed agile squads.</li>
    </ul>
  </div>

  <!-- Ness Digital Engineering -->
  <div class="exp-item">
    <div class="exp-header">
      <div>
        <span class="exp-role">Development Lead / Senior Analyst</span> — 
        <span class="exp-company">Ness Digital Engineering</span>
      </div>
      <span class="exp-tenure">Oct 2019 – Apr 2020</span>
    </div>
    <div class="exp-subhead">Bengaluru, India · Entertainment Management Application (Angular / AWS / Node.js)</div>
    <ul class="exp-bullets">
      <li>Architected the complete single-page application structure using Angular, TypeScript, Node.js, and AWS cloud infrastructure.</li>
      <li>Enforced strict accessibility standards (WCAG 2.1 AA), frontend security best practices, and code quality linters across the engineering squad.</li>
      <li>Took technical ownership of the CI/CD deployment pipelines, successfully delivering the application to client production on schedule.</li>
    </ul>
  </div>

  <!-- Moonraft Innovation Labs -->
  <div class="exp-item">
    <div class="exp-header">
      <div>
        <span class="exp-role">User Interface Architect</span> — 
        <span class="exp-company">Moonraft Innovation Labs (Unit of UST Global)</span>
      </div>
      <span class="exp-tenure">May 2019 – Jul 2019</span>
    </div>
    <div class="exp-subhead">Bengaluru, India · Enterprise UI Design System & Mobile Engineering</div>
    <ul class="exp-bullets">
      <li>Architected and engineered a centralized <strong>Cross-Framework UI Design System</strong> using <strong>LitElement (Web Components), React, and Angular</strong>, packaged and distributed via npm.</li>
      <li>Completely eliminated component duplication across multiple engineering squads, ensuring seamless brand coherence and automated upgradability.</li>
      <li>Led the mobile application development squad building a high-performance cross-platform guest booking app for <strong>TLC Group of Hotels</strong> using Ionic and Angular.</li>
    </ul>
  </div>

  <!-- UST Global / Cisco -->
  <div class="exp-item">
    <div class="exp-header">
      <div>
        <span class="exp-role">Associate Project Manager & Senior Systems Analyst</span> — 
        <span class="exp-company">UST Global / Cisco Systems</span>
      </div>
      <span class="exp-tenure">Feb 2015 – Feb 2019</span>
    </div>
    <div class="exp-subhead">Bengaluru, India & Global Deployment · Cisco Stadium Vision Director (4+ Years Dedicated Tenure)</div>
    <ul class="exp-bullets">
      <li>Led the phased, zero-downtime legacy modernization of <strong>Cisco Stadium Vision Director</strong> from legacy Adobe Flash/Flex to modern <strong>Angular and React</strong> modules across premier international sporting stadiums.</li>
      <li>Architected hybrid micro-frontend bridges allowing legacy and modern components to coexist, preventing any disruption to live stadium operations.</li>
      <li>Managed cross-functional agile teams delivering single-page operational dashboards that substantially improved venue operational efficiency.</li>
      <li>Awarded three consecutive <strong>UST Global Certificates of Excellence (2015, 2016, 2018)</strong> for client-first commitment and outstanding engineering delivery.</li>
    </ul>
  </div>

  <div class="page-break"></div>

  <!-- ThoughtFocus -->
  <div class="exp-item">
    <div class="exp-header">
      <div>
        <span class="exp-role">UI Architect & Tech Lead</span> — 
        <span class="exp-company">ThoughtFocus Technologies</span>
      </div>
      <span class="exp-tenure">Oct 2011 – Mar 2014</span>
    </div>
    <div class="exp-subhead">Bengaluru, India · Aftermarket Parts 3D Explorer & Enterprise Solutions</div>
    <ul class="exp-bullets">
      <li>Architected an enterprise Aftermarket Parts Explorer catalog supporting millions of industrial and automotive parts with high-speed search and filtering.</li>
      <li>Engineered an interactive 3D inspection viewer enabling buyers to explore, rotate, and measure 3D models of components prior to purchasing.</li>
      <li>Established rapid design-to-code prototyping pipelines; bootstrapped enterprise search systems and logistics management applications for a large milk/dairy corporation.</li>
    </ul>
  </div>

  <!-- Independent Consultant / Cisco BMS -->
  <div class="exp-item">
    <div class="exp-header">
      <div>
        <span class="exp-role">Independent Consultant (UX Designer & Full-Stack Developer)</span> — 
        <span class="exp-company">Cisco Systems & Vodafone</span>
      </div>
      <span class="exp-tenure">Apr 2008 – Feb 2011</span>
    </div>
    <div class="exp-subhead">Bengaluru, India · Building Management Systems (BMS) Unified Dashboard</div>
    <ul class="exp-bullets">
      <li>Designed and developed the <strong>Cisco Campus Unified Facility Dashboard</strong>, integrating telemetry and control for AHUs, VRVs, industrial chillers, and campus environmental sensors.</li>
      <li>Awarded formal <strong>Cisco Certificate of Appreciation (2010)</strong> for outstanding operational visualization and intelligent facility telemetry. Delivered real-time data visualization dashboards for <strong>Vodafone</strong>.</li>
    </ul>
  </div>

  <!-- Earlier Career Foundation -->
  <div class="exp-item" style="margin-bottom: 6px;">
    <div class="exp-header">
      <span class="exp-role">Earlier Career & Foundational Experience</span>
      <span class="exp-tenure">2004 – 2015</span>
    </div>
    <ul class="exp-bullets">
      <li><strong>InnoBrik Software Technologies</strong> — Co-Founder & Technical Leader (Feb 2011 – Jan 2015): Spearheaded product engineering, tech stack evaluation, and agile delivery across startup ventures and enterprise client engagements.</li>
      <li><strong>CAE Simulation Technologies</strong> — Visual Database Developer (Sep 2007 – Apr 2008): Engineered 3D synthetic visual databases, topographical terrain models, and runway textures for real-time military and civil flight simulators under locked 60 FPS budgets.</li>
      <li><strong>Cognizant Technology Solutions</strong> — Programmer Analyst Trainee (Apr 2004 – Dec 2004): Maintained mission-critical mainframe applications, COBOL routines, and DB2 queries for the DUNSLINK commercial credit platform.</li>
    </ul>
  </div>
</section>

<!-- EDUCATION & AWARDS -->
<section>
  <div class="two-col-grid">
    <div>
      <h2 class="section-title">Education</h2>
      <div class="edu-card">
        <h4>Master of Science (M.S.) in Computing</h4>
        <p><strong>Robert Gordon University</strong>, Aberdeen, Scotland, UK (2005 – 2006)</p>
        <p style="font-size: 8pt; color: #64748b;">Specialization: Human Interface Design & Development</p>
      </div>
      <div class="edu-card">
        <h4>Bachelor of Engineering (B.E.) in ECE</h4>
        <p><strong>Bapuji Institute of Engineering & Technology (BIET)</strong>, Davanagere, India (1999 – 2003)</p>
        <p style="font-size: 8pt; color: #64748b;">Electronics & Communication Engineering</p>
      </div>
    </div>
    <div>
      <h2 class="section-title">Key Honors & Awards</h2>
      <div class="award-card">
        <h4>Cisco Certificate of Appreciation (2010)</h4>
        <p>Awarded for excellence in UX design and engineering of the Cisco Campus Unified BMS Facility Dashboard.</p>
      </div>
      <div class="award-card">
        <h4>UST Global Certificates of Excellence (2015, 2016, 2018)</h4>
        <p>Triple recognition for technical leadership, innovation, and client delivery on Cisco Stadium Vision.</p>
      </div>
    </div>
  </div>
</section>

</body>
</html>
"""
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[OK] Generated HTML at: {HTML_PATH}")

    # Search for headless browser
    browser_exe = None
    for candidate in [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]:
        if os.path.exists(candidate):
            browser_exe = candidate
            break

    if not browser_exe:
        print("[WARN] No headless Edge/Chrome found. PDF skipped.")
        return

    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        HTML_PATH
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(PDF_PATH) and os.path.getsize(PDF_PATH) > 0:
        print(f"[OK] Generated PDF ({os.path.getsize(PDF_PATH)} bytes) at: {PDF_PATH}")
    else:
        print("[ERROR] PDF generation failed:", res.stderr)


# ==============================================================================
# 2. MICROSOFT WORD (.DOCX) GENERATOR
# ==============================================================================
def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_heading_with_bottom_border(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text.upper())
    run.bold = True
    run.font.name = "Segoe UI"
    run.font.size = Pt(10.5)
    run.font.color.rgb = RGBColor(15, 23, 42) # Slate 900
    
    # Add bottom border in XML
    pPr = p._p.get_or_add_pPr()
    pBdr = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                     r'<w:bottom w:val="single" w:sz="12" w:space="4" w:color="0284C7"/>'
                     r'</w:pBdr>')
    pPr.append(pBdr)
    return p

def add_bullet_item(doc, title, text, sub_bullets=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.15
    if title:
        r_title = p.add_run(title)
        r_title.bold = True
        r_title.font.name = "Segoe UI"
        r_title.font.size = Pt(9.5)
        r_title.font.color.rgb = RGBColor(15, 23, 42)
    if text:
        r_text = p.add_run(text)
        r_text.font.name = "Segoe UI"
        r_text.font.size = Pt(9.5)
        r_text.font.color.rgb = RGBColor(51, 65, 85)

    if sub_bullets:
        for sb_title, sb_text in sub_bullets:
            sp = doc.add_paragraph(style='List Bullet 2')
            sp.paragraph_format.space_before = Pt(1)
            sp.paragraph_format.space_after = Pt(2)
            sp.paragraph_format.line_spacing = 1.12
            if sb_title:
                s_title = sp.add_run(sb_title)
                s_title.bold = True
                s_title.font.name = "Segoe UI"
                s_title.font.size = Pt(9)
                s_title.font.color.rgb = RGBColor(15, 23, 42)
            if sb_text:
                s_text = sp.add_run(sb_text)
                s_text.font.name = "Segoe UI"
                s_text.font.size = Pt(9)
                s_text.font.color.rgb = RGBColor(51, 65, 85)

def generate_docx():
    doc = Document()
    
    # Page Setup (Letter: 8.5 x 11 in, 0.65 in margins)
    sections = doc.sections
    for section in sections:
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)

    # HEADER TABLE (2 columns: info on left, photo on right)
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    col_widths = [Inches(5.8), Inches(1.4)]
    for i, col in enumerate(table.columns):
        col.width = col_widths[i]
        for cell in col.cells:
            cell.width = col_widths[i]
            
    cell_info, cell_photo = table.rows[0].cells[0], table.rows[0].cells[1]
    set_cell_margins(cell_info, top=0, bottom=60, left=0, right=60)
    set_cell_margins(cell_photo, top=0, bottom=60, left=60, right=0)
    
    # Name
    p_name = cell_info.paragraphs[0]
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(2)
    r_name = p_name.add_run("MAHESHCHANDRA HEGDE")
    r_name.font.name = "Segoe UI"
    r_name.font.size = Pt(19)
    r_name.bold = True
    r_name.font.color.rgb = RGBColor(15, 23, 42)
    
    # Title
    p_title = cell_info.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("Fractional CTO | Technical Architect | Creative Technologist")
    r_title.font.name = "Segoe UI"
    r_title.font.size = Pt(11)
    r_title.bold = True
    r_title.font.color.rgb = RGBColor(2, 132, 199)
    
    # Contact
    p_contact = cell_info.add_paragraph()
    p_contact.paragraph_format.space_before = Pt(0)
    p_contact.paragraph_format.space_after = Pt(0)
    p_contact.paragraph_format.line_spacing = 1.25
    r_c1 = p_contact.add_run("Bangalore, India  |  +91 9535253329 / 7022407280  |  hid.mahesh@gmail.com\n")
    r_c1.font.name = "Segoe UI"
    r_c1.font.size = Pt(9)
    r_c1.font.color.rgb = RGBColor(71, 85, 105)
    r_c2 = p_contact.add_run("Portfolio: hegdemahesh.in  |  Technoyana: technoyana.in  |  LinkedIn: linkedin.com/in/maheshchandrahegde")
    r_c2.font.name = "Segoe UI"
    r_c2.font.size = Pt(9)
    r_c2.font.color.rgb = RGBColor(2, 132, 199)

    # Photo in right cell
    p_photo = cell_photo.paragraphs[0]
    p_photo.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if os.path.exists(photo_path):
        p_photo.add_run().add_picture(photo_path, width=Inches(1.25))

    # Divider below header
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_before = Pt(4)
    p_div.paragraph_format.space_after = Pt(6)
    pPr = p_div._p.get_or_add_pPr()
    pBdr = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                     r'<w:bottom w:val="single" w:sz="16" w:space="1" w:color="0284C7"/>'
                     r'</w:pBdr>')
    pPr.append(pBdr)

    # 1. SUMMARY
    add_heading_with_bottom_border(doc, "Executive Profile & Summary")
    p_sum1 = doc.add_paragraph()
    p_sum1.paragraph_format.space_before = Pt(2)
    p_sum1.paragraph_format.space_after = Pt(4)
    p_sum1.paragraph_format.line_spacing = 1.2
    r_s1_b = p_sum1.add_run("Versatile Technology Leader, Principal Architect, and Product Strategist ")
    r_s1_b.bold = True
    r_s1_b.font.name = "Segoe UI"
    r_s1_b.font.size = Pt(9.5)
    r_s1_b.font.color.rgb = RGBColor(15, 23, 42)
    r_s1 = p_sum1.add_run("with 18+ years of track record architecting high-performance digital products, distributed cloud platforms, and immersive spatial 3D systems. Expert in React, Angular, TypeScript, Node.js, Web Components (LitElement), Cloud architectures (GCP/Firebase, AWS), and resilient offline-first PWAs. Dual-disciplined background blending Human Interface Design (M.S. in Computing, UK) with Electronics & Communication Engineering (B.E.), bridging high-level executive vision with hands-on architectural rigor.")
    r_s1.font.name = "Segoe UI"
    r_s1.font.size = Pt(9.5)
    r_s1.font.color.rgb = RGBColor(51, 65, 85)

    p_sum2 = doc.add_paragraph()
    p_sum2.paragraph_format.space_before = Pt(2)
    p_sum2.paragraph_format.space_after = Pt(8)
    p_sum2.paragraph_format.line_spacing = 1.2
    r_s2 = p_sum2.add_run("Currently serving as Fractional CTO at eBodhya Technologies (advancing AI-powered Academic Intelligence Operating System for schools) and Founder & CTO at Technoyana Digital Transformation Services, incubating deep-tech product studios including SrushtiLabs (generative 3D asset platforms, VoxelForge AI, Ayam3d) and Twitan (high-reliability sports tournament management OS, Shutlify & Twicket). Proven background executing mission-critical enterprise modernizations (4-year zero-downtime migration of Cisco Stadium Vision Director), clinical ICU software (Philips Healthcare ICCA), and cross-framework UI design systems. Available for fractional leadership, architecture governance, and technical consulting.")
    r_s2.font.name = "Segoe UI"
    r_s2.font.size = Pt(9.5)
    r_s2.font.color.rgb = RGBColor(51, 65, 85)

    # 2. CORE SKILLS
    add_heading_with_bottom_border(doc, "Core Competencies & Technical Skills")
    skills = [
        ("Executive & Technical Leadership: ", "Fractional CTO, Technical Architecture, System Modernization, Product Strategy, Agile/Scrum, Mentorship, Engineering Roadmaps"),
        ("Frontend & Web Systems: ", "React, TypeScript, Angular, Web Components (LitElement), Next.js, Vite, Redux, Modern JavaScript (ES6+), HTML5/CSS3, WCAG 2.1 AA"),
        ("AI, Spatial Computing & 3D: ", "Generative 3D Asset Creation, Mesh Synthesis, Automated Retopology, Tileable PBR Textures & Upscaling, Three.js, WebGL, 3ds Max, Blender"),
        ("Cloud, Backend & Offline: ", "Node.js, Express, Firebase / Google Cloud Platform (GCP), AWS, REST APIs, Micro-frontends, PWA (Offline-first / IndexedDB)"),
        ("Enterprise Security & Reliability: ", "Healthcare Security (MFA, RBAC, XSS Prevention), HIPAA/PHI Data Protection, Zero Memory-Leak Continuous Clinical Uptime"),
        ("Design Systems & UX Strategy: ", "Enterprise UI Design Systems, Design-to-Code Automation, Interactive Prototyping, Figma, Adobe XD, Photoshop, Human-Interface Design")
    ]
    for cat, items in skills:
        p_sk = doc.add_paragraph(style='List Bullet')
        p_sk.paragraph_format.space_before = Pt(1)
        p_sk.paragraph_format.space_after = Pt(2.5)
        p_sk.paragraph_format.line_spacing = 1.15
        r_c = p_sk.add_run(cat)
        r_c.bold = True
        r_c.font.name = "Segoe UI"
        r_c.font.size = Pt(9.3)
        r_c.font.color.rgb = RGBColor(15, 23, 42)
        r_i = p_sk.add_run(items)
        r_i.font.name = "Segoe UI"
        r_i.font.size = Pt(9.3)
        r_i.font.color.rgb = RGBColor(51, 65, 85)

    # 3. PROFESSIONAL EXPERIENCE
    add_heading_with_bottom_border(doc, "Professional Experience")

    # Helper for job role header
    def add_job_header(role, company, tenure, location_desc):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.keep_with_next = True
        r1 = p.add_run(f"{role}  |  ")
        r1.bold = True
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(10)
        r1.font.color.rgb = RGBColor(15, 23, 42)
        
        r2 = p.add_run(company)
        r2.bold = True
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(10)
        r2.font.color.rgb = RGBColor(2, 132, 199)
        
        r3 = p.add_run(f"  ({tenure})")
        r3.font.name = "Segoe UI"
        r3.font.size = Pt(9)
        r3.font.color.rgb = RGBColor(100, 116, 139)
        
        if location_desc:
            p_sub = doc.add_paragraph()
            p_sub.paragraph_format.space_before = Pt(0)
            p_sub.paragraph_format.space_after = Pt(3)
            p_sub.paragraph_format.keep_with_next = True
            r_sub = p_sub.add_run(location_desc)
            r_sub.font.name = "Segoe UI"
            r_sub.font.size = Pt(8.5)
            r_sub.italic = True
            r_sub.font.color.rgb = RGBColor(100, 116, 139)

    # eBodhya
    add_job_header("Fractional Chief Technology Officer (CTO)", "eBodhya Technologies Private Limited", "Sep 2026 – Present", "Bengaluru, India · Academic Intelligence Operating System & EdTech SaaS Platform")
    add_bullet_item(doc, "", "Drive technical leadership and architectural vision for an interconnected Academic Intelligence OS designed to streamline school operations, curriculum workflows, and assessment processes.")
    add_bullet_item(doc, "", "Architect curriculum-aware AI workflows and evaluation engines linking question banks, automated grading, and real-time student analytics into a unified source of truth.")
    add_bullet_item(doc, "", "Establish modular full-stack architecture, scalability guidelines, and automated deployment pipelines, empowering educators and accelerating product-market rollout.")

    # Technoyana
    add_job_header("Founder & Chief Technology Officer (CTO)", "Technoyana Digital Transformation Services Pvt. Ltd.", "May 2021 – Present", "Bengaluru, India · Enterprise Product Engineering, Spatial AI & High-Reliability SaaS Studio")
    add_bullet_item(doc, "", "Direct end-to-end technology vision, cloud architecture, and product engineering across Technoyana's incubator portfolio and enterprise consulting initiatives.")
    add_bullet_item(doc, "SrushtiLabs (Spatial AI & 3D Tech Division): ", "Architected VoxelForge AI (srushtilabs.com/voxelforge/), a generative 3D asset platform producing modular, low-poly 3D models and asset bundles optimized for real-time engines including Unreal Engine, Unity, and WebGL.", [
        ("Ayam3d (ayam3d.in): ", "Engineered parametric AI 3D mesh synthesis engine transforming natural language prompts into production 3D assets with automated retopology and tileable PBR texture pipelines; secured early investor validation.")
    ])
    add_bullet_item(doc, "Twitan (Sports SaaS Studio): ", "Architected Shutlify (Badminton OS - twitan.com), an end-to-end tournament management platform featuring automated knockout/round-robin fixture engines, live court arbitration, multi-court scheduling, and offline-first PWA resilience for venue Wi-Fi drops (deployed at tournaments like HBL Sirsi).", [
        ("Twicket: ", "Developed high-fidelity real-time scoring and match statistics engine for cricket tournaments.")
    ])
    add_bullet_item(doc, "Specialized Engineering Solutions: ", "Designed customized CNC machine controller interfaces and automated CAD/CAM toolpath pipelines; delivered architectural 3D simulations and consumer IoT parking payment applications.")

    # Cyient / Philips
    add_job_header("Senior Technical Lead (React / Node.js)", "Cyient Limited / Philips Healthcare", "Nov 2023 – Mar 2025", "Bengaluru, India · Philips IntelliSpace Critical Care & Anesthesia (ICCA) · Mission-Critical ICU Software")
    add_bullet_item(doc, "", "Led web-tier engineering and frontend architecture for Philips ICCA clinical software deployed in hospital ICUs and anesthesia departments globally.")
    add_bullet_item(doc, "", "Ensured 24/7 continuous clinical reliability with zero memory leaks and sub-second UI responsiveness under dense, real-time streaming patient telemetry.")
    add_bullet_item(doc, "", "Strictly enforced enterprise healthcare security policies including Multi-Factor Authentication (MFA), Cross-Site Scripting (XSS) prevention, granular Role-Based Access Control (RBAC), and strict patient data privacy compliance.")
    add_bullet_item(doc, "", "Governed code quality, architectural standards, automated regression testing, and modular micro-frontends across distributed agile squads.")

    # Ness Digital Engineering
    add_job_header("Development Lead / Senior Analyst", "Ness Digital Engineering", "Oct 2019 – Apr 2020", "Bengaluru, India · Entertainment Management Application (Angular / AWS / Node.js)")
    add_bullet_item(doc, "", "Architected the complete single-page application structure using Angular, TypeScript, Node.js, and AWS cloud infrastructure.")
    add_bullet_item(doc, "", "Enforced strict accessibility standards (WCAG 2.1 AA), frontend security best practices, and code quality linters across the engineering squad.")
    add_bullet_item(doc, "", "Took technical ownership of the CI/CD deployment pipelines, successfully delivering the application to client production on schedule.")

    # Moonraft
    add_job_header("User Interface Architect", "Moonraft Innovation Labs (Unit of UST Global)", "May 2019 – Jul 2019", "Bengaluru, India · Enterprise UI Design System & Mobile Engineering")
    add_bullet_item(doc, "", "Architected and engineered a centralized Cross-Framework UI Design System using LitElement (Web Components), React, and Angular, packaged and distributed via npm.")
    add_bullet_item(doc, "", "Completely eliminated component duplication across multiple engineering squads, ensuring seamless brand coherence and automated upgradability.")
    add_bullet_item(doc, "", "Led the mobile application development squad building a high-performance cross-platform guest booking app for TLC Group of Hotels using Ionic and Angular.")

    # UST Global / Cisco
    add_job_header("Associate Project Manager & Senior Systems Analyst", "UST Global / Cisco Systems", "Feb 2015 – Feb 2019", "Bengaluru, India & Global Deployment · Cisco Stadium Vision Director (4+ Years Dedicated Tenure)")
    add_bullet_item(doc, "", "Led the phased, zero-downtime legacy modernization of Cisco Stadium Vision Director from legacy Adobe Flash/Flex to modern Angular and React modules across premier international sporting stadiums.")
    add_bullet_item(doc, "", "Architected hybrid micro-frontend bridges allowing legacy and modern components to coexist, preventing any disruption to live stadium operations.")
    add_bullet_item(doc, "", "Managed cross-functional agile teams delivering single-page operational dashboards that substantially improved venue operational efficiency.")
    add_bullet_item(doc, "", "Awarded three consecutive UST Global Certificates of Excellence (2015, 2016, 2018) for client-first commitment and outstanding engineering delivery.")

    # ThoughtFocus
    add_job_header("UI Architect & Tech Lead", "ThoughtFocus Technologies", "Oct 2011 – Mar 2014", "Bengaluru, India · Aftermarket Parts 3D Explorer & Enterprise Solutions")
    add_bullet_item(doc, "", "Architected an enterprise Aftermarket Parts Explorer catalog supporting millions of industrial and automotive parts with high-speed search and filtering.")
    add_bullet_item(doc, "", "Engineered an interactive 3D inspection viewer enabling buyers to explore, rotate, and measure 3D models of components prior to purchasing.")
    add_bullet_item(doc, "", "Established rapid design-to-code prototyping pipelines; bootstrapped enterprise search systems and logistics management applications for a large milk/dairy corporation.")

    # Independent Consultant
    add_job_header("Independent Consultant (UX Designer & Full-Stack Developer)", "Cisco Systems & Vodafone", "Apr 2008 – Feb 2011", "Bengaluru, India · Building Management Systems (BMS) Unified Dashboard")
    add_bullet_item(doc, "", "Designed and developed the Cisco Campus Unified Facility Dashboard, integrating telemetry and control for AHUs, VRVs, industrial chillers, and campus environmental sensors.")
    add_bullet_item(doc, "", "Awarded formal Cisco Certificate of Appreciation (2010) for outstanding operational visualization and intelligent facility telemetry. Delivered real-time data visualization dashboards for Vodafone.")

    # Earlier Career Foundation
    add_job_header("Earlier Career & Foundational Experience", "InnoBrik, CAE, Cognizant", "2004 – 2015", "Bengaluru & Chennai, India · Product Advisory, Flight Simulators & Mainframe Systems")
    add_bullet_item(doc, "InnoBrik Software Technologies (Co-Founder & Technical Leader | Feb 2011 – Jan 2015): ", "Spearheaded product engineering, tech stack evaluation, and agile delivery across startup ventures and enterprise client engagements.")
    add_bullet_item(doc, "CAE Simulation Technologies (Visual Database Developer | Sep 2007 – Apr 2008): ", "Engineered high-fidelity 3D synthetic visual databases, topographical terrain models, and procedural runway textures for real-time military and civil flight simulators under locked 60 FPS budgets.")
    add_bullet_item(doc, "Cognizant Technology Solutions (Programmer Analyst Trainee | Apr 2004 – Dec 2004): ", "Maintained mission-critical mainframe applications, COBOL routines, and DB2 database queries for the DUNSLINK commercial credit platform.")

    # 4. EDUCATION & HONORS
    add_heading_with_bottom_border(doc, "Education & Honors")
    edu_table = doc.add_table(rows=1, cols=2)
    edu_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    edu_table.autofit = False
    for i, col in enumerate(edu_table.columns):
        col.width = Inches(3.6)
        for cell in col.cells:
            cell.width = Inches(3.6)
            
    c_edu, c_awd = edu_table.rows[0].cells[0], edu_table.rows[0].cells[1]
    set_cell_margins(c_edu, top=40, bottom=40, left=40, right=40)
    set_cell_margins(c_awd, top=40, bottom=40, left=40, right=40)
    
    # Edu
    p_e = c_edu.paragraphs[0]
    p_e.paragraph_format.space_before = Pt(0)
    p_e.paragraph_format.space_after = Pt(2)
    r1 = p_e.add_run("Master of Science (M.S.) in Computing\n")
    r1.bold = True
    r1.font.name = "Segoe UI"
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = RGBColor(15, 23, 42)
    r2 = p_e.add_run("Robert Gordon University, Scotland, UK (2005–2006)\nSpecialization: Human Interface Design & Development\n\n")
    r2.font.name = "Segoe UI"
    r2.font.size = Pt(8.5)
    r2.font.color.rgb = RGBColor(71, 85, 105)
    
    r3 = p_e.add_run("Bachelor of Engineering (B.E.) in ECE\n")
    r3.bold = True
    r3.font.name = "Segoe UI"
    r3.font.size = Pt(9.5)
    r3.font.color.rgb = RGBColor(15, 23, 42)
    r4 = p_e.add_run("Bapuji Institute of Engineering & Technology, Davanagere (1999–2003)\nElectronics & Communication Engineering")
    r4.font.name = "Segoe UI"
    r4.font.size = Pt(8.5)
    r4.font.color.rgb = RGBColor(71, 85, 105)

    # Awards
    p_a = c_awd.paragraphs[0]
    p_a.paragraph_format.space_before = Pt(0)
    p_a.paragraph_format.space_after = Pt(2)
    ra1 = p_a.add_run("Cisco Certificate of Appreciation (2010)\n")
    ra1.bold = True
    ra1.font.name = "Segoe UI"
    ra1.font.size = Pt(9.5)
    ra1.font.color.rgb = RGBColor(15, 23, 42)
    ra2 = p_a.add_run("Excellence in UX design and engineering for Cisco Campus Unified BMS Facility Dashboard.\n\n")
    ra2.font.name = "Segoe UI"
    ra2.font.size = Pt(8.5)
    ra2.font.color.rgb = RGBColor(71, 85, 105)
    
    ra3 = p_a.add_run("UST Global Certificates of Excellence (2015, 2016, 2018)\n")
    ra3.bold = True
    ra3.font.name = "Segoe UI"
    ra3.font.size = Pt(9.5)
    ra3.font.color.rgb = RGBColor(15, 23, 42)
    ra4 = p_a.add_run("Triple recognition for technical leadership, zero-downtime migration, and delivery on Cisco Stadium Vision.")
    ra4.font.name = "Segoe UI"
    ra4.font.size = Pt(8.5)
    ra4.font.color.rgb = RGBColor(71, 85, 105)

    try:
        doc.save(DOCX_PATH)
        print(f"[OK] Generated DOCX ({os.path.getsize(DOCX_PATH)} bytes) at: {DOCX_PATH}")
    except PermissionError:
        fallback_path = os.path.join(script_dir, "CV_maheshchandra_hegde_updated.docx")
        doc.save(fallback_path)
        print(f"[NOTE] '{DOCX_PATH}' is currently open in Microsoft Word. Saved updated file to: {fallback_path}")


def main():
    print("=" * 60)
    print("  MAHESHCHANDRA HEGDE - RESUME BUILD PIPELINE")
    print("  Formats: HTML -> Vector PDF, Native Microsoft Word (.docx)")
    print("=" * 60)
    
    generate_html_and_pdf()
    generate_docx()
    
    print("\nGeneration completed successfully!")

if __name__ == "__main__":
    main()
