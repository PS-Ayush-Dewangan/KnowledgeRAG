import streamlit as st

from Sources.wikipedia_loader import load_wikipedia
from Sources.website_loader import load_website

from Chunking.chunk_utils import create_chunks
from VectorDB.vector_store import create_vector_store

from RAG.rag_pipeline import ask_rag


st.set_page_config(
    page_title="KnowledgeRAG",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 KnowledgeRAG")

st.markdown(
    "Build a knowledge base from Wikipedia or Websites and ask questions."
)

# ----------------------------------
# Source Selection
# ----------------------------------

source_type = st.radio(
    "Select Source",
    ["Wikipedia", "Website"]
)

if source_type == "Wikipedia":

    topic = st.text_input(
        "Enter Wikipedia Topic"
    )

else:

    url = st.text_input(
        "Enter Website URL"
    )

# ----------------------------------
# Load Knowledge Button
# ----------------------------------

load_button = st.button(
    "Load Knowledge"
)

if load_button:

    try:

        with st.spinner("Loading Knowledge Base..."):

            if source_type == "Wikipedia":

                if not topic:
                    st.warning(
                        "Please enter a Wikipedia topic."
                    )

                else:

                    text = load_wikipedia(topic)

                    chunks = create_chunks(text)

                    create_vector_store(chunks)

                    st.success(
                        f"Knowledge loaded successfully from Wikipedia topic: {topic}"
                    )

                    st.info(
                        f"Chunks Created: {len(chunks)}"
                    )

            else:

                if not url:
                    st.warning(
                        "Please enter a Website URL."
                    )

                else:

                    text = load_website(url)

                    chunks = create_chunks(text)

                    create_vector_store(chunks)

                    st.success(
                        "Knowledge loaded successfully from Website."
                    )

                    st.info(
                        f"Chunks Created: {len(chunks)}"
                    )

    except Exception as error:

        st.error(
            f"Error: {error}"
        )

# ----------------------------------
# Ask Question Section
# ----------------------------------

st.divider()

question = st.text_input(
    "Ask a Question"
)

ask_button = st.button(
    "Ask"
)

if ask_button:

    if not question:

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            with st.spinner(
                "Generating Answer..."
            ):

                answer = ask_rag(question)

            st.subheader(
                "Answer"
            )

            st.write(answer)

        except Exception as error:

            st.error(
                f"Error: {error}"
            )