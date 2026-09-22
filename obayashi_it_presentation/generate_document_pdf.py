"""
Script to generate a beautifully styled Executive PDF Document from WORK_EXPERIENCE_DOCUMENT.md
Uses Headless Microsoft Edge / Google Chrome built into Windows.
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
    margin: 18mm 16mm 18mm 16mm;
    @bottom-right {
      content: counter(page);
    }
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    line-height: 1.55;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
  }
  .header-container {
    border-bottom: 3px solid #004e96;
    padding-bottom: 14px;
    margin-bottom: 22px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .corp-name {
    font-size: 13pt;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #cc2229;
    text-transform: uppercase;
  }
  .doc-title {
    font-size: 19pt;
    font-weight: 800;
    color: #0f1e36;
    margin: 4px 0 2px 0;
  }
  .doc-subtitle {
    font-size: 11pt;
    font-weight: 600;
    color: #004e96;
  }
  .candidate-meta {
    text-align: right;
    font-size: 9.5pt;
    color: #475569;
    line-height: 1.4;
  }
  .candidate-meta strong {
    color: #0f1e36;
    font-size: 10.5pt;
  }
  h2 {
    color: #0f1e36;
    font-size: 13pt;
    border-left: 4px solid #004e96;
    padding-left: 8px;
    margin-top: 22px;
    margin-bottom: 10px;
    page-break-after: avoid;
  }
  h3 {
    color: #004e96;
    font-size: 11pt;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }
  p {
    margin: 6px 0;
    text-align: justify;
  }
  ul {
    margin: 6px 0 10px 20px;
    padding: 0;
  }
  li {
    margin-bottom: 4px;
  }
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin: 12px 0;
  }
  .card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 12px 14px;
    page-break-inside: avoid;
  }
  .card h4 {
    margin: 0 0 6px 0;
    color: #004e96;
    font-size: 10.5pt;
  }
  .card p {
    margin: 0;
    font-size: 9.5pt;
    color: #334155;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
  }
  th {
    background: #0f1e36;
    color: #ffffff;
    font-weight: 700;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #0f1e36;
  }
  td {
    padding: 7px 10px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
  }
  tr:nth-child(even) {
    background: #f8fafc;
  }
  .stat-badge {
    font-weight: 800;
    color: #004e96;
    font-size: 11pt;
    white-space: nowrap;
  }
  .callout {
    background: #eff6ff;
    border-left: 4px solid #0284c7;
    padding: 10px 14px;
    border-radius: 0 6px 6px 0;
    margin: 12px 0;
    font-size: 9.5pt;
  }
  .roadmap-box {
    background: #0f1e36;
    color: #ffffff;
    border-radius: 6px;
    padding: 14px 16px;
    margin: 14px 0;
    page-break-inside: avoid;
  }
  .roadmap-box h3 {
    color: #38bdf8;
    margin-top: 0;
    font-size: 11pt;
    border-bottom: 1px solid #334155;
    padding-bottom: 6px;
  }
  .roadmap-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-top: 10px;
  }
  .roadmap-col {
    background: #182b49;
    padding: 10px;
    border-radius: 4px;
    font-size: 9pt;
  }
  .roadmap-col strong {
    color: #67e8f9;
    display: block;
    margin-bottom: 6px;
  }
  .roadmap-col ul {
    margin: 0;
    padding-left: 14px;
  }
  .roadmap-col li {
    margin-bottom: 5px;
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

<p><strong>Executive Overview:</strong> A comprehensive technical experience portfolio mapping over 20 years of technology leadership, systems architecture, mission-critical infrastructure, and IT governance directly to the operational mandates of Obayashi Corporation.</p>

<div class="grid-2">
  <div class="card">
    <h4>Enterprise Systems & High Availability</h4>
    <p>Proven track record engineering safety-critical platforms (Philips Healthcare / Cyient) with 99.95%+ uptime, automated failover, and zero-loss offline data resilience (Technoyana).</p>
  </div>
  <div class="card">
    <h4>Cybersecurity, Risk & Compliance</h4>
    <p>Deep expertise in Zero-Trust Network Access (ZTNA), RBAC, ISO 27001 standards, vulnerability remediation, and continuous disaster recovery readiness.</p>
  </div>
  <div class="card">
    <h4>Project Execution & Digital Innovation</h4>
    <p>Extensive experience modernizing legacy systems, managing agile cross-functional squads, and developing spatial 3D/BIM-aligned technologies.</p>
  </div>
  <div class="card">
    <h4>Vendor Governance & Fiscal Discipline</h4>
    <p>Demonstrated capability managing multi-vendor contracts, cloud infrastructures (AWS/Azure), SLAs, and driving significant recurring CapEx/OpEx cost reductions.</p>
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

<h3>Project 2: High-Availability Cloud Modernization & Edge-Resilient Platform (Technoyana Digital)</h3>
<p><strong>Role & Tenure:</strong> Co-Founder & Director of Technology / Architecture Lead (May 2021 – Oct 2023; Strategic Advisor)<br>
<strong>Scope & Scale:</strong> Distributed multi-tenant platforms (Twitan Sports OS, automated bracket engines, and spatial AI pipelines) operating across physical venues with degraded cellular networks.<br>
<strong>Core Objectives:</strong></p>
<ul>
  <li><strong>Offline-First Field Resilience:</strong> Engineer a zero-loss offline architecture using local client persistence and Service Workers that allows uninterrupted field operations during network outages, synchronizing automatically when reconnected <em>(directly applicable to Obayashi's remote construction sites)</em>.</li>
  <li><strong>Cloud Cost & Infrastructure Governance:</strong> Directed cloud infrastructure roadmaps across AWS, Firebase, and serverless architectures, automating scaling and reducing recurring cloud expenditures by 22%.</li>
  <li><strong>Spatial & 3D Engineering (Srushtilabs):</strong> Researched and deployed automated 3D mesh workflows and WebGL visualization pipelines—establishing direct technical continuity with Obayashi’s Building Information Modeling (BIM) and Digital Twin roadmaps.</li>
</ul>

<h2>2. Role & Core Responsibilities</h2>

<div class="grid-2">
  <div class="card">
    <h4>IT Strategy, Policies & Architecture</h4>
    <ul>
      <li>Formulated multi-year enterprise technology roadmaps aligning IT investments with corporate growth.</li>
      <li>Established standardized IT governance policies, coding standards, and change management protocols.</li>
      <li>Conducted Architecture Review Boards (ARBs) to eliminate technical debt and prevent vendor lock-in.</li>
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
    <h4>Cybersecurity, Access Control & Risk</h4>
    <ul>
      <li>Enforced Zero-Trust principles, role-based access control (RBAC), and mandatory multi-factor authentication (MFA).</li>
      <li>Executed vulnerability scans (SAST/DAST), code audits, and third-party vendor risk assessments.</li>
      <li>Maintained disaster containment playbooks and compliance with ISO 27001 and industry safety standards.</li>
    </ul>
  </div>
  <div class="card">
    <h4>Team Leadership, Vendors & Budgets</h4>
    <ul>
      <li>Led, mentored, and developed cross-functional squads across development, infrastructure, and QA.</li>
      <li>Governed multi-vendor contracts, CSP relationships, and enforced strict SLA compliance.</li>
      <li>Optimized CapEx/OpEx allocations through license rationalization and cloud cost management.</li>
    </ul>
  </div>
</div>

<div class="page-break"></div>

<h2>3. Major Achievements & Measurable Milestones</h2>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Milestone / Metric</th>
      <th style="width: 15%;">Result</th>
      <th style="width: 60%;">Operational Context & Measurable Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Critical System Availability</strong></td>
      <td><span class="stat-badge">99.95%+</span></td>
      <td>Maintained 24/7 continuous uptime across clinical ICU operations and high-traffic event workloads without single-point failures.</td>
    </tr>
    <tr>
      <td><strong>Edge Data Preservation</strong></td>
      <td><span class="stat-badge">100%</span></td>
      <td>Zero data loss recorded during remote venue network dropouts using offline-first state engine and transactional event queueing.</td>
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
      <td><strong>Incident MTTR</strong></td>
      <td><span class="stat-badge">40% Faster</span></td>
      <td>Cut Mean-Time-To-Resolution (MTTR) by implementing proactive synthetic monitoring and standardized incident escalation runbooks.</td>
    </tr>
    <tr>
      <td><strong>Security Audit Cleanliness</strong></td>
      <td><span class="stat-badge">Zero Highs</span></td>
      <td>Successfully cleared rigorous enterprise and healthcare security audits with zero unresolved high-severity vulnerabilities.</td>
    </tr>
  </tbody>
</table>

<h2>4. Challenges Faced & Resolutions Implemented</h2>

<div class="card" style="margin-bottom: 12px;">
  <h4>Challenge 1: Severe Network Fluctuation & Remote Field Disconnections</h4>
  <p><strong>Context:</strong> Remote venues and distributed client sites frequently suffered from unstable cellular coverage, local Wi-Fi interference, and sudden ISP dropouts, risking broken transactions and user data loss.<br>
  <strong>Resolution:</strong> Re-architected data ingestion to an <strong>Offline-First model</strong> using client-side IndexedDB persistence and Service Workers. Implemented an optimistic UI pattern with an automated transactional replay queue. When offline, transactions are stored locally with cryptographic timestamps; upon reconnection, the queue replays in the background with deterministic conflict resolution.<br>
  <strong>Impact:</strong> 100% data preservation, zero operator workflow interruptions, seamless user experience.</p>
</div>

<div class="card" style="margin-bottom: 12px;">
  <h4>Challenge 2: Architectural Fragility & High Downtime Risk in Monolithic Legacy Systems</h4>
  <p><strong>Context:</strong> Critical enterprise applications were bound within monolithic codebases where simple updates risked triggering cascading failures across unrelated modules, leading to long testing cycles and deployment anxiety.<br>
  <strong>Resolution:</strong> Decomposed the monolith into decoupled <strong>micro-frontends</strong> and standardized REST/WebSocket API contracts. Established automated test pipelines and canary / blue-green deployments with instant rollback capability.<br>
  <strong>Impact:</strong> Reduced regression risks to near zero, cut deployment release cycles by 35%, and enabled independent modular upgrades.</p>
</div>

<div class="card" style="margin-bottom: 12px;">
  <h4>Challenge 3: Complex Multi-Vendor Dependencies & SLA Enforcement Gaps</h4>
  <p><strong>Context:</strong> Proliferation of disjointed third-party cloud tools, software licenses, and ISP vendors led to finger-pointing during service degradation, lack of unified visibility, and unchecked budget leakage.<br>
  <strong>Resolution:</strong> Designed and deployed an <strong>IT Operational & SLA Governance Dashboard</strong> providing real-time telemetry on vendor uptime, latency, and support turnaround times. Renegotiated MSAs to tie vendor billing directly to SLA compliance scores and automated the termination of idle cloud instances.<br>
  <strong>Impact:</strong> Slashed incident MTTR by 40% and trimmed recurring monthly infrastructure expenditures by 22%.</p>
</div>

<h2>5. Lessons Learned & Operational Best Practices</h2>
<ul>
  <li><strong>Design for Failure & Network Resilience from Day 1:</strong> In mission-critical operations—whether in clinical hospital wards or remote construction job sites—assuming continuous 100% network uptime is an architectural flaw. Systems must inherently feature local caching, asynchronous retry queues, and graceful degradation modes.</li>
  <li><strong>Cybersecurity Must Be Cultural, Not Merely a Perimeter Firewall:</strong> Modern enterprise defense requires the Zero-Trust paradigm: continuous verification, least-privilege access, automated multi-factor authentication, and regular staff hygiene training. Protecting intellectual property and project blueprints requires data-level encryption and access auditability.</li>
  <li><strong>Proactive Observability Over Reactive Incident Response:</strong> An IT organization should never learn about a system outage from an end-user ticket. Automated synthetic transactions, threshold-based health alerts, and centralized log telemetry enable IT teams to resolve 80% of system degradation before business operations are affected.</li>
  <li><strong>Bridging Field Realities with Executive Strategy:</strong> Effective IT leadership is achieved in the field. Understanding the daily friction points of site engineers and project managers ensures technology investments solve tangible business problems and deliver measurable ROI.</li>
</ul>

<h2>6. Suggestions for Future Process Improvements (Tailored for Obayashi Corporation)</h2>

<div class="grid-2">
  <div class="card">
    <h4>1. Construction Site "IT-in-a-Box" Rapid Deployment Kit</h4>
    <p>Develop containerized, pre-configured site IT units featuring dual-SIM bonded 5G/satellite SD-WAN, localized edge caching nodes, biometric access control, and ruggedized Wi-Fi 6 mesh. Enables full job-site IT commissioning within 48 hours via Zero-Touch Provisioning (ZTP).</p>
  </div>
  <div class="card">
    <h4>2. Cloud BIM & Common Data Environment (CDE) Acceleration</h4>
    <p>Deploy localized on-site BIM caching nodes paired with WebGL-based progressive 3D rendering pipelines. Allows field engineers to inspect multi-gigabyte 3D models and digital twins on mobile tablets with zero latency, synchronizing annotations back to corporate CDE asynchronously.</p>
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
        <li>Interview site project managers & business heads for pain points.</li>
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
        <li>Prototype the "Site IT-in-a-Box" rapid deployment kit.</li>
        <li>Institute automated CI/CD and self-service IT ticketing workflows.</li>
        <li>Establish structured upskilling and mentorship tracks for IT team.</li>
      </ul>
    </div>
  </div>
</div>

<p style="text-align: center; margin-top: 24px; font-weight: 600; color: #004e96;">
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

    # Find edge or chrome
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
