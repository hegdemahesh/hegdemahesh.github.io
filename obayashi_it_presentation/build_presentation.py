"""
Script to generate the Executive Work Experience Presentation for Obayashi Corporation
Candidate: Maheshchandra Hegde
Position: Senior Manager - IT
Format: 16:9 Widescreen PowerPoint Presentation (.pptx) - 12 Slides Executive Edition
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(output_pptx_path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

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
    COLOR_CYAN_ACCENT  = RGBColor(56, 189, 248)   # Bright Cyan #38BDF8

    TOTAL_SLIDES = 12

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, category, title, dark=False):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_ACCENT_RED if dark else COLOR_PRIMARY_BLUE

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = RGBColor(255, 255, 255) if dark else COLOR_PRIMARY_DARK

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

    def add_footer(slide, current_page, total_pages=TOTAL_SLIDES, dark=False):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.35))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = f"Obayashi Corporation · Senior Manager – IT Candidate Portfolio | Maheshchandra Hegde · Slide {current_page} of {total_pages}"
        p.font.size = Pt(9)
        p.font.color.rgb = RGBColor(148, 163, 184) if dark else COLOR_TEXT_MUTED

    # ==========================================
    # SLIDE 1: Title Slide (Dark Theme Executive)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLOR_PRIMARY_DARK)

    strip = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(0.3), Inches(5.1))
    strip.fill.solid()
    strip.fill.fore_color.rgb = COLOR_ACCENT_RED
    strip.line.fill.background()

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
    p2.font.color.rgb = COLOR_CYAN_ACCENT
    p2.space_after = Pt(8)

    p3 = tf1.add_paragraph()
    p3.text = "A comprehensive portfolio mapping enterprise technology leadership, mission-critical infrastructure, 3D visualization / spatial AI engineering (Voxelforge AI, ayam3d), and operational resilience to Obayashi's global engineering mandates."
    p3.font.size = Pt(12.5)
    p3.font.color.rgb = RGBColor(203, 213, 225)

    pillars = [
        ("IT Operations & Infra", "High availability, hybrid cloud, disaster recovery & multi-site continuity"),
        ("Cybersecurity & Risk", "Zero Trust, access controls, vulnerability mitigation & ISO compliance"),
        ("3D Visualization & AI", "50+ 3D/CAD projects, Voxelforge AI, ayam3d, spatial digital twins"),
        ("Vendor & Budget Control", "SLA governance, contract management, resource optimization & CapEx/OpEx")
    ]
    card_w = Inches(2.75)
    card_h = Inches(1.35)
    start_x = Inches(1.4)
    start_y = Inches(4.9)
    gap = Inches(0.24)

    for i, (title, desc) in enumerate(pillars):
        cx = start_x + i * (card_w + gap)
        add_card(s1, cx, start_y, card_w, card_h, bg_color=RGBColor(24, 43, 73), border_color=RGBColor(51, 65, 85))
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
        cp2.font.size = Pt(9.5)
        cp2.font.color.rgb = RGBColor(148, 163, 184)

    add_footer(s1, 1, TOTAL_SLIDES, dark=True)

    # ==========================================
    # SLIDE 2: Professional Profile & Strategic Alignment
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, COLOR_BG_LIGHT)
    add_header(s2, "Executive Profile", "Strategic Leadership Profile & Alignment with Obayashi Corporation")

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
    p.text = "Technology Leader · Systems Architect · 3D Spatial Expert"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_BLUE
    p.space_after = Pt(12)

    creds = [
        ("Total Experience", "20+ Years leading enterprise IT, systems architectures & digital delivery"),
        ("Education", "MS in Computing (Robert Gordon Univ., UK) · B.E. in Electronics & Communication"),
        ("Key Tenures", "Cyient (Philips Critical Care), Technoyana, UST Global (Cisco Systems), CAE Simulation, Cognizant"),
        ("Dual Mastery", "Enterprise IT Infrastructure / Cyber + 3D Visualization, CAD, BIM alignment & Spatial AI"),
        ("Industry Domain", "High-Reliability Healthcare, Enterprise Networking Dashboards, 3D Graphics & SaaS")
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

    right_x = Inches(5.25)
    rw = Inches(7.28)
    card_h2 = Inches(1.18)

    alignments = [
        ("1. Multi-Site Infrastructure & High Availability",
         "Proven expertise running mission-critical platforms demanding 99.95%+ uptime. Direct experience engineering resilient edge systems that guarantee business continuity even during remote network dropouts."),
        ("2. Cybersecurity Governance & Risk Mitigation",
         "Strict adherence to compliance frameworks, role-based access governance (RBAC), data protection policies, secure CI/CD pipelines, and active threat vulnerability management."),
        ("3. 3D Spatial Computing & Digital Construction Synergy",
         "Rare blend of enterprise IT governance and hands-on 3D visualization expertise (50+ projects, Voxelforge AI, ayam3d), directly bridging traditional IT with Obayashi's BIM and Digital Twin roadmaps."),
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

    add_footer(s2, 2, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 3: Project 1: Mission-Critical Enterprise System (Philips/Cyient)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, COLOR_BG_LIGHT)
    add_header(s3, "Project Experience 1", "Project Overview: Mission-Critical Clinical Systems (Philips / Cyient)")

    add_card(s3, Inches(0.8), Inches(1.6), Inches(4.3), Inches(5.2))
    p1_tb = s3.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(3.8), Inches(4.8))
    p1_tf = p1_tb.text_frame
    p1_tf.word_wrap = True

    p = p1_tf.paragraphs[0]
    p.text = "Philips ICCA"
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

    add_footer(s3, 3, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 4: Project 2: High-Availability Cloud & Edge Resilience (Technoyana)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, COLOR_BG_LIGHT)
    add_header(s4, "Project Experience 2", "Project Overview: Cloud Transformation & Edge-Resilient Platform (Technoyana)")

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
    p.text = "Digital Transformation & Distributed Cloud Ecosystem"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_BLUE
    p.space_after = Pt(10)

    p2_meta = [
        ("Role", "Co-Founder & Director of Technology / Architecture Lead"),
        ("Tenure", "May 2021 - Oct 2023 (Strategic Advisor)"),
        ("Key Platforms", "Twitan Sports OS (Shutlify), Fintech Operations Engine, Cloud Multi-Tenant Architecture"),
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

    r4_x = Inches(5.35)
    r4_w = Inches(7.18)

    p2_cards = [
        ("1. Edge-Resilient 'Offline-First' Architecture for Unstable Networks",
         "Architected an offline-first data model utilizing local storage, background Service Workers, and optimistic transactional queuing. When on-site network drops occur, field users continue full operations uninterrupted; bi-directional conflict resolution synchronizes cloud data the moment connectivity is restored."),
        ("2. Cloud Infrastructure & Cost Governance (AWS / Firebase / Serverless)",
         "Directed cloud infrastructure roadmap, automated CI/CD pipelines, containerized deployments, and disaster recovery replication. Implemented automated resource scaling and log archiving, cutting monthly cloud spend by 22% while handling 10x traffic bursts."),
        ("3. High-Concurrency Event Telemetry & Operational Uptime",
         "Built resilient real-time WebSocket state channels with automatic fallback to polling, ensuring zero operational downtime for critical tournament arbitration and multi-site scoring dashboards.")
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

    add_footer(s4, 4, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 5: 3D Visualization & Spatial AI Leadership (Voxelforge AI, ayam3d, 50+ Projects)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, COLOR_BG_LIGHT)
    add_header(s5, "Spatial Computing & 3D Engineering", "3D Visualization Pedigree & Spatial AI: Voxelforge AI, ayam3d & 50+ Projects")

    # Left Column: 50+ 3D Projects & Visualizer Expert Track Record (Width: 5.6)
    add_card(s5, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))

    # Badge Bar
    vbar = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.81), Inches(1.61), Inches(5.58), Inches(0.44))
    vbar.fill.solid()
    vbar.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
    vbar.line.fill.background()

    vht = s5.shapes.add_textbox(Inches(0.95), Inches(1.68), Inches(5.3), Inches(0.35))
    vhtf = vht.text_frame
    vhp = vhtf.paragraphs[0]
    vhp.text = "3D VISUALIZER EXPERT: 50+ PROJECTS DELIVERED"
    vhp.font.size = Pt(11)
    vhp.font.bold = True
    vhp.font.color.rgb = RGBColor(255, 255, 255)

    v_tb = s5.shapes.add_textbox(Inches(1.0), Inches(2.15), Inches(5.2), Inches(4.5))
    v_tf = v_tb.text_frame
    v_tf.word_wrap = True

    v_items = [
        ("Architectural Visualization & 3D Walkthroughs (35+ Projects)",
         "Extensive portfolio producing photorealistic architectural visualizations, exterior/interior 3D renderings, and high-impact 3D animated walkthroughs for commercial complexes, residential townships, and infrastructure projects."),
        ("CAE Simulation Technologies (Flight Simulator 3D Databases)",
         "Visual Database Developer creating high-fidelity 3D terrain databases, elevation grids, and precision 3D aircraft models for military and civil flight simulation systems."),
        ("Cisco Systems: Enterprise Facility & Smart Campus 3D Dashboards",
         "Architected rich interactive facility monitoring dashboards visualizing campus physical infrastructure, spatial rack layouts, power utilization, and environmental sensor telemetry."),
        ("CAD & Digital Construction Interoperability",
         "Hands-on expertise bridging 2D CAD blueprints, 3D coordinate geometry, polygonal mesh optimization, Level of Detail (LOD) management, and spatial rendering engines.")
    ]

    for v_i, (vt, vd) in enumerate(v_items):
        vp1 = v_tf.paragraphs[0] if v_i == 0 else v_tf.add_paragraph()
        vp1.text = f"★ {vt}"
        vp1.font.size = Pt(10.5)
        vp1.font.bold = True
        vp1.font.color.rgb = COLOR_PRIMARY_DARK
        vp1.space_after = Pt(2)
        vp2 = v_tf.add_paragraph()
        vp2.text = vd
        vp2.font.size = Pt(9)
        vp2.font.color.rgb = COLOR_TEXT_MUTED
        vp2.space_after = Pt(6)

    # Right Column: Current Flagship Spatial AI Projects: Voxelforge AI & ayam3d (Width: 5.85)
    rx5 = Inches(6.68)
    rw5 = Inches(5.85)

    # Card 1: Voxelforge AI
    add_card(s5, rx5, Inches(1.6), rw5, Inches(1.65))
    vox_tb = s5.shapes.add_textbox(rx5 + Inches(0.2), Inches(1.72), rw5 - Inches(0.4), Inches(1.4))
    vox_tf = vox_tb.text_frame
    vox_tf.word_wrap = True

    vp1 = vox_tf.paragraphs[0]
    vp1.text = "1. Voxelforge AI — Generative 3D Asset Workflows"
    vp1.font.size = Pt(12)
    vp1.font.bold = True
    vp1.font.color.rgb = COLOR_PRIMARY_BLUE
    vp1.space_after = Pt(3)

    vp2 = vox_tf.add_paragraph()
    vp2.text = "• AI-assisted generative 3D pipeline producing game-ready, modular low-poly 3D assets for WebGL, Unity, and Unreal Engine.\n• Automates prompt-to-3D synthesis, texture baking, and real-time polygon reduction, enabling instant browser-based 3D digital twin rendering."
    vp2.font.size = Pt(9.5)
    vp2.font.color.rgb = COLOR_TEXT_MAIN

    # Card 2: ayam3d
    add_card(s5, rx5, Inches(3.38), rw5, Inches(1.65))
    ayam_tb = s5.shapes.add_textbox(rx5 + Inches(0.2), Inches(3.5), rw5 - Inches(0.4), Inches(1.4))
    ayam_tf = ayam_tb.text_frame
    ayam_tf.word_wrap = True

    ap1 = ayam_tf.paragraphs[0]
    ap1.text = "2. ayam3d — Generative Mesh Synthesis & Retopology"
    ap1.font.size = Pt(12)
    ap1.font.bold = True
    ap1.font.color.rgb = COLOR_ACCENT_BLUE
    ap1.space_after = Pt(3)

    ap2 = ayam_tf.add_paragraph()
    ap2.text = "• Advanced spatial computing R&D in automated 3D mesh synthesis, intelligent quad/tri retopology, and PBR (Physically Based Rendering) texture generation.\n• Transforms heavy, raw 3D scans and photogrammetry point clouds into lightweight, optimized assets suitable for real-time edge streaming."
    ap2.font.size = Pt(9.5)
    ap2.font.color.rgb = COLOR_TEXT_MAIN

    # Card 3: Direct Synergy with Obayashi Construction
    add_card(s5, rx5, Inches(5.15), rw5, Inches(1.65), bg_color=RGBColor(240, 249, 255), border_color=COLOR_PRIMARY_BLUE)
    syn_tb = s5.shapes.add_textbox(rx5 + Inches(0.2), Inches(5.27), rw5 - Inches(0.4), Inches(1.4))
    syn_tf = syn_tb.text_frame
    syn_tf.word_wrap = True

    sp1 = syn_tf.paragraphs[0]
    sp1.text = "Direct Synergy with Obayashi Corporation's Vision"
    sp1.font.size = Pt(11.5)
    sp1.font.bold = True
    sp1.font.color.rgb = COLOR_PRIMARY_BLUE
    sp1.space_after = Pt(3)

    sp2 = syn_tf.add_paragraph()
    sp2.text = "• Bridges Enterprise IT with Digital Construction: Unifies BIM (Building Information Modeling 3D/4D/5D), Common Data Environments (CDE), and Digital Twins.\n• Solves the IT infrastructure bottleneck: GPU workstation virtualization, automated asset compression, and low-latency 3D rendering on job-site mobile devices."
    sp2.font.size = Pt(9)
    sp2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s5, 5, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 6: Role & Core Responsibilities (Mapped to Obayashi's Job Description)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, COLOR_BG_LIGHT)
    add_header(s6, "Leadership & Execution", "Your Role & Core Responsibilities: IT Strategy, Operations & Governance")

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
        add_card(s6, c_x, c_y, grid_w, grid_h)

        hbar = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_x + Inches(0.01), c_y + Inches(0.01), grid_w - Inches(0.02), Inches(0.42))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = p_color
        hbar.line.fill.background()

        htext = s6.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(0.06), grid_w - Inches(0.4), Inches(0.35))
        htf = htext.text_frame
        hp = htf.paragraphs[0]
        hp.text = p_title
        hp.font.size = Pt(11)
        hp.font.bold = True
        hp.font.color.rgb = RGBColor(255, 255, 255)

        btb = s6.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(0.48), grid_w - Inches(0.4), grid_h - Inches(0.55))
        btf = btb.text_frame
        btf.word_wrap = True
        for b_i, bullet in enumerate(p_bullets):
            bp = btf.paragraphs[0] if b_i == 0 else btf.add_paragraph()
            bp.text = f"• {bullet}"
            bp.font.size = Pt(9.5)
            bp.font.color.rgb = COLOR_TEXT_MAIN
            bp.space_after = Pt(3)

    add_footer(s6, 6, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 7: Major Achievements & Measurable Milestones
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, COLOR_BG_LIGHT)
    add_header(s7, "Business Impact & Value Delivery", "Major Achievements & Quantifiable IT & Spatial Engineering Milestones")

    metrics = [
        ("99.95%+", "System Availability", "Sustained across 24/7 clinical ICU operations and high-traffic event workloads"),
        ("100%", "Data Persistence at Edge", "Zero data loss during field network disconnections via offline-first syncing engine"),
        ("50+", "3D & Spatial Projects", "Delivered across architectural visualization, CAD, flight simulation & AI workflows"),
        ("22%", "Cloud Cost Optimization", "Saved through resource rightsizing, auto-scaling policies, and license rationalization")
    ]
    m_w = Inches(2.78)
    m_h = Inches(1.5)
    for i, (stat, label, detail) in enumerate(metrics):
        mx = Inches(0.8) + i * (m_w + Inches(0.2))
        add_card(s7, mx, Inches(1.6), m_w, m_h, bg_color=RGBColor(255, 255, 255), border_color=COLOR_PRIMARY_BLUE)

        tb = s7.shapes.add_textbox(mx + Inches(0.12), Inches(1.72), m_w - Inches(0.24), m_h - Inches(0.24))
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

    achievements = [
        ("Enterprise Architecture Modernization & Zero-Downtime Migration",
         "Successfully transformed legacy monolithic systems into modular, API-driven architectures at Cyient/Philips and Technoyana. Reduced regression cycles from weeks to hours and eliminated deployment downtime, ensuring hospital and enterprise operations remained completely uninterrupted during version upgrades."),
        ("Multi-Site Network Resilience & Field Data Integrity Engine",
         "Designed and deployed an edge-resilient synchronization pipeline for environments plagued by unstable cellular and local networks. Handled thousands of concurrent transactional updates offline with automatic background sync and deterministic conflict resolution upon network restoration."),
        ("Spatial 3D Asset Pipelines & Generative AI Innovation (Voxelforge AI / ayam3d)",
         "Successfully built scalable automated pipelines converting complex 3D meshes into real-time, low-poly assets with automated retopology and PBR texturing. Unlocked web-based 3D digital twin rendering without requiring expensive on-site graphics hardware."),
        ("Enterprise Operational Governance & Multi-Vendor SLA Excellence",
         "Managed cross-functional technical teams (15+ engineers, QA, DevOps) and vendor relationships with infrastructure providers, software vendors, and hardware suppliers. Standardized SLA benchmarks, improved incident MTTR by 40%, and received multiple corporate awards for excellence.")
    ]

    for i, (title, body) in enumerate(achievements):
        ay = Inches(3.25) + i * Inches(0.92)
        add_card(s7, Inches(0.8), ay, Inches(11.733), Inches(0.84))
        atb = s7.shapes.add_textbox(Inches(1.0), ay + Inches(0.08), Inches(11.3), Inches(0.68))
        atf = atb.text_frame
        atf.word_wrap = True

        ap1 = atf.paragraphs[0]
        ap1.text = f"★  {title}"
        ap1.font.size = Pt(11)
        ap1.font.bold = True
        ap1.font.color.rgb = COLOR_PRIMARY_DARK
        ap1.space_after = Pt(2)

        ap2 = atf.add_paragraph()
        ap2.text = body
        ap2.font.size = Pt(9)
        ap2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s7, 7, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 8: Challenges Faced & Resolutions Implemented
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, COLOR_BG_LIGHT)
    add_header(s8, "Problem Solving & Crisis Management", "Challenges Faced & Strategic Resolutions Implemented")

    c_cards = [
        ("Challenge 1: Severe Network Fluctuation & Remote Connectivity Drops",
         "Operating conditions at remote event venues and distributed client sites suffered frequent Wi-Fi packet drops, ISP latency spikes, and dead zones, causing cloud disconnects and user data loss.",
         "Resolution Implemented:",
         "Architected an 'Offline-First' state engine using IndexedDB client persistence and service workers. Implemented optimistic UI updates and a transactional event replay queue that automatically resynchronizes once the network reconnects.",
         "Impact: 100% data preservation, zero operator workflow interruptions, seamless user experience."),

        ("Challenge 2: High Bandwidth Saturation & Latency Rendering Heavy 3D Assets on Edge Devices",
         "Heavy 3D models, complex CAD geometry, and unoptimized high-poly meshes caused browser crashes, memory overflows, and unacceptable load times over mobile job-site networks.",
         "Resolution Implemented:",
         "Leveraged Voxelforge AI and ayam3d retopology algorithms to automate progressive LOD (Level of Detail) mesh compression and texture atlas baking, paired with client-side WebGL progressive loading.",
         "Impact: Slashed 3D asset file sizes by 75%, achieved 60 FPS rendering on mobile devices without expensive GPU workstations."),

        ("Challenge 3: Complex Multi-Vendor Dependencies & SLA Enforcement Gaps",
         "Dispersed third-party cloud tools, software licenses, and hardware vendors lacked centralized SLA tracking, resulting in finger-pointing during service degradation and creeping monthly cloud expenditure.",
         "Resolution Implemented:",
         "Instituted a centralized IT Governance & SLA Dashboard with automated latency/uptime telemetry. Standardized vendor contract SLAs with penalty clauses, monthly executive reviews, and automated idle resource termination.",
         "Impact: Slashed mean-time-to-resolution (MTTR) by 40% and trimmed recurring cloud/vendor spend by 22%.")
    ]

    for i, (ch_title, ch_desc, res_lbl, res_desc, impact) in enumerate(c_cards):
        cy = Inches(1.6) + i * Inches(1.76)
        add_card(s8, Inches(0.8), cy, Inches(11.733), Inches(1.62))

        ltb = s8.shapes.add_textbox(Inches(1.0), cy + Inches(0.12), Inches(4.8), Inches(1.4))
        ltf = ltb.text_frame
        ltf.word_wrap = True
        lp1 = ltf.paragraphs[0]
        lp1.text = ch_title
        lp1.font.size = Pt(11)
        lp1.font.bold = True
        lp1.font.color.rgb = COLOR_ACCENT_RED
        lp1.space_after = Pt(3)
        lp2 = ltf.add_paragraph()
        lp2.text = ch_desc
        lp2.font.size = Pt(9)
        lp2.font.color.rgb = COLOR_TEXT_MAIN

        vdiv = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.0), cy + Inches(0.15), Inches(0.02), Inches(1.3))
        vdiv.fill.solid()
        vdiv.fill.fore_color.rgb = COLOR_CARD_BORDER
        vdiv.line.fill.background()

        rtb = s8.shapes.add_textbox(Inches(6.2), cy + Inches(0.12), Inches(6.1), Inches(1.4))
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
        rp2.font.size = Pt(9)
        rp2.font.color.rgb = COLOR_TEXT_MAIN
        rp2.space_after = Pt(3)
        rp3 = rtf.add_paragraph()
        rp3.text = f"Result: {impact}"
        rp3.font.size = Pt(9)
        rp3.font.bold = True
        rp3.font.color.rgb = COLOR_SUCCESS

    add_footer(s8, 8, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 9: Lessons Learned & Operational Best Practices
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, COLOR_BG_LIGHT)
    add_header(s9, "Operational Philosophy", "Lessons Learned & Enterprise Best Practices")

    best_practices = [
        ("1. Resilience Must Be Engineered into the Architecture, Not Added as an Afterthought",
         "In critical operations (whether hospitals or construction job sites), network connectivity and hardware will inevitably experience degradation. Systems must be designed with graceful degradation, local caching, and deterministic reconciliation rather than assuming continuous, low-latency broadband."),
        ("2. Cybersecurity is an Organizational Culture, Not Merely a Perimeter Firewall",
         "A majority of enterprise security breaches stem from misconfigured access rights, third-party vendor credentials, or unpatched endpoints. Implementing Zero Trust Network Access (ZTNA), strict least-privilege RBAC, and continuous security hygiene reviews protects the organization far more effectively than traditional boundary defenses alone."),
        ("3. Proactive Telemetry & Observability Prevents Operational Crises",
         "Waiting for users to report an outage is a failed IT strategy. Instituting synthetic transactions, automated latency monitoring, CPU/memory threshold alerts, and automated runbooks allows IT operations to resolve 80% of potential incidents before end users or project sites notice any disruption."),
        ("4. Bridging 3D Engineering Realities with Corporate IT Strategy",
         "In modern engineering corporations, IT is no longer just back-office software; it is the backbone for heavy 3D CAD/BIM pipelines, digital twins, and job-site spatial data. IT leadership must understand 3D data workflows to provide infrastructure that accelerates rather than slows down engineering production.")
    ]

    for i, (title, desc) in enumerate(best_practices):
        by = Inches(1.6) + i * Inches(1.3)
        add_card(s9, Inches(0.8), by, Inches(11.733), Inches(1.15))

        tag = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), by, Inches(0.12), Inches(1.15))
        tag.fill.solid()
        tag.fill.fore_color.rgb = COLOR_PRIMARY_BLUE
        tag.line.fill.background()

        btb = s9.shapes.add_textbox(Inches(1.15), by + Inches(0.12), Inches(11.1), Inches(0.95))
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

    add_footer(s9, 9, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 10: Suggestions for Future Process Improvements (Tailored for Obayashi)
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, COLOR_BG_LIGHT)
    add_header(s10, "Strategic Vision for Obayashi", "Suggestions for Future Process Improvements at Obayashi Corporation")

    proposals = [
        ("1. Standardized Construction Site 'IT-in-a-Box' Rapid Deployment Kit",
         "Opportunity: Setting up reliable IT infrastructure at new construction sites often takes weeks and suffers from inconsistent hardware and security standards.",
         "Proposed Solution: Design a containerized 'Site IT Kit' combining dual-SIM 5G/satellite SD-WAN routers, local edge server/caching node, pre-configured biometric access control, and ruggedized Wi-Fi 6 access points. Enables full site IT commissioning within 48 hours with automated zero-touch provisioning."),

        ("2. Cloud BIM & Common Data Environment (CDE) Acceleration Node (Powered by Spatial 3D Tech)",
         "Opportunity: Field teams struggle downloading and rendering multi-gigabyte 3D BIM models, CAD drawings, and point clouds over remote job-site cellular connections.",
         "Proposed Solution: Deploy localized edge-caching appliances paired with Voxelforge AI / ayam3d retopology and WebGL progressive 3D rendering. Site engineers view and markup complex 3D digital twins instantly without saturating job-site uplink bandwidth."),

        ("3. Subcontractor Zero-Trust Security Mesh & Automated Vendor Compliance",
         "Opportunity: General contractors interact with hundreds of specialized subcontractors and vendors, introducing major cybersecurity and intellectual property leakage risks.",
         "Proposed Solution: Establish a cloud-native Zero-Trust Network Access (ZTNA) portal. Subcontractors access only designated project folders with time-bound credentials, multi-factor authentication, watermarked document viewers, and automated endpoint compliance checks."),

        ("4. AIOps for Predictive IT Maintenance & Automated Disaster Recovery (DR)",
         "Opportunity: Unplanned server outages, ISP disconnections, or backup failures at remote regional hubs disrupt critical construction scheduling and bid deadlines.",
         "Proposed Solution: Implement AI-assisted log analysis and telemetry to detect early indicators of disk failure, bandwidth saturation, or cyber anomalies. Pair with automated immutable cloud backups (ransomware-proof) and scheduled push-button disaster recovery failover drills.")
    ]

    for i, (title, opp, sol) in enumerate(proposals):
        py = Inches(1.6) + i * Inches(1.3)
        add_card(s10, Inches(0.8), py, Inches(11.733), Inches(1.18))

        ptb = s10.shapes.add_textbox(Inches(1.05), py + Inches(0.1), Inches(11.2), Inches(1.0))
        ptf = ptb.text_frame
        ptf.word_wrap = True

        p1 = ptf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(11.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_PRIMARY_BLUE
        p1.space_after = Pt(2)

        p2 = ptf.add_paragraph()
        p2.text = opp
        p2.font.size = Pt(9)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_after = Pt(2)

        p3 = ptf.add_paragraph()
        p3.text = sol
        p3.font.size = Pt(8.5)
        p3.font.color.rgb = COLOR_TEXT_MUTED

    add_footer(s10, 10, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 11: 90-Day Operational Execution Roadmap for Senior Manager – IT
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, COLOR_BG_LIGHT)
    add_header(s11, "Leadership Onboarding & Value Realization", "First 90 Days: Strategic Execution Roadmap for Senior Manager – IT")

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
        add_card(s11, px, Inches(1.6), p_w, p_h)

        p_hdr = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, px + Inches(0.01), Inches(1.61), p_w - Inches(0.02), Inches(0.48))
        p_hdr.fill.solid()
        p_hdr.fill.fore_color.rgb = p_col
        p_hdr.line.fill.background()

        ht = s11.shapes.add_textbox(px + Inches(0.12), Inches(1.68), p_w - Inches(0.24), Inches(0.35))
        htf = ht.text_frame
        hp = htf.paragraphs[0]
        hp.text = p_title
        hp.font.size = Pt(11)
        hp.font.bold = True
        hp.font.color.rgb = RGBColor(255, 255, 255)

        ct = s11.shapes.add_textbox(px + Inches(0.15), Inches(2.2), p_w - Inches(0.3), Inches(4.4))
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

    add_footer(s11, 11, TOTAL_SLIDES)

    # ==========================================
    # SLIDE 12: Conclusion, Commitment & Q&A
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, COLOR_PRIMARY_DARK)

    c_w = Inches(10.5)
    c_h = Inches(5.2)
    cx = Inches(1.416)
    cy = Inches(1.15)
    add_card(s12, cx, cy, c_w, c_h, bg_color=RGBColor(24, 43, 73), border_color=RGBColor(51, 65, 85))

    q_tb = s12.shapes.add_textbox(cx + Inches(0.6), cy + Inches(0.5), c_w - Inches(1.2), c_h - Inches(1.0))
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
        "Digital Construction & 3D Synergy: Leveraging 50+ project visualization pedigree, Voxelforge AI, and ayam3d to power next-generation BIM and digital twins.",
        "Robust Cybersecurity & Risk Mitigation: Protecting critical blueprints, intellectual property, and supply chain integrity with Zero Trust governance.",
        "Collaborative Culture & Team Growth: Mentoring high-performing IT talent while upholding Japanese corporate standards of precision, quality, and mutual respect."
    ]
    for comm in commitments:
        cp = q_tf.add_paragraph()
        cp.text = f"• {comm}"
        cp.font.size = Pt(10.5)
        cp.font.color.rgb = RGBColor(226, 232, 240)
        cp.space_after = Pt(7)

    qp_contact = q_tf.add_paragraph()
    qp_contact.text = "\nThank you for the opportunity. I look forward to our Final Interview discussion.\nMaheshchandra Hegde  |  hid.mahesh@gmail.com  |  +91 9535253329 / +91 7022407280"
    qp_contact.font.size = Pt(11)
    qp_contact.font.bold = True
    qp_contact.font.color.rgb = COLOR_CYAN_ACCENT

    add_footer(s12, 12, TOTAL_SLIDES, dark=True)

    prs.save(output_pptx_path)
    print(f"Successfully generated 12-Slide PowerPoint presentation at: {output_pptx_path}")

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(out_dir, "Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pptx")
    create_deck(out_file)
