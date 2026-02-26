How to Run This Project Locally

Follow these steps to run the Fake News Detector for Students on your system.

🔹 1. Install Python

Make sure Python 3.9 or higher is installed.

Check:

python --version

If Python is not installed, download it from:
👉 https://www.python.org/downloads/

⚠️ During installation, make sure to check “Add Python to PATH”

🔹 2. Clone the Repository
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector

(Or download the ZIP and extract it)

🔹 3. Create a Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate
🔹 4. Install Dependencies
python -m pip install -r requirements.txt
🔹 5. Add API Key

Create a .env file in the project root and add:

GOOGLE_API_KEY=your_api_key_here

You can get a free API key from Google AI Studio

🔹 6. Run the Application
python -m streamlit run app.py
🔹 7. Open in Browser

Streamlit will open automatically or show a link like:

http://localhost:8501
✅ That’s It!

You should now see the Fake News Detector for Students running in your browser 🎉

🧪 Testing

Paste any:

News article

Social media post

Fake or real content

Click Analyze Article to view:

Credibility score

Fake/Real verdict

AI-generated summary
