# MediScan AI — AI Medical Report Interpreter

A student project prototype that helps users understand the wording and values in medical reports.

## Features
- Upload PDF and TXT reports, or paste report text.
- Optional image OCR (requires Tesseract installed on the host).
- Optional Google Gemini-powered plain-language explanation.
- Basic offline text extraction fallback when no Gemini key is supplied.
- Download the explanation as a text file.
- Medical safety disclaimer and privacy reminders.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```

The browser should open the app at the local address shown in the terminal.

## Enable AI explanations

- Create a Google Gemini API key in Google AI Studio.
- Run the app and paste the key into the **Google Gemini API key** field in the sidebar.
- The key is held in Streamlit session state for the current session and is not written into this project.
- Never commit API keys or real patient reports to GitHub.

Without an API key, the app still runs and provides a basic text summary, but it will not generate AI medical explanations.

## Deploy on Streamlit Community Cloud

1. Push this project to a GitHub repository.
2. Sign in to Streamlit Community Cloud and deploy the repository.
3. Set `app.py` as the main file.
4. Add any required secrets in the deployment settings; alternatively, enter the Gemini key in the app sidebar for a demo.
5. Test with synthetic/sample data only.

## Suggested 5-minute demo
1. Introduce the problem and the purpose of MediScan AI (30 seconds).
2. Show the dashboard and upload a synthetic sample report (45 seconds).
3. Paste or upload sample lab results and click **Interpret my report** (90 seconds).
4. Explain the output, reference-range limitations, and download option (60 seconds).
5. Explain the technology stack, privacy safeguards, and medical disclaimer (45 seconds).

## Important limitations and responsible use
- This is an educational prototype, not a medical device or clinical decision-support system.
- It must not be used to diagnose, prescribe, or make treatment decisions.
- Lab reference intervals vary by laboratory and patient context.
- The basic fallback mode only extracts lines containing numbers; it does not clinically classify results.
- Do not upload real patient information unless you have appropriate permission and understand the privacy implications.
- Before any real-world deployment, obtain qualified clinical, privacy, and security review.
