# KnowledgeRAG

An End-to-End Retrieval-Augmented Generation (RAG) System that enables users to query information from Wikipedia, Websites, and PDF documents using Large Language Models (LLMs).

KnowledgeRAG combines dynamic knowledge retrieval, semantic search, vector embeddings, and LLM-powered question answering to generate accurate and context-aware responses.

---

# Overview

KnowledgeRAG allows users to interact with external knowledge sources through a unified interface.

The system supports:

* Dynamic Wikipedia Search
* Website Content Ingestion
* PDF Document Processing
* Semantic Search using Vector Embeddings
* Retrieval-Augmented Generation (RAG)
* Interactive Streamlit Interface

The project uses FAISS as a vector database, mxbai-embed-large for embeddings, and Llama 3.2 for answer generation.

---

# Features

## Wikipedia Search

* Ask questions directly without manually loading articles.
* Automatically searches Wikipedia.
* Retrieves the most relevant article.
* Processes article content through the RAG pipeline.
* Generates context-aware answers.

### Example

```text
Question:
What is Ray Ban?
```

---

## Website Knowledge Base

* Extract content from websites.
* Chunk and embed website data.
* Store embeddings in FAISS.
* Ask questions based on website content.

### Example

```text
URL:
https://fastapi.tiangolo.com/

Question:
What is FastAPI?
```

---

## PDF Knowledge Base

* Upload PDF documents directly through the UI.
* Extract text from PDFs.
* Generate embeddings.
* Store content in FAISS.
* Query uploaded documents.

### Example

```text
Question:
What is Retrieval-Augmented Generation?
```

---

# Core Concepts Used

This project implements several important AI and LLM engineering concepts:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Embeddings
* Vector Databases
* Similarity Search
* Prompt Engineering
* Document Chunking
* Information Retrieval
* Large Language Models
* Dynamic Knowledge Retrieval

---

# Architecture

## Wikipedia Workflow

```text
User Question
      │
      ▼
Wikipedia Search
      │
      ▼
Best Matching Article
      │
      ▼
Article Content
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Relevant Context
      │
      ▼
Prompt Builder
      │
      ▼
Llama 3.2
      │
      ▼
Generated Answer
```

---

## Website Workflow

```text
Website URL
      │
      ▼
Website Loader
      │
      ▼
Extract Website Content
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Relevant Context
      │
      ▼
Prompt Builder
      │
      ▼
Llama 3.2
      │
      ▼
Generated Answer
```

---

## PDF Workflow

```text
PDF Upload
      │
      ▼
PDF Loader
      │
      ▼
Extract Text
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Relevant Context
      │
      ▼
Prompt Builder
      │
      ▼
Llama 3.2
      │
      ▼
Generated Answer
```

---

## Complete System Architecture

```text
                           User Question
                                  │
                                  ▼
                    ┌────────────────────────┐
                    │      Source Type       │
                    └──────────┬─────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
      Wikipedia            Website               PDF
          │                    │                    │
          ▼                    ▼                    ▼
   Wikipedia Search      Website Loader       PDF Loader
          │                    │                    │
          ▼                    ▼                    ▼
      Article Text        Extracted Text      Extracted Text
          │                    │                    │
          └────────────┬───────┴───────┬────────────┘
                       │               │
                       ▼
                    Chunking
                       │
                       ▼
              Embedding Generation
                       │
                       ▼
              FAISS Vector Database
                       │
                       ▼
                   Retriever
                       │
                       ▼
               Relevant Chunks
                       │
                       ▼
                 Prompt Builder
                       │
                       ▼
                    Llama 3.2
                       │
                       ▼
                Generated Answer
```

---

# Project Structure

```text
L1 RAG/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── config/
│   └── config.py
│
├── Data/
│   ├── sample.txt
│   ├── topics.py
│   └── pdfs/
│
├── Docs/
│
├── LLM/
│   ├── llm_utils.py
│   ├── prompts.py
│   └── llama_test.py
│
├── Embeddings/
│   ├── embedding_utils.py
│   └── embedding_test.py
│
├── Chunking/
│   ├── chunk_utils.py
│   └── __init__.py
│
├── Retrieval/
│   └── retriever.py
│
├── RAG/
│   ├── prompt_builder.py
│   └── rag_pipeline.py
│
├── Sources/
│   ├── wikipedia_loader.py
│   ├── website_loader.py
│   └── pdf_loader.py
│
├── VectorDB/
│   ├── vector_store.py
│   ├── pdf_index/
│   └── website_index/
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── Tests/
│
└── venv/
```

---

# Tech Stack

## Programming Language

* Python 3.14

## Large Language Model

* Llama 3.2 (Ollama)

## Embedding Model

* mxbai-embed-large

## Frameworks & Libraries

* LangChain
* Streamlit
* Ollama
* BeautifulSoup4
* Requests
* Wikipedia
* PyPDF

## Vector Database

* FAISS (Facebook AI Similarity Search)

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd L1-RAG
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Pull the required models:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

Verify installation:

```bash
ollama list
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Usage

## Wikipedia

1. Select Wikipedia.
2. Ask a question directly.
3. System automatically searches Wikipedia.
4. Relevant article is processed through the RAG pipeline.
5. Answer is generated.

---

## Website

1. Select Website.
2. Enter website URL.
3. Load knowledge.
4. Ask questions.

---

## PDF

1. Select PDF.
2. Upload PDF document.
3. Load knowledge.
4. Ask questions.

---

# Example Questions

## Wikipedia

* What is Artificial Intelligence?
* What is Ray Ban?
* Who founded Tesla?
* Explain Machine Learning.

## Website

* What is FastAPI?
* What are FastAPI features?
* Explain Dependency Injection.

## PDF

* What is Retrieval-Augmented Generation?
* Summarize the paper.
* What challenges do LLMs face?

---

# Author

Ayush Raj Dewangan

