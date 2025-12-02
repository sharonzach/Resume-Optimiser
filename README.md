# 🌸 Resume Optimizer AI

A beautiful, intelligent, and fully automated Resume Optimization system powered exclusively by **Google Gemini**.

![UI Preview](https://via.placeholder.com/800x400?text=Pastel+UI+Preview)

## ✨ Features

- **🎨 Pastel & Cute UI**: A user-friendly, interactive interface with glassmorphism and soft animations.
- **🧠 100% Gemini Powered**: Uses Gemini 1.5 Flash & Pro for OCR, parsing, reasoning, and rewriting.
- **⚡ High Performance**: Parallelized pipeline for fast analysis.
- **📄 PDF In / PDF Out**: Upload your resume, get a detailed PDF report with optimized versions.
- **📊 Comprehensive Scoring**:
  - **ATS Score**: Keyword optimization check.
  - **JD Match**: Semantic alignment with the job description.
  - **Skill Gap**: Identifies missing critical skills.
  - **Bias Detection**: Checks for unconscious bias markers.
  - **Layout Analysis**: Visual structure evaluation.
- **✍️ Multi-Persona Rewriting**:
  - *ATS Optimized* (Machine friendly)
  - *HR Optimized* (Human friendly)
  - *Achievement Boosted* (Impact focused)
  - *Domain Specific* (Jargon heavy)

## 🛠️ Tech Stack

- **Backend**: Python FastAPI (Async/Parallel)
- **Frontend**: React (Single File Component via CDN)
- **AI Engine**: Google Gemini 1.5 Flash (Speed) & Pro (Reasoning)
- **PDF Engine**: PyMuPDF (OCR input) & ReportLab (Report output)
- **Styling**: Vanilla CSS (Custom Design System)

## 🚀 Setup & Run

1.  **Clone & Install**:
    ```bash
    # Install Python dependencies
    pip install -r backend/requirements.txt
    ```

2.  **Configure API Key**:
    Create a `.env` file in `backend/.env`:
    ```env
    GOOGLE_API_KEY=YOUR_API_KEY
    ```

3.  **Start the Server**:
    ```bash
    cd backend
    python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

4.  **Launch**:
    Open your browser to `http://localhost:8000`.

## 📝 Example Usage

### Input
**Upload**: Your current PDF Resume.

**Job Description (Paste this sample)**:
```text
Role: Generative AI Engineer
Experience: 1–3 years
Location: Remote / Hybrid

Responsibilities:
- Build LLM-powered applications (RAG, chatbots, summarizers).
- Fine-tune transformer models for NLP tasks.
- Implement vector databases (Pinecone/Qdrant) for semantic search.
- Integrate LLM workflows using LangChain or LlamaIndex.
- Evaluate model performance using BLEU, ROUGE, perplexity.

Required Skills:
- Python, PyTorch
- HuggingFace Transformers
- Prompt engineering
- Knowledge of embeddings & vector search
- Experience with REST APIs and microservices

Good to Have:
- Experience with multimodal LLMs
- Cloud deployment (AWS/GCP)
- Coursework/research in GenAI
```

### Output
The system will generate:
1.  **Scores**: e.g., "ATS Score: 85/100", "Skill Gap: 12%".
2.  **Missing Skills**: e.g., "LangChain", "Pinecone".
3.  **Rewritten Resume**: A fully rewritten version tailored to "Generative AI Engineer".
4.  **PDF Report**: A downloadable summary.

## 📂 Project Structure

```
resume_optimizer/
├── backend/
│   ├── app/
│   │   ├── services/      # Gemini AI Wrappers (OCR, Scorer, Rewriter)
│   │   ├── main.py        # FastAPI Entrypoint
│   │   └── ...
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── index.html         # React App Entry
│   ├── styles.css         # Pastel Theme Styles
│   └── app.js             # Frontend Logic
└── README.md
```

---
*Built with ❤️ using Google Gemini*

