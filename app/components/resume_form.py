import reflex as rx
from ..styles.theme import theme
from ..state import ResumeState

def resume_form():
    return rx.form(
        rx.input(name="Name", placeholder="Full Name", value=ResumeState.name, on_change=ResumeState.set_name),
        rx.input(name="Email", placeholder="Email", value=ResumeState.email, on_change=ResumeState.set_email),
        rx.text_area(
            name="Summary",
            placeholder="Professional Summary",
            value=ResumeState.summary,
            on_change=ResumeState.set_summary,
        ),
        rx.button("Save & Preview", type="submit"),
        style={
            "display": "flex",
            "flex_direction": "column",
            "background_color": "#1E1E1E",
            "padding": "1.5rem",
            "border_radius": "8px",
        },
    )
