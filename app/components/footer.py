import reflex as rx
from ..styles.theme import theme

def footer():
    return rx.box(
        rx.text(
            "© 2024 Resume Builder. All rights reserved.",
            font_size="sm",
            color="gray",
        ),
        style={
            "text_align": "center",
            "padding": "1rem",
            "background_color": "#f8f8f8",
            "border_top": "1px solid #e0e0e0",
        },
    )

