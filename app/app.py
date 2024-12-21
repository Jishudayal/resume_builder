import reflex as rx
from .state import ResumeState
from .pages.index import index
from .pages.templates import templates
from .pages.customize import customize

app = rx.App()

app.add_page(index)
app.add_page(templates)
app.add_page(customize)

# Set the global app state
app.state = ResumeState


