# 🧠 KnowledgeRAG

> An End-to-End Retrieval-Augmented Generation (RAG) system that lets you query knowledge from Wikipedia, Websites, and PDF documents using Large Language Models — powered by Pinecone vector search and Llama 3.2.

---

## 📌 Overview

KnowledgeRAG is a production-ready RAG application that combines semantic search, vector embeddings, cloud-based vector storage, and LLM-powered question answering into a unified, interactive interface.

Users can ask questions against three knowledge sources:

- **Wikipedia** — ask any question and the system automatically searches and retrieves the most relevant article
- **Websites** — extract and index content from any URL
- **PDFs** — upload documents and query them instantly

The system uses **Pinecone** as the cloud vector database, **mxbai-embed-large** for embeddings, and **Llama 3.2** (via Ollama) for answer generation.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 Dynamic Wikipedia Search | Ask any question — Wikipedia is searched automatically |
| 🌐 Website Knowledge Base | Extract, embed, and query any website |
| 📄 PDF Knowledge Base | Upload PDFs and ask questions against them |
| 🗄️ Pinecone Vector Database | Cloud-hosted, persistent, scalable vector storage |
| 🏷️ Metadata Storage | Every chunk stores source, document, and position metadata |
| 🎯 Source-Based Filtering | Retrieval is filtered by source for precision |
| 🧠 Prompt Engineering | Advanced prompt builder that prevents hallucinations |
| 💬 Streamlit UI | Clean, interactive, market-ready web interface |
| 🤖 LLM-powered Answers | Llama 3.2 generates context-aware, structured answers |

---

## 🧪 Core AI Concepts

**Retrieval-Augmented Generation (RAG)**
Combines information retrieval with LLM generation. Instead of relying on the model's training data, relevant context is retrieved from a knowledge base and injected into the prompt.

**Semantic Search**
Searches by meaning rather than keywords. Queries and documents are converted to embeddings and compared by cosine similarity.

**Embeddings**
Dense vector representations of text. Semantically similar texts produce similar vectors, enabling meaning-based search.

**Chunking**
Long documents are split into smaller overlapping segments so each chunk fits within the embedding model's context window and carries focused information.

**Vector Databases**
Specialized databases optimized for storing and searching high-dimensional vectors at scale using approximate nearest neighbor (ANN) search.

**Pinecone**
A cloud-native, serverless vector database. Provides persistent storage, metadata filtering, horizontal scalability, and fast similarity search — without managing infrastructure.

**Metadata**
Structured attributes attached to each vector. Enables filtering, source tracking, citations, and explainability.

**Metadata Filtering**
Narrows vector search to a specific subset (e.g., only PDF chunks) before similarity comparison, improving precision and reducing noise.

**Prompt Engineering**
Designing prompts that guide the LLM to produce accurate, structured, and hallucination-free responses using retrieved context.

**Similarity Search**
Finding the top-k vectors closest to a query vector using distance metrics like cosine similarity or dot product.

**Large Language Models (LLMs)**
Foundation models trained on large text corpora. Used here to synthesize retrieved context into coherent, human-readable answers.

---

## 🏗️ Architecture

### Wikipedia Workflow

```
User Question
      │
      ▼
Wikipedia Auto-Search
      │
      ▼
Best Matching Article Selected
      │
      ▼
Extract Article Text
      │
      ▼
Chunking
      │
      ▼
Embedding Generation (mxbai-embed-large)
      │
      ▼
Pinecone (Store + Metadata)
      │
      ▼
Metadata Filtering (source = "Wikipedia")
      │
      ▼
Retriever — Top Relevant Chunks
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

### Website Workflow

```
Website URL
      │
      ▼
Website Loader (BeautifulSoup)
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
Pinecone (Store + Metadata)
      │
      ▼
Metadata Filtering (source = "Website")
      │
      ▼
Retriever — Top Relevant Chunks
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

### PDF Workflow

```
PDF Upload
      │
      ▼
PDF Loader (PyPDF)
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
Pinecone (Store + Metadata)
      │
      ▼
Metadata Filtering (source = "PDF")
      │
      ▼
Retriever — Top Relevant Chunks
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

### Complete System Architecture

```
                          User
                           │
                           ▼
               ┌───────────────────────┐
               │     Choose Source     │
               └──────────┬────────────┘
                          │
         ┌────────────────┼─────────────────┐
         │                │                 │
         ▼                ▼                 ▼
     Wikipedia         Website            PDF
         │                │                 │
         ▼                ▼                 ▼
  Auto Wikipedia     Website Loader    PDF Loader
     Search               │                 │
         │                ▼                 ▼
         ▼           Extract Text      Extract Text
   Article Text           │                 │
         │                └────────┬────────┘
         └────────────────┘        │
                                   ▼
                               Chunking
                                   │
                                   ▼
                         Embedding Generation
                        (mxbai-embed-large)
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │         Pinecone          │
                    │   Cloud Vector Database   │
                    │    + Metadata Storage     │
                    └──────────────┬───────────┘
                                   │
                                   ▼
                         Metadata Filtering
                         (by source type)
                                   │
                                   ▼
                               Retriever
                          (Top-k Relevant Chunks)
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

## 🗄️ Pinecone Metadata

Every chunk stored in Pinecone includes structured metadata:

```json
{
    "text": "chunk content",
    "source": "Wikipedia | Website | PDF",
    "document": "article title | URL | filename",
    "chunk_number": 0
}
```

### Why Metadata Matters

- **Source Tracking** — know exactly where each answer came from
- **Explainable AI** — trace answers back to specific documents
- **Citations** — reference the original source in responses
- **Debugging** — inspect which chunks were retrieved
- **Multi-document Retrieval** — manage multiple knowledge sources in one index
- **Filtering** — query only the relevant source, improving precision

---

## 🎯 Source-Based Retrieval Filtering

Instead of searching all vectors in the Pinecone index, the retriever applies a metadata filter based on the active source type.

```
Website selected
       │
       ▼
Pinecone query with filter: { "source": "Website" }
       │
       ▼
Only Website chunks are searched and returned
```

```
PDF selected
       │
       ▼
Pinecone query with filter: { "source": "PDF" }
       │
       ▼
Only PDF chunks are searched and returned
```

```
Wikipedia selected
       │
       ▼
Pinecone query with filter: { "source": "Wikipedia" }
       │
       ▼
Only Wikipedia chunks are searched and returned
```

This ensures answers are always grounded in the correct knowledge source.

---

## 📁 Project Structure

```
L1 RAG/
│
├── app.py                        # Streamlit UI
├── README.md
├── requirements.txt
├── .env                          # API keys (not committed)
├── .gitignore
│
├── config/
│   └── config.py                 # Configuration and env loading
│
├── Sources/
│   ├── wikipedia_loader.py       # Auto Wikipedia search & extraction
│   ├── website_loader.py         # Website content extraction
│   └── pdf_loader.py             # PDF text extraction
│
├── Chunking/
│   ├── chunk_utils.py            # RecursiveCharacterTextSplitter
│   └── __init__.py
│
├── Embeddings/
│   ├── embedding_utils.py
│   └── embedding_test.py
│
├── VectorDB/
│   └── pinecone_store.py         # Pinecone store, retrieve, delete
│
├── Retrieval/
│   └── retriever.py              # Source-filtered retrieval
│
├── RAG/
│   ├── prompt_builder.py         # Prompt engineering
│   └── rag_pipeline.py           # ask_rag + ask_wikipedia
│
├── LLM/
│   ├── llm_utils.py              # Llama 3.2 via Ollama
│   ├── prompts.py
│   └── llama_test.py
│
├── Tests/
│   ├── test_wikipedia_rag.py
│   ├── test_pinecone_rag.py
│   ├── test_clear_pinecone.py
│   ├── test_website_rag.py
│   ├── test_pdf_rag.py
│   └── test_embeddings.py
│
├── Data/
│   ├── sample.txt
│   ├── topics.py
│   └── pdfs/
│
├── Docs/
└── venv/
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.14 |
| UI | Streamlit |
| LLM | Llama 3.2 (Ollama) |
| Embedding Model | mxbai-embed-large |
| Vector Database | Pinecone (Serverless) |
| RAG Framework | LangChain |
| Wikipedia | Wikipedia API |
| Web Scraping | BeautifulSoup4, Requests |
| PDF Processing | PyPDF |
| Env Management | python-dotenv |

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd L1-RAG
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_pinecone_api_key_here
```

### 6. Ollama Setup

Pull the required models:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

Verify:

```bash
ollama list
```

---

## 🚀 Run Application

```bash
streamlit run app.py
```

---

## 📖 Usage

### Wikipedia

1. Select **Wikipedia** from the sidebar
2. Ask any question directly in the input box
3. The system automatically searches Wikipedia, retrieves the best article, indexes it in Pinecone, and generates an answer

> No manual loading required — the entire pipeline runs on question submission.

---

### Website

1. Select **Website** from the sidebar
2. Enter the website URL
3. Click **⚡ Load Knowledge Base**
4. Ask questions against the website content

---

### PDF

1. Select **PDF** from the sidebar
2. Upload a PDF document
3. Click **⚡ Load Knowledge Base**
4. Ask questions against the document

---

## 💬 Example Questions

### Wikipedia
```
What is Artificial Intelligence?
Who founded Tesla?
What is Ray Ban?
Explain Machine Learning.
What is Quantum Computing?
```

### Website
```
What is FastAPI?
What are the main features of FastAPI?
Explain Dependency Injection in FastAPI.
```

### PDF
```
What is Retrieval-Augmented Generation?
Summarize the paper.
What challenges do LLMs face?
What methodology was used in this research?
```

---

## 🧪 Testing

| Test File | Purpose |
|---|---|
| `test_wikipedia_rag.py` | Load Wikipedia article → store in Pinecone → verify |
| `test_pinecone_rag.py` | Query Pinecone and generate answer |
| `test_clear_pinecone.py` | Delete all vectors from Pinecone index |
| `test_website_rag.py` | Load website → store in Pinecone → query |
| `test_pdf_rag.py` | Load PDF → store in Pinecone → query |
| `test_embeddings.py` | Verify embedding dimensions and model |

Run any test:

```bash
py -m Tests.test_wikipedia_rag
py -m Tests.test_pinecone_rag
py -m Tests.test_clear_pinecone
```

---

## 👤 Author

**Ayush Raj Dewangan**
