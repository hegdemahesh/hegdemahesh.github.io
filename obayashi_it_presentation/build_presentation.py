"""
Script to generate the Technical Work Experience Presentation for Maheshchandra Hegde
Three Major Sections:
1. Introduction & Executive Profile (with Photo)
2. Project / Experience Skillset (Grouped by Client: 1 to 8)
3. Conclusion: Role Fit & Self-Training / Certification Pledge

Format: 16:9 Widescreen PowerPoint Presentation (.pptx)
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

    # Elegant Executive Color Palette
    COLOR_PRIMARY_DARK = RGBColor(15, 23, 42)     # Slate 900 #0F172A
    COLOR_PRIMARY_BLUE = RGBColor(2, 132, 199)    # Sky / Tech Blue #0284C7
    COLOR_BRAND_DEEP   = RGBColor(14, 116, 144)   # Deep Ocean Teal #0E7490
    COLOR_ACCENT_AMBER = RGBColor(217, 119, 6)    # Warm Amber #D97706
    COLOR_BG_LIGHT     = RGBColor(248, 250, 252)  # Canvas Light #F8FAFC
    COLOR_CARD_BG      = RGBColor(255, 255, 255)  # Pure White #FFFFFF
    COLOR_CARD_BORDER  = RGBColor(226, 232, 240)  # Border Subtle #E2E8F0
    COLOR_TEXT_MAIN    = RGBColor(30, 41, 59)     # Slate 800 #1E293B
    COLOR_TEXT_MUTED   = RGBColor(100, 116, 139)  # Slate 500 #64748B
    COLOR_SUCCESS      = RGBColor(16, 149, 99)    # Emerald Green #109563
    COLOR_CYAN_ACCENT  = RGBColor(56, 189, 248)   # Cyan #38BDF8

    TOTAL_SLIDES = 9
    script_dir = os.path.dirname(os.path.abspath(__file__))
    photo_path = os.path.join(script_dir, "maheshForResume.jpg")

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, section_tag, title, dark=False):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = section_tag.upper()
        p_cat.font.size = Pt(10.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_CYAN_ACCENT if dark else COLOR_BRAND_DEEP

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
        line.fill.fore_color.rgb = RGBColor(51, 65, 85) if dark else COLOR_CARD_BORDER
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
        p.text = f"Maheshchandra Hegde · Technical Work Experience Presentation | Slide {current_page} of {total_pages}"
        p.font.size = Pt(9)
        p.font.color.rgb = RGBColor(148, 163, 184) if dark else COLOR_TEXT_MUTED

    # =========================================================================
    # SLIDE 1: SECTION 1 — INTRODUCTION & EXECUTIVE PROFILE (WITH PHOTO)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLOR_PRIMARY_DARK)

    # Left Column: Candidate Photo & Contact Details Card
    card_photo = add_card(s1, Inches(0.8), Inches(0.8), Inches(3.4), Inches(5.95),
                          bg_color=RGBColor(24, 34, 53), border_color=RGBColor(51, 65, 85))

    if os.path.exists(photo_path):
        s1.shapes.add_picture(photo_path, Inches(1.0), Inches(1.0), Inches(3.0), Inches(4.0))

    # Contact Info beneath photo
    c_box = s1.shapes.add_textbox(Inches(0.9), Inches(5.1), Inches(3.2), Inches(1.5))
    ctf = c_box.text_frame
    ctf.word_wrap = True
    ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = 0

    cp = ctf.paragraphs[0]
    cp.text = "Bangalore, India"
    cp.font.size = Pt(9.5)
    cp.font.bold = True
    cp.font.color.rgb = RGBColor(226, 232, 240)

    cp = ctf.add_paragraph()
    cp.text = "+91 9535253329 / 7022407280"
    cp.font.size = Pt(9)
    cp.font.color.rgb = RGBColor(203, 213, 225)

    cp = ctf.add_paragraph()
    cp.text = "hid.mahesh@gmail.com"
    cp.font.size = Pt(9)
    cp.font.color.rgb = COLOR_CYAN_ACCENT

    cp = ctf.add_paragraph()
    cp.text = "hegdemahesh.in | linkedin.com/in/maheshchandrahegde"
    cp.font.size = Pt(8.5)
    cp.font.color.rgb = COLOR_CYAN_ACCENT

    # Right Column: Name, LinkedIn Headline, and Summary
    rw = Inches(8.1)
    rx = Inches(4.45)

    add_card(s1, rx, Inches(0.8), rw, Inches(5.95),
             bg_color=RGBColor(24, 34, 53), border_color=RGBColor(51, 65, 85))

    t_box = s1.shapes.add_textbox(rx + Inches(0.4), Inches(1.05), rw - Inches(0.8), Inches(5.4))
    tf = t_box.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "SECTION 1 · EXECUTIVE INTRODUCTION"
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_CYAN_ACCENT
    p0.space_after = Pt(4)

    p1 = tf.add_paragraph()
    p1.text = "Maheshchandra Hegde"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    p1.space_after = Pt(4)

    p2 = tf.add_paragraph()
    p2.text = "Founder & CTO | Building AI‑Driven 3D Asset Platforms & Spatial Computing Solutions @srushtilabs.com"
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_PRIMARY_BLUE
    p2.space_after = Pt(12)

    p_sum = tf.add_paragraph()
    p_sum.text = (
        "Innovative technologist and product strategist with 18+ years of experience architecting end-to-end digital products, "
        "interactive 3D experiences, and domain-specific SaaS platforms. Co-Founder and Technology Leader at Technoyana Digital "
        "Transformation Services Pvt. Ltd., driving product architecture and creative tech vision across flagship divisions:\n\n"
        "• Twitan.com — AI-driven sports management app & operational SaaS suite (Shutlify badminton OS).\n"
        "• Srushtilabs.com — Generative AI & modular 3D computing platform for games, simulations, and 3D visualization.\n\n"
        "Holds a postgraduate degree in Human Interface Design & Development (M.S. in Computing, Robert Gordon University, UK) "
        "and an engineering background in Electronics & Communication (B.E.). Expertise spans modern web/mobile stacks "
        "(React, TypeScript, Angular, Web Components, Node.js, Firebase), interactive 3D/PBR pipelines, and design-to-code automation."
    )
    p_sum.font.size = Pt(10)
    p_sum.font.color.rgb = RGBColor(203, 213, 225)
    p_sum.space_after = Pt(10)

    p_arc = tf.add_paragraph()
    p_arc.text = (
        "Architectural Heritage: Growing up assisting my architect father in his studio provided my earliest practical foundation in "
        "architectural drawings, CAD drafting, and spatial visualization—cultivating a natural synergy between software systems and 3D engineering."
    )
    p_arc.font.size = Pt(9.5)
    p_arc.font.italic = True
    p_arc.font.color.rgb = RGBColor(148, 163, 184)

    add_footer(s1, 1, TOTAL_SLIDES, dark=True)

    # =========================================================================
    # SLIDE 2: SECTION 2 — GROUP 1: TECHNOYANA & SRUSHTILABS (VOXELFORGE & AYAM3D)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, COLOR_BG_LIGHT)
    add_header(s2, "Section 2 · Project Experience (Client Group 1)", "Technoyana & SrushtiLabs: Generative 3D Platforms & Spatial Computing")

    c_w = Inches(5.72)
    c_h = Inches(5.2)

    # Left: Voxelforge AI
    add_card(s2, Inches(0.8), Inches(1.6), c_w, c_h)
    tb1 = s2.shapes.add_textbox(Inches(1.0), Inches(1.8), c_w - Inches(0.4), c_h - Inches(0.4))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "Voxelforge AI"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Modular 3D Generative AI Platform | srushtilabs.com/voxelforge/"
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_BRAND_DEEP
    p_sub.space_after = Pt(12)

    v_points = [
        ("Role & Entity", "Founder & CTO at SrushtiLabs (Technoyana Digital Transformation Services Pvt. Ltd.)."),
        ("Core Product Innovation", "Developed Voxelforge AI, a generative AI product creating modular 3D assets based on user prompt inputs."),
        ("Multi-Platform Assembly", "Produces game-ready, low-poly 3D models and bundles optimized for immediate integration into Unreal Engine, Unity, and real-time WebGL engines."),
        ("Design-to-Asset Speed", "Automates prompt-to-3D geometry conversion, texture baking, and polygon optimization, reducing prototyping turnaround from days to minutes."),
        ("Live Demonstration", "Fully functional application deployed and accessible at srushtilabs.com/voxelforge/.")
    ]
    for lbl, val in v_points:
        vp = tf1.add_paragraph()
        vp.text = f"• {lbl}: "
        vp.font.bold = True
        vp.font.size = Pt(10)
        vp.font.color.rgb = COLOR_PRIMARY_DARK
        vp2 = tf1.add_paragraph()
        vp2.text = f"  {val}"
        vp2.font.size = Pt(9.5)
        vp2.font.color.rgb = COLOR_TEXT_MUTED
        vp2.space_after = Pt(6)

    # Right: Ayam3d
    add_card(s2, Inches(6.8), Inches(1.6), c_w, c_h)
    tb2 = s2.shapes.add_textbox(Inches(7.0), Inches(1.8), c_w - Inches(0.4), c_h - Inches(0.4))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "Ayam3d (Ayam = Dimension)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p_sub2 = tf2.add_paragraph()
    p_sub2.text = "Parametric AI 3D Model Generation | ayam3d.in"
    p_sub2.font.size = Pt(11)
    p_sub2.font.bold = True
    p_sub2.font.color.rgb = COLOR_PRIMARY_BLUE
    p_sub2.space_after = Pt(12)

    a_points = [
        ("Concept & Vision", "Extended the Voxelforge concept into Ayam3d ('Ayam' meaning Dimension), focusing on parametric-based 3D model generation from natural language prompts."),
        ("Instant Generation", "Emphasizes generating structured 3D models in seconds utilizing custom trained AI models and geometric constraint solvers."),
        ("Investor Interest", "Successfully generated early investor interest, validating the commercial potential of real-time generative 3D synthesis for digital twins, architecture, and games."),
        ("Active Development", "Currently under active development; seeking strategic industry partners and promoters to scale the underlying AI pipeline."),
        ("Application Reference", "Preliminary landing page and concept documentation available at ayam3d.in.")
    ]
    for lbl, val in a_points:
        ap = tf2.add_paragraph()
        ap.text = f"• {lbl}: "
        ap.font.bold = True
        ap.font.size = Pt(10)
        ap.font.color.rgb = COLOR_PRIMARY_DARK
        ap2 = tf2.add_paragraph()
        ap2.text = f"  {val}"
        ap2.font.size = Pt(9.5)
        ap2.font.color.rgb = COLOR_TEXT_MUTED
        ap2.space_after = Pt(6)

    add_footer(s2, 2, TOTAL_SLIDES)

    # =========================================================================
    # SLIDE 3: SECTION 2 — GROUP 2: CYIENT / PHILIPS HEALTHCARE (ICCA)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, COLOR_BG_LIGHT)
    add_header(s3, "Section 2 · Project Experience (Client Group 2)", "Cyient / PHILIPS: Intellispace Critical Care & Anesthesia (ICCA)")

    # Left: Project Scope Card (Width: 4.5)
    add_card(s3, Inches(0.8), Inches(1.6), Inches(4.5), Inches(5.2))
    p3_tb = s3.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(4.0), Inches(4.8))
    p3_tf = p3_tb.text_frame
    p3_tf.word_wrap = True

    p = p3_tf.paragraphs[0]
    p.text = "Philips ICCA"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p = p3_tf.add_paragraph()
    p.text = "Intellispace Critical Care & Anesthesia"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_BRAND_DEEP
    p.space_after = Pt(10)

    p3_meta = [
        ("Role", "Senior Technology Leader (React / NodeJS)"),
        ("Tenure", "Nov 2023 – Mar 2025"),
        ("Client & Facility", "Cyient Limited for Philips Healthcare, Bangalore"),
        ("Operational Reality", "Mission-critical hospital ICU and anesthesia suites operating continuously 24/7."),
        ("Delivery Mandate", "Delivered clinical software passing all stringent quality, reliability, and security gates established by Philips and hospital networks.")
    ]
    for lbl, val in p3_meta:
        p = p3_tf.add_paragraph()
        p.text = f"{lbl}: "
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_PRIMARY_DARK
        p2 = p3_tf.add_paragraph()
        p2.text = f"{val}"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.space_after = Pt(6)

    # Right: 3 Core Pillars of Execution (Width: 6.98)
    r3_x = Inches(5.55)
    r3_w = Inches(6.98)

    p3_cards = [
        ("1. Rigorous Quality Benchmarks & Zero-Downtime Reliability",
         "Successfully delivered the software to meet demanding medical quality requirements set by Philips and healthcare providers. Architected fail-safe clinical data rendering with zero memory leaks, ensuring bedside patient monitoring displays remain completely responsive across multi-day uninterrupted operations."),
        ("2. Comprehensive Security Architecture & Policy Enforcement",
         "Enforced strict enterprise cybersecurity measures as per Philips global policies: integrated Multi-Factor Authentication (MFA), protected against Cross-Site Scripting (XSS) and injection vulnerabilities, enforced role-based access control (RBAC), and maintained immutable audit logs for sensitive patient medical data."),
        ("3. End-to-End Best Practices & Scalable Modular Delivery",
         "Led the end-to-end technical execution—from architectural design and modular component breakdown to automated test suites and production deployment. Delivered a fully supported software product backed by complete documentation and service support protocols.")
    ]

    for i, (title, desc) in enumerate(p3_cards):
        cy = Inches(1.6) + i * Inches(1.76)
        add_card(s3, r3_x, cy, r3_w, Inches(1.6))
        otb = s3.shapes.add_textbox(r3_x + Inches(0.2), cy + Inches(0.15), r3_w - Inches(0.4), Inches(1.3))
        otf = otb.text_frame
        otf.word_wrap = True
        op1 = otf.paragraphs[0]
        op1.text = title
        op1.font.size = Pt(12)
        op1.font.bold = True
        op1.font.color.rgb = COLOR_PRIMARY_BLUE
        op1.space_after = Pt(5)
        op2 = otf.add_paragraph()
        op2.text = desc
        op2.font.size = Pt(9.5)
        op2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s3, 3, TOTAL_SLIDES)

    # =========================================================================
    # SLIDE 4: SECTION 2 — GROUP 3 & 4: NESS DIGITAL & MOONRAFT INNOVATION LABS
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, COLOR_BG_LIGHT)
    add_header(s4, "Section 2 · Project Experience (Client Groups 3 & 4)", "Ness Digital Engineering & Moonraft Innovation Labs (UST Global Unit)")

    # Left: Ness Digital Engineering
    add_card(s4, Inches(0.8), Inches(1.6), c_w, c_h)
    tb_n = s4.shapes.add_textbox(Inches(1.0), Inches(1.8), c_w - Inches(0.4), c_h - Inches(0.4))
    tf_n = tb_n.text_frame
    tf_n.word_wrap = True

    p = tf_n.paragraphs[0]
    p.text = "Ness Digital Engineering"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p_sub = tf_n.add_paragraph()
    p_sub.text = "Senior Analyst / Tech Lead | Oct 2019 – Apr 2020"
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_BRAND_DEEP
    p_sub.space_after = Pt(12)

    n_points = [
        ("Project Focus", "Entertainment Management Application for a major client."),
        ("Technology Stack", "Angular, TypeScript, AWS cloud infrastructure, Node.js."),
        ("System Architecture", "Architected the complete single-page application structure, establishing clean state management and secure API communication layers."),
        ("Standards & Best Practices", "Enforced accessibility standards (WCAG), code quality linters, and strict frontend security guidelines across the engineering team."),
        ("Technical Leadership", "Led the development squad through agile sprints, code reviews, and end-to-end technical deployment to client environments on schedule.")
    ]
    for lbl, val in n_points:
        np = tf_n.add_paragraph()
        np.text = f"• {lbl}: "
        np.font.bold = True
        np.font.size = Pt(10)
        np.font.color.rgb = COLOR_PRIMARY_DARK
        np2 = tf_n.add_paragraph()
        np2.text = f"  {val}"
        np2.font.size = Pt(9.5)
        np2.font.color.rgb = COLOR_TEXT_MUTED
        np2.space_after = Pt(6)

    # Right: Moonraft Innovation Labs
    add_card(s4, Inches(6.8), Inches(1.6), c_w, c_h)
    tb_m = s4.shapes.add_textbox(Inches(7.0), Inches(1.8), c_w - Inches(0.4), c_h - Inches(0.4))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True

    p = tf_m.paragraphs[0]
    p.text = "Moonraft Innovation Labs"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p_sub = tf_m.add_paragraph()
    p_sub.text = "UI Architect | May 2019 – Jul 2019 (UST Global Specialized Unit)"
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_PRIMARY_BLUE
    p_sub.space_after = Pt(12)

    m_points = [
        ("Enterprise Design System", "Architected and engineered a centralized cross-framework UI Design System using LitElement Web Components, React, AngularJS, Node.js, and npm packaging."),
        ("Eliminated Duplication", "Stored all standardized UI components in a central repository, preventing teams from reinventing the wheel for new client projects."),
        ("Unified Look & Feel", "Guaranteed visual consistency and brand coherence across all digital products from a single, shared codebase."),
        ("Automated Upgradability", "When the core component library is updated, client projects automatically inherit updates and enhancements via standard package management."),
        ("Luxury Hotel Mobile App", "Led mobile application development for a premier Indian hotel group (TLC Group of Hotels) built using Ionic and Angular.")
    ]
    for lbl, val in m_points:
        mp = tf_m.add_paragraph()
        mp.text = f"• {lbl}: "
        mp.font.bold = True
        mp.font.size = Pt(10)
        mp.font.color.rgb = COLOR_PRIMARY_DARK
        mp2 = tf_m.add_paragraph()
        mp2.text = f"  {val}"
        mp2.font.size = Pt(9.5)
        mp2.font.color.rgb = COLOR_TEXT_MUTED
        mp2.space_after = Pt(6)

    add_footer(s4, 4, TOTAL_SLIDES)

    # =========================================================================
    # SLIDE 5: SECTION 2 — GROUP 5: UST GLOBAL / CISCO (STADIUM VISION DIRECTOR)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, COLOR_BG_LIGHT)
    add_header(s5, "Section 2 · Project Experience (Client Group 5)", "UST Global / CISCO: Stadium Vision Director Migration")

    # Left: Project Overview Card
    add_card(s5, Inches(0.8), Inches(1.6), Inches(4.5), Inches(5.2))
    p5_tb = s5.shapes.add_textbox(Inches(1.05), Inches(1.8), Inches(4.0), Inches(4.8))
    p5_tf = p5_tb.text_frame
    p5_tf.word_wrap = True

    p = p5_tf.paragraphs[0]
    p.text = "Cisco Stadium Vision"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p = p5_tf.add_paragraph()
    p.text = "Stadium Vision Director Enterprise Platform"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_BRAND_DEEP
    p.space_after = Pt(10)

    p5_meta = [
        ("Role", "Senior Analyst & Associate Project Manager"),
        ("Tenure", "Feb 2015 – Feb 2019 (4+ Years Dedicated Tenure)"),
        ("Client", "Cisco Systems India Private Limited via UST Global"),
        ("Product Scope", "Centralized digital media, live video distribution, and dynamic stadium display management deployed at major international sporting arenas."),
        ("Core Mandate", "Modernize a massive legacy application suite with numerous active sub-applications and active global customers.")
    ]
    for lbl, val in p5_meta:
        p = p5_tf.add_paragraph()
        p.text = f"{lbl}: "
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_PRIMARY_DARK
        p2 = p5_tf.add_paragraph()
        p2.text = f"{val}"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_TEXT_MUTED
        p2.space_after = Pt(6)

    # Right: Migration Architecture & Accomplishments
    r5_x = Inches(5.55)
    r5_w = Inches(6.98)

    p5_cards = [
        ("1. Phased Zero-Downtime Migration from Legacy Flash/Flex",
         "The platform was originally built using Adobe Flash, Flex, and ActionScript. Took technical leadership in architecting and executing a phased migration to modern Angular and React modules without interrupting active stadium operations or breaking existing client workflows."),
        ("2. Hybrid Interoperability & Multi-Stack Engineering",
         "Maintained seamless interoperability between legacy components and modernized Single Page Application (SPA) modules using TypeScript, Angular, React, and Node.js backend services until complete deprecation was achieved."),
        ("3. Sub-Application Management & Sustained Excellence",
         "Governed multiple parallel UI sub-applications serving venue operators, technicians, and broadcast controllers. Awarded multiple Certificates of Excellence by UST Global (2015, 2016, 2018) for client-first commitment and outstanding delivery.")
    ]

    for i, (title, desc) in enumerate(p5_cards):
        cy = Inches(1.6) + i * Inches(1.76)
        add_card(s5, r5_x, cy, r5_w, Inches(1.6))
        otb = s5.shapes.add_textbox(r5_x + Inches(0.2), cy + Inches(0.15), r5_w - Inches(0.4), Inches(1.3))
        otf = otb.text_frame
        otf.word_wrap = True
        op1 = otf.paragraphs[0]
        op1.text = title
        op1.font.size = Pt(12)
        op1.font.bold = True
        op1.font.color.rgb = COLOR_PRIMARY_BLUE
        op1.space_after = Pt(5)
        op2 = otf.add_paragraph()
        op2.text = desc
        op2.font.size = Pt(9.5)
        op2.font.color.rgb = COLOR_TEXT_MAIN

    add_footer(s5, 5, TOTAL_SLIDES)

    # =========================================================================
    # SLIDE 6: SECTION 2 — GROUP 6: THOUGHTFOCUS TECHNOLOGIES
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, COLOR_BG_LIGHT)
    add_header(s6, "Section 2 · Project Experience (Client Group 6)", "ThoughtFocus Technologies: Aftermarket Parts 3D Explorer & Enterprise Solutions")

    # Left: Aftermarket Parts Explorer
    add_card(s6, Inches(0.8), Inches(1.6), c_w, c_h)
    tb_tf1 = s6.shapes.add_textbox(Inches(1.0), Inches(1.8), c_w - Inches(0.4), c_h - Inches(0.4))
    tf_tf1 = tb_tf1.text_frame
    tf_tf1.word_wrap = True

    p = tf_tf1.paragraphs[0]
    p.text = "Aftermarket Parts Explorer"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p_sub = tf_tf1.add_paragraph()
    p_sub.text = "UI Architect & Tech Lead | Oct 2011 – Mar 2014"
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_BRAND_DEEP
    p_sub.space_after = Pt(12)

    tf1_points = [
        ("Platform Scope", "Massive parts marketplace serving aftermarket automotive & industrial parts vendors and buyers."),
        ("Scale & Catalog", "Supported millions of parts across hundreds of manufacturer catalogs with deep search capabilities."),
        ("Interactive 3D Viewer", "Architected an interactive 3D interface allowing buyers to inspect 3D models and dimensions of thousands of components before purchase."),
        ("Full E-Commerce Flow", "Integrated shopping cart, quotation workflows, and secure payment gateway integrations."),
        ("Technologies Used", "Adobe Flex, ActionScript, Mate architectural framework, HTML, CSS, and backend data services.")
    ]
    for lbl, val in tf1_points:
        tp = tf_tf1.add_paragraph()
        tp.text = f"• {lbl}: "
        tp.font.bold = True
        tp.font.size = Pt(10)
        tp.font.color.rgb = COLOR_PRIMARY_DARK
        tp2 = tf_tf1.add_paragraph()
        tp2.text = f"  {val}"
        tp2.font.size = Pt(9.5)
        tp2.font.color.rgb = COLOR_TEXT_MUTED
        tp2.space_after = Pt(6)

    # Right: Bootstrapping Enterprise UI Applications
    add_card(s6, Inches(6.8), Inches(1.6), c_w, c_h)
    tb_tf2 = s6.shapes.add_textbox(Inches(7.0), Inches(1.8), c_w - Inches(0.4), c_h - Inches(0.4))
    tf_tf2 = tb_tf2.text_frame
    tf_tf2.word_wrap = True

    p = tf_tf2.paragraphs[0]
    p.text = "Enterprise UI Solutions"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p_sub = tf_tf2.add_paragraph()
    p_sub.text = "Prototyping & Multi-Client Solutions Delivery"
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_PRIMARY_BLUE
    p_sub.space_after = Pt(12)

    tf2_points = [
        ("Design-to-Code Pipeline", "Established an early user involvement process—validating concepts with interactive mockups and prototypes prior to delivery."),
        ("Enterprise Search App", "Guided team to design and bootstrap a high-speed enterprise search application with advanced filtering and metadata indexing."),
        ("Dairy / Milk Corporation App", "Led the architecture and delivery of an operational management application for a large milk corporation handling distribution and supply logistics."),
        ("Technology Stack", "HTML, CSS, JavaScript, TypeScript, Adobe Flex, Flash, and early Single-Page Application patterns."),
        ("Mentorship & Guidance", "Coached junior engineers on clean modular UI architecture and user-centered design standards.")
    ]
    for lbl, val in tf2_points:
        tp = tf_tf2.add_paragraph()
        tp.text = f"• {lbl}: "
        tp.font.bold = True
        tp.font.size = Pt(10)
        tp.font.color.rgb = COLOR_PRIMARY_DARK
        tp2 = tf_tf2.add_paragraph()
        tp2.text = f"  {val}"
        tp2.font.size = Pt(9.5)
        tp2.font.color.rgb = COLOR_TEXT_MUTED
        tp2.space_after = Pt(6)

    add_footer(s6, 6, TOTAL_SLIDES)

    # =========================================================================
    # SLIDE 7: SECTION 2 — GROUP 7 & 8: CISCO/VODAFONE BMS & SPECIALIZED PROJECTS
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, COLOR_BG_LIGHT)
    add_header(s7, "Section 2 · Project Experience (Client Groups 7 & 8)", "Cisco & Vodafone BMS Dashboards & Technoyana Specialized Engineering")

    # Left: Facility Dashboard at Cisco & Vodafone
    add_card(s7, Inches(0.8), Inches(1.6), c_w, c_h)
    tb_bms = s7.shapes.add_textbox(Inches(1.0), Inches(1.8), c_w - Inches(0.4), c_h - Inches(0.4))
    tf_bms = tb_bms.text_frame
    tf_bms.word_wrap = True

    p = tf_bms.paragraphs[0]
    p.text = "Cisco & Vodafone Dashboards"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p_sub = tf_bms.add_paragraph()
    p_sub.text = "Building Management Systems (BMS) Unified Interface"
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_BRAND_DEEP
    p_sub.space_after = Pt(12)

    bms_points = [
        ("Facility Dashboard at Cisco", "Designed and developed an interactive facility dashboard at Cisco Systems campus as a full-time consultant (2009–2010)."),
        ("Unified BMS Control", "Connected to and visualized diverse Building Management Systems: Air Handling Units (AHUs), Variable Refrigerant Volume (VRVs), industrial chillers, and power meters."),
        ("Environmental Telemetry", "Provided facility managers with real-time operational status, thermal mapping, energy consumption, and alarm thresholds."),
        ("Formal Cisco Recognition", "Received official Certificate of Appreciation from Cisco leadership in 2010 for outstanding visualization and operational utility."),
        ("Vodafone Solutions", "Delivered specialized data visualization dashboards for Vodafone operations to monitor network and facility metrics.")
    ]
    for lbl, val in bms_points:
        bp = tf_bms.add_paragraph()
        bp.text = f"• {lbl}: "
        bp.font.bold = True
        bp.font.size = Pt(10)
        bp.font.color.rgb = COLOR_PRIMARY_DARK
        bp2 = tf_bms.add_paragraph()
        bp2.text = f"  {val}"
        bp2.font.size = Pt(9.5)
        bp2.font.color.rgb = COLOR_TEXT_MUTED
        bp2.space_after = Pt(6)

    # Right: Other Specialized Projects (Technoyana)
    add_card(s7, Inches(6.8), Inches(1.6), c_w, c_h)
    tb_sp = s7.shapes.add_textbox(Inches(7.0), Inches(1.8), c_w - Inches(0.4), c_h - Inches(0.4))
    tf_sp = tb_sp.text_frame
    tf_sp.word_wrap = True

    p = tf_sp.paragraphs[0]
    p.text = "Specialized Engineering Projects"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK
    p.space_after = Pt(2)

    p_sub = tf_sp.add_paragraph()
    p_sub.text = "CAD/CAM, CNC, 3D Visualization & Mobile Products"
    p_sub.font.size = Pt(11)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_PRIMARY_BLUE
    p_sub.space_after = Pt(12)

    sp_points = [
        ("Architectural Visualization", "Delivered multiple architectural 3D visualizations, spatial renderings, and walkthroughs for commercial and real estate projects."),
        ("CAD/CAM & CNC Development", "Led customized CNC machine development and automated CAD/CAM toolpath pipelines, bridging physical fabrication with digital software."),
        ("SellAny Mobile Marketplace", "Built and launched 'SellAny'—a consumer mobile application allowing users to list and sell items effortlessly."),
        ("Payment Parking Mobile App", "Led an engineering team to develop an automated parking payment mobile application with real-time slot occupancy tracking."),
        ("Flight Simulation Visuals (CAE)", "Visual Database Developer creating 3D terrain and aircraft simulation databases under locked 60 FPS budgets.")
    ]
    for lbl, val in sp_points:
        sp = tf_sp.add_paragraph()
        sp.text = f"• {lbl}: "
        sp.font.bold = True
        sp.font.size = Pt(10)
        sp.font.color.rgb = COLOR_PRIMARY_DARK
        sp2 = tf_sp.add_paragraph()
        sp2.text = f"  {val}"
        sp2.font.size = Pt(9.5)
        sp2.font.color.rgb = COLOR_TEXT_MUTED
        sp2.space_after = Pt(6)

    add_footer(s7, 7, TOTAL_SLIDES)

    # =========================================================================
    # SLIDE 8: CORE SKILLSET MATRIX ACROSS 18+ YEARS
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, COLOR_BG_LIGHT)
    add_header(s8, "Comprehensive Skillset Matrix", "Technical & Managerial Mastery Across 18+ Years of Delivery")

    grid_w = Inches(5.72)
    grid_h = Inches(2.45)
    cols = [Inches(0.8), Inches(6.8)]
    rows = [Inches(1.6), Inches(4.3)]

    matrix_data = [
        ("1. Scalable Frontend & Modular Architecture",
         COLOR_PRIMARY_BLUE,
         [
             "React, Angular, TypeScript, JavaScript, Node.js, Web Components (LitElement).",
             "Architected Enterprise UI Design Systems used across diverse development teams.",
             "State management, micro-frontends, REST, WebSockets, and streaming telemetry.",
             "4-year zero-downtime migration of Cisco Stadium Vision from Flash/Flex to Angular/React."
         ]),
        ("2. Spatial 3D, CAD & Generative AI",
         COLOR_BRAND_DEEP,
         [
             "Voxelforge AI (generative modular 3D for Unreal/Unity/WebGL) & Ayam3d (parametric 3D).",
             "Architectural 3D visualization, animated walkthroughs, and CAD/CAM CNC machine development.",
             "Flight simulator 3D terrain and aircraft databases under locked 60 FPS budgets (CAE).",
             "Interactive 3D parts inspection explorer supporting millions of catalog components."
         ]),
        ("3. High Reliability & Operational Security",
         COLOR_ACCENT_AMBER,
         [
             "Delivered Philips ICU healthcare software meeting stringent clinical safety benchmarks.",
             "Strict cybersecurity enforcement: Multi-factor authentication (MFA), XSS mitigation, RBAC.",
             "Offline-first mobile architecture (IndexedDB/Service Workers) with conflict-free cloud sync.",
             "Building Management System (BMS) unified interface for AHUs, chillers, and telemetry (Cisco)."
         ]),
        ("4. Agile Leadership & Startup Delivery",
         COLOR_SUCCESS,
         [
             "Founder/Co-Founder: Technoyana, Twitan.com, SrushtiLabs, InnoBrik.",
             "Associate Project Manager at UST Global; managed cross-functional squads for Cisco.",
             "Early user prototyping, design-to-code pipelines, and active stakeholder governance.",
             "Honored with Cisco Appreciation (2010) and 3 UST Global Excellence Awards (2015, 2016, 2018)."
         ])
    ]

    for idx, (p_title, p_color, p_bullets) in enumerate(matrix_data):
        c_x = cols[idx % 2]
        c_y = rows[idx // 2]
        add_card(s8, c_x, c_y, grid_w, grid_h)

        hbar = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_x + Inches(0.01), c_y + Inches(0.01), grid_w - Inches(0.02), Inches(0.42))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = p_color
        hbar.line.fill.background()

        htext = s8.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(0.06), grid_w - Inches(0.4), Inches(0.35))
        htf = htext.text_frame
        hp = htf.paragraphs[0]
        hp.text = p_title
        hp.font.size = Pt(11)
        hp.font.bold = True
        hp.font.color.rgb = RGBColor(255, 255, 255)

        btb = s8.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(0.48), grid_w - Inches(0.4), grid_h - Inches(0.55))
        btf = btb.text_frame
        btf.word_wrap = True
        for b_i, bullet in enumerate(p_bullets):
            bp = btf.paragraphs[0] if b_i == 0 else btf.add_paragraph()
            bp.text = f"• {bullet}"
            bp.font.size = Pt(9.5)
            bp.font.color.rgb = COLOR_TEXT_MAIN
            bp.space_after = Pt(3)

    add_footer(s8, 8, TOTAL_SLIDES)

    # =========================================================================
    # SLIDE 9: SECTION 3 — CONCLUSION: ROLE FIT & CERTIFICATION PLEDGE
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, COLOR_PRIMARY_DARK)

    # Large Center Container
    c_w = Inches(11.733)
    c_h = Inches(5.5)
    cx = Inches(0.8)
    cy = Inches(1.2)
    add_card(s9, cx, cy, c_w, c_h, bg_color=RGBColor(24, 34, 53), border_color=RGBColor(51, 65, 85))

    q_tb = s9.shapes.add_textbox(cx + Inches(0.5), cy + Inches(0.35), c_w - Inches(1.0), c_h - Inches(0.7))
    q_tf = q_tb.text_frame
    q_tf.word_wrap = True

    qp1 = q_tf.paragraphs[0]
    qp1.text = "SECTION 3 · CONCLUSION & ROLE ALIGNMENT"
    qp1.font.size = Pt(11.5)
    qp1.font.bold = True
    qp1.font.color.rgb = COLOR_CYAN_ACCENT
    qp1.space_after = Pt(4)

    qp2 = q_tf.add_paragraph()
    qp2.text = "Alignment to Senior Manager – IT & Continuous Learning Pledge"
    qp2.font.size = Pt(21)
    qp2.font.bold = True
    qp2.font.color.rgb = RGBColor(255, 255, 255)
    qp2.space_after = Pt(12)

    conclusions = [
        ("Design and Engineering Synthesis",
         "Holding a postgraduate degree in Human Interface Design (M.S. in Computing, UK) combined with an engineering degree in Electronics and Communication (B.E.), I bring a rare, balanced capability spanning both human-centered UX design and deep technical software architecture."),

        ("Proven Breadth Across Startup Velocity & Enterprise Scale",
         "My 18+ years of experience encompass leading agile, high-velocity startup product incubation (Technoyana, SrushtiLabs, Twitan, InnoBrik) as well as managing complex multi-year enterprise projects with stringent quality, security, and uptime mandates (Philips ICU Healthcare, Cisco Systems, UST Global, Ness)."),

        ("Handling Products Across Every Stage of the Lifecycle",
         "Demonstrated expertise across every product phase: early discovery prototypes, building reusable design systems, legacy system migrations (Flash to Angular/React), production deployment, security compliance, and long-term customer support."),

        ("Pledge for Self-Training & Certification",
         "I am fully committed to the success of the organization and team. As per the specific operational requirements of the Senior Manager – IT role, I pledge to proactively upskill myself and complete any required enterprise certifications (e.g., Cloud Architecture, ITIL, Cybersecurity, or project governance) to align completely with team goals and project needs.")
    ]

    for c_title, c_desc in conclusions:
        cp1 = q_tf.add_paragraph()
        cp1.text = f"✔ {c_title}: "
        cp1.font.bold = True
        cp1.font.size = Pt(10.5)
        cp1.font.color.rgb = COLOR_CYAN_ACCENT
        cp2 = q_tf.add_paragraph()
        cp2.text = f"   {c_desc}"
        cp2.font.size = Pt(9.5)
        cp2.font.color.rgb = RGBColor(203, 213, 225)
        cp2.space_after = Pt(6)

    qp_contact = q_tf.add_paragraph()
    qp_contact.text = "\nMaheshchandra Hegde  |  hid.mahesh@gmail.com  |  +91 9535253329 / 7022407280  |  hegdemahesh.in"
    qp_contact.font.size = Pt(10.5)
    qp_contact.font.bold = True
    qp_contact.font.color.rgb = RGBColor(255, 255, 255)

    add_footer(s9, 9, TOTAL_SLIDES, dark=True)

    prs.save(output_pptx_path)
    print(f"Successfully generated Structured 9-Slide PowerPoint presentation at: {output_pptx_path}")

if __name__ == "__main__":
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(out_dir, "Obayashi_Senior_Manager_IT_Presentation_Maheshchandra_Hegde.pptx")
    create_deck(out_file)
