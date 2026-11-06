# MediScan AI — Demo Video Script (3–4 minutes)

## 0:00–0:25 — Introduction
"Hello, my name is [Your Name], roll number 25BTRA0038. My project is MediScan AI, an AI Medical Report Interpreter. It aims to make medical report wording easier to understand."

## 0:25–0:55 — Problem and solution
"Medical reports often contain technical terms and laboratory values. This application lets a user upload a report or paste report text and receive a plain-language explanation."

## 0:55–1:45 — Live demonstration
"Here is the MediScan AI interface. I will use the synthetic sample_report.txt file, which contains fictional values and no real patient information. I can upload the file or paste report text, then select Interpret my report. Without an API key, the app shows a basic text summary. With a Google Gemini API key, it can generate a structured explanation."

## 1:45–2:35 — Explain the result
"The output explains the report content and, when AI is enabled, discusses values in relation to reference ranges printed in the report. I can download the explanation as a text file."

## 2:35–3:15 — Technology
"The frontend is built with Streamlit. PDF extraction uses pypdf, image processing uses Pillow and optional Tesseract OCR, and optional AI explanation uses the Google Gemini API."

## 3:15–3:45 — Safety and conclusion
"This is an educational prototype only. It cannot diagnose or replace a doctor. OCR and AI can make mistakes, so results must be checked against the original report and discussed with a healthcare professional. Thank you."

## Recording checklist
- Use synthetic/sample data only; never show real patient information.
- Show the upload or paste-text flow and a successful result.
- Show the download option.
- Keep the recording under 5 minutes.
- Upload to YouTube as Unlisted or Public and paste the video URL into SUBMISSION_DETAILS.md.
