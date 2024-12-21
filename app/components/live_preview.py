import reflex as rx
from ..state import ResumeState

def live_preview():
    return rx.box(
        # Name Section
        rx.text(
            rx.cond(
                ResumeState.name,  # If `ResumeState.name` is not empty
                ResumeState.name,  # Show the value of `ResumeState.name`
                "John Doe",        # Otherwise, show the placeholder
            ),
            font_size="2xl",
            font_weight="bold",
            margin_bottom="0.5rem",
            color="#FFFFFF",
        ),
        # Contact Information Section
        rx.text(
            rx.cond(ResumeState.email, ResumeState.email, "johndoe@example.com"),
            font_size="md",
            color="#E0E0E0",
            margin_bottom="1rem",
        ),
        # Phone Section
        rx.hstack(
            rx.text("Phone: ", font_weight="bold", color="#FFFFFF"),
            rx.text(
                rx.cond(ResumeState.phone, ResumeState.phone, "(123) 456-7890"),
                color="#E0E0E0",
            ),
            style={"gap": "0.5rem"},  # Use `style` instead of `spacing`
        ),
        # LinkedIn Section
        rx.hstack(
            rx.text("LinkedIn: ", font_weight="bold", color="#FFFFFF"),
            rx.text(
                rx.cond(ResumeState.linkedin, ResumeState.linkedin, "linkedin.com/in/johndoe"),
                color="#E0E0E0",
            ),
            style={"gap": "0.5rem"},  # Use `style` instead of `spacing`
        ),
        rx.divider(margin="1rem 0", border_color="#444444"),
        # Summary Section
        rx.text(
            "Professional Summary",
            font_size="lg",
            font_weight="bold",
            margin_bottom="0.5rem",
            color="#FFFFFF",
        ),
        rx.text(
            rx.cond(
                ResumeState.summary,
                ResumeState.summary,
                "A dedicated professional with proven experience in the industry.",
            ),
            font_size="sm",
            color="#B0B0B0",
            margin_bottom="1rem",
        ),
        rx.divider(margin="1rem 0", border_color="#444444"),
        # Work Experience Section
        rx.text(
            "Work Experience",
            font_size="lg",
            font_weight="bold",
            margin_bottom="0.5rem",
            color="#FFFFFF",
        ),
        rx.text(
            rx.cond(
                ResumeState.experience,
                ResumeState.experience,
                "Add your work experience here.",
            ),
            font_size="sm",
            color="#B0B0B0",
            margin_bottom="1rem",
        ),
        rx.divider(margin="1rem 0", border_color="#444444"),
        # Education Section
        rx.text(
            "Education",
            font_size="lg",
            font_weight="bold",
            margin_bottom="0.5rem",
            color="#FFFFFF",
        ),
        rx.text(
            rx.cond(
                ResumeState.education,
                ResumeState.education,
                "Add your education details here.",
            ),
            font_size="sm",
            color="#B0B0B0",
        ),
        # Overall Styling
        style={
            "padding": "1.5rem",
            "background_color": "#1E1E1E",
            "border_radius": "8px",
            "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.2)",
            "color": "#FFFFFF",
            "width": "100%",
        },
    )
