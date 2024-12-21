import reflex as rx

class ResumeState(rx.State):
    # Personal details
    name: str = ""
    email: str = ""
    phone: str = ""
    linkedin: str = ""

    # Professional summary
    summary: str = ""

    # Work experience
    experience: str = ""

    # Education
    education: str = ""

