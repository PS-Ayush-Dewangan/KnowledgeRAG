# KnowledgeRAG

An end-to-end Retrieval-Augmented Generation (RAG) application that enables users to create custom knowledge bases from Wikipedia articles, websites, and PDF documents, and interact with them using natural language queries powered by Large Language Models.

---

# Overview

KnowledgeRAG combines modern AI technologies including Large Language Models (LLMs), embeddings, vector databases, and semantic retrieval to provide accurate and context-aware answers from user-provided knowledge sources.

The application allows users to:

* Load knowledge from Wikipedia
* Scrape and process website content
* Upload and analyze PDF documents
* Generate vector embeddings
* Store embeddings in a FAISS vector database
* Retrieve relevant context using semantic search
* Generate answers using Llama 3.2
* Interact through a Streamlit-based web interface

---

# Features

## Knowledge Source Integration

* Wikipedia Article Ingestion
* Website Content Scraping
* PDF Document Processing

## Retrieval-Augmented Generation (RAG)

* Semantic Text Chunking
* Vector Embedding Generation
* FAISS Vector Database Storage
* Similarity-Based Document Retrieval
* Context-Aware Answer Generation

## AI Capabilities

* Llama 3.2 Integration via Ollama
* MXBAI Embed Large Embeddings
* Semantic Search
* Question Answering over Custom Knowledge Bases

## Interactive Web Interface

* Streamlit Dashboard
* Wikipedia Topic Selection
* Website URL Input
* PDF Upload Support
* Interactive Question Answering

---

# Architecture

```text
Wikipedia / Website / PDF
            │
            ▼
      Data Loaders
            │
            ▼
     Text Extraction
            │
            ▼
        Chunking
            │
            ▼
   Embedding Generation
            │
            ▼
      FAISS Vector DB
            │
            ▼
        Retriever
            │
            ▼
        Llama 3.2
            │
            ▼
     Answer Generation
            │
            ▼
       Streamlit UI
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
│   ├── chunking_test.py
│   ├── vector_test.py
│   ├── test_llm_context.py
│   ├── test_retrieval.py
│   ├── test_rag.py
│   ├── test_multi_wikipedia.py
│   ├── test_wikipedia_loader.py
│   ├── test_wikipedia_query.py
│   ├── test_wikipedia_rag.py
│   ├── test_website_loader.py
│   ├── test_website_rag.py
│   ├── test_pdf_loader.py
│   ├── test_pdf_rag.py
│   └── test_pdf_query.py
│
└── venv/
```

---

# Tech Stack

## Programming Language

* Python 3.14

## AI & LLM

* Ollama
* Llama 3.2

## Embedding Model

* MXBAI Embed Large

## Frameworks & Libraries

* LangChain
* Streamlit
* FAISS
* BeautifulSoup4
* Requests
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

Install Ollama and pull required models:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

Verify models:

```bash
ollama list
```

---

# Run Application

Start the Streamlit application:

```bash
streamlit run app.py
```

---

# Usage

## Wikipedia Knowledge Base

1. Select **Wikipedia**
2. Enter a topic
3. Click **Load Knowledge**
4. Ask questions related to the topic

### Example

```text
Topic:
Artificial Intelligence

Question:
What is Machine Learning?
```

---

## Website Knowledge Base

1. Select **Website**
2. Enter a website URL
3. Click **Load Knowledge**
4. Ask questions based on website content

### Example

```text
URL:
https://fastapi.tiangolo.com/

Question:
What is FastAPI?
```

---

## PDF Knowledge Base

1. Select **PDF**
2. Upload a PDF document
3. Click **Load Knowledge**
4. Ask questions based on document content

### Example

```text
PDF:
Research Paper

Question:
What is Retrieval-Augmented Generation?
```

---

# Example Queries

## Wikipedia

```text
What is Artificial Intelligence?
What is Deep Learning?
Explain Neural Networks.
```

## Website

```text
What is FastAPI?
What are the features of FastAPI?
How does dependency injection work?
```

## PDF

```text
What is Retrieval-Augmented Generation?
Summarize the paper.
What challenges do LLMs face?
```

---

# Author

**Ayush Raj Dewangan**

