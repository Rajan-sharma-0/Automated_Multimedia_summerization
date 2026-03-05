# helpers/save_text_to_pdf.py

from fpdf import FPDF

def save_text_to_pdf(text: str, output_path: str):
    """
    Save text to PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in text.splitlines():
        pdf.multi_cell(0, 10, txt=line)

    pdf.output(output_path)
