# MediScan AI — AI Medical Report Interpreter

A student project prototype that helps users understand the wording and values in medical reports.

**Student roll number:** 25BTRA0038  
**GitHub repository:** https://github.com/sanathrpoojary109-alt/MediScan-AI

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
   .venv\\Scripts\\activate
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
- Never commit API keys or real patient reports to GitHub.
- The app can still demonstrate report text extraction without an API key.

## Screenshots

Capture genuine screenshots after running the application. Use the fictional `sample_report.txt` file in this repository.

Save screenshots in a `screenshots/` folder:
- `screenshots/home.png` — application home screen
- `screenshots/input.png` — fictional report loaded
- `screenshots/result.png` — generated explanation
- `screenshots/download.png` — download control

See [SCREENSHOTS_GUIDE.md](SCREENSHOTS_GUIDE.md) for instructions. Do not upload real patient information or API keys. Add the images to GitHub before the final submission.

## Suggested demo video (under 5 minutes)

1. Introduce the problem and project (30 seconds).
2. Show the dashboard and upload the synthetic sample report (45 seconds).
3. Click **Interpret my report** and show the result (90 seconds).
4. Explain the output and download option (60 seconds).
5. Explain the technology stack and safety limitations (45 seconds).

See [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md) for a ready-to-read script.

## Important limitations and responsible use

- This is an educational prototype, not a medical device or clinical decision-support system.
- It must not be used to diagnose, prescribe, or make treatment decisions.
- Lab reference intervals vary by laboratory and patient context.
- The basic fallback mode only extracts lines containing numbers; it does not clinically classify results.
- OCR and AI may make mistakes. Verify values against the original report.
- Do not upload real patient information unless you have appropriate permission and understand the privacy implications.
- Before any real-world deployment, obtain qualified clinical, privacy, and security review.

## Submission details

- **Roll number:** 25BTRA0038
- **Student name:** To be filled in by the student
- **YouTube demo:** Add the uploaded video URL to [SUBMISSION_DETAILS.md](SUBMISSION_DETAILS.md)
