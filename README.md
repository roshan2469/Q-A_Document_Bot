## 📄 RAG Document Chatbot (Offline with Ollama)

## 1. Project Overview

This project is a Retrieval-Augmented Generation (RAG) based document chatbot that allows users to ask questions from their own documents (PDF, TXT, DOCX).
It retrieves relevant context from the documents and uses a local LLM via Ollama to generate accurate, source-grounded answers.
The system runs completely offline without requiring any paid APIs.

---

## 2. Tech Stack

* Python 3.13
* LangChain (core framework)
* langchain-community
* langchain-text-splitters
* ChromaDB (vector database)
* sentence-transformers (embedding model)
* Ollama (local LLM runtime)
* Model used: `phi` (via Ollama)
* PyPDF (PDF loader)
* docx2txt (DOCX loader)

---

## 3. Architecture Overview

The system follows a standard RAG pipeline:

**Ingestion → Chunking → Embedding → Storage → Retrieval → Generation**

### Workflow:

1. Documents are loaded from the `data/` folder
2. Text is split into smaller chunks
3. Each chunk is converted into embeddings (vector representations)
4. Embeddings are stored in ChromaDB
5. User query is converted into an embedding
6. Relevant chunks are retrieved using similarity search
7. Retrieved context is passed to the LLM (Ollama)
8. LLM generates a final answer based only on retrieved context

---

## 4. Chunking Strategy

* Method: Recursive Character Text Splitter
* Chunk size: 800 characters
* Chunk overlap: 150 characters

### Why this strategy?

* Maintains context continuity between chunks
* Prevents loss of meaning at chunk boundaries
* Optimizes retrieval accuracy and LLM input size

---

## 5. Embedding Model & Vector Database

### Embedding Model:

* `all-MiniLM-L6-v2` (from sentence-transformers)

**Why chosen:**

* Lightweight and fast
* Works offline
* Good semantic similarity performance

---

### Vector Database:

* ChromaDB (local persistent storage)

**Why chosen:**

* Easy to set up
* No external dependencies
* Fast similarity search
* Stores data locally

---

## 6. Setup Instructions

### Step 1: Clone Repository

```bash
git clone <your-repo-url>
cd rag-doc-bot
```

---

### Step 2: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Step 3: Install Dependencies

```bash
pip install langchain langchain-community langchain-text-splitters chromadb sentence-transformers pypdf docx2txt
```

---

### Step 4: Install Ollama

Download and install from: https://ollama.com/

---

### Step 5: Install LLM Model

```bash
ollama pull phi
```

---

### Step 6: Add Documents

Place your files inside:

```
data/
```

Supported formats:

* PDF
* TXT
* DOCX

---

### Step 7: Run Ingestion Pipeline

```bash
python src/ingest.py
```

---

### Step 8: Run Chatbot

```bash
python src/main.py
```

---

## 7. Environment Variables

This project does NOT require any API keys because it uses local models via Ollama.

If switching to cloud models (e.g., OpenAI), create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 8. Example Queries

1. What is Artificial Intelligence?
2. What are the types of AI mentioned in the document?
3. Explain machine learning from the document
4. What are the ethical concerns of AI?
5. Summarize the key points of the document

### Expected Answer Behavior:

* Answers are derived only from document content
* Includes references to source file and page number
* Returns "I don't know" if answer is not found

---

## 9. Known Limitations

* Local LLM (phi) may generate less detailed answers compared to large cloud models
* Retrieval quality depends on chunking and document quality
* Cannot handle very large documents efficiently on low-RAM systems
* Occasional duplicate source outputs
* Strict context-only answering depends on prompt compliance (LLM may still hallucinate in rare cases)

---

## 🚀 Future Improvements

* Add Streamlit UI for better interaction
* Improve source formatting
* Add chat history
* Use better local models if hardware allows
* Deploy as a web application

---

## 📌 Conclusion

This project demonstrates a complete end-to-end RAG pipeline using local tools, making it cost-effective and suitable for offline environments. It showcases practical skills in document processing, embeddings, vector databases, and LLM integration.

---
