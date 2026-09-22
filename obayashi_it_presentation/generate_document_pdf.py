"""
Script to generate a beautifully styled Executive PDF Document from WORK_EXPERIENCE_DOCUMENT.md
Uses Headless Microsoft Edge / Google Chrome built into Windows.
Authentic Profile: Maheshchandra Hegde (16+ Years Experience, Architectural Heritage, 50+ 3D Projects)
"""

import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Maheshchandra Hegde - Technical Work Experience & Capability Document</title>
<style>
  @page {
    size: A4 portrait;
    margin: 16mm 14mm 16mm 14mm;
    @bottom-right {
      content: counter(page);
    }
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    line-height: 1.5;
    font-size: 10pt;
    margin: 0;
    padding: 0;
  }
  .header-container {
    border-bottom: 3px solid #0284c7;
    padding-bottom: 12px;
    margin-bottom: 16px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .doc-title {
    font-size: 18pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 2px 0;
  }
  .doc-subtitle {
    font-size: 11pt;
    font-weight: 600;
    color: #0284c7;
  }
  .candidate-meta {
    text-align: right;
    font-size: 9pt;
    color: #475569;
    line-height: 1.35;
  }
  .candidate-meta strong {
    color: #0f172a;
    font-size: 10pt;
  }
  .candidate-meta a {
    color: #0284c7;
    text-decoration: none;
  }
  h2 {
    color: #0f172a;
    font-size: 12pt;
    border-left: 4px solid #0284c7;
    padding-left: 8px;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }
  h3 {
    color: #0e7490;
    font-size: 10.5pt;
    margin-top: 12px;
    margin-bottom: 5px;
    page-break-after: avoid;
  }
  p {
    margin: 5px 0;
    text-align: justify;
  }
  ul {
    margin: 5px 0 8px 18px;
    padding: 0;
  }
  li {
    margin-bottom: 3px;
  }
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 10px 0;
  }
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px 12px;
    page-break-inside: avoid;
  }
  .card h4 {
    margin: 0 0 5px 0;
    color: #0284c7;
    font-size: 10pt;
  }
  .card p {
    margin: 0;
    font-size: 9pt;
    color: #334155;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 9pt;
    page-break-inside: avoid;
  }
  th {
    background: #0f172a;
    color: #ffffff;
    font-weight: 700;
    padding: 7px 9px;
    text-align: left;
    border: 1px solid #0f172a;
  }
  td {
    padding: 6px 9px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
  }
  tr:nth-child(even) {
    background: #f8fafc;
  }
  .stat-badge {
    font-weight: 800;
    color: #0284c7;
    font-size: 10pt;
    white-space: nowrap;
  }
  .callout {
    background: #f0f9ff;
    border-left: 4px solid #0284c7;
    padding: 9px 12px;
    border-radius: 0 6px 6px 0;
    margin: 10px 0;
    font-size: 9pt;
  }
  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<div class="header-container">
  <div>
    <div class="doc-title">Maheshchandra Hegde</div>
    <div class="doc-subtitle">Product Design Expert | UX Architect | Creative Technologist</div>
  </div>
  <div class="candidate-meta">
    Bangalore, India &nbsp;|&nbsp; +91 9535253329 / 7022407280<br>
    hid.mahesh@gmail.com &nbsp;|&nbsp; <a href="https://hegdemahesh.in">hegdemahesh.in</a> &nbsp;|&nbsp; <a href="https://www.linkedin.com/in/maheshchandrahegde/">LinkedIn</a><br>
    Submission Recipient: talent@obayashi.org
  </div>
</div>

<div class="callout">
  <strong>Architectural Heritage & Career Profile:</strong> Versatile Developer, Designer, and Architect with <strong>16+ years of core technology experience</strong> delivering scalable frontend systems, immersive UX, and operational digital products. <em>Because my father is an architect</em>, helping him in his studio gave me early foundational skills in architectural drawings, CAD drafting, and 3D visualization. Combined with a B.E. in Electronics & Communication and an M.S. in Computing from the UK (specializing in Human Interface Design), this background blends engineering precision with intuitive design and spatial technology.
</div>

<div class="grid-2">
  <div class="card">
    <h4>Scalable Enterprise Frontend Systems</h4>
    <p>Senior Technical Lead on Philips Intellispace Critical Care & Anesthesia (Cyient); architected high-performance React modules for 24/7 ICU patient vitals and clinical alarms.</p>
  </div>
  <div class="card">
    <h4>Startup Ventures & Operational Reliability</h4>
    <p>Co-Founder at Technoyana (technoyana.in) and Founder at Twitan.com; architected offline-first PWA architectures ensuring zero data loss during physical venue network drops.</p>
  </div>
  <div class="card">
    <h4>Spatial AI & Generative 3D Pipelines</h4>
    <p>Founder at SrushtiLabs developing <strong>Voxelforge AI</strong> (srushtilabs.com/voxelforge/) for generative low-poly 3D assets, alongside <strong>ayam3d</strong> for automated mesh retopology.</p>
  </div>
  <div class="card">
    <h4>3D Visualizer Expert & Industry Recognition</h4>
    <p>Delivered 50+ 3D/CAD projects (architectural walkthroughs, CAE flight simulator 3D terrain databases, and Cisco Systems campus Facility Dashboard awarded appreciation).</p>
  </div>
</div>

<h2>1. Project Overview & Objectives</h2>

<h3>Project 1: Philips Intellispace Critical Care & Anesthesia (Cyient Limited)</h3>
<p><strong>Role & Tenure:</strong> Senior Technical Lead (React / NodeJS) | Nov 2023 – Mar 2025<br>
<strong>Scope & Operational Context:</strong> Clinical decision support and bedside monitoring platform deployed in 24/7 ICU environments worldwide.<br>
<strong>Core Objectives:</strong></p>
<ul>
  <li><strong>Life-Critical Reliability:</strong> Deliver rock-solid frontend performance with zero UI freezes or dropped vitals during continuous multi-day bedside monitoring.</li>
  <li><strong>Modular Architecture:</strong> Deconstruct complex monolithic interfaces into reusable, decoupled React modules, eliminating regression risks across teams.</li>
  <li><strong>Healthcare Compliance:</strong> Enforce strict adherence to healthcare data privacy, clinician RBAC, and clinical audit trail requirements.</li>
</ul>

<h3>Project 2: Startup Ventures — Technoyana & Twitan.com</h3>
<p><strong>Role & Tenure:</strong> Founder & Product Lead, Twitan.com (Apr 2025 – Present) | Co-Founder & Director, Technoyana.in (May 2021 – Oct 2023)<br>
<strong>Scope:</strong> High-reliability sports tournament management platform (Shutlify badminton OS) and commercial fintech/enterprise web/mobile applications.<br>
<strong>Core Objectives:</strong></p>
<ul>
  <li><strong>Offline-First Field Resilience:</strong> Engineer an architecture capable of running fully offline on local devices during network drops at physical venues, with automatic conflict-free cloud sync upon reconnection.</li>
  <li><strong>Scalable Cloud Architecture:</strong> Architect GCP/Firebase and Node.js microservices handling heavy live tournament traffic spikes while maintaining lean operating costs.</li>
</ul>

<h3>Project 3: Spatial AI & Generative 3D (SrushtiLabs — Voxelforge AI & ayam3d)</h3>
<p><strong>Role & Tenure:</strong> Founder & Lead Spatial Architect | Apr 2025 – Present<br>
<strong>Platforms:</strong></p>
<ul>
  <li><strong>Voxelforge AI (<a href="https://srushtilabs.com/voxelforge/">srushtilabs.com/voxelforge/</a>):</strong> AI-assisted generative 3D asset pipeline producing game-ready, low-poly modular 3D models for Unreal Engine, Unity, and real-time WebGL. Automates prompt-to-3D synthesis and texture baking.</li>
  <li><strong>ayam3d:</strong> Advanced spatial computing R&D in automated 3D mesh synthesis, intelligent retopology, and PBR texturing, transforming heavy 3D scans into lightweight web assets.</li>
</ul>

<h3>Project 4: 3D Visualizer Expert Track Record (50+ Projects Delivered)</h3>
<ul>
  <li><strong>Architectural Visualization & 3D Walkthroughs (35+ Projects):</strong> Assisting my architect father built my expertise in translating 2D CAD floor plans, elevations, and structural blueprints into photorealistic 3D renderings and animated walkthroughs for real estate developers and commercial builders.</li>
  <li><strong>CAE Simulation Technologies (Visual Database Developer | Sep 2007 – Apr 2008):</strong> Created high-fidelity 3D model libraries and elevation terrain databases for military and civil aircraft flight simulators under strict locked-60 FPS budgets.</li>
  <li><strong>Cisco Systems Facility Dashboard (2009 – 2010):</strong> Designed and developed the interactive campus Facility Dashboard at Cisco Bangalore, visualizing physical data centers, rack layouts, and environmental telemetry. Formally appreciated by Cisco leadership in 2010.</li>
</ul>

<div class="page-break"></div>

<h2>2. Core Responsibilities & Technical Leadership</h2>

<div class="grid-2">
  <div class="card">
    <h4>Scalable Architecture & System Design</h4>
    <ul>
      <li>Architected enterprise frontend applications using React, Angular, and LitElement Web Components.</li>
      <li>Designed cross-platform UI Design Systems adopted across multiple engineering teams (Moonraft / TLC Hotels).</li>
      <li>Defined clear API contracts (REST, WebSockets, streaming state) to decouple client presentation from backend microservices.</li>
    </ul>
  </div>
  <div class="card">
    <h4>Operational Reliability & Edge Resilience</h4>
    <ul>
      <li>Designed offline-first state architectures using IndexedDB and Service Workers to ensure zero work loss in environments with unstable internet.</li>
      <li>Engineered high-performance clinical UI rendering with zero memory leaks for long-running hospital bedside systems (Philips ICCA).</li>
      <li>Supervised cloud deployments on GCP, Firebase, and AWS with automated scaling and log monitoring.</li>
    </ul>
  </div>
  <div class="card">
    <h4>Spatial 3D & Generative AI Engineering</h4>
    <ul>
      <li>Developed generative 3D asset pipelines (Voxelforge AI) and automated mesh retopology algorithms (ayam3d).</li>
      <li>Bridged CAD drawings, 3D coordinate geometry, polygon reduction, and WebGL rendering for real-time digital twins.</li>
      <li>Ensured 3D assets stream smoothly in standard web browsers without saturating client memory or network bandwidth.</li>
    </ul>
  </div>
  <div class="card">
    <h4>Agile Team Leadership & Mentorship</h4>
    <ul>
      <li>Led, mentored, and guided cross-functional squads of frontend developers, UX designers, and QA engineers.</li>
      <li>Instituted design-to-code pipelines involving users early through rapid prototypes and usability validation.</li>
      <li>Managed sprint planning, technical backlogs, stakeholder demos, and engineering delivery velocity.</li>
    </ul>
  </div>
</div>

<h2>3. Major Achievements, Milestones & Awards</h2>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Metric / Milestone</th>
      <th style="width: 18%;">Result / Honor</th>
      <th style="width: 57%;">Context & Practical Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Track Record</strong></td>
      <td><span class="stat-badge">16+ Years</span></td>
      <td>Proven experience across enterprise leaders (Cyient, UST Global, Ness, Cognizant) and high-impact startups (Technoyana, Twitan, SrushtiLabs).</td>
    </tr>
    <tr>
      <td><strong>3D & Spatial Projects</strong></td>
      <td><span class="stat-badge">50+ Projects</span></td>
      <td>Delivered across architectural visualization, CAD drafting, flight simulation visual databases, and AI-driven generative 3D pipelines.</td>
    </tr>
    <tr>
      <td><strong>Clinical UI Performance</strong></td>
      <td><span class="stat-badge">60 FPS / Flat Memory</span></td>
      <td>Shipped React clinical modules for Philips Healthcare (ICCA) maintaining stable memory and frame rates across multi-day continuous ICU sessions.</td>
    </tr>
    <tr>
      <td><strong>Edge Data Integrity</strong></td>
      <td><span class="stat-badge">100% Offline</span></td>
      <td>Zero data loss recorded during physical venue network drops via offline-first IndexedDB state engine and transactional replay queue.</td>
    </tr>
    <tr>
      <td><strong>3D Optimization</strong></td>
      <td><span class="stat-badge">Up to 75% Saved</span></td>
      <td>Slashed 3D asset payload sizes using automated retopology and LOD hierarchies, enabling instant in-browser WebGL rendering.</td>
    </tr>
    <tr>
      <td><strong>Cisco Appreciation Award</strong></td>
      <td><span class="stat-badge">Formal Award (2010)</span></td>
      <td>Received formal Certificate of Appreciation from Cisco Systems for developing the interactive campus Facility Dashboard.</td>
    </tr>
    <tr>
      <td><strong>UST Global Awards</strong></td>
      <td><span class="stat-badge">3 Corporate Awards</span></td>
      <td>Recognized with "Inspiring People" (2018), "Putting Client First" (2016), and "Living the Values" (2015) for outstanding project delivery.</td>
    </tr>
  </tbody>
</table>

<h2>4. Challenges Faced & Resolutions Implemented</h2>

<div class="card" style="margin-bottom: 10px;">
  <h4>Challenge 1: Unstable Network Connectivity in Physical Operational Venues (Twitan / Technoyana)</h4>
  <p><strong>Context:</strong> Operating live match arbitration and scoring at sports arenas often involves crowded RF spectrum, dead zones, and dropped Wi-Fi, risking broken submissions and lost data.<br>
  <strong>Resolution:</strong> Re-architected data persistence to an <strong>Offline-First model</strong> using client-side IndexedDB and Service Workers. Implemented an optimistic UI pattern with an automated transactional replay queue that automatically resynchronizes once connectivity is restored.<br>
  <strong>Impact:</strong> 100% data preservation, zero operator workflow interruptions, seamless user experience.</p>
</div>

<div class="card" style="margin-bottom: 10px;">
  <h4>Challenge 2: Life-Critical Performance & Memory Leak Prevention in 24/7 Clinical Monitoring (Philips ICCA)</h4>
  <p><strong>Context:</strong> ICU bedside monitors run uninterrupted for weeks. Rapidly incoming telemetry streams and continuous DOM updates risked browser memory accumulation and UI sluggishness during critical medical alerts.<br>
  <strong>Resolution:</strong> Enforced strict immutable state updates, decoupled rendering loops from data ingestion, implemented virtualized list rendering, and utilized Chrome DevTools heap profiling to systematically eliminate closure leaks.<br>
  <strong>Impact:</strong> Guaranteed stable 60 FPS UI rendering and flat memory profiles across multi-day continuous ICU sessions, fully complying with healthcare software safety benchmarks.</p>
</div>

<div class="card" style="margin-bottom: 10px;">
  <h4>Challenge 3: Heavy 3D Asset Payload & Browser Lag in Web 3D (SrushtiLabs / Voxelforge AI)</h4>
  <p><strong>Context:</strong> Delivering rich 3D models over the web created large file download sizes, long initialization times, and frame drops on lower-spec client laptops and mobile tablets.<br>
  <strong>Resolution:</strong> Developed automated retopology workflows (ayam3d) to decimate unnecessary polygons while preserving silhouette geometry; baked normal maps and bundled assets into lightweight modular formats for WebGL.<br>
  <strong>Impact:</strong> Reduced 3D model payload sizes by up to 75%, enabling instant in-browser loading and smooth real-time manipulation.</p>
</div>

<div class="page-break"></div>

<h2>5. Lessons Learned & Engineering Best Practices</h2>
<ul>
  <li><strong>Involve Users Early Through Rapid Prototypes:</strong> Building early interactive prototypes with real users uncovers fundamental workflow flaws before expensive engineering code is written. Prototyping early prevents technical debt and aligns developers with real human needs.</li>
  <li><strong>Design for Real-World Edge Conditions, Not Ideal Lab Environments:</strong> Software rarely operates in perfect network and hardware conditions. Building applications with offline caching, graceful degradation, and asynchronous retry logic ensures systems remain reliable whether in a hospital ICU, sports arena, or remote field office.</li>
  <li><strong>Standardize Design Systems & Component Libraries:</strong> Re-inventing UI components across teams leads to inconsistent user experiences and bloated maintenance. Investing upfront in unified, framework-agnostic design systems (as demonstrated at Moonraft with LitElement) dramatically accelerates organizational delivery speed.</li>
  <li><strong>Ground Technology Decisions in Practical Value:</strong> Technology is a vehicle for solving human problems. Whether building spatial AI tools (Voxelforge AI), sports arbitration engines (Twitan), or ICU monitoring (Philips), the ultimate metric of success is operational simplicity, reliability, and tangible value to the user.</li>
</ul>

<h2>6. Suggestions for Future Process Improvements</h2>
<div class="grid-2">
  <div class="card">
    <h4>1. Unified 3D Spatial & Web Integration</h4>
    <p>Bridge complex 3D CAD, architectural models, and spatial data into lightweight, interactive web formats using progressive Level of Detail (LOD) hierarchies and automated retopology (leveraging principles from Voxelforge AI and ayam3d), enabling smooth browser inspection on standard tablets without dedicated GPU hardware.</p>
  </div>
  <div class="card">
    <h4>2. Resilient Edge-First Mobile Workflows</h4>
    <p>Standardize offline-first client persistence and background transactional queuing across all field-facing mobile applications, eliminating data loss caused by remote connectivity dropouts.</p>
  </div>
  <div class="card">
    <h4>3. Enterprise Design Systems & Reusable Standards</h4>
    <p>Establish centralized, cross-platform component libraries and design tokens to streamline multi-team digital product delivery, enforce visual consistency, and eliminate duplicated engineering effort.</p>
  </div>
  <div class="card">
    <h4>4. AI-Assisted Prototyping & Development</h4>
    <p>Incorporate generative AI and automation tools into early product discovery and asset creation pipelines, cutting design-to-code iteration cycles by 40%.</p>
  </div>
</div>

<p style="text-align: center; margin-top: 24px; font-weight: 600; color: #0284c7;">
  Maheshchandra Hegde &nbsp;|&nbsp; Bangalore, India &nbsp;|&nbsp; hid.mahesh@gmail.com &nbsp;|&nbsp; +91 9535253329 / 7022407280 &nbsp;|&nbsp; hegdemahesh.in
</p>

</body>
</html>
"""

def generate_pdf():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(script_dir, "WORK_EXPERIENCE_DOCUMENT.html")
    pdf_file = os.path.join(script_dir, "Obayashi_Senior_Manager_IT_Work_Experience_Document_Maheshchandra_Hegde.pdf")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated HTML template at: {html_file}")

    browser_exe = None
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    for c in candidates:
        if os.path.exists(c):
            browser_exe = c
            break

    if not browser_exe:
        print("No headless browser found to convert HTML to PDF.")
        return

    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]
    print(f"Running command: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
        print(f"SUCCESS: Generated Authentic Executive Document PDF at: {pdf_file} (Size: {os.path.getsize(pdf_file)} bytes)")
    else:
        print("Failed to generate PDF. Subprocess output:", res.stderr)

if __name__ == "__main__":
    generate_pdf()
