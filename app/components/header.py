import reflex as rx
from ..styles.theme import theme

def header():
    return rx.box(
        rx.text(
            "Resume Builder",
            font_size="2xl",
            font_weight="bold",
            color=theme["colors"]["primary"],
        ),
        rx.box(
            rx.link("Home", href="/", style={"margin": "0 1rem", "color": theme["colors"]["text"]}),
            rx.link("Templates", href="/templates", style={"margin": "0 1rem", "color": theme["colors"]["text"]}),
            rx.link("Customize", href="/customize", style={"margin": "0 1rem", "color": theme["colors"]["text"]}),
        ),
        style={
            "display": "flex",
            "justify_content": "space-between",
            "padding": "1rem",
            "background_color": theme["colors"]["background"],
            "box_shadow": theme["box_shadow"],
        },
    )

