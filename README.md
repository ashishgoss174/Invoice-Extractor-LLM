# MultiLanguage Invoice Extractor

A Streamlit web application that uses Google's Gemini 1.5 Flash API to extract and understand invoice data from images.  
Supports multiple image formats (JPG, PNG, WebP) for invoices.  
**Note:** PDF upload support is disabled for deployment compatibility.

---

## Features

- Upload invoice images and ask questions about the content.
- Leverages Google's Gemini generative AI for powerful invoice analysis.
- Supports multiple languages in invoices.
- Easy-to-use, interactive web interface built with Streamlit.

---

## Demo

https://ashish-gossain-invoice-extractor-app.streamlit.app/

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- [Google Generative AI API Key](https://developers.generativeai.google/)
- Streamlit account for deployment (optional)

---

### Clone the repository

```bash
git clone https://github.com/ashishgoss174/Invoice-Extractor-LLM-APP
cd Invoice-Extractor-App

---

## 📁 Project Structure

invoice-extractor/
│
├── app.py # Main Streamlit app for image invoices
├── app_pdf.py # Local-only PDF extractor (not for deployment)
├── requirements.txt # All required dependencies
├── readme.md # This documentation file
│
├── .streamlit/
│ └── secrets.toml # (Add API key securely for deployment – not committed)
│
├── .gitignore # Prevents accidental commits of secrets or venv
├── poppler-24.08.0/ # PDF rendering dependency (local use)
├── venv/ # Virtual environment
└── ...

yaml
Copy
Edit

---

## 🚀 How to Run

### 🔹 1. Install Dependencies

```bash
pip install -r requirements.txt
🔹 2. Set Up Your API Key
Use .streamlit/secrets.toml (do not hardcode your API key):

ini
Copy
Edit
[general]
GOOGLE_API_KEY = "your-google-api-key"
On Streamlit Cloud, add this secret through the "Secrets" tab in your app settings.

🖼️ app.py — Image Invoice Extractor (Deployable)
Supports the following image formats:

JPG

JPEG

PNG

WEBP

Run with:

bash
Copy
Edit
streamlit run app.py
⚠️ PDF Not Supported
Due to limitations in Streamlit Cloud, PDF file reading is not supported here.

📄 app_pdf.py — Local PDF Invoice Extractor
This version is meant to be run only locally, where you can analyze PDF invoices.

Requires:

pdf2image

poppler (Make sure the poppler-24.08.0 folder is configured properly)

Run with:

bash
Copy
Edit
streamlit run app_pdf.py
Make sure to update the path to Poppler in your script if needed.

✅ Deployment (Streamlit Cloud)
Push this project (without .env or API keys) to GitHub.

Connect your GitHub repo to Streamlit Cloud.

In App Settings → Secrets, add:

toml
Copy
Edit
GOOGLE_API_KEY = "your-secret-key"
Deploy the app with app.py.

👤 Author
Created by Ashish Gossain

📜 License
MIT License

vbnet
Copy
Edit

Let me know if you'd like a version with badges, a live demo link, or how to add a sample invoice for demo