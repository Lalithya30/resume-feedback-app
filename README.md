
# 🧾 Resume Feedback Web App

This is a Flask-based web application that allows users to upload their resumes (PDF format) and receive automated feedback based on **keywords**, **readability**, and **presence of essential sections** (like Projects, Education, and Career Objective).

## 🚀 Features

- 🔍 **Keyword Analysis**: Checks for the presence of in-demand tech keywords like Python, Java, SQL, etc.
- 📖 **Readability Check**: Analyzes sentence structure to provide suggestions on clarity.
- 🧾 **Formatting Feedback**: Verifies if key resume sections (Projects, Education, Objective) are included.

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **Libraries**: PyPDF2, werkzeug


## 📂 Project Structure

```
.
├── app.py              # Flask backend logic
├── index.html          # Frontend form & result display
├── uploads/            # Folder for uploaded PDF resumes
├── static/             # Optional: CSS or images if added
├── README.md           # Project documentation
```

## ⚙️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/resume-feedback-app.git
cd resume-feedback-app
```

2. Install dependencies:
```bash
pip install flask PyPDF2
```

3. Run the app:
```bash
python app.py
```

4. Visit `http://127.0.0.1:5000/` in your browser.

## 📝 Sample Feedback Output

```html
🔍 Keyword Check:
✅ Found keywords: Python, Java, HTML

📖 Readability:
Total words: 512
Avg words per sentence: 18.73
✅ Sentence length is appropriate.

🧾 Formatting Tips:
✅ Career Objective section found.
✅ Projects section found.
⚠️ Education section missing.
```

## 📌 Future Enhancements

- Add login system for saving feedback
- Integrate with AI models for smarter suggestions
- Support DOCX resumes
