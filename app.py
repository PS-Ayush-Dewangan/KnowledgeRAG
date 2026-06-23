import streamlit as st

from Sources.wikipedia_loader import load_wikipedia
from Sources.website_loader import load_website
from Sources.pdf_loader import load_pdf

from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store

from RAG.rag_pipeline import ask_rag, ask_wikipedia


st.set_page_config(
    page_title="KnowledgeRAG",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Global */
    [data-testid="stAppViewContainer"] {
        background-color: #f8f9fa;
        color: #1a1a1a;
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    [data-testid="stSidebar"] * {
        color: #1a1a1a !important;
    }
    [data-testid="stSidebar"] h2 {
        color: #4f46e5 !important;
    }
    [data-testid="stSidebar"] .stTextInput input {
        background: #f1f5f9 !important;
        border: 1px solid #cbd5e1 !important;
        color: #1a1a1a !important;
        border-radius: 8px !important;
    }
    [data-testid="stSidebar"] [data-testid="stFileUploader"] *,
    [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] *,
    [data-testid="stSidebar"] [data-testid="stFileUploaderDropzoneInstructions"] * {
        color: #1a1a1a !important;
    }
    [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
        background: #f1f5f9 !important;
        border: 1px dashed #94a3b8 !important;
        border-radius: 8px !important;
    }
    [data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button {
        background: #4f46e5 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
    }
    /* Hero */
    .hero {
        text-align: center;
        padding: 2rem 0 1rem;
    }
    .hero h1 {
        font-size: 2.8rem;
        font-weight: 800;
        color: #4f46e5;
        margin-bottom: 0.3rem;
    }
    .hero p {
        color: #64748b;
        font-size: 1.05rem;
    }
    /* Cards */
    .card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .card-title {
        font-size: 0.9rem;
        font-weight: 700;
        color: #4f46e5;
        margin-bottom: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        padding: 0.55rem 1rem;
        font-weight: 600;
        font-size: 0.95rem;
        background-color: #4f46e5;
        color: #ffffff;
        border: none;
        transition: background 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #4338ca !important;
        color: #ffffff !important;
    }
    /* Inputs */
    .stTextInput > div > div > input {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        color: #1a1a1a;
    }
    /* Answer box */
    .answer-box {
        background: #f0fdf4;
        border: 1px solid #86efac;
        border-radius: 12px;
        padding: 1.25rem;
        margin-top: 1rem;
        color: #1a1a1a;
        line-height: 1.8;
        font-size: 1rem;
    }
    /* Stat badge */
    .stat-badge {
        display: inline-block;
        background: #ede9fe;
        border: 1px solid #c4b5fd;
        color: #4f46e5;
        border-radius: 20px;
        padding: 0.25rem 0.8rem;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    /* Sidebar section label */
    .sidebar-section {
        color: #64748b;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin: 1rem 0 0.3rem;
    }
    /* Hide default chrome */
    #MainMenu, footer, header { visibility: hidden; }
    [data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# Hero Header
# ----------------------------------
st.markdown("""
<div class="hero">
    <h1>🧠 KnowledgeRAG</h1>
    <p style="color:#64748b;">Build a private AI knowledge base from Wikipedia, Websites, or PDFs — and chat with it instantly.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------
# Sidebar — Knowledge Source
# ----------------------------------
with st.sidebar:
    st.markdown("## ⚙️ Knowledge Source")
    st.markdown('<div class="sidebar-section">Select Source Type</div>', unsafe_allow_html=True)

    source_type = st.radio(
        "",
        ["📖 Wikipedia", "🌐 Website", "📄 PDF"],
        label_visibility="collapsed"
    )
    source_type = source_type.split(" ", 1)[1]  # strip emoji

    st.markdown('<div class="sidebar-section">Configure Source</div>', unsafe_allow_html=True)

    url = uploaded_file = None

    if source_type == "Wikipedia":
        st.info("💡 Just ask any question — Wikipedia will be searched automatically.")
    elif source_type == "Website":
        url = st.text_input("Website URL", placeholder="https://example.com")
    else:
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if source_type != "Wikipedia":
        st.markdown("---")
        load_button = st.button("⚡ Load Knowledge Base")
    else:
        load_button = False

    st.markdown("---")
    st.markdown('<div class="sidebar-section">About</div>', unsafe_allow_html=True)
    st.caption("Powered by **Llama 3.2** · FAISS · LangChain · Streamlit")

# ----------------------------------
# Main Area — Status + Q&A
# ----------------------------------
col1, col2 = st.columns([1, 1], gap="large")

if source_type != "Wikipedia":
    with col1:
        st.markdown('<div class="card"><div class="card-title">📦 Knowledge Base Status</div>', unsafe_allow_html=True)

        if load_button:
            try:
                with st.spinner("Loading & indexing your knowledge source..."):
                    if source_type == "Website":
                        if not url:
                            st.warning("Please enter a Website URL.")
                        else:
                            text = load_website(url)
                            chunks = create_chunks(text)
                            create_vector_store(chunks)
                            st.session_state["kb_loaded"] = True
                            st.session_state["kb_info"] = f"Website · {url} · {len(chunks)} chunks"
                            st.success("✅ Website content loaded successfully.")
                            st.markdown(f'<div class="stat-badge">📌 {len(chunks)} chunks indexed</div>', unsafe_allow_html=True)

                    else:
                        if uploaded_file is None:
                            st.warning("Please upload a PDF file.")
                        else:
                            temp_pdf_path = "temp_uploaded.pdf"
                            with open(temp_pdf_path, "wb") as f:
                                f.write(uploaded_file.getbuffer())
                            text = load_pdf(temp_pdf_path)
                            chunks = create_chunks(text)
                            create_vector_store(chunks)
                            st.session_state["kb_loaded"] = True
                            st.session_state["kb_info"] = f"PDF · **{uploaded_file.name}** · {len(chunks)} chunks"
                            st.success(f"✅ PDF loaded: **{uploaded_file.name}**")
                            st.markdown(f'<div class="stat-badge">📌 {len(chunks)} chunks indexed</div>', unsafe_allow_html=True)

            except Exception as error:
                st.error(f"❌ {error}")

        elif st.session_state.get("kb_loaded"):
            st.info(f"🗂️ Active: {st.session_state.get('kb_info', 'Knowledge base ready')}")
        else:
            st.markdown('<p style="color:#64748b; font-size:0.95rem;">No knowledge base loaded yet. Select a source and click <b>Load Knowledge Base</b>.</p>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

ask_col = col2 if source_type != "Wikipedia" else st.container()
with ask_col:
    st.markdown('<div class="card"><div class="card-title">💬 Ask a Question</div>', unsafe_allow_html=True)

    question = st.text_input("", placeholder="What would you like to know?", label_visibility="collapsed")
    ask_button = st.button("🔍 Get Answer")

    st.markdown('</div>', unsafe_allow_html=True)

if ask_button:
    if not question:
        st.warning("Please enter a question.")
    elif source_type == "Wikipedia":
        try:
            with st.spinner("Searching Wikipedia & generating answer..."):
                answer = ask_wikipedia(question)
            st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
        except Exception as error:
            st.error(f"❌ {error}")
    elif not st.session_state.get("kb_loaded"):
        st.warning("Load a knowledge base first.")
    else:
        try:
            with st.spinner("Thinking..."):
                answer = ask_rag(question)
            st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
        except Exception as error:
            st.error(f"❌ {error}")
