import os
import re
from io import BytesIO
from datetime import datetime

import streamlit as st
from pypdf import PdfReader
from PIL import Image

st.set_page_config(page_title="MediScan AI | Medical Report Interpreter", page_icon="🩺", layout="wide")

CUSTOM_CSS = """
<style>
.main {background: #f5f8fc;}
.block-container {padding-top: 2rem; max-width: 1180px;}
.hero {background: linear-gradient(120deg,#0b3c70,#167ac6); padding: 28px 32px; border-radius: 18px; color: white; margin-bottom: 20px;}
.hero h1 {font-size: 2.25rem; margin: 0 0 8px 0;}
.hero p {font-size: 1.03rem; opacity: .92; margin: 0;}
.metric-card {background: white; border: 1px solid #e3ebf4; border-radius: 14px; padding: 16px;}
.small-muted {color: #60748a; font-size: .9rem;}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>🩺 MediScan AI</h1>
  <p>Understand your medical reports in simple language — with AI-assisted explanations.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("About MediScan")
    st.write("Upload a report or paste its text to receive a plain-language explanation.")
    st.divider()
    st.subheader("AI configuration")
    api_key = st.text_input("Google Gemini API key (optional)", type="password",
                            help="Used only for this session. If omitted, the app provides a basic report summary.")
    st.caption("Get an API key from Google AI Studio. Never share your key.")
    st.divider()
    st.caption("Privacy: uploaded report contents are processed for this session. Avoid uploading reports you do not have permission to use.")

def extract_text(uploaded_file):
    name = uploaded_file.name.lower()
    raw = uploaded_file.getvalue()
    if name.endswith(".pdf"):
        reader = PdfReader(BytesIO(raw))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    if name.endswith(".txt"):
        return raw.decode("utf-8", errors="ignore")
    if name.endswith((".png", ".jpg", ".jpeg", ".webp")):
        try:
            import pytesseract
            image = Image.open(BytesIO(raw))
            return pytesseract.image_to_string(image)
        except Exception:
            return ""
    return ""

def local_summary(report_text):
    lines = [x.strip() for x in report_text.splitlines() if x.strip()]
    numeric = []
    for line in lines:
        # Identify lines that contain a number and a possible reference interval.
        if re.search(r"\d", line):
            numeric.append(line)
    if not numeric:
        return ("I could not reliably identify individual test values in this report. "
                "Please check that the PDF contains selectable text, or paste the report text manually.")
    excerpt = "\n".join(f"• {line}" for line in numeric[:35])
    return (
        "### Report text detected\n"
        "I found the following lines containing numbers. This basic mode does not determine "
        "whether a result is medically normal unless the report's reference range is clearly shown.\n\n"
        f"{excerpt}\n\n"
        "**Next step:** Compare each result with the reference interval printed by the laboratory. "
        "Reference ranges can vary by lab, age, sex, and other factors."
    )

def gemini_explain(report_text, key):
    from google import genai
    client = genai.Client(api_key=key)
    prompt = f"""
You are a careful medical-report explainer, not a clinician. Explain the report below for a general adult reader.
Use simple, non-alarming language and organize the answer under:
1. Short overview
2. Test-by-test explanation (value, unit, lab reference range if present, and whether it is inside/outside that stated range)
3. What out-of-range results can commonly be associated with (say these are possibilities, not diagnoses)
4. Questions to ask a qualified healthcare professional
5. Important limitations

Rules:
- Do not diagnose, prescribe, recommend stopping/changing medicines, or claim certainty.
- Do not invent values, units, or reference ranges.
- If a reference range is missing or unclear, say so.
- Mention that results must be interpreted with symptoms, history, medicines, and clinician assessment.
- If a result appears urgent or the report itself says critical, advise prompt contact with a healthcare professional/emergency services as appropriate.
- Keep the explanation understandable and balanced.
Report:
{report_text[:24000]}
"""
    response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
    return response.text

st.subheader("1. Add your medical report")
col1, col2 = st.columns([1, 1])
with col1:
    uploaded = st.file_uploader("Upload PDF, TXT, or image", type=["pdf", "txt", "png", "jpg", "jpeg", "webp"])
with col2:
    st.info("For best results, upload a clear PDF or paste selectable report text. Image OCR requires Tesseract to be installed on the computer running the app.")

pasted_text = st.text_area("Or paste the report text here", height=190,
                            placeholder="Example: Haemoglobin: 13.5 g/dL (Reference range: 12.0–15.5 g/dL)")

report_text = pasted_text.strip()
if uploaded is not None:
    extracted = extract_text(uploaded)
    if extracted.strip():
        report_text = (report_text + "\n\n" + extracted).strip()
        st.success(f"Text extracted from {uploaded.name}.")
    elif uploaded.name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        st.warning("Image text could not be extracted. Install Tesseract OCR or paste the report text manually.")
    else:
        st.warning("No selectable text was found. Try another PDF or paste the report text manually.")

st.subheader("2. Understand your results")
if st.button("Interpret my report", type="primary", disabled=not bool(report_text)):
    with st.spinner("Preparing your explanation..."):
        try:
            if api_key.strip():
                explanation = gemini_explain(report_text, api_key.strip())
                mode = "AI-assisted explanation (Gemini)"
            else:
                explanation = local_summary(report_text)
                mode = "Basic text summary (no AI key supplied)"
            st.session_state["explanation"] = explanation
            st.session_state["mode"] = mode
            st.session_state["source_text"] = report_text
        except Exception as e:
            st.error(f"Gemini error: {type(e).__name__}: {e}")
            st.session_state["explanation"] = local_summary(report_text)
            st.session_state["mode"] = "Basic fallback summary"
            st.session_state["source_text"] = report_text

if "explanation" in st.session_state:
    st.caption(f"Result mode: {st.session_state.get('mode', 'Summary')}")
    st.markdown(st.session_state["explanation"])
    download_content = (
        "MEDISCAN AI — MEDICAL REPORT EXPLANATION\n"
        f"Generated: {datetime.now().strftime('%d %b %Y, %I:%M %p')}\n"
        f"Mode: {st.session_state.get('mode', '')}\n\n"
        "EXPLANATION\n"
        f"{st.session_state['explanation']}\n\n"
        "DISCLAIMER\n"
        "This is educational information, not a diagnosis or medical advice. Consult a qualified healthcare professional.\n"
    )
    st.download_button("⬇️ Download explanation (.txt)", data=download_content,
                       file_name="mediscan_report_explanation.txt", mime="text/plain")

st.divider()
st.subheader("How it works")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**① Upload**")
    st.write("The app reads text from a PDF or text file, or accepts pasted report content.")
with c2:
    st.markdown("**② Interpret**")
    st.write("Gemini can explain values and reference ranges in everyday language.")
with c3:
    st.markdown("**③ Review**")
    st.write("Save the explanation and discuss results with your healthcare professional.")

st.warning("**Medical safety notice:** MediScan AI is an educational aid only. It cannot diagnose disease, assess emergencies, or replace a doctor. Do not make treatment or medication decisions based on this app. If you have severe or rapidly worsening symptoms, seek urgent medical care.")
st.caption("Student project prototype • MediScan AI")
