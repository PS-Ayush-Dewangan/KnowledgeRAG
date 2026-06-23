# KnowledgeRAG

KnowledgeRAG is an end-to-end Retrieval-Augmented Generation (RAG) application that enables users to query information from Wikipedia, websites, and PDF documents using Large Language Models (LLMs).

The system retrieves relevant information from external knowledge sources, augments the prompt with the retrieved context, and generates accurate, context-aware responses using Llama 3.2.

---

# Overview

KnowledgeRAG combines semantic search, vector embeddings, and Retrieval-Augmented Generation (RAG) to answer user queries using custom knowledge sources.

The application supports:

* Dynamic Wikipedia Search
* Website Content Scraping
* PDF Document Processing
* Semantic Search using FAISS
* Context-Aware Question Answering
* Interactive Streamlit User Interface

---

# Features

## Wikipedia Search

* Ask questions directly without manually loading articles.
* Automatically searches Wikipedia.
* Retrieves the most relevant article.
* Generates answers using retrieved knowledge.

## Website Knowledge Base

* Extracts content from websites.
* Creates embeddings and stores them in FAISS.
* Answers questions based on website content.

## PDF Knowledge Base

* Upload PDF documents directly from the UI.
* Extracts and processes document content.
* Supports question answering over uploaded documents.

## Retrieval-Augmented Generation

* Semantic Chunking
* Embedding Generation
* Vector Similarity Search
* Context Retrieval
* LLM-Based Answer Generation

## User Interface

* Built using Streamlit
* Dynamic source selection
* PDF upload support
* Interactive question-answering workflow

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
Llama 3.2
      │
      ▼
Generated Answer
```

## Website / PDF Workflow

```text
Website / PDF
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

## Complete System Architecture

```text
                    ┌─────────────────┐
                    │ User Question   │
                    └────────┬────────┘
                             │
               ┌─────────────┼─────────────┐
               │             │             │
               ▼             ▼             ▼
        Wikipedia       Website         PDF
          Search        Loader         Loader
               │             │             │
               │             ▼             ▼
               │      Text Extraction  Text Extraction
               │             │             │
               │             ▼             ▼
               │          Chunking     Chunking
               │             │             │
               │             ▼             ▼
               │        Embeddings    Embeddings
               │             │             │
               │             ▼             ▼
               │          FAISS DB     FAISS DB
               │             │             │
               │             ▼             ▼
               │          Retriever   Retriever
               │             │             │
               └───────┬─────┴─────┬───────┘
                       │           │
                       ▼           ▼
                   Context Retrieval
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

# Tech Stack

## Programming Language

* Python 3.14

## Large Language Model

* Llama 3.2

## Embedding Model

* mxbai-embed-large

## Frameworks & Libraries

* LangChain
* Streamlit
* Ollama
* BeautifulSoup4
* PyPDF
* Wikipedia API

## Vector Database

* FAISS (Facebook AI Similarity Search)

---

# Core Concepts Used

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Embeddings
* Vector Databases
* Similarity Search
* Prompt Engineering
* Document Chunking
* Information Retrieval
* Large Language Models

---

# Project Structure

```text
L1 RAG/
│
├── app.py
├── README.md
├── requirements.txt
│
├── config/
│   └── config.py
│
├── Data/
│   ├── sample.txt
│   ├── topics.py
│   └── pdfs/
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
│   └── chunk_utils.py
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
│   └── vector_store.py
│
├── Tests/
│
└── faiss_index/
```

---

# Author

Ayush Raj Dewangan


