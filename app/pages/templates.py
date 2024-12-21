import reflex as rx
from ..components.template_card import template_card

@rx.page(route="/templates")
def templates():
    return rx.box(
        rx.text(
            "Select a Resume Template",
            font_size="2xl",
            font_weight="bold",
            color="#E0E0E0",
            text_align="center",
        ),
        rx.box(
            template_card("Modern Template", "/assets/images/modern.png", "/customize?template=modern"),
            template_card("Classic Template", "/assets/images/classic.png", "/customize?template=classic"),
            style={"display": "flex", "gap": "1.5rem", "justify_content": "center", "margin_top": "2rem"},
        ),
        style={"background_color": "#121212", "padding": "2rem"},
    )
