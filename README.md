# UrbanRoof DDR AI

## Overview

UrbanRoof DDR AI is an AI-powered system that automatically generates a Detailed Diagnostic Report (DDR) from:

* Inspection Reports
* Thermal Inspection Reports

The system extracts observations, identifies probable root causes, assesses severity, recommends corrective actions, and generates a client-ready report.

---

## Features

* PDF text extraction
* Thermal report analysis
* Observation extraction
* Duplicate finding merging
* Root cause identification
* Severity assessment
* Recommended actions generation
* Missing information detection
* Conflicting information detection
* DOCX report generation
* Streamlit web interface

---

## Project Structure

```text
urbanroof-ddr-ai/

├── app.py
├── streamlit_app.py
├── pdf_extractor.py
├── image_extractor.py
├── ai_analyzer.py
├── report_generator.py
├── requirements.txt
├── README.md
├── uploads/
└── outputs/
```

---

## Workflow

```text
Inspection Report PDF
        +
Thermal Report PDF
        ↓
PDF Text Extraction
        ↓
Image Extraction
        ↓
Gemini AI Analysis
        ↓
Observation Merging
        ↓
Root Cause Analysis
        ↓
Severity Assessment
        ↓
DDR Generation
        ↓
DOCX Report
```

---

## Technologies Used

* Python
* Streamlit
* PyMuPDF (fitz)
* Google Gemini API
* python-docx

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/urbanroof-ddr-ai.git
cd urbanroof-ddr-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run Application

### Streamlit UI

```bash
streamlit run streamlit_app.py
```

### Command Line

```bash
python app.py
```

---

## Output

The system generates:

* Detailed Diagnostic Report (DDR)
* DOCX Report
* Structured observations
* Root cause analysis
* Severity assessment
* Recommendations

---

## Sample DDR Sections

* Property Issue Summary
* Area-wise Observations
* Probable Root Cause
* Severity Assessment
* Recommended Actions
* Additional Notes
* Missing or Unclear Information
* Conflicting Information

---

## Future Enhancements

* Automatic image-to-observation mapping
* Embedded images inside DDR
* PDF export
* Confidence scoring
* Multi-property processing
* Cloud deployment

---

## Assignment Objective

This project was developed for the UrbanRoof Applied AI Builder Assessment to demonstrate:

* Document understanding
* Information extraction
* Reasoning and diagnostics
* Report generation
* AI workflow design
