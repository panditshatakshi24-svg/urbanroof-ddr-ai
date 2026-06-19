import streamlit as st
from datetime import datetime

from pdf_extractor import extract_text
from ai_analyzer import analyze_documents
from report_generator import generate_ddr

st.set_page_config(page_title="UrbanRoof DDR Generator")

st.title("🏠 UrbanRoof DDR Generator")

st.write(
"Upload Inspection and Thermal Reports to generate a DDR."
)

inspection_file = st.file_uploader(
"Upload Inspection Report PDF",
type=["pdf"]
)

thermal_file = st.file_uploader(
"Upload Thermal Report PDF",
type=["pdf"]
)

if st.button("Generate DDR"):
    if inspection_file and thermal_file:
        # Save uploaded files
        with open("uploads/inspection.pdf", "wb") as f:
            f.write(inspection_file.read())

        with open("uploads/thermal.pdf", "wb") as f:
            f.write(thermal_file.read())

        st.info("Reading PDFs...")

        inspection_text = extract_text(
            "uploads/inspection.pdf"
        )

        thermal_text = extract_text(
            "uploads/thermal.pdf"
        )

        st.info("Analyzing reports...")

        try:
            result = analyze_documents(
                inspection_text,
                thermal_text
            )
        except RuntimeError as exc:
            st.error(str(exc))
            st.stop()

        # Generate DDR with timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"outputs/DDR_Report_{timestamp}.docx"
        
        generate_ddr(
            result,
            output_file
        )

        st.success("DDR Generated Successfully!")

        st.text_area(
            "DDR Preview",
            result,
            height=400
        )

        with open(
            output_file,
            "rb"
        ) as file:

            st.download_button(
                "Download DDR Report",
                file,
                file_name="DDR_Report.docx"
            )

else:
    st.warning(
        "Please upload both PDFs."
    )

