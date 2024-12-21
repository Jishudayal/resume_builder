import reflex as rx
from ..components.header import header
from ..components.footer import footer
from ..components.template_card import template_card
from ..styles.theme import theme


@rx.page(route="/")
def index():
    return rx.fragment(
        # Header Component
        header(),
        # Main Landing Page Content
        rx.box(
            # Hero Section
            rx.box(
                rx.image(
                    src="landing_banner.png",
                    alt="Resume Builder",
                    width="100%",
                    height="auto",
                    border_radius="12px",
                    margin_bottom="2rem",
                ),
                rx.text(
                    "Build Your Dream Resume",
                    font_size="5xl",
                    font_weight="bold",
                    text_align="center",
                    color="#FFFFFF",
                    margin_bottom="1rem",
                ),
                rx.text(
                    "Our resume builder is designed to meet industry standards and help you stand out. With a variety of ATS-friendly templates, crafting your professional story has never been easier.",
                    font_size="lg",
                    color="#B0B0B0",
                    text_align="center",
                    max_width="800px",
                    margin="0 auto",
                    margin_bottom="2rem",
                ),
                style={
                    "background_color": "#1E1E1E",
                    "padding": "2rem",
                    "border_radius": "12px",
                    "box_shadow": "0 4px 8px rgba(0, 0, 0, 0.3)",
                    "margin_bottom": "3rem",
                },
            ),
            # Template Section
            rx.text(
                "Choose Your Template",
                font_size="3xl",
                font_weight="bold",
                text_align="center",
                color="#FFFFFF",
                margin_bottom="1rem",
            ),
            rx.text(
                "Select a design that matches your style and start building your resume effortlessly.",
                font_size="md",
                color="#B0B0B0",
                text_align="center",
                margin_bottom="2rem",
            ),
            rx.box(
                # Card Layout for Templates
                rx.box(
                    template_card("Modern Template", "/assets/images/modern.png", "/templates/modern"),
                    template_card("Classic Template", "/assets/images/classic.png", "/templates/classic"),
                    template_card("Creative Template", "/assets/images/creative.png", "/templates/creative"),
                    style={
                        "display": "grid",
                        "grid_template_columns": "repeat(auto-fit, minmax(300px, 1fr))",
                        "gap": "2rem",
                        "justify_content": "center",
                    },
                ),
                style={
                    "padding": "2rem",
                    "background_color": "#121212",
                    "border_radius": "12px",
                    "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.2)",
                },
            ),
        ),
        # Footer Component
        footer(),
    )
