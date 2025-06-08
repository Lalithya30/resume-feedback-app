from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text_from_pdf(filepath):
    text = ""
    try:
        reader = PdfReader(filepath)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception:
        text = "Could not extract text."
    return text

def generate_feedback(text):
    feedback = ""

    # Keyword analysis
    keywords = ["Python", "Java", "HTML", "CSS", "SQL", "Git", "Machine Learning", "Django", "Flask", "REST API"]
    found_keywords = [kw for kw in keywords if kw.lower() in text.lower()]
    feedback += "<strong>🔍 Keyword Check:</strong><br>"
    feedback += f"{'✅ Found' if found_keywords else '❌ No'} keywords: {', '.join(found_keywords) if found_keywords else ''}<br>"

    # Readability (basic)
    words = text.split()
    sentences = text.count('.') + text.count('!') + text.count('?')
    avg_words_per_sentence = len(words) / sentences if sentences else 0

    feedback += "<br><strong>📖 Readability:</strong><br>"
    feedback += f"Total words: {len(words)}<br>"
    feedback += f"Avg words per sentence: {avg_words_per_sentence:.2f}<br>"
    if avg_words_per_sentence > 25:
        feedback += "🟡 Try shorter sentences for clarity.<br>"
    elif avg_words_per_sentence < 10:
        feedback += "🟡 Sentences may be too short or choppy.<br>"
    else:
        feedback += "✅ Sentence length is appropriate.<br>"

    # Formatting & sections
    feedback += "<br><strong>🧾 Formatting Tips:</strong><br>"
    sections = {
        "Career Objective": ["Objective", "CAREER OBJECTIVE"],
        "Projects": ["Project", "PROJECT WORK"],
        "Education": ["Education"]
    }

    for section, keywords in sections.items():
        found = any(keyword in text for keyword in keywords)
        feedback += f"{'✅' if found else '⚠️'} {section} section {'found' if found else 'missing'}.<br>"

    return feedback

@app.route("/", methods=["GET", "POST"])
def upload_file():
    feedback = ""
    if request.method == "POST":
        file = request.files["resume"]
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path)
            text = extract_text_from_pdf(path)
            feedback = generate_feedback(text)
    return render_template("index.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
