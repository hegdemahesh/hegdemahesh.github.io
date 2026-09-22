"""
Script to generate a beautifully styled Executive PDF Document from WORK_EXPERIENCE_DOCUMENT.md
Uses Headless Microsoft Edge / Google Chrome built into Windows.
Updated with 3D Visualizer Expert Pedigree (50+ Projects), Voxelforge AI & ayam3d.
"""

import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Obayashi Corporation - Senior Manager IT Work Experience Document</title>
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
    border-bottom: 3px solid #004e96;
    padding-bottom: 12px;
    margin-bottom: 18px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .corp-name {
    font-size: 12pt;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #cc2229;
    text-transform: uppercase;
  }
  .doc-title {
    font-size: 18pt;
    font-weight: 800;
    color: #0f1e36;
    margin: 4px 0 2px 0;
  }
  .doc-subtitle {
    font-size: 10.5pt;
    font-weight: 600;
    color: #004e96;
  }
  .candidate-meta {
    text-align: right;
    font-size: 9pt;
    color: #475569;
    line-height: 1.35;
  }
  .candidate-meta strong {
    color: #0f1e36;
    font-size: 10pt;
  }
  h2 {
    color: #0f1e36;
    font-size: 12pt;
    border-left: 4px solid #004e96;
    padding-left: 8px;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }
  h3 {
    color: #004e96;
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
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
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
    color: #004e96;
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
    background: #0f1e36;
    color: #ffffff;
    font-weight: 700;
    padding: 7px 9px;
    text-align: left;
    border: 1px solid #0f1e36;
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
    color: #004e96;
    font-size: 10.5pt;
    white-space: nowrap;
  }
  .callout {
    background: #eff6ff;
    border-left: 4px solid #0284c7;
    padding: 9px 12px;
    border-radius: 0 6px 6px 0;
    margin: 10px 0;
    font-size: 9pt;
  }
  .roadmap-box {
    background: #0f1e36;
    color: #ffffff;
    border-radius: 6px;
    padding: 12px 14px;
    margin: 12px 0;
    page-break-inside: avoid;
  }
  .roadmap-box h3 {
    color: #38bdf8;
    margin-top: 0;
    font-size: 10.5pt;
    border-bottom: 1px solid #334155;
    padding-bottom: 5px;
  }
  .roadmap-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
    margin-top: 8px;
  }
  .roadmap-col {
    background: #182b49;
    padding: 8px;
    border-radius: 4px;
    font-size: 8.5pt;
  }
  .roadmap-col strong {
    color: #67e8f9;
    display: block;
    margin-bottom: 5px;
  }
  .roadmap-col ul {
    margin: 0;
    padding-left: 12px;
  }
  .roadmap-col li {
    margin-bottom: 4px;
    color: #cbd5e1;
  }
  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<div class="header-container">
  <div>
    <div class="corp-name">Obayashi Corporation</div>
    <div class="doc-title">Work Experience Document</div>
    <div class="doc-subtitle">Final Interview Submission: Senior Manager – IT</div>
  </div>
  <div class="candidate-meta">
    <strong>Maheshchandra Hegde</strong><br>
    hid.mahesh@gmail.com<br>
    +91 9535253329 / +91 7022407280<br>
    Recipient: talent@obayashi.org
  </div>
</div>

<p><strong>Executive Overview:</strong> A comprehensive technical portfolio mapping over 20 years of enterprise technology leadership, mission-critical infrastructure, and 3D visualization / spatial AI engineering (Voxelforge AI, ayam3d, 50+ industry projects) directly to the operational and digital construction mandates of Obayashi Corporation.</p>

<div class="grid-2">
  <div class="card">
    <h4>Enterprise Systems & Mission-Critical Reliability</h4>
    <p>Proven track record engineering safety-critical platforms (Philips Healthcare / Cyient) with 99.95%+ uptime, automated failover, and zero-loss offline field data resilience (Technoyana).</p>
  </div>
  <div class="card">
    <h4>3D Spatial Tech & Digital Construction (BIM)</h4>
    <p>Visualizer expert across 50+ architectural, simulation, and CAD projects. Currently pioneering <strong>Voxelforge AI</strong> (generative 3D low-poly) and <strong>ayam3d</strong> (mesh synthesis & retopology) for real-time digital twins.</p>
  </div>
  <div class="card">
    <h4>Cybersecurity, Access & Risk Governance</h4>
    <p>Deep expertise in Zero-Trust Network Access (ZTNA), RBAC, ISO 27001 standards, vulnerability remediation, and continuous disaster recovery readiness.</p>
  </div>
  <div class="card">
    <h4>Vendor Governance & Fiscal Discipline</h4>
    <p>Demonstrated capability managing multi-vendor contracts, cloud infrastructures (AWS/Azure), SLAs, and driving significant recurring CapEx/OpEx cost reductions (22% savings).</p>
  </div>
</div>

<h2>1. Project Overview & Objectives</h2>

<h3>Project 1: Mission-Critical Clinical Systems (Philips Healthcare / Cyient)</h3>
<p><strong>Role & Tenure:</strong> Senior Technical Lead / Systems Architect (Nov 2023 – Mar 2025)<br>
<strong>Scope & Scale:</strong> Philips Intellispace Critical Care and Anesthesia (ICCA)—an enterprise-grade healthcare monitoring and clinical decision support system deployed across major hospital networks globally.<br>
<strong>Core Objectives:</strong></p>
<ul>
  <li><strong>Zero-Downtime Reliability:</strong> Guarantee fail-safe system availability and instantaneous clinical alert rendering in 24/7 ICU environments where system latency carries life-safety consequences.</li>
  <li><strong>Security & Regulatory Compliance:</strong> Implement strict healthcare data governance (HIPAA, FDA software safety benchmarks, ISO 27001 data classification, and end-to-end cryptographic transit).</li>
  <li><strong>Modular Architecture Modernization:</strong> Transition legacy monolithic modules into scalable micro-frontends and standardized API communication layers, accelerating release cadence without regression risk.</li>
</ul>

<h3>Project 2: High-Availability Cloud Modernization & Edge Resilience (Technoyana Digital)</h3>
<p><strong>Role & Tenure:</strong> Co-Founder & Director of Technology / Architecture Lead (May 2021 – Oct 2023; Strategic Advisor)<br>
<strong>Scope & Scale:</strong> Distributed multi-tenant platforms (Twitan Sports OS) operating across physical arenas with degraded cellular networks.<br>
<strong>Core Objectives:</strong></p>
<ul>
  <li><strong>Offline-First Field Resilience:</strong> Engineer a zero-loss offline architecture using local client persistence and Service Workers that allows uninterrupted field operations during network outages, synchronizing automatically when reconnected <em>(directly applicable to Obayashi's remote construction sites)</em>.</li>
  <li><strong>Cloud Cost & Infrastructure Governance:</strong> Directed cloud infrastructure roadmaps across AWS, Firebase, and serverless architectures, automating scaling and reducing recurring cloud expenditures by 22%.</li>
</ul>

<h3>Project 3: Spatial Computing, Generative 3D Pipelines & 50+ Visualization Projects (Voxelforge AI & ayam3d)</h3>
<p><strong>Role & Tenure:</strong> Founder, Lead Spatial Architect & 3D Visualizer Expert (Ongoing R&D & Production)<br>
<strong>Flagship Platforms:</strong></p>
<ul>
  <li><strong>Voxelforge AI (<a href="https://voxelforge.ai">voxelforge.ai</a>):</strong> AI-assisted generative 3D asset pipeline producing game-ready, low-poly modular 3D assets for WebGL, Unity, and Unreal Engine. Automates prompt-to-3D synthesis and real-time polygon reduction for browser-based digital twin rendering.</li>
  <li><strong>ayam3d (<a href="https://srushtilabs.com">ayam3d</a>):</strong> Advanced spatial computing R&D in automated 3D mesh synthesis, intelligent retopology, and PBR texturing. Converts heavy raw 3D scans and photogrammetry point clouds into lightweight, real-time assets.</li>
  <li><strong>50+ Industry 3D Projects Track Record:</strong> Delivered 35+ architectural visualization and 3D animated walkthrough projects for commercial/residential developments, created military and civil flight simulator 3D terrain databases at <strong>CAE Simulation Technologies</strong>, and engineered interactive 3D physical campus dashboards at <strong>Cisco Systems</strong>.</li>
  <li><strong>Obayashi Synergy:</strong> Directly bridges the gap between traditional IT infrastructure and Obayashi’s BIM (Building Information Modeling), 3D point cloud streaming, and Digital Twin roadmaps.</li>
</ul>

<div class="page-break"></div>

<h2>2. Role & Core Responsibilities</h2>

<div class="grid-2">
  <div class="card">
    <h4>IT Strategy, Policies & Architecture</h4>
    <ul>
      <li>Formulated multi-year enterprise technology roadmaps aligning IT investments with corporate growth.</li>
      <li>Established standardized IT governance policies, coding standards, and change management protocols.</li>
      <li>Conducted Architecture Review Boards (ARBs) to eliminate technical debt and validate tech selection.</li>
    </ul>
  </div>
  <div class="card">
    <h4>Infrastructure Operations & Business Continuity</h4>
    <ul>
      <li>Ensured 24/7 availability of critical multi-tier infrastructure, cloud tenancies, and network topologies.</li>
      <li>Supervised automated multi-region backup regimens and formal Disaster Recovery (DR) tabletop drills.</li>
      <li>Implemented proactive synthetic monitoring and telemetry to preemptively resolve system anomalies.</li>
    </ul>
  </div>
  <div class="card">
    <h4>3D Spatial Tech & Digital Construction (BIM)</h4>
    <ul>
      <li>Architected high-performance computing infra for heavy 3D CAD/BIM model distribution and GPU virtualization.</li>
      <li>Automated 3D mesh retopology pipelines (Voxelforge AI, ayam3d) to convert raw 3D scans for mobile inspection.</li>
      <li>Bridged civil engineers, BIM managers, and IT systems across Common Data Environments (CDE).</li>
    </ul>
  </div>
  <div class="card">
    <h4>Cybersecurity, Team & Vendor Governance</h4>
    <ul>
      <li>Enforced Zero-Trust principles, role-based access control (RBAC), and mandatory multi-factor authentication.</li>
      <li>Led cross-functional squads across development, DevOps, 3D graphics, and QA.</li>
      <li>Governed multi-vendor contracts, CSP relationships (AWS/Azure), and cut cloud spend by 22%.</li>
    </ul>
  </div>
</div>

<h2>3. Major Achievements & Measurable Milestones</h2>

<table>
  <thead>
    <tr>
      <th style="width: 26%;">Milestone / Metric</th>
      <th style="width: 14%;">Result</th>
      <th style="width: 60%;">Operational Context & Measurable Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Critical System Availability</strong></td>
      <td><span class="stat-badge">99.95%+</span></td>
      <td>Maintained 24/7 continuous uptime across clinical ICU operations and high-traffic workloads without single-point failures.</td>
    </tr>
    <tr>
      <td><strong>Edge Data Preservation</strong></td>
      <td><span class="stat-badge">100%</span></td>
      <td>Zero data loss recorded during remote venue network dropouts using offline-first state engine and transactional event queueing.</td>
    </tr>
    <tr>
      <td><strong>3D & Spatial Projects</strong></td>
      <td><span class="stat-badge">50+ Projects</span></td>
      <td>Delivered across architectural visualization, CAD drafting, flight simulation visual databases, and generative 3D AI pipelines.</td>
    </tr>
    <tr>
      <td><strong>Release Velocity</strong></td>
      <td><span class="stat-badge">+35%</span></td>
      <td>Accelerated deployment and release cycles from weeks to hours via automated CI/CD pipelines, containerization, and linting suites.</td>
    </tr>
    <tr>
      <td><strong>Cloud Cost Optimization</strong></td>
      <td><span class="stat-badge">22% Saved</span></td>
      <td>Reduced recurring monthly cloud spend through proactive rightsizing, autoscaling policies, idle asset pruning, and license audits.</td>
    </tr>
    <tr>
      <td><strong>3D Asset File Size Reduction</strong></td>
      <td><span class="stat-badge">75% Saved</span></td>
      <td>Slashed 3D asset payload sizes using Voxelforge AI / ayam3d retopology algorithms, enabling 60 FPS mobile WebGL rendering.</td>
    </tr>
    <tr>
      <td><strong>Incident MTTR</strong></td>
      <td><span class="stat-badge">40% Faster</span></td>
      <td>Cut Mean-Time-To-Resolution (MTTR) by implementing proactive synthetic monitoring and standardized incident escalation runbooks.</td>
    </tr>
  </tbody>
</table>

<h2>4. Challenges Faced & Resolutions Implemented</h2>

<div class="card" style="margin-bottom: 10px;">
  <h4>Challenge 1: Severe Network Fluctuation & Remote Field Disconnections</h4>
  <p><strong>Context:</strong> Remote venues and distributed client sites frequently suffered from unstable cellular coverage, local Wi-Fi interference, and sudden ISP dropouts, risking broken transactions and user data loss.<br>
  <strong>Resolution:</strong> Re-architected data ingestion to an <strong>Offline-First model</strong> using client-side IndexedDB persistence and Service Workers. Implemented an optimistic UI pattern with an automated transactional replay queue that resynchronizes once the network reconnects.<br>
  <strong>Impact:</strong> 100% data preservation, zero operator workflow interruptions, seamless user experience.</p>
</div>

<div class="card" style="margin-bottom: 10px;">
  <h4>Challenge 2: Heavy 3D Asset Bandwidth Saturation & Mobile Device Crashes</h4>
  <p><strong>Context:</strong> Delivering multi-gigabyte 3D CAD/BIM models, architectural scans, and unoptimized polygonal meshes to mobile tablets in the field caused severe browser lag, memory overflows, and lengthy download times over cellular networks.<br>
  <strong>Resolution:</strong> Leveraged <strong>Voxelforge AI</strong> and <strong>ayam3d</strong> retopology algorithms to establish an automated 3D optimization pipeline: progressive Level of Detail (LOD) generation, polygon decimation, draw-call batching, and PBR texture atlas compression, paired with WebGL progressive streaming shaders.<br>
  <strong>Impact:</strong> Slashed 3D asset download size by 75%, eliminated mobile browser memory crashes, and achieved smooth 60 FPS interactive rendering on standard mobile tablets.</p>
</div>

<div class="card" style="margin-bottom: 10px;">
  <h4>Challenge 3: Complex Multi-Vendor Dependencies & SLA Enforcement Gaps</h4>
  <p><strong>Context:</strong> Proliferation of disjointed third-party cloud tools, software licenses, and ISP vendors led to finger-pointing during service degradation, lack of unified visibility, and unchecked budget leakage.<br>
  <strong>Resolution:</strong> Designed and deployed an <strong>IT Operational & SLA Governance Dashboard</strong> providing real-time telemetry on vendor uptime, latency, and support turnaround times. Renegotiated MSAs to tie vendor billing directly to SLA compliance scores and automated the termination of idle cloud instances.<br>
  <strong>Impact:</strong> Slashed incident MTTR by 40% and trimmed recurring monthly infrastructure expenditures by 22%.</p>
</div>

<div class="page-break"></div>

<h2>5. Lessons Learned & Operational Best Practices</h2>
<ul>
  <li><strong>Design for Failure & Network Resilience from Day 1:</strong> In mission-critical operations—whether in clinical hospital wards or remote construction job sites—assuming continuous 100% network uptime is an architectural flaw. Systems must inherently feature local caching, asynchronous retry queues, and graceful degradation modes.</li>
  <li><strong>Unify 3D Engineering Realities with Corporate IT Strategy:</strong> In a tier-1 construction corporation, IT is no longer just back-office software; it is the vital infrastructure enabling heavy 3D BIM coordination, drone photogrammetry, virtual reality safety drills, and digital twins. IT leadership must understand 3D graphics pipelines and geometry optimization to provision computing resources that empower engineering teams.</li>
  <li><strong>Cybersecurity Must Be Cultural, Not Merely a Perimeter Firewall:</strong> Modern enterprise defense requires the Zero-Trust paradigm: continuous verification, least-privilege access, automated multi-factor authentication, and regular staff hygiene training. Protecting intellectual property and project blueprints requires data-level encryption and access auditability.</li>
  <li><strong>Proactive Observability Over Reactive Incident Response:</strong> An IT organization should never learn about a system outage from an end-user ticket. Automated synthetic transactions, threshold-based health alerts, and centralized log telemetry enable IT teams to resolve 80% of system degradation before business operations are affected.</li>
  <li><strong>Bridging Field Realities with Executive Strategy:</strong> Effective IT leadership is achieved on the job site. Understanding the daily friction points of site engineers and BIM managers ensures technology investments solve tangible business problems and deliver measurable ROI.</li>
</ul>

<h2>6. Suggestions for Future Process Improvements (Tailored for Obayashi Corporation)</h2>

<div class="grid-2">
  <div class="card">
    <h4>1. Construction Site "IT-in-a-Box" Rapid Deployment Kit</h4>
    <p>Develop containerized, pre-configured site IT units featuring dual-SIM bonded 5G/satellite SD-WAN, localized edge caching nodes, biometric access control, and ruggedized Wi-Fi 6 mesh. Enables full job-site IT commissioning within 48 hours via Zero-Touch Provisioning (ZTP).</p>
  </div>
  <div class="card">
    <h4>2. Cloud BIM & CDE Acceleration Node (Powered by Spatial 3D Tech)</h4>
    <p>Deploy localized on-site BIM caching nodes paired with <strong>Voxelforge AI / ayam3d retopology algorithms</strong> and WebGL progressive 3D rendering. Allows field engineers to inspect multi-gigabyte 3D models and digital twins on mobile tablets with zero latency.</p>
  </div>
  <div class="card">
    <h4>3. Subcontractor Zero-Trust Security Mesh</h4>
    <p>Establish a cloud-native Zero-Trust Network Access (ZTNA) portal granting subcontractors strictly time-bound, role-scoped access to authorized project work packages with dynamic watermarking on proprietary blueprints and commercial bids to eliminate data leakage.</p>
  </div>
  <div class="card">
    <h4>4. AIOps Predictive Maintenance & Automated DR</h4>
    <p>Implement AI-assisted log telemetry across regional hubs and active construction sites to predict hardware/network failures before outages occur. Couple with immutable air-gapped backups to guarantee ransomware protection and automated quarterly disaster recovery drills.</p>
  </div>
</div>

<div class="roadmap-box">
  <h3>First 90 Days: Strategic Execution Roadmap for Senior Manager – IT</h3>
  <div class="roadmap-grid">
    <div class="roadmap-col">
      <strong>Days 1 – 30: Discovery & Baseline</strong>
      <ul>
        <li>Audit all IT infrastructure, multi-site networks & cloud tenancies.</li>
        <li>Interview site project managers & BIM leads for pain points.</li>
        <li>Review cybersecurity posture, MFA enforcement & DR readiness.</li>
        <li>Benchmark IT budget expenditures, vendor contracts & SLAs.</li>
      </ul>
    </div>
    <div class="roadmap-col">
      <strong>Days 31 – 60: Stabilization & Quick Wins</strong>
      <ul>
        <li>Remediate high-risk security vulnerabilities; standardize IAM.</li>
        <li>Resolve immediate job-site network connectivity bottlenecks.</li>
        <li>Implement proactive monitoring dashboards for critical systems.</li>
        <li>Conduct full tabletop Disaster Recovery (DR) simulation drill.</li>
      </ul>
    </div>
    <div class="roadmap-col">
      <strong>Days 61 – 90: Modernization & Growth</strong>
      <ul>
        <li>Present 2-3 Year IT Strategy aligned with corporate goals.</li>
        <li>Pilot the "Site IT-in-a-Box" rapid deployment kit.</li>
        <li>Integrate 3D asset optimization pipelines for digital twin streaming.</li>
        <li>Establish structured upskilling and mentorship tracks for IT team.</li>
      </ul>
    </div>
  </div>
</div>

<p style="text-align: center; margin-top: 20px; font-weight: 600; color: #004e96;">
  Maheshchandra Hegde &nbsp;|&nbsp; Senior Manager – IT Candidate &nbsp;|&nbsp; Obayashi Corporation
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
        print(f"SUCCESS: Generated Executive Document PDF at: {pdf_file} (Size: {os.path.getsize(pdf_file)} bytes)")
    else:
        print("Failed to generate PDF. Subprocess output:", res.stderr)

if __name__ == "__main__":
    generate_pdf()
