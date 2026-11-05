import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_section_header(title, width, primary_color, line_color):
    section_title_style = ParagraphStyle(
        'ResumeSectionTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=primary_color,
        textTransform='uppercase',
        spaceBefore=0,
        spaceAfter=0
    )
    title_p = Paragraph(title, section_title_style)
    t = Table([[title_p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, -1), 1.2, line_color),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    return t

def create_item_header(left_title, right_date, left_sub="", right_loc="", width=523, secondary_color=colors.HexColor('#2563EB'), muted_color=colors.HexColor('#475569')):
    title_style = ParagraphStyle(
        'ItemTitle',
        fontName='Helvetica-Bold',
        fontSize=8.6,
        leading=10.5,
        textColor=colors.HexColor('#0F172A')
    )
    sub_style = ParagraphStyle(
        'ItemSub',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=9.8,
        textColor=secondary_color
    )
    date_style = ParagraphStyle(
        'ItemDate',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=9.8,
        textColor=muted_color,
        alignment=2
    )
    loc_style = ParagraphStyle(
        'ItemLoc',
        fontName='Helvetica',
        fontSize=8,
        leading=9.8,
        textColor=muted_color,
        alignment=2
    )
    
    p_title = Paragraph(left_title, title_style)
    p_date = Paragraph(right_date, date_style)
    
    if left_sub or right_loc:
        p_sub = Paragraph(left_sub, sub_style)
        p_loc = Paragraph(right_loc, loc_style)
        data = [[p_title, p_date], [p_sub, p_loc]]
    else:
        data = [[p_title, p_date]]
        
    t = Table(data, colWidths=[width - 150, 150])
    t.setStyle(TableStyle([
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.5),
        ('TOPPADDING', (0, 0), (-1, -1), 0.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t

def create_skills_row(category, skills_str, width=523, text_color=colors.HexColor('#1E293B')):
    cat_style = ParagraphStyle(
        'SkillCategory',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#0F172A')
    )
    list_style = ParagraphStyle(
        'SkillList',
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=text_color
    )
    p_cat = Paragraph(category, cat_style)
    p_list = Paragraph(skills_str, list_style)
    t = Table([[p_cat, p_list]], colWidths=[125, width - 125])
    t.setStyle(TableStyle([
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0.8),
        ('TOPPADDING', (0, 0), (-1, -1), 0.8),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    return t

def main():
    pdf_filename = "resume.pdf"
    
    # 32pt margins for clean A4 single page fit
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=34,
        rightMargin=34,
        topMargin=24,
        bottomMargin=24
    )
    
    PRIMARY_COLOR = colors.HexColor('#0F172A')    # Slate 900
    SECONDARY_COLOR = colors.HexColor('#2563EB')  # Royal Blue
    TEXT_COLOR = colors.HexColor('#1E293B')       # Slate 800
    MUTED_COLOR = colors.HexColor('#475569')      # Slate 600
    LINE_COLOR = colors.HexColor('#2563EB')       # Section border
    
    name_style = ParagraphStyle(
        'ResumeName',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=21,
        textColor=PRIMARY_COLOR,
        alignment=1,
        spaceAfter=1
    )

    role_style = ParagraphStyle(
        'ResumeRole',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=SECONDARY_COLOR,
        alignment=1,
        spaceAfter=2
    )

    contact_style = ParagraphStyle(
        'ResumeContact',
        fontName='Helvetica',
        fontSize=7.6,
        leading=10,
        textColor=MUTED_COLOR,
        alignment=1
    )

    summary_style = ParagraphStyle(
        'ResumeSummary',
        fontName='Helvetica',
        fontSize=8,
        leading=10.8,
        textColor=TEXT_COLOR
    )

    bullet_style = ParagraphStyle(
        'ResumeBullet',
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=TEXT_COLOR,
        leftIndent=8,
        firstLineIndent=-5,
        spaceAfter=1
    )

    cert_style = ParagraphStyle(
        'ResumeCert',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.2,
        textColor=TEXT_COLOR,
        leftIndent=8,
        firstLineIndent=-5,
        spaceAfter=1
    )

    story = []
    width = 527

    # 1. HEADER
    story.append(Paragraph("Rohit Chhonkar", name_style))
    story.append(Paragraph("Full Stack Developer | React, Node.js &amp; MongoDB", role_style))
    
    contact_line = (
        "Agra, India  &bull;  "
        "+91 6398099404  &bull;  "
        "<a href='mailto:contact@rohitchhonkar.click'><font color='#2563EB'>contact@rohitchhonkar.click</font></a>  &bull;  "
        "<a href='https://rohitchhonkar.click'><font color='#2563EB'>rohitchhonkar.click</font></a>  &bull;  "
        "<a href='https://github.com/rohitunheard'><font color='#2563EB'>github.com/rohitunheard</font></a>  &bull;  "
        "<a href='https://www.linkedin.com/in/rohit-chhonkar-3b07622a2/'><font color='#2563EB'>LinkedIn</font></a>"
    )
    story.append(Paragraph(contact_line, contact_style))
    story.append(Spacer(1, 4))

    # 2. SUMMARY
    story.append(create_section_header("Summary", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    summary_text = (
        "Full-stack developer with a practical dual foundation in computer science engineering and business management. "
        "Completed a BBA and currently pursuing an MBA in HR (both through distance education) alongside the final year of B.Tech CSE. "
        "Experienced in building web applications, real-time audio systems, and RESTful APIs using React, Node.js, Express, "
        "MongoDB, and FastAPI."
    )
    story.append(Paragraph(summary_text, summary_style))
    story.append(Spacer(1, 4))

    # 3. TECHNICAL & BUSINESS SKILLS
    story.append(create_section_header("Skills & Competencies", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    skills = [
        ("Languages:", "JavaScript (ES6+), TypeScript, HTML5, CSS3, C, C++, Python, SQL"),
        ("Frontend & UI:", "React.js, Vite, Next.js, Tailwind CSS, Responsive Design, State Context"),
        ("Backend & APIs:", "Node.js, Express.js, FastAPI, RESTful APIs, JWT & Cookies, WebSockets, WebRTC"),
        ("Databases & Tools:", "MongoDB, Mongoose, Git, GitHub Actions, Postman, Vercel, VS Code"),
        ("Business & Operations:", "Talent Acquisition & Screening, Training & Development, Organizational Theory, Quantitative Methods")
    ]
    for category, skills_str in skills:
        story.append(create_skills_row(category, skills_str, width, TEXT_COLOR))
    story.append(Spacer(1, 4))

    # 4. EXPERIENCE
    story.append(create_section_header("Professional Experience", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    story.append(create_item_header(
        "Full Stack Web Development Intern",
        "June 2026",
        "Academy of Skill Development (ASD) &bull; Grade A++",
        "Remote, India",
        width,
        SECONDARY_COLOR,
        MUTED_COLOR
    ))
    story.append(Spacer(1, 1.5))
    story.append(Paragraph("&#8226; Engineered recruiter-candidate authentication flows using JWT and secure HTTP-only cookies for session protection.", bullet_style))
    story.append(Paragraph("&#8226; Built responsive React UI components and RESTful API endpoints in Node.js/Express for candidate screening.", bullet_style))
    story.append(Paragraph("&#8226; Awarded outstanding Grade <b>A++</b> and project completion letter for the Smart Job Portal system.", bullet_style))
    story.append(Spacer(1, 4))

    # 5. KEY PROJECTS
    story.append(create_section_header("Key Shipped Projects", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    # Project 1: Lilly Voice
    links_lilly = "FastAPI, Groq API, Whisper, F5-TTS, React.js &bull; <a href='https://github.com/rohitunheard/Lilly-Voice'><font color='#2563EB'>[GitHub]</font></a>"
    story.append(create_item_header("Lilly Voice &mdash; Real-Time AI Voice Assistant", "2026", links_lilly, "", width, SECONDARY_COLOR, MUTED_COLOR))
    story.append(Paragraph("&#8226; Built a voice assistant with real-time speech responses using FastAPI, WebSockets, Whisper STT, Groq API, and voice interruption handling.", bullet_style))
    story.append(Spacer(1, 2.5))

    # Project 2: Smart Job Portal
    links_job = "React, Node.js, Express, MongoDB, Gemini API &bull; <a href='https://github.com/rohitunheard/Job-Portal-with-AI-Resume-Screening'><font color='#2563EB'>[GitHub]</font></a>"
    story.append(create_item_header("Smart Job Portal with AI Resume Screening", "2026", links_job, "", width, SECONDARY_COLOR, MUTED_COLOR))
    story.append(Paragraph("&#8226; Built an AI-assisted job portal with resume matching, recruiter/candidate dashboards, and role-based JWT authentication.", bullet_style))
    story.append(Spacer(1, 2.5))

    # Project 3: Vyaapaar
    links_vyaapaar = "React.js, TypeScript, Vite, Tailwind CSS &bull; <a href='https://github.com/rohitunheard/-Vyaapaar-'><font color='#2563EB'>[GitHub]</font></a>"
    story.append(create_item_header("Vyaapaar &mdash; Retail Billing &amp; Inventory POS", "2025", links_vyaapaar, "", width, SECONDARY_COLOR, MUTED_COLOR))
    story.append(Paragraph("&#8226; Designed a billing system for everyday retail operations with barcode search, automatic stock deduction, and KhataBook customer ledger.", bullet_style))
    story.append(Spacer(1, 2.5))

    # Project 4: Arogya Bharat
    links_arogya = "React, Vite, Client-side NLP, Tailwind &bull; <a href='https://arogyabharat-iota.vercel.app/'><font color='#2563EB'>[Live Demo]</font></a> &bull; <a href='https://github.com/rohitunheard/Arogya-Bharat'><font color='#2563EB'>[GitHub]</font></a>"
    story.append(create_item_header("Arogya Bharat &mdash; Clinical Portal &amp; Triage Engine", "2025", links_arogya, "", width, SECONDARY_COLOR, MUTED_COLOR))
    story.append(Paragraph("&#8226; Built separate dashboards for doctors, patients and administrators with appointment scheduling, digital prescriptions, and patient triage logic.", bullet_style))
    story.append(Spacer(1, 4))

    # 6. EDUCATION
    story.append(create_section_header("Education", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    # MBA
    story.append(create_item_header(
        "MBA in Human Resources (Distance Mode)",
        "July 2026 &mdash; Present",
        "Mangalayatan University &bull; ODL",
        "In Progress",
        width,
        SECONDARY_COLOR,
        MUTED_COLOR
    ))
    story.append(Spacer(1, 2))

    # B.Tech
    story.append(create_item_header(
        "B.Tech in Computer Science &amp; Engineering",
        "2023 &mdash; 2027 (Expected)",
        "Anand Engineering College, Agra (AKTU)",
        "Final Year",
        width,
        SECONDARY_COLOR,
        MUTED_COLOR
    ))
    story.append(Spacer(1, 2))

    # BBA
    story.append(create_item_header(
        "Bachelor of Business Administration (Distance Mode)",
        "2022 &mdash; 2025",
        "Swami Vivekanand Subharti University &bull; CDOE",
        "Completed Apr 2025",
        width,
        SECONDARY_COLOR,
        MUTED_COLOR
    ))
    story.append(Paragraph("&#8226; Result: <b>First Division</b> &bull; Centre for Distance and Online Education.", bullet_style))
    story.append(Spacer(1, 4))

    # 7. CERTIFICATIONS & ACHIEVEMENTS
    story.append(create_section_header("Key Certifications", width, PRIMARY_COLOR, LINE_COLOR))
    story.append(Spacer(1, 2))
    
    left_certs = [
        Paragraph("&#8226; <b>JavaScript Essentials 1</b> &mdash; Cisco &amp; JS Institute", cert_style),
        Paragraph("&#8226; <b>MERN Stack Internship (Grade A++)</b> &mdash; ASD", cert_style),
        Paragraph("&#8226; <b>Introduction to Cybersecurity</b> &mdash; Cisco Academy", cert_style)
    ]
    right_certs = [
        Paragraph("&#8226; <b>AI Revolution Workshop</b> &mdash; Skillo &amp; Shiksha Nation", cert_style),
        Paragraph("&#8226; <b>Data Science to MAANG</b> &mdash; GUVI | HCL", cert_style),
        Paragraph("&#8226; <b>Meta Marketing Skilling</b> &mdash; Meta Small Business Academy", cert_style)
    ]
    
    col_width = (width - 10) / 2
    footer_table = Table([[left_certs, right_certs]], colWidths=[col_width, col_width])
    footer_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(footer_table)

    doc.build(story)
    print("PDF Resume generated successfully as 'resume.pdf'")

if __name__ == "__main__":
    main()
