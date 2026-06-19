from pdf_extractor import extract_text
from ai_analyzer import analyze_documents
from report_generator import generate_ddr

print("Reading PDFs...")

inspection_text = extract_text(
    "uploads/Sample Report.pdf"
)

thermal_text = extract_text(
    "uploads/Thermal Images.pdf"
)

print("Analyzing...")

result = analyze_documents(
    inspection_text,
    thermal_text
)
generate_ddr(
    result,
    "outputs/DDR_Report.docx"
)

print("DDR Report Created!")