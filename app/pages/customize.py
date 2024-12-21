import reflex as rx
from ..components.resume_form import resume_form
from ..components.live_preview import live_preview

@rx.page(route="/customize")
def customize():
    return rx.box(
        rx.text(
            "Customize Your Resume",
            font_size="2xl",
            font_weight="bold",
            color="#E0E0E0",
            text_align="center",
            margin_bottom="1rem",
        ),
        rx.box(
            rx.hstack(
                rx.box(
                    resume_form(),
                    style={
                        "flex": "1",
                        "margin_right": "1rem",
                        "padding": "1rem",
                        "background_color": "#1E1E1E",
                        "border_radius": "8px",
                        "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.2)",
                    },
                ),
                rx.box(
                    live_preview(),
                    style={
                        "flex": "1",
                        "margin_left": "1rem",
                        "padding": "1rem",
                        "background_color": "#1E1E1E",
                        "border_radius": "8px",
                        "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.2)",
                    },
                ),
                style={"display": "flex", "flex_direction": "row"},
            ),
            style={"margin": "2rem", "padding": "1rem"},
        ),
        style={"background_color": "#121212", "padding": "2rem"},
    )
