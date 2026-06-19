import os
import google.generativeai as genai

# Read API key from environment for safety. Set GEMINI_API_KEY (preferred)
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_documents(inspection_text, thermal_text):
    prompt = f"""
You are a Building Diagnostics Expert.

Generate a professional Detailed Diagnostic Report.

DO NOT RETURN JSON.

Use these headings exactly:

Property Issue Summary

Area-wise Observations

Probable Root Cause

Severity Assessment

Recommended Actions

Additional Notes

Missing or Unclear Information

Conflicting Information

Inspection Report:
{inspection_text[:12000]}

Thermal Report:
{thermal_text[:12000]}
"""

    try:
        response = model.generate_content(prompt)
    except Exception as exc:
        error_message = str(exc)
        if "ResourceExhausted" in error_message or "quota" in error_message.lower():
            raise RuntimeError(
                "Gemini quota exceeded. Please wait and retry later, or upgrade your Google Cloud quota. "
                "If you’re hitting free tier limits, switch to a paid plan or reduce usage."
            ) from exc
        raise

    text = response.text.strip()

    # Remove markdown fences if present
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return text
