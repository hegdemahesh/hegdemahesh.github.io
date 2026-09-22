"""
Script to generate a beautifully styled Executive PDF Document from WORK_EXPERIENCE_DOCUMENT.md
Uses Headless Microsoft Edge / Google Chrome built into Windows.
Covers:
1. Introduction & Executive Profile (with Photo)
2. Project / Experience Skillset (Client Groups 1 to 8)
3. Conclusion: Role Fit & Self-Training / Certification Pledge
"""

import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
photo_rel_url = "maheshForResume.jpg"

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Maheshchandra Hegde - Technical Work Experience & Capability Document</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 15mm 14mm 15mm 14mm;
    @bottom-right {{
      content: counter(page);
    }}
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    line-height: 1.48;
    font-size: 9.5pt;
    margin: 0;
    padding: 0;
  }}
  .header-card {{
    background: #0f172a;
    color: #ffffff;
    border-radius: 6px;
    padding: 14px 16px;
    margin-bottom: 16px;
    display: flex;
    gap: 16px;
    align-items: center;
  }}
  .photo-box {{
    width: 105px;
    height: 135px;
    border-radius: 4px;
    overflow: hidden;
    flex-shrink: 0;
    border: 2px solid #38bdf8;
  }}
  .photo-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .header-info {{
    flex-grow: 1;
  }}
  .header-info h1 {{
    font-size: 18pt;
    font-weight: 800;
    margin: 0 0 3px 0;
    color: #ffffff;
  }}
  .header-headline {{
    font-size: 10pt;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 6px;
  }}
  .header-meta {{
    font-size: 8.5pt;
    color: #cbd5e1;
    line-height: 1.4;
  }}
  .header-meta a {{
    color: #38bdf8;
    text-decoration: none;
  }}
  h2 {{
    color: #0f172a;
    font-size: 11.5pt;
    border-left: 4px solid #0284c7;
    padding-left: 8px;
    margin-top: 16px;
    margin-bottom: 8px;
    page-break-after: avoid;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  h3 {{
    color: #0e7490;
    font-size: 10pt;
    margin-top: 10px;
    margin-bottom: 4px;
    page-break-after: avoid;
    font-weight: 700;
  }}
  p {{
    margin: 4px 0;
    text-align: justify;
  }}
  ul {{
    margin: 4px 0 8px 16px;
    padding: 0;
  }}
  li {{
    margin-bottom: 3px;
  }}
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: 8px 0;
  }}
  .card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 9px 11px;
    page-break-inside: avoid;
  }}
  .card h4 {{
    margin: 0 0 4px 0;
    color: #0284c7;
    font-size: 9.5pt;
  }}
  .card p {{
    margin: 0;
    font-size: 8.5pt;
    color: #334155;
  }}
  .callout {{
    background: #f0f9ff;
    border-left: 4px solid #0284c7;
    padding: 8px 12px;
    border-radius: 0 5px 5px 0;
    margin: 8px 0;
    font-size: 8.8pt;
  }}
  .pledge-box {{
    background: #0f172a;
    color: #ffffff;
    border-radius: 6px;
    padding: 12px 14px;
    margin-top: 12px;
    page-break-inside: avoid;
  }}
  .pledge-box h3 {{
    color: #38bdf8;
    margin: 0 0 6px 0;
    font-size: 10.5pt;
    border-bottom: 1px solid #334155;
    padding-bottom: 4px;
  }}
  .pledge-box p {{
    color: #e2e8f0;
    font-size: 8.8pt;
    margin: 4px 0;
  }}
  .page-break {{
    page-break-before: always;
  }}
</style>
</head>
<body>

<div class="header-card">
  <div class="photo-box">
    <img src="{photo_rel_url}" alt="Maheshchandra Hegde">
  </div>
  <div class="header-info">
    <h1>Maheshchandra Hegde</h1>
    <div class="header-headline">Founder & Technology Leader at Technoayan Digital Transformation Services Pvt. Ltd. | Building AI‑driven 3D asset platforms and 3d computing solutions @srushtilabs.com</div>
    <div class="header-meta">
      <strong>Bangalore, India</strong> &nbsp;|&nbsp; +91 9535253329 / 7022407280 &nbsp;|&nbsp; hid.mahesh@gmail.com<br>
      Website: <a href="https://hegdemahesh.in">hegdemahesh.in</a> &nbsp;|&nbsp; LinkedIn: <a href="https://www.linkedin.com/in/maheshchandrahegde/">linkedin.com/in/maheshchandrahegde</a>
    </div>
  </div>
</div>

<div class="callout">
  <strong>Executive Introduction:</strong> Innovative technologist and product strategist with <strong>18+ years of experience</strong> architecting end-to-end digital products, interactive 3D experiences, and domain-specific SaaS platforms. Co-Founder and Technology Leader at <strong>Technoyana Digital Transformation Services Pvt. Ltd.</strong>, driving product architecture, cloud scalability, and creative technical vision across modern web/mobile application stacks, interactive 3D/PBR pipelines, real-time spatial computing, and design-to-code automation across both high-velocity startups and mission-critical enterprise systems.
</div>

<h2>Project Experience & Technical Track Record</h2>

<h3>1. Projects Executed as Founder at Technoyana Digital Transformation Services Pvt. Ltd.</h3>
<div class="grid-2">
  <div class="card">
    <h4>Voxelforge AI (srushtilabs.com/voxelforge/)</h4>
    <p>Developed Voxelforge AI, a generative AI platform creating modular 3D assets from user prompt inputs. Generates game-ready, low-poly modular 3D models and asset bundles optimized for immediate assembly in Unreal Engine, Unity, and real-time WebGL engines, cutting prototyping turnaround from days to minutes.</p>
  </div>
  <div class="card">
    <h4>Ayam3d (ayam3d.in)</h4>
    <p>Extended the Voxelforge concept into Ayam3d ('Ayam' meaning Dimension), generating parametric-based 3D models from natural language prompts in seconds using custom trained AI models. Received early investor interest; actively developing and seeking strategic partners to scale the AI pipeline.</p>
  </div>
</div>

<h3>2. Projects Executed at Cyient Limited / PHILIPS Healthcare</h3>
<div class="card">
  <h4>Philips Intellispace Critical Care & Anesthesia (ICCA)</h4>
  <p>Served as Senior Technology Leader (React / NodeJS) delivering hospital ICU software products. Challenging 24/7 mission-critical healthcare environment passing stringent quality and safety benchmarks set by Philips and hospital networks. Security of the application was critical: strictly enforced Multi-Factor Authentication (MFA), Cross-Site Scripting (XSS) prevention, role-based access control (RBAC), and patient data protection. Delivered end-to-end best practices, modular architecture, and production services.</p>
</div>

<div class="page-break"></div>

<h3>3. Projects Executed at Ness Digital Engineering</h3>
<div class="card">
  <h4>Entertainment Management Application</h4>
  <p>As Senior Analyst / Tech Lead, led a development squad to build an Entertainment Management Application using Angular, TypeScript, Node.js, and AWS. Architected the complete single-page application structure, enforced accessibility standards (WCAG) and code quality linters, and took technical leadership in deploying and delivering the application to the client on schedule.</p>
</div>

<h3>4. Projects Executed at Moonraft Innovation Labs (Unit of UST Global)</h3>
<div class="grid-2">
  <div class="card">
    <h4>Enterprise Cross-Framework UI Design System</h4>
    <p>Built, architected, and engineered a centralized design system using LitElement Web Components, React, AngularJS, Node.js, and npm packaging. Stored all standardized UI components in a central repository, eliminating reinventing the wheel across client projects and guaranteeing brand coherence from a single codebase.</p>
  </div>
  <div class="card">
    <h4>Luxury Hotel Group Mobile Application</h4>
    <p>Led mobile engineering team to develop a cross-platform mobile booking application for a premier Indian hotel group (TLC Group of Hotels) built using Ionic and Angular, delivering high performance and polished guest experiences.</p>
  </div>
</div>

<h3>5. Projects Executed at UST Global / CISCO</h3>
<div class="card">
  <h4>Cisco Stadium Vision Director Platform Modernization</h4>
  <p>Senior Systems Analyst and Associate Project Manager for 4+ years on Cisco Stadium Vision Director—an enterprise digital media distribution platform deployed in major international stadiums. Took technical leadership in systematically migrating the legacy Flash and Flex platform to modern Angular and React modules step by step. Comprised numerous sub-applications with active global clients; successfully executed the migration without disrupting live stadium operations. Recognized with multiple UST Global Excellence Awards.</p>
</div>

<h3>6. Projects Executed at ThoughtFocus Technologies</h3>
<div class="grid-2">
  <div class="card">
    <h4>Aftermarket Parts Explorer Application</h4>
    <p>UI Architect and Tech Lead for an enterprise aftermarket parts procurement platform supporting millions of parts from diverse manufacturers. Built an interactive 3D viewer allowing buyers to inspect 3D models and dimensions of thousands of components, integrated with cart and payment gateways (Adobe Flex, Mate, ActionScript, HTML).</p>
  </div>
  <div class="card">
    <h4>Enterprise UI Solutions & Bootstrapping</h4>
    <p>Established early user prototyping pipelines. Guided team to bootstrap high-speed enterprise search applications and an operational logistics management application for a large milk/dairy corporation (HTML, CSS, JavaScript, TypeScript, Flex).</p>
  </div>
</div>

<h3>7. Facility Dashboard Development at CISCO & Vodafone (Independent Consultant)</h3>
<div class="card">
  <h4>Unified Building Management Systems (BMS) Dashboard</h4>
  <p>Designed and developed an interactive facility dashboard at Cisco Systems campus as a full-time consultant (2009–2010). Developed a unified web interface connecting to and controlling diverse Building Management Systems: Air Handling Units (AHUs), Variable Refrigerant Volume (VRVs), industrial chillers, and environmental sensor telemetry. Awarded formal Certificate of Appreciation from Cisco in 2010. Also delivered data visualization dashboards for Vodafone operations.</p>
</div>

<h3>8. CAE Simulation Technologies (Canadian Aeronautical Engineering)</h3>
<div class="card">
  <h4>Flight Simulator Visual Database Development</h4>
  <p>Worked as a Visual Database Developer (Sep 2007 – Apr 2008) at CAE, the global leader in civil and military aircraft flight simulators. Purely visual and structural design work where visual, topographical, and structural details were modeled and fed into databases used by real-time flight simulators. Created high-fidelity 3D synthetic environments (runways, airports, terrain) using 3D modeling packages, Adobe Photoshop for procedural texture generation, and strict Level of Detail (LOD) hierarchies under locked 60 FPS simulator budgets.</p>
</div>

<h3>9. Other Specialized Engineering Projects (Technoyana Digital)</h3>
<div class="card">
  <p>Apart from traditional software development, led and delivered diverse multi-disciplinary projects: architectural 3D visualization and animated walkthroughs; customized CNC machine development and automated CAD/CAM toolpath pipelines; built consumer mobile application <em>SellAny</em>; and led development of an automated parking payment mobile application with real-time slot occupancy tracking.</p>
</div>

<h2>Major Achievements & Milestones</h2>
<div class="grid-2">
  <div class="card">
    <h4>1. Zero-Downtime Global Stadium Platform Migration</h4>
    <p>Modernized Cisco Stadium Vision Director deployed at international sporting arenas across a 4-year tenure. Led phased migration from Adobe Flash/Flex to Angular/React without a single minute of venue downtime. Awarded 3 UST Global Excellence Awards (2015, 2016, 2018).</p>
  </div>
  <div class="card">
    <h4>2. Healthcare-Grade ICU Software Delivery (Philips)</h4>
    <p>Delivered web-tier clinical software for Philips ICCA in 24/7 ICU suites. Passed stringent hospital quality, safety, and zero-leak reliability benchmarks for bedside patient monitoring. Enforced MFA, RBAC, and strict medical data protection.</p>
  </div>
  <div class="card">
    <h4>3. Generative 3D Asset & Spatial AI (SrushtiLabs)</h4>
    <p>Founded and launched Voxelforge AI (srushtilabs.com/voxelforge/) creating modular, game-ready 3D bundles for Unreal Engine, Unity, and WebGL. Developed Ayam3d (ayam3d.in) for parametric 3D model generation, earning early investor interest.</p>
  </div>
  <div class="card">
    <h4>4. Enterprise UI Design System & Cisco BMS Telemetry</h4>
    <p>Architected centralized Web Components design system (LitElement, React, Angular) at Moonraft / UST, eliminating duplicated UI effort across teams. Designed unified Cisco facility telemetry dashboard; awarded formal Cisco Certificate of Appreciation (2010).</p>
  </div>
</div>

<h2>Challenges Faced & Resolutions Implemented</h2>
<div class="grid-2">
  <div class="card">
    <h4>Legacy Codebase Modernization (Cisco)</h4>
    <p><strong>Challenge:</strong> Adobe Flash/Flex deprecation required migrating complex global stadium platform without venue downtime.<br>
    <strong>Resolution:</strong> Built hybrid micro-frontend event bridge allowing legacy and modern React/Angular modules to coexist and migrate incrementally.</p>
  </div>
  <div class="card">
    <h4>Continuous Bedside Reliability (Philips ICU)</h4>
    <p><strong>Challenge:</strong> 24/7 multi-day operation without browser memory leaks or UI freezes under dense patient telemetry.<br>
    <strong>Resolution:</strong> Enforced rigorous memory profiling, deterministic component cleanup on unmount, and automated regression test gates.</p>
  </div>
  <div class="card">
    <h4>Fragmented UI Development (Moonraft)</h4>
    <p><strong>Challenge:</strong> Multiple squads independently building identical UI widgets across React and Angular, causing brand drift.<br>
    <strong>Resolution:</strong> Architected centralized LitElement design system packaged via npm, standardizing components across all teams.</p>
  </div>
  <div class="card">
    <h4>Generative 3D Mesh Topology (SrushtiLabs)</h4>
    <p><strong>Challenge:</strong> Raw AI 3D meshes produced chaotic vertex topology and high polycounts unsuited for real-time rendering.<br>
    <strong>Resolution:</strong> Built automated retopology, polygon reduction, UV unwrapping, and texture baking pipeline for lightweight game-ready assets.</p>
  </div>
</div>

<div class="page-break"></div>

<h2>Lessons Learned & Best Practices</h2>
<div class="grid-2">
  <div class="card">
    <h4>Incremental Modernization Over Rewrites</h4>
    <p>Complete rewrites carry high operational risk and delayed value. Strangler-fig micro-frontends and backward-compatible APIs enable continuous delivery with zero downtime.</p>
  </div>
  <div class="card">
    <h4>Security & Compliance from Day Zero</h4>
    <p>Retrofitting security late causes friction and vulnerabilities. Embed MFA, RBAC, automated vulnerability scanning, and audit logging into the CI/CD pipeline from inception.</p>
  </div>
  <div class="card">
    <h4>Design Systems as Strategic Products</h4>
    <p>Treat shared UI libraries as internal products with semantic versioning and framework-agnostic standards to compound ROI and brand consistency across squads.</p>
  </div>
  <div class="card">
    <h4>Interactive Prototyping Resolves Ambiguity</h4>
    <p>Early functional mockups and clickable UI prototypes validate operational workflows with users and leadership, preventing costly changes post-deployment.</p>
  </div>
</div>

<h2>Suggestions for Future Process Improvements</h2>
<div class="grid-2">
  <div class="card">
    <h4>Automated IT Governance & Self-Service IDPs</h4>
    <p>Establish standardized developer platforms and Infrastructure-as-Code (IaC) templates, cutting environment provisioning time from weeks to hours with built-in security baselines.</p>
  </div>
  <div class="card">
    <h4>AI-Assisted Engineering Toolchains</h4>
    <p>Integrate generative AI tooling for automated test generation, synthetic data simulation, and design-to-code pipelines, boosting engineering throughput by 30–40%.</p>
  </div>
  <div class="card">
    <h4>Unified Enterprise Telemetry & APM</h4>
    <p>Combine application monitoring, network metrics, and facility sensor data (BMS) into unified dashboards to transition IT operations from reactive fix to predictive observability.</p>
  </div>
  <div class="card">
    <h4>Structured Upskilling & Certification</h4>
    <p>Institute regular cross-functional architecture reviews and sponsored certification tracks (Cloud, Security, ITIL, Agile) to ensure continuous organizational agility.</p>
  </div>
</div>

<div class="page-break"></div>

<h2>Summary</h2>

<div class="card" style="margin-bottom: 10px;">
  <h4>Synthesis of Design & Engineering Mastery</h4>
  <p>As a graduate in Human Interface Design (M.S. in Computing, UK) and holding an engineering degree in Electronics and Communication (B.E.), I possess a balanced, end-to-end mastery of both the design and software development aspects of digital product creation with vast experience across the entire product lifecycle.</p>
</div>

<div class="card" style="margin-bottom: 10px;">
  <h4>Proven Versatility Across Startup Velocity & Enterprise Scale</h4>
  <p>My 18+ years of experience encompass handling both small and large teams and projects at various stages of product maturity—from fast-paced startup incubation (Technoyana, SrushtiLabs, Twitan) to large-scale, safety-critical enterprise systems (Philips ICU Healthcare, Cisco Systems, UST Global, Ness).</p>
</div>

<div class="pledge-box">
  <h3>Pledge for Self-Training & Professional Certification</h3>
  <p>As per the requirements of the <strong>Senior Manager – IT</strong> role, I pledge to proactively upskill myself for the needs of the team, role, and organizational responsibilities.</p>
  <p>I agree to undertake and complete any required professional and enterprise certifications (e.g., Cloud Architecture, ITIL, Cybersecurity/CISSP, or Project Governance) as per project and team needs before and upon joining.</p>
</div>

<p style="text-align: center; margin-top: 20px; font-weight: 700; color: #0284c7;">
  Maheshchandra Hegde &nbsp;|&nbsp; Bangalore, India &nbsp;|&nbsp; hid.mahesh@gmail.com &nbsp;|&nbsp; +91 9535253329 / 7022407280 &nbsp;|&nbsp; hegdemahesh.in
</p>

</body>
</html>
"""

def generate_pdf():
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
        print(f"SUCCESS: Generated Executive Document PDF at: {pdf_file} (Size: {os.path.getsize(pdf_file)} bytes)")
    else:
        print("Failed to generate PDF. Subprocess output:", res.stderr)

if __name__ == "__main__":
    generate_pdf()
