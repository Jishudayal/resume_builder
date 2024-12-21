from weasyprint import HTML

def generate_pdf(data, template_path="templates/modern.html"):
    # Render the template with user data
    rendered_html = render_template(template_path, data)
    pdf = HTML(string=rendered_html).write_pdf()
    return pdf
