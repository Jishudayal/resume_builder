import reflex as rx
from ..utils.pdf_generator import generate_pdf
from ..utils.excel_generator import generate_excel

@rx.page(route="/download")
def download():
    return rx.box(
        rx.button("Download PDF", on_click=lambda: generate_pdf(ResumeState.data)),
        rx.button("Download Excel", on_click=lambda: generate_excel(ResumeState.data)),
    )
