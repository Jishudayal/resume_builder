import reflex as rx
from ..styles.theme import theme

def template_card(template_name, preview_image_url, href):
    return rx.box(
        rx.image(
            src=preview_image_url,
            width="100%",
            height="200px",
            border_radius=theme["border_radius"],
            object_fit="cover",
        ),
        rx.text(
            template_name,
            font_size="lg",
            font_weight="bold",
            margin_top="1rem",
            font_family="Georgia, serif",
        ),
        rx.link(
            rx.button(
                "Use Template",
                background_color=theme["colors"]["primary"],
                color="white",
                border_radius="4px",
                padding="0.5rem 1rem",
            ),
            href=href,
        ),
        style={
            "padding": "1rem",
            "box_shadow": theme["box_shadow"],
            "border_radius": theme["border_radius"],
            "background_color": "white",
        },
    )

