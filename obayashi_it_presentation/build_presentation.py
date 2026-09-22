"""
Script to generate the Executive Work Experience Presentation for Obayashi Corporation
Candidate: Maheshchandra Hegde
Position: Senior Manager - IT
Format: 16:9 Widescreen PowerPoint Presentation (.pptx)
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_pptx_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # blank layout

    # Brand Colors (Obayashi Corporate Blue, Precision Navy, Steel Gray, Red Accent, Card White)
    COLOR_PRIMARY_DARK = RGBColor(15, 30, 54)     # Deep Corporate Navy #0F1E36
    COLOR_PRIMARY_BLUE = RGBColor(0, 78, 150)     # Obayashi / Precision Blue #004E96
    COLOR_ACCENT_RED   = RGBColor(204, 34, 41)    # Corporate Accent Red #CC2229
    COLOR_BG_LIGHT     = RGBColor(248, 250, 252)  # Soft Canvas Light #F8FAFC
    COLOR_CARD_BG      = RGBColor(255, 255, 255)  # Pure White #FFFFFF
    COLOR_CARD_BORDER  = RGBColor(226, 232, 240)  # Border Subtle #E2E8F0
    COLOR_TEXT_MAIN    = RGBColor(30, 41, 59)     # Slate 800 #1E293B
    COLOR_TEXT_MUTED   = RGBColor(100, 116, 139)  # Slate 500 #64748B
    COLOR_ACCENT_BLUE  = RGBColor(14, 116, 144)   # Teal/Ocean #0E7490
    COLOR_SUCCESS      = RGBColor(16, 149, 99)    # Emerald Green #109563

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title, dark=False):
        # Category pill/subtitle
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_ACCENT_RED if dark else COLOR_PRIMARY_BLUE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = RGBColor(255, 255, 255) if dark else COLOR_PRIMARY_DARK

        # Top Accent Divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.025))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(255, 255, 255) if dark else COLOR_CARD_BORDER
        line.line.fill.background()

    def add_card(slide, left, top, width, height, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
        return card

    def add_footer(slide, current_page, total_pages=11, dark=False):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.35))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"Obayashi Corporation · Senior Manager – IT Candidate Portfolio | Maheshchandra Hegde · Page {current_page} of {total_pages}"
        p.font.size = Pt(9)
        p.font.color.rgb = RGBColor(148, 163, 184) if dark else COLOR_TEXT_MUTED

    # ==========================================
    # SLIDE 1: Title Slide (Dark Theme Executive)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLOR_PRIMARY_DARK)

    # Accent decorative strip
    strip = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(0.3), Inches(5.1))
    strip.fill.solid()
    strip.fill.fore_color.rgb = COLOR_ACCENT_RED
    strip.line.fill.background()

    # Title & Subtitle block
    t_box = s1.shapes.add_textbox(Inches(1.4), Inches(1.3), Inches(11.0), Inches(3.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "OBAYASHI CORPORATION  |  FINAL INTERVIEW SUBMISSION"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(148, 163, 184)
    p0.space_after = Pt(14)

    p1 = tf1.add_paragraph()
    p1.text = "Executive Work Experience & Strategic IT Capability Presentation"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    p1.space_after = Pt(12)

    p2 = tf1.add_paragraph()
    p2.text = "Candidate: Maheshchandra Hegde  |  Position: Senior Manager – IT"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(56, 189, 248) # Cyan highlight
    p2.space_after = Pt(8)

    p3 = tf1.add_paragraph()
    p3.text = "A comprehensive portfolio mapping enterprise technology leadership, mission-critical infrastructure, cybersecurity governance, and operational resilience to Obayashi's global engineering mandates."
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(203, 213, 225)

    # 4 Quick Pillar Highlights in Cards
    pillars = [
        ("IT Operations & Infra", "High availability, hybrid cloud, disaster recovery & multi-site continuity"),
        ("Cybersecurity & Risk", "Zero Trust, access controls, vulnerability mitigation & ISO compliance"),
        ("Project & Team Delivery", "Enterprise systems, cross-functional squads, digital transformation"),
        ("Vendor & Budget Control", "SLA governance, contract management, resource optimization & CapEx/OpEx")
    ]
    card_w = Inches(2.75)
    card_h = Inches(1.35)
    start_x = Inches(1.4)
    start_y = Inches(4.9)
    gap = Inches(0.24)

    for i, (title, desc) in enumerate(pillars):
        cx = start_x + i * (card_w + gap)
        c_shape = add_card(s1, cx, start_y, card_w, card_h, bg_color=RGBColor(24, 43, 73), border_color=RGBColor(51, 65, 85))
        tb = s1.shapes.add_textbox(cx + Inches(0.15), start_y + Inches(0.15), card_w - Inches(0.3), card_h - Inches(0.3))
        ctf = tb.text_frame
        ctf.word_wrap = True
        cp1 = ctf.paragraphs[0]
        cp1.text = title
        cp1.font.size = Pt(12)
        cp1.font.bold = True
        cp1.font.color.rgb = RGBColor(255, 255, 255)
        cp1.space_after = Pt(4)
        cp2 = ctf.add_paragraph()
        cp2.text = desc
        cp2.font.size = Pt(10)
        cp2.font.color.rgb = RGBColor(148, 163, 184)

    add_footer(s1, 1, 11, dark=True)

    # ==========================================
    # SLIDE 2: Professional Profile & Strategic Alignment
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, COLOR_BG_LIGHT)
    add_header(s2, "Executive Profile", "Strategic Leadership Profile & Alignment with Obayashi Corporation")

    # Left Column: Profile & Credentials Card (width: 4.8)
    add_card(s2, Inches(0.8), Inches(1.6), Inches(4.2), Inches(5.2))
    prof_tb = s2.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(3.7), Inches(4.8))
    ptf = prof_tb.text_frame
    ptf.word_wrap = True

    p = ptf.paragraphs[0]
    p.text = "Maheshchandra Hegde"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(4)

    p = ptf.add_paragraph()
    p.text = "Technology Leader · Systems Architect · Enterprise Delivery Expert"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_BLUE
    p.space_after = Pt(12)

    creds = [
        ("Total Experience", "20+ Years leading enterprise IT, architectures & engineering teams"),
        ("Education", "MS in Computing (Robert Gordon Univ., UK) · B.E. in Electronics & Communication"),
        ("Key Past Tenures", "Cyient (Philips Critical Care), Technoyana, UST Global (Cisco Systems), Moonraft, Ness, ThoughtFocus, Cognizant"),
        ("Core Competencies", "Hybrid Infrastructure, IT Operations, Mission-Critical Availability, Cybersecurity, Team Mentorship, Vendor SLAs"),
        ("Industry Domain", "Healthcare Critical Systems, Enterprise Networking & Dashboards, High-Reliability SaaS, 3D/Spatial Tech")
    ]
    for lbl, val in creds:
        p = ptf.add_paragraph()
        p.text = f"• {lbl}: "
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_PRIMARY_DARK
        p2 = ptf.add_paragraph()
        p2.text = f"  {val}"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.space_after = Pt(6)

    # Right Column: 4 Strategic Alignment Cards (width: 7.3)
    right_x = Inches(5.25)
    rw = Inches(7.28)
    card_h2 = Inches(1.18)

    alignments = [
        ("1. Multi-Site Infrastructure & High Availability",
         "Proven expertise running mission-critical platforms demanding 99.95%+ uptime. Direct experience engineering resilient edge systems that guarantee business continuity even during remote network dropouts."),
        ("2. Cybersecurity Governance & Risk Mitigation",
         "Strict adherence to compliance frameworks, role-based access governance (RBAC), data protection policies, secure CI/CD pipelines, and active threat vulnerability management."),
        ("3. Digital Transformation & Enterprise Systems",
         "Spearheaded enterprise system integrations, API gateways, automated telemetry, and modernized legacy workflows into performant, scalable cloud architectures."),
        ("4. Team Empowerment, Vendor Governance & Fiscal Discipline",
         "Led cross-functional squads of engineers, QA, and analysts. Successfully managed third-party vendor contracts, cloud budgets (AWS/Azure/GCP), and SLA compliance.")
    ]

    for i, (title, desc) in enumerate(alignments):
        ry = Inches(1.6) + i * Inches(1.34)
        add_card(s2, right_x, ry, rw, card_h2)
        atb = s2.shapes.add_textbox(right_x + Inches(0.2), ry + Inches(0.12), rw - Inches(0.4), card_h2 - Inches(0.24))
        atf = atb.text_frame
        atf.word_wrap = True
        ap1 = atf.paragraphs[0]
        ap1.text = title
        ap1.font.size = Pt(12)
        ap1.font.bold = True
        ap1.font.color.rgb = COLOR_PRIMARY_BLUE
        ap1.space_after = Pt(3)
        ap2 = atf.add_paragraph()
        ap2.text = desc
        ap2.font.size = Pt(9.5)
        ap2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s2, 2, 11)

    # ==========================================
    # SLIDE 3: Project 1 Overview & Objectives (Mission-Critical Clinical Platform)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, COLOR_BG_LIGHT)
    add_header(s3, "Project Experience 1", "Project Overview & Objectives: Mission-Critical Enterprise System (Philips/Cyient)")

    # Left: Project Snapshot Card
    add_card(s3, Inches(0.8), Inches(1.6), Inches(4.3), Inches(5.2))
    p1_tb = s3.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(3.8), Inches(4.8))
    p1_tf = p1_tb.text_frame
    p1_tf.word_wrap = True

    p = p1_tf.paragraphs[0]
    p.text = "Project Profile: Philips ICCA"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(4)

    p = p1_tf.add_paragraph()
    p.text = "Intellispace Critical Care & Anesthesia Platform"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_BLUE
    p.space_after = Pt(10)

    p1_meta = [
        ("Role", "Senior Technical Lead / Systems Architect"),
        ("Tenure", "Nov 2023 - Mar 2025"),
        ("Scale", "Enterprise Global Hospital Deployments & High-Availability Clinical ICU Units"),
        ("Domain Context", "Life-critical, real-time patient monitoring, zero-latency clinical alerts & strict regulatory compliance"),
        ("Tech Ecosystem", "React, Node.js, Micro-frontends, REST/WebSocket APIs, Secure Auth, Enterprise Telemetry")
    ]
    for lbl, val in p1_meta:
        p = p1_tf.add_paragraph()
        p.text = f"{lbl}: "
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_PRIMARY_DARK
        p2 = p1_tf.add_paragraph()
        p2.text = f"{val}"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.space_after = Pt(6)

    # Right: 3 Core Objectives & Architecture Cards
    r3_x = Inches(5.35)
    r3_w = Inches(7.18)

    obj_cards = [
        ("Strategic Objective 1: High Availability & Zero-Fault Operational Resilience",
         "Architect and deliver web-tier systems for ICU and anesthesia workflows where system downtime is life-threatening. Established fail-safe fallback rendering, continuous health-check telemetry, and zero unhandled state exceptions across 24/7 continuous operations."),
        ("Strategic Objective 2: Data Protection, Security & Regulatory Compliance",
         "Enforce strict healthcare information security standards (HIPAA, FDA software safety benchmarks, ISO 27001 compliance). Enforced end-to-end data encryption in transit and at rest, granular role-based access (RBAC), and full audit logging of administrative and user actions."),
        ("Strategic Objective 3: Scalable Modular Architecture & Seamless Integration",
         "Transitioned monolithic legacy interfaces into a decoupled, micro-frontend architecture with standardized APIs. Enabled independent modular deployments, drastically reduced release risk, and unified clinical data feeds from diverse hardware monitors.")
    ]

    for i, (title, desc) in enumerate(obj_cards):
        cy = Inches(1.6) + i * Inches(1.76)
        add_card(s3, r3_x, cy, r3_w, Inches(1.6))
        otb = s3.shapes.add_textbox(r3_x + Inches(0.2), cy + Inches(0.15), r3_w - Inches(0.4), Inches(1.3))
        otf = otb.text_frame
        otf.word_wrap = True
        op1 = otf.paragraphs[0]
        op1.text = title
        op1.font.size = Pt(12.5)
        op1.font.bold = True
        op1.font.color.rgb = COLOR_PRIMARY_BLUE
        op1.space_after = Pt(5)
        op2 = otf.add_paragraph()
        op2.text = desc
        op2.font.size = Pt(10)
        op2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s3, 3, 11)

    # ==========================================
    # SLIDE 4: Project 2 Overview: Cloud Modernization & Offline-First Edge Resilience
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, COLOR_BG_LIGHT)
    add_header(s4, "Project Experience 2", "Project Overview: High-Availability Cloud Transformation & Edge Resilience (Technoyana)")

    # Left: Project Snapshot Card
    add_card(s4, Inches(0.8), Inches(1.6), Inches(4.3), Inches(5.2))
    p2_tb = s4.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(3.8), Inches(4.8))
    p2_tf = p2_tb.text_frame
    p2_tf.word_wrap = True

    p = p2_tf.paragraphs[0]
    p.text = "Technoyana Platforms"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(4)

    p = p2_tf.add_paragraph()
    p.text = "Digital Transformation & Distributed SaaS Ecosystem"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_BLUE
    p.space_after = Pt(10)

    p2_meta = [
        ("Role", "Co-Founder & Director of Technology / Architecture Lead"),
        ("Tenure", "May 2021 - Oct 2023 (Ongoing Strategic Advisor)"),
        ("Key Platforms", "Twitan Sports OS (Shutlify), Fintech Operations Engine, Spatial AI Pipelines (Srushtilabs)"),
        ("Operational Reality", "High-concurrency events, remote arenas/venues with degraded cellular connectivity, multi-tenant cloud infra"),
        ("Relevance to Obayashi", "Directly mirrors remote construction site challenges: volatile network connectivity, field staff data capture, automated cloud sync")
    ]
    for lbl, val in p2_meta:
        p = p2_tf.add_paragraph()
        p.text = f"{lbl}: "
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_PRIMARY_DARK
        p2 = p2_tf.add_paragraph()
        p2.text = f"{val}"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.space_after = Pt(6)

    # Right: 3 Key Dimensions
    r4_x = Inches(5.35)
    r4_w = Inches(7.18)

    p2_cards = [
        ("1. Edge-Resilient 'Offline-First' Architecture for Unstable Networks",
         "Architected an offline-first data model utilizing local storage, background Service Workers, and optimistic transactional queuing. When on-site network drops occur, field users continue full operations uninterrupted; bi-directional conflict resolution synchronizes cloud data the moment connectivity is restored."),
        ("2. Cloud Infrastructure & Cost Governance (AWS / Firebase / Serverless)",
         "Directed cloud infrastructure roadmap, automated CI/CD pipelines, containerized deployments, and disaster recovery replication. Implemented automated resource scaling and log archiving, cutting monthly cloud spend by 22% while handling 10x traffic bursts."),
        ("3. Digital Innovation: Spatial 3D & Automated Asset Workflows",
         "Pioneered spatial technology workflows (Voxelforge / Srushtilabs) producing modular 3D assets, automated mesh optimization, and WebGL visualizations. Establishes deep alignment with Obayashi's BIM, Digital Twin, and 3D construction modeling initiatives.")
    ]

    for i, (title, desc) in enumerate(p2_cards):
        cy = Inches(1.6) + i * Inches(1.76)
        add_card(s4, r4_x, cy, r4_w, Inches(1.6))
        otb = s4.shapes.add_textbox(r4_x + Inches(0.2), cy + Inches(0.15), r4_w - Inches(0.4), Inches(1.3))
        otf = otb.text_frame
        otf.word_wrap = True
        op1 = otf.paragraphs[0]
        op1.text = title
        op1.font.size = Pt(12.5)
        op1.font.bold = True
        op1.font.color.rgb = COLOR_PRIMARY_BLUE
        op1.space_after = Pt(5)
        op2 = otf.add_paragraph()
        op2.text = desc
        op2.font.size = Pt(10)
        op2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s4, 4, 11)

    # ==========================================
    # SLIDE 5: Role & Core Responsibilities (Mapped to Obayashi's Job Description)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, COLOR_BG_LIGHT)
    add_header(s5, "Leadership & Execution", "Your Role & Core Responsibilities: IT Strategy, Operations & Governance")

    # 4 Structured Functional Pillars (2x2 Grid)
    grid_w = Inches(5.72)
    grid_h = Inches(2.45)
    cols = [Inches(0.8), Inches(6.8)]
    rows = [Inches(1.6), Inches(4.3)]

    pillars_data = [
        ("1. IT Strategy, Policy & Enterprise Architecture",
         COLOR_PRIMARY_BLUE,
         [
             "Formulated multi-year technology roadmaps aligning IT investments with organizational growth objectives.",
             "Established standardized IT policies, coding standards, system architectures, and documentation protocols.",
             "Conducted architectural governance reviews to ensure maintainability, scalability, and technical debt reduction.",
             "Evaluated emerging enterprise technologies (cloud, automation, spatial 3D) to drive continuous capability evolution."
         ]),
        ("2. Infrastructure Operations, Cloud & Business Continuity",
         COLOR_ACCENT_BLUE,
         [
             "Ensured 24/7 availability and resilience of mission-critical systems and multi-tier network topologies.",
             "Supervised automated backup regimens, disaster recovery (DR) simulations, and zero-loss business continuity plans.",
             "Managed hybrid cloud workloads, virtualization environments, network security boundaries, and telemetry.",
             "Instituted synthetic monitoring and automated alerting to resolve system anomalies before end-user impact."
         ]),
        ("3. Cybersecurity Controls, Access Management & Risk Mitigation",
         COLOR_ACCENT_RED,
         [
             "Enforced Zero-Trust principles, role-based access control (RBAC), multi-factor authentication (MFA), and audit logging.",
             "Conducted proactive vulnerability assessments, dependency scanning, code audits, and third-party risk evaluations.",
             "Partnered with enterprise compliance teams to ensure strict adherence to ISO 27001 and industry safety standards.",
             "Formulated incident response playbooks, disaster containment procedures, and cybersecurity staff training."
         ]),
        ("4. Team Leadership, Vendor Governance & Fiscal Management",
         COLOR_SUCCESS,
         [
             "Led, mentored, and fostered technical excellence across cross-functional engineering, infrastructure, and QA squads.",
             "Governed multi-vendor contracts, service provider RFPs, cloud infrastructure budgets, and strict SLA compliance.",
             "Optimized CapEx and OpEx allocations through license rationalization, automation, and cloud cost management.",
             "Instituted transparent KPI dashboards tracking uptime, incident resolution MTTR, and engineering delivery velocity."
         ])
    ]

    for idx, (p_title, p_color, p_bullets) in enumerate(pillars_data):
        c_x = cols[idx % 2]
        c_y = rows[idx // 2]
        add_card(s5, c_x, c_y, grid_w, grid_h)

        # Header bar inside card
        hbar = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_x + Inches(0.01), c_y + Inches(0.01), grid_w - Inches(0.02), Inches(0.42))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = p_color
        hbar.line.fill.background()

        htext = s5.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(0.06), grid_w - Inches(0.4), Inches(0.35))
        htf = htext.text_frame
        hp = htf.paragraphs[0]
        hp.text = p_title
        hp.font.size = Pt(11)
        hp.font.bold = True
        hp.font.color.rgb = RGBColor(255, 255, 255)

        # Bullets
        btb = s5.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(0.48), grid_w - Inches(0.4), grid_h - Inches(0.55))
        btf = btb.text_frame
        btf.word_wrap = True
        for b_i, bullet in enumerate(p_bullets):
            bp = btf.paragraphs[0] if b_i == 0 else btf.add_paragraph()
            bp.text = f"• {bullet}"
            bp.font.size = Pt(9.5)
            bp.font.color.rgb = COLOR_TEXT_MAIN
            bp.space_after = Pt(3)

    add_footer(s5, 5, 11)

    # ==========================================
    # SLIDE 6: Major Achievements & Measurable Milestones
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, COLOR_BG_LIGHT)
    add_header(s6, "Business Impact & Value Delivery", "Major Achievements & Quantifiable IT Milestones")

    # 4 Key Metrics Banners at Top
    metrics = [
        ("99.95%+", "Critical System Availability", "Sustained across 24/7 clinical ICU operations and high-traffic event workloads"),
        ("100%", "Data Persistence at Edge", "Zero data loss during field network disconnections via offline-first syncing engine"),
        ("35%", "Faster Release Cycles", "Achieved by implementing automated CI/CD pipelines, containerization & lint tests"),
        ("22%", "Cloud Cost Optimization", "Saved through resource rightsizing, auto-scaling policies, and license rationalization")
    ]
    m_w = Inches(2.78)
    m_h = Inches(1.5)
    for i, (stat, label, detail) in enumerate(metrics):
        mx = Inches(0.8) + i * (m_w + Inches(0.2))
        add_card(s6, mx, Inches(1.6), m_w, m_h, bg_color=RGBColor(255, 255, 255), border_color=COLOR_PRIMARY_BLUE)

        tb = s6.shapes.add_textbox(mx + Inches(0.12), Inches(1.72), m_w - Inches(0.24), m_h - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = stat
        p1.font.size = Pt(24)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_PRIMARY_BLUE
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = label
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_PRIMARY_DARK
        p2.space_after = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = detail
        p3.font.size = Pt(8.5)
        p3.font.color.rgb = COLOR_TEXT_MUTED

    # Bottom Area: 3 Detailed Achievement Deep-Dives
    achievements = [
        ("Enterprise Architecture Modernization & Zero-Downtime Migration",
         "Successfully transformed legacy monolithic systems into modular, API-driven architectures at Cyient/Philips and Technoyana. Reduced regression cycles from weeks to hours and eliminated deployment downtime, ensuring hospital and enterprise operations remained completely uninterrupted during version upgrades."),
        ("Multi-Site Network Resilience & Field Data Integrity Engine",
         "Designed and deployed an edge-resilient synchronization pipeline for environments plagued by unstable cellular and local networks. Handled thousands of concurrent transactional updates offline with automatic background sync and deterministic conflict resolution upon network restoration."),
        ("Enterprise Operational Governance & Multi-Vendor SLA Excellence",
         "Managed cross-functional technical teams (15+ engineers, QA, DevOps) and vendor relationships with infrastructure providers, software vendors, and hardware suppliers. Standardized SLA benchmarks, improved incident MTTR by 40%, and received multiple corporate awards for excellence.")
    ]

    for i, (title, body) in enumerate(achievements):
        ay = Inches(3.3) + i * Inches(1.18)
        add_card(s6, Inches(0.8), ay, Inches(11.733), Inches(1.06))
        atb = s6.shapes.add_textbox(Inches(1.0), ay + Inches(0.12), Inches(11.3), Inches(0.85))
        atf = atb.text_frame
        atf.word_wrap = True

        ap1 = atf.paragraphs[0]
        ap1.text = f"★  {title}"
        ap1.font.size = Pt(12)
        ap1.font.bold = True
        ap1.font.color.rgb = COLOR_PRIMARY_DARK
        ap1.space_after = Pt(3)

        ap2 = atf.add_paragraph()
        ap2.text = body
        ap2.font.size = Pt(9.5)
        ap2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s6, 6, 11)

    # ==========================================
    # SLIDE 7: Challenges Faced & Resolutions Implemented
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, COLOR_BG_LIGHT)
    add_header(s7, "Problem Solving & Crisis Management", "Challenges Faced & Strategic Resolutions Implemented")

    # 3 Structured Rows: Challenge vs. Resolution vs. Business Outcome
    c_cards = [
        ("Challenge 1: Severe Network Fluctuation & Remote Connectivity Drops",
         "Operating conditions at remote event venues and distributed client sites suffered frequent Wi-Fi packet drops, ISP latency spikes, and dead zones, causing cloud disconnects and user data loss.",
         "Resolution Implemented:",
         "Architected an 'Offline-First' state engine using IndexedDB client persistence and service workers. Implemented optimistic UI updates and a transactional event replay queue that automatically resynchronizes once the network reconnects.",
         "Impact: 100% data preservation, zero operator workflow interruptions, seamless user experience."),

        ("Challenge 2: Architectural Fragility & High Downtime Risk in Monolithic Legacy Systems",
         "A legacy codebase had tight coupling between presentation and backend data layers. Deploying bug fixes or new features carried severe risks of regressions and system outages in critical environments.",
         "Resolution Implemented:",
         "Decomposed the monolith into isolated micro-frontends and standardized REST/WebSocket contracts. Established automated unit/integration testing pipelines and canary deployments to validate changes in staging.",
         "Impact: Reduced regression risk to near-zero, cut deployment cycles by 35%, and enabled independent modular upgrades."),

        ("Challenge 3: Complex Multi-Vendor Dependencies & SLA Enforcement Gaps",
         "Dispersed third-party cloud tools, software licenses, and hardware vendors lacked centralized SLA tracking, resulting in finger-pointing during service degradation and creeping monthly cloud expenditure.",
         "Resolution Implemented:",
         "Instituted a centralized IT Governance & SLA Dashboard with automated latency/uptime telemetry. Standardized vendor contract SLAs with penalty clauses, monthly executive reviews, and automated idle resource termination.",
         "Impact: Slashed mean-time-to-resolution (MTTR) by 40% and trimmed overall recurring cloud/vendor spend by 22%.")
    ]

    for i, (ch_title, ch_desc, res_lbl, res_desc, impact) in enumerate(c_cards):
        cy = Inches(1.6) + i * Inches(1.76)
        add_card(s7, Inches(0.8), cy, Inches(11.733), Inches(1.62))

        # Left Column: Challenge (width: 4.8)
        ltb = s7.shapes.add_textbox(Inches(1.0), cy + Inches(0.12), Inches(4.8), Inches(1.4))
        ltf = ltb.text_frame
        ltf.word_wrap = True
        lp1 = ltf.paragraphs[0]
        lp1.text = ch_title
        lp1.font.size = Pt(11.5)
        lp1.font.bold = True
        lp1.font.color.rgb = COLOR_ACCENT_RED
        lp1.space_after = Pt(4)
        lp2 = ltf.add_paragraph()
        lp2.text = ch_desc
        lp2.font.size = Pt(9.5)
        lp2.font.color.rgb = COLOR_TEXT_MAIN

        # Vertical Divider
        vdiv = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.0), cy + Inches(0.15), Inches(0.02), Inches(1.3))
        vdiv.fill.solid()
        vdiv.fill.fore_color.rgb = COLOR_CARD_BORDER
        vdiv.line.fill.background()

        # Right Column: Resolution & Outcome (width: 6.2)
        rtb = s7.shapes.add_textbox(Inches(6.2), cy + Inches(0.12), Inches(6.1), Inches(1.4))
        rtf = rtb.text_frame
        rtf.word_wrap = True
        rp1 = rtf.paragraphs[0]
        rp1.text = res_lbl
        rp1.font.size = Pt(11)
        rp1.font.bold = True
        rp1.font.color.rgb = COLOR_PRIMARY_BLUE
        rp1.space_after = Pt(2)
        rp2 = rtf.add_paragraph()
        rp2.text = res_desc
        rp2.font.size = Pt(9.5)
        rp2.font.color.rgb = COLOR_TEXT_MAIN
        rp2.space_after = Pt(3)
        rp3 = rtf.add_paragraph()
        rp3.text = f"Result: {impact}"
        rp3.font.size = Pt(9.5)
        rp3.font.bold = True
        rp3.font.color.rgb = COLOR_SUCCESS

    add_footer(s7, 7, 11)

    # ==========================================
    # SLIDE 8: Lessons Learned & Operational Best Practices
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, COLOR_BG_LIGHT)
    add_header(s8, "Operational Philosophy", "Lessons Learned & Enterprise Best Practices")

    # 4 Thematic Pillars (Horizontal Cards)
    best_practices = [
        ("1. Resilience Must Be Engineered into the Architecture, Not Added as an Afterthought",
         "In critical operations (whether hospitals or construction job sites), network connectivity and hardware will inevitably experience degradation. Systems must be designed with graceful degradation, local caching, and deterministic reconciliation rather than assuming continuous, low-latency broadband."),
        ("2. Cybersecurity is an Organizational Culture, Not Merely a Perimeter Firewall",
         "A majority of enterprise security breaches stem from misconfigured access rights, third-party vendor credentials, or unpatched endpoints. Implementing Zero Trust Network Access (ZTNA), strict least-privilege RBAC, and continuous security hygiene reviews protects the organization far more effectively than traditional boundary defenses alone."),
        ("3. Proactive Telemetry & Observability Prevents Operational Crises",
         "Waiting for users to report an outage is a failed IT strategy. Instituting synthetic transactions, automated latency monitoring, CPU/memory threshold alerts, and automated runbooks allows IT operations to resolve 80% of potential incidents before end users or project sites notice any disruption."),
        ("4. Technical Leadership Requires Bridging Field Realities with Executive Strategy",
         "Successful IT leadership is not about adopting technology for its own sake; it is about solving concrete business pain points. Spending time understanding how field teams, site managers, and business stakeholders operate ensures IT investments deliver measurable productivity, safety, and financial returns.")
    ]

    for i, (title, desc) in enumerate(best_practices):
        by = Inches(1.6) + i * Inches(1.3)
        add_card(s8, Inches(0.8), by, Inches(11.733), Inches(1.15))

        # Blue Accent Tag on the left of each card
        tag = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), by, Inches(0.12), Inches(1.15))
        tag.fill.solid()
        tag.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        tag.line.fill.background()

        btb = s8.shapes.add_textbox(Inches(1.15), by + Inches(0.12), Inches(11.1), Inches(0.95))
        btf = btb.text_frame
        btf.word_wrap = True

        bp1 = btf.paragraphs[0]
        bp1.text = title
        bp1.font.size = Pt(12)
        bp1.font.bold = True
        bp1.font.color.rgb = COLOR_PRIMARY_DARK
        bp1.space_after = Pt(4)

        bp2 = btf.add_paragraph()
        bp2.text = desc
        bp2.font.size = Pt(9.5)
        bp2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s8, 8, 11)

    # ==========================================
    # SLIDE 9: Suggestions for Future Process Improvements (Tailored for Obayashi)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, COLOR_BG_LIGHT)
    add_header(s9, "Strategic Vision for Obayashi", "Suggestions for Future Process Improvements at Obayashi Corporation")

    # 4 Strategic Improvement Proposals tailored to Obayashi Construction & Engineering
    proposals = [
        ("1. Standardized Construction Site 'IT-in-a-Box' Rapid Deployment Kit",
         "Opportunity: Setting up reliable IT infrastructure at new construction sites often takes weeks and suffers from inconsistent hardware and security standards.",
         "Proposed Solution: Design a containerized 'Site IT Kit' combining dual-SIM 5G/satellite SD-WAN routers, local edge server/caching node, pre-configured biometric access control, and ruggedized Wi-Fi 6 access points. Enables full site IT commissioning within 48 hours with automated zero-touch provisioning."),

        ("2. Cloud BIM & Common Data Environment (CDE) Acceleration Node",
         "Opportunity: Field teams struggle downloading and rendering multi-gigabyte 3D BIM models, CAD drawings, and point clouds over remote job-site cellular connections.",
         "Proposed Solution: Deploy localized edge-caching appliances paired with WebGL-based progressive 3D rendering (leveraging spatial engineering patterns). Site engineers view and markup complex 3D digital twins instantly without saturating job-site uplink bandwidth."),

        ("3. Subcontractor Zero-Trust Security Mesh & Automated Vendor Compliance",
         "Opportunity: General contractors interact with hundreds of specialized subcontractors and vendors, introducing major cybersecurity and intellectual property leakage risks.",
         "Proposed Solution: Establish a cloud-native Zero-Trust Network Access (ZTNA) portal. Subcontractors access only designated project folders with time-bound credentials, multi-factor authentication, watermarked document viewers, and automated endpoint compliance checks."),

        ("4. AIOps for Predictive IT Maintenance & Automated Disaster Recovery (DR)",
         "Opportunity: Unplanned server outages, ISP disconnections, or backup failures at remote regional hubs disrupt critical construction scheduling and bid deadlines.",
         "Proposed Solution: Implement AI-assisted log analysis and telemetry to detect early indicators of disk failure, bandwidth saturation, or cyber anomalies. Pair with automated immutable cloud backups (ransomware-proof) and scheduled push-button disaster recovery failover drills.")
    ]

    for i, (title, opp, sol) in enumerate(proposals):
        py = Inches(1.6) + i * Inches(1.3)
        add_card(s9, Inches(0.8), py, Inches(11.733), Inches(1.18))

        ptb = s9.shapes.add_textbox(Inches(1.05), py + Inches(0.1), Inches(11.2), Inches(1.0))
        ptf = ptb.text_frame
        ptf.word_wrap = True

        p1 = ptf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_PRIMARY_BLUE
        p1.space_after = Pt(2)

        p2 = ptf.add_paragraph()
        p2.text = opp
        p2.font.size = Pt(9.5)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(2)

        p3 = ptf.add_paragraph()
        p3.text = sol
        p3.font.size = Pt(9)
        p3.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s9, 9, 11)

    # ==========================================
    # SLIDE 10: 90-Day Operational Execution Roadmap for Senior Manager – IT
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, COLOR_BG_LIGHT)
    add_header(s10, "Leadership Onboarding & Value Realization", "First 90 Days: Strategic Execution Roadmap for Senior Manager – IT")

    # 3 Phase Cards: Days 1-30, Days 31-60, Days 61-90
    phases = [
        ("Days 1 – 30: Discovery & Baseline Assessment",
         COLOR_PRIMARY_BLUE,
         "Objective: Understand Current State, Build Relationships & Audit Risks",
         [
             "Audit all existing IT infrastructure, networks, cloud tenancies, and active construction site connections.",
             "Interview business unit heads, site project managers, and executive leadership to identify operational bottlenecks.",
             "Review existing cybersecurity controls, backup regimes, DR documentation, and compliance standings.",
             "Analyze IT budget utilization, vendor contracts, software licenses, and current SLA performance metrics."
         ]),
        ("Days 31 – 60: Stabilization & Quick Wins",
         COLOR_ACCENT_BLUE,
         "Objective: Fortify Security, Address Gaps & Streamline Operations",
         [
             "Remediate critical vulnerabilities identified during audit; enforce uniform MFA and access policies.",
             "Optimize job-site connectivity baselines; resolve recurring network instability pain points at active sites.",
             "Consolidate vendor SLAs, eliminate redundant licenses, and introduce transparent IT support ticketing KPIs.",
             "Conduct a full table-top Disaster Recovery (DR) and backup verification exercise to guarantee system resilience."
         ]),
        ("Days 61 – 90: Modernization & Strategic Roadmap",
         COLOR_SUCCESS,
         "Objective: Drive Scalability, Digital Transformation & Long-Term Value",
         [
             "Present a 2-3 Year IT Strategy & Digital Roadmap aligned directly with Obayashi's corporate objectives.",
             "Pilot the 'Site IT-in-a-Box' rapid deployment kit for upcoming construction projects.",
             "Initiate automation initiatives (CI/CD, automated log telemetry, self-service IT service catalog).",
             "Foster continuous team upskilling, mentorship, and technical excellence within the internal IT workforce."
         ])
    ]

    p_w = Inches(3.72)
    p_h = Inches(5.2)
    for i, (p_title, p_col, p_obj, p_tasks) in enumerate(phases):
        px = Inches(0.8) + i * (p_w + Inches(0.28))
        add_card(s10, px, Inches(1.6), p_w, p_h)

        # Header banner
        p_hdr = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, px + Inches(0.01), Inches(1.61), p_w - Inches(0.02), Inches(0.48))
        p_hdr.fill.solid()
        p_hdr.fill.fore_color.rgb = p_col
        p_hdr.line.fill.background()

        ht = s10.shapes.add_textbox(px + Inches(0.12), Inches(1.68), p_w - Inches(0.24), Inches(0.35))
        htf = ht.text_frame
        hp = htf.paragraphs[0]
        hp.text = p_title
        hp.font.size = Pt(11)
        hp.font.bold = True
        hp.font.color.rgb = RGBColor(255, 255, 255)

        # Content
        ct = s10.shapes.add_textbox(px + Inches(0.15), Inches(2.2), p_w - Inches(0.3), Inches(4.4))
        ctf = ct.text_frame
        ctf.word_wrap = True

        op = ctf.paragraphs[0]
        op.text = p_obj
        op.font.size = Pt(9.5)
        op.font.bold = True
        op.font.color.rgb = COLOR_PRIMARY_DARK
        op.space_after = Pt(10)

        for t_i, task in enumerate(p_tasks):
            tp = ctf.add_paragraph()
            tp.text = f"✔ {task}"
            tp.font.size = Pt(9.5)
            tp.font.color.rgb = COLOR_TEXT_MAIN
            tp.space_after = Pt(8)

    add_footer(s10, 10, 11)

    # ==========================================
    # SLIDE 11: Conclusion, Commitment & Q&A
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, COLOR_PRIMARY_DARK)

    # Center card / container
    c_w = Inches(10.5)
    c_h = Inches(5.2)
    cx = Inches(1.416)
    cy = Inches(1.15)
    add_card(s11, cx, cy, c_w, c_h, bg_color=RGBColor(24, 43, 73), border_color=RGBColor(51, 65, 85))

    q_tb = s11.shapes.add_textbox(cx + Inches(0.6), cy + Inches(0.5), c_w - Inches(1.2), c_h - Inches(1.0))
    q_tf = q_tb.text_frame
    q_tf.word_wrap = True

    qp1 = q_tf.paragraphs[0]
    qp1.text = "OBAYASHI CORPORATION · IT LEADERSHIP COMMITMENT"
    qp1.font.size = Pt(12)
    qp1.font.bold = True
    qp1.font.color.rgb = COLOR_ACCENT_RED
    qp1.space_after = Pt(8)

    qp2 = q_tf.add_paragraph()
    qp2.text = "Delivering Reliable, Secure & Future-Ready Technology Services"
    qp2.font.size = Pt(24)
    qp2.font.bold = True
    qp2.font.color.rgb = RGBColor(255, 255, 255)
    qp2.space_after = Pt(14)

    commitments = [
        "Strategic Value Creation: Aligning IT roadmaps directly with Obayashi's engineering excellence and corporate vision.",
        "Operational Dependability: Ensuring 24/7 resilience, zero data loss, and rapid incident resolution across all offices and project job-sites.",
        "Robust Cybersecurity & Risk Mitigation: Protecting critical blueprints, intellectual property, and supply chain integrity with Zero Trust governance.",
        "Collaborative Culture & Team Growth: Mentoring high-performing IT talent while upholding Japanese corporate standards of precision, quality, and mutual respect."
    ]
    for comm in commitments:
        cp = q_tf.add_paragraph()
        cp.text = f"• {comm}"
        cp.font.size = Pt(11)
        cp.font.color.rgb = RGBColor(226, 232, 240)
        cp.space_after = Pt(8)

    qp_contact = q_tf.add_paragraph()
    qp_contact.text = "\nThank you for the opportunity. I look forward to our Final Interview discussion.\nMaheshchandra Hegde  |  hid.mahesh@gmail.com  |  +91 9535253329 / +91 7022407280"
    qp_contact.font.size = Pt(11)
    qp_contact.font.bold = True
    qp_contact.font.color.rgb = RGBColor(56, 189, 248)

    add_footer(s11, 11, 11, dark=True)

    # Save Presentation
    prs.save(output_pptx_path)
    print(f"Successfully generated PowerPoint presentation at: {output_pptx_path}")

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(out_dir, "Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pptx")
    create_deck(out_file)
