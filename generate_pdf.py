import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_section_header(title, width, primary_color, line_color):
    section_title_style = ParagraphStyle(
        'ResumeSectionTitle',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=11.5,
        textColor=primary_color,
        textTransform='uppercase',
        spaceBefore=0,
        spaceAfter=0
    )
    title_p = Paragraph(title, section_title_style)
    t = Table([[title_p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 1.2, line_color),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return t

def create_item_header(left_title, right_date, left_sub="", right_loc="", width=523, secondary_color=colors.HexColor('#4F46E5'), muted_color=colors.HexColor('#4B5563')):
    title_style = ParagraphStyle(
        'ItemTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )
    sub_style = ParagraphStyle(
        'ItemSub',
        fontName='Helvetica-BoldOblique',
        fontSize=8.2,
        leading=10,
        textColor=secondary_color
    )
    date_style = ParagraphStyle(
        'ItemDate',
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10,
        textColor=muted_color,
        alignment=2 # Right-aligned
    )
    loc_style = ParagraphStyle(
        'ItemLoc',
        fontName='Helvetica',
        fontSize=8.2,
        leading=10,
        textColor=muted_color,
        alignment=2 # Right-aligned
    )
    
    p_title = Paragraph(left_title, title_style)
    p_date = Paragraph(right_date, date_style)
    
    if left_sub or right_loc:
        p_sub = Paragraph(left_sub, sub_style)
        p_loc = Paragraph(right_loc, loc_style)
        data = [[p_title, p_date], [p_sub, p_loc]]
    else:
        data = [[p_title, p_date]]
        
    t = Table(data, colWidths=[width - 170, 170])
    t.setStyle(TableStyle([
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t

def create_skills_row(category, skills_str, width=523, text_color=colors.HexColor('#1F2937')):
    cat_style = ParagraphStyle(
        'SkillCategory',
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10.5,
        textColor=colors.HexColor('#0F172A')
    )
    list_style = ParagraphStyle(
        'SkillList',
        fontName='Helvetica',
        fontSize=8.2,
        leading=10.5,
        textColor=text_color
    )
    p_cat = Paragraph(category, cat_style)
    p_list = Paragraph(skills_str, list_style)
    t = Table([[p_cat, p_list]], colWidths=[120, width - 120])
    t.setStyle(TableStyle([
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t

def main():
    pdf_filename = "resume.pdf"
    
    # 0.5 inch (36pt) margins to optimize printable area on A4
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=26,
        bottomMargin=26
    )
    
    # Palette
    PRIMARY_COLOR = colors.HexColor('#0F172A')    # Slate 900
    SECONDARY_COLOR = colors.HexColor('#4F46E5')  # Indigo
    TEXT_COLOR = colors.HexColor('#1F2937')       # Slate 800
    MUTED_COLOR = colors.HexColor('#4B5563')      # Slate 600
    LINE_COLOR = colors.HexColor('#4F46E5')       # Indigo Accent Line for Sections
    
    # Styles
    name_style = ParagraphStyle(
        'ResumeName',
        fontName='Helvetica-Bold',
        fontSize=19.5,
        leading=22.5,
        textColor=PRIMARY_COLOR,
        alignment=1, # Centered
        spaceAfter=1
    )

    role_style = ParagraphStyle(
        'ResumeRole',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=SECONDARY_COLOR,
        textTransform='uppercase',
        alignment=1, # Centered
        spaceAfter=2
    )

    contact_style = ParagraphStyle(
        'ResumeContact',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=MUTED_COLOR,
        alignment=1 # Centered
    )

    summary_style = ParagraphStyle(
        'ResumeSummary',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=TEXT_COLOR
    )

    bullet_style = ParagraphStyle(
        'ResumeBullet',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=TEXT_COLOR,
        leftIndent=9,
        firstLineIndent=-5,
        spaceAfter=1
    )

    other_projects_style = ParagraphStyle(
        'ResumeOtherProj',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=TEXT_COLOR
    )

    cert_style = ParagraphStyle(
        'ResumeCert',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=TEXT_COLOR,
        leftIndent=9,
        firstLineIndent=-5,
        spaceAfter=1
    )

    story = []
    width = 523 # A4 width (595.27) - margins (72)

    # 1. HEADER SECTION
    p_name = Paragraph("Rohit Chhonkar", name_style)
    p_role = Paragraph("Full Stack &amp; AI Developer", role_style)
    
    contact_line1 = (
        "Agra, India  <font color='#4F46E5'>&#8226;</font>  "
        "+91 6398099404  <font color='#4F46E5'>&#8226;</font>  "
        "<a href='mailto:contact@rohitchhonkar.click'><font color='#4F46E5'>contact@rohitchhonkar.click</font></a>  <font color='#4F46E5'>&#8226;</font>  "
        "<a href='https://rohitchhonkar.click'><font color='#4F46E5'>rohitchhonkar.click</font></a>"
    )
    contact_line2 = (
        "<a href='https://github.com/rohitunheard'><font color='#4F46E5'>github.com/rohitunheard</font></a>  <font color='#4F46E5'>&#8226;</font>  "
        "<a href='https://www.linkedin.com/in/rohit-chhonkar-3b07622a2/'><font color='#4F46E5'>linkedin.com/in/rohit-chhonkar-3b07622a2</font></a>"
    )
    p_contact1 = Paragraph(contact_line1, contact_style)
    p_contact2 = Paragraph(contact_line2, contact_style)
    
    story.append(p_name)
    story.append(p_role)
    story.append(p_contact1)
    story.append(p_contact2)
    story.append(Spacer(1, 5))

    # 2. SUMMARY
    story.append(create_section_header("Summary", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    summary_text = (
        "Full-stack developer building real-time web applications and AI-driven platforms using Node.js, FastAPI, "
        "and WebRTC. Experienced in designing scalable backends, database schemas, and secure authentication flows. "
        "Handled the complete development cycle for 10+ web apps, including voice assistants, collaborative coding "
        "spaces, and POS billing tools."
    )
    story.append(Paragraph(summary_text, summary_style))
    story.append(Spacer(1, 5))

    # 3. TECHNICAL SKILLS
    story.append(create_section_header("Technical Skills", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    skills = [
        ("Languages:", "JavaScript (ES6+), TypeScript, HTML5, CSS3, C, Java"),
        ("Web &amp; Frameworks:", "React.js, Next.js, Node.js, Express.js, FastAPI, WebRTC, Socket.io, Tailwind CSS"),
        ("Databases &amp; Tools:", "MongoDB, Git, GitHub Actions, Postman, JWT, REST APIs, CI/CD Workflows"),
        ("AI &amp; Integrations:", "ElevenLabs, Whisper, Groq Cloud API, Clerk Auth, Stream SDK, Cloudinary, F5-TTS")
    ]
    for category, skills_str in skills:
        story.append(create_skills_row(category, skills_str, width, TEXT_COLOR))
    story.append(Spacer(1, 5))

    # 4. EXPERIENCE & INTERNSHIPS
    story.append(create_section_header("Professional Experience", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    story.append(create_item_header(
        "Full Stack Web Development Intern",
        "June 2026",
        "Academy of Skill Development (ASD)",
        "Remote, India",
        width,
        SECONDARY_COLOR,
        MUTED_COLOR
    ))
    story.append(Spacer(1, 2))
    story.append(Paragraph("&#8226; Developed core recruiter and applicant authentication modules using JWT and secure HTTP-only session cookies.", bullet_style))
    story.append(Paragraph("&#8226; Engineered 20+ reusable, highly responsive user interface components in React, reducing client-side load latency.", bullet_style))
    story.append(Paragraph("&#8226; Built and optimized REST API endpoints in Node.js/Express for recruiter-applicant matching across 15+ database collections.", bullet_style))
    story.append(Paragraph("&#8226; Adopted collaborative Git workflow best practices and participated in Agile development cycles with team mentors.", bullet_style))
    story.append(Spacer(1, 5))

    # 5. PROJECTS
    story.append(create_section_header("Key Projects", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    # Project 1: Arogya Bharat (Live Demo + Direct GitHub)
    links_arogya = (
        "React.js, Vite, Client-side NLP, Tailwind CSS  <font color='#4F46E5'>&#8226;</font>  "
        "<a href='https://arogyabharat-iota.vercel.app/'><font color='#4F46E5'>[Live Demo]</font></a>  "
        "<a href='https://github.com/rohitunheard/Arogya-Bharat'><font color='#4F46E5'>[GitHub]</font></a>"
    )
    story.append(create_item_header("Arogya Bharat — Clinical Portal &amp; Triage", "2025", links_arogya, "", width, SECONDARY_COLOR, MUTED_COLOR))
    story.append(Spacer(1, 1.5))
    story.append(Paragraph("&#8226; Developed a clinical dashboard supporting digital prescriptions, doctor schedules, and clinical symptom assessments.", bullet_style))
    story.append(Paragraph("&#8226; Built light, client-side NLP query engines to categorize and prioritize patient symptom severity routes for automated triage.", bullet_style))
    story.append(Spacer(1, 3))

    # Project 2: RoamFlow (Live Demo + Direct GitHub)
    links_roam = (
        "React.js, Vite, Lucide Icons, Tailwind CSS  <font color='#4F46E5'>&#8226;</font>  "
        "<a href='https://roamflow-brown.vercel.app/'><font color='#4F46E5'>[Live Demo]</font></a>  "
        "<a href='https://github.com/rohitunheard/RoamFlow-India'><font color='#4F46E5'>[GitHub]</font></a>"
    )
    story.append(create_item_header("RoamFlow — Tour &amp; Travel Planning System", "2025", links_roam, "", width, SECONDARY_COLOR, MUTED_COLOR))
    story.append(Spacer(1, 1.5))
    story.append(Paragraph("&#8226; Architected an interactive itinerary builder featuring vacation package selectors, hotels, and custom travel timelines.", bullet_style))
    story.append(Paragraph("&#8226; Programmed budget estimators and reactive flight schedules, maintaining clean layouts for tablet and mobile views.", bullet_style))
    story.append(Spacer(1, 3))

    # Project 3: E-Commerce-Store (Live Demo + Direct GitHub)
    links_ecommerce = (
        "HTML5, CSS3, JavaScript, Local Storage  <font color='#4F46E5'>&#8226;</font>  "
        "<a href='https://e-sommerce-store.vercel.app/'><font color='#4F46E5'>[Live Demo]</font></a>  "
        "<a href='https://github.com/rohitunheard/E-Commerce-Store'><font color='#4F46E5'>[GitHub]</font></a>"
    )
    story.append(create_item_header("E-Commerce-Store — Retail Storefront", "2024", links_ecommerce, "", width, SECONDARY_COLOR, MUTED_COLOR))
    story.append(Spacer(1, 1.5))
    story.append(Paragraph("&#8226; Designed a fully responsive online retail storefront featuring smooth search query filtering and interactive shopping cart views.", bullet_style))
    story.append(Paragraph("&#8226; Utilized HTML5, CSS3 transitions, and Local Storage APIs to persist cart items across browser sessions without backend dependencies.", bullet_style))
    story.append(Spacer(1, 3))

    # Project 4: Smart Job Portal (Direct GitHub)
    links_job = (
        "MERN Stack, REST APIs, JSON Web Tokens, Cookies  <font color='#4F46E5'>&#8226;</font>  "
        "<a href='https://github.com/rohitunheard/Job-Portal-with-AI-Resume-Screening'><font color='#4F46E5'>[GitHub]</font></a>"
    )
    story.append(create_item_header("Smart Job Portal with AI Resume Screening", "2026", links_job, "", width, SECONDARY_COLOR, MUTED_COLOR))
    story.append(Spacer(1, 1.5))
    story.append(Paragraph("&#8226; Developed a recruitment hub managing applicant workflows with 20+ REST endpoints and role-based client dashboards.", bullet_style))
    story.append(Paragraph("&#8226; Implemented secure session handling via HTTP-only cookies and optimized database indexes for fast candidate search queries.", bullet_style))
    story.append(Spacer(1, 3))

    # Other Projects line (featuring Lilly Voice, CodeChat-IQ, Vyaapaar, NexaCall, Synergy-Boards with direct Git links)
    other_projects_text = (
        "<b>Other Projects:</b> <b>Lilly Voice</b> (Voice assistant responding under 500ms using FastAPI, Groq, and Whisper — "
        "<a href='https://github.com/rohitunheard/Lilly-Voice'><font color='#4F46E5'>[GitHub]</font></a>), "
        "<b>CodeChat-IQ</b> (WebRTC collaborative pair programming workspace via Stream SDK — "
        "<a href='https://github.com/rohitunheard/codechat-iq'><font color='#4F46E5'>[GitHub]</font></a>), "
        "<b>Vyaapaar</b> (TypeScript POS dashboard — "
        "<a href='https://github.com/rohitunheard/-Vyaapaar-'><font color='#4F46E5'>[GitHub]</font></a>), "
        "<b>NexaCall</b> (WebRTC peer video chat application — "
        "<a href='https://github.com/rohitunheard/NexaCall'><font color='#4F46E5'>[GitHub]</font></a>), and "
        "<b>Synergy-Boards</b> (Kanban project planner — "
        "<a href='https://github.com/rohitunheard/Synergy-Boards'><font color='#4F46E5'>[GitHub]</font></a>)."
    )
    story.append(Paragraph(other_projects_text, other_projects_style))
    story.append(Spacer(1, 5))

    # 6. EDUCATION
    story.append(create_section_header("Education", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    # B.Tech
    story.append(create_item_header(
        "Bachelor of Technology in Computer Science &amp; Engineering",
        "2023 — Present",
        "Anand Engineering College",
        "Agra, India",
        width,
        SECONDARY_COLOR,
        MUTED_COLOR
    ))
    story.append(Spacer(1, 1))
    story.append(Paragraph("&#8226; Key Coursework: Data Structures &amp; Algorithms, Object-Oriented Programming (OOP), Database Systems (DBMS), Web Architecture.", bullet_style))
    story.append(Spacer(1, 2.5))

    # High School & Intermediate
    story.append(create_item_header(
        "S.N.S.M. Inter College (Intermediate PCM &amp; High School)",
        "Class of 2021 &amp; 2019",
        "Hathras, UP, India",
        "",
        width,
        SECONDARY_COLOR,
        MUTED_COLOR
    ))
    story.append(Spacer(1, 5))

    # 7. CERTIFICATIONS & ACHIEVEMENTS
    story.append(create_section_header("Certifications &amp; Achievements", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    # We will lay this out as two columns to keep it clean and save vertical space
    left_certs = []
    right_achievements = []
    
    certs = [
        "<b>JavaScript Essentials 1</b> — Cisco Networking Academy &amp; JS Institute",
        "<b>MERN Stack Training &amp; Internship (Grade A++)</b> — ASD",
        "<b>Introduction to Cybersecurity</b> — Cisco Networking Academy",
        "<b>AI Tools &amp; Data Science Workshops</b> — HCL | GUVI | be10x"
    ]
    for c in certs:
        left_certs.append(Paragraph(f"&#8226; {c}", cert_style))
        
    achievements = [
        "Shipped 10+ MERN/FastAPI web applications and real-time platforms.",
        "Scored top grade of <b>A++</b> in industrial internship at ASD.",
        "Active GitHub contributor with 11+ repositories and 300+ commits."
    ]
    for a in achievements:
        right_achievements.append(Paragraph(f"&#8226; {a}", cert_style))
        
    col_width = (width - 12) / 2
    footer_table = Table([[left_certs, right_achievements]], colWidths=[col_width, col_width])
    footer_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    
    story.append(footer_table)

    # Build Document
    doc.build(story)
    print("PDF Resume generated successfully as 'resume.pdf'")

if __name__ == "__main__":
    main()
