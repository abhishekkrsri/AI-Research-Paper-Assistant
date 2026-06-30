# 📚 AI Research Paper Assistant

An AI-powered web application that enables users to upload research papers in PDF format, generate concise summaries, and ask intelligent questions about the document using Google's Gemini AI. Built with **Python**, **Streamlit**, and **Google Gemini API**, the application simplifies academic research by transforming lengthy papers into interactive conversations.

---

## 🚀 Features

* 📄 Upload and analyze research papers in PDF format
* 🤖 AI-powered question answering using Google Gemini
* 📝 Automatic research paper summarization
* 🔍 Context-aware responses based on uploaded documents
* ⚡ Fast and interactive Streamlit interface
* 💬 Chat-like experience for exploring research papers
* 🔒 Secure API key management using environment variables

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & NLP

* Google Gemini API

### PDF Processing

* PyPDF2 / PyMuPDF

### Environment Management

* python-dotenv

---

## 📂 Project Structure

```text
AI-Research-Paper-Assistant/
│── app.py                 # Main Streamlit application
│── requirements.txt       # Python dependencies
│── .env                   # Gemini API key (not committed)
│── assets/                # Images and static resources
│── uploads/               # Uploaded PDF files
│── utils.py               # Helper functions
│── README.md              # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/abhishekkrsri/AI-Research-Paper-Assistant.git
```

### 2. Navigate to the project

```bash
cd AI-Research-Paper-Assistant
```

### 3. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 🖥️ How It Works

1. Upload a research paper in PDF format.
2. The application extracts text from the document.
3. Google Gemini processes the extracted content.
4. Users can:

   * Generate a concise summary
   * Ask questions related to the paper
   * Receive intelligent, context-aware responses
5. The application displays answers in an interactive chat interface.

---

## 💡 Use Cases

* Students studying research papers
* Academic researchers
* Professors and educators
* Literature review assistance
* Technical documentation analysis
* AI-assisted learning

---

## 🔮 Future Improvements

* Multi-PDF support
* Research paper comparison
* Citation extraction
* AI-generated literature reviews
* Semantic search using vector embeddings
* Chat history
* Voice interaction
* User authentication
* Dark mode
* Export summaries to PDF

---

## 📊 Skills Demonstrated

* Python
* Streamlit
* Google Gemini API
* Prompt Engineering
* Natural Language Processing
* PDF Processing
* AI Application Development
* API Integration
* Environment Variable Management

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Abhishek Kumar Srivastava**

* GitHub: https://github.com/abhishekkrsri
* LinkedIn: *(https://www.linkedin.com/in/abhishek-kumar-srivastava-350204330)*
* Email: [abhishekkumarsrivastava101@gmail.com]

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

## 📄 License

This project is licensed under the MIT License.
