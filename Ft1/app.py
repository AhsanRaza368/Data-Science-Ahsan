import streamlit as st
from dotenv import load_dotenv
import os

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

from transformers import pipeline

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="📄 PDF Chatbot")
st.title("📄 Ask Questions From Your PDFs")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload PDF files
uploaded_files = st.file_uploader("Upload one or more PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.info("Reading and processing uploaded PDFs...")

    # Extract text
    raw_text = ""
    for pdf in uploaded_files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                raw_text += text

    # Split text
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(raw_text)

    # Embeddings and vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts, embeddings)

    # Load QA model
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    st.success("PDFs processed. You can now ask questions!")

    # Input box for questions
    question = st.text_input("Ask a question about your documents:")

    if question:
        docs = vectorstore.similarity_search(question, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        result = qa_pipeline(question=question, context=context)

        # Store and display Q&A history
        st.session_state.chat_history.append({"question": question, "answer": result["answer"]})

        st.subheader("Chat History:")
        for i, qa in enumerate(st.session_state.chat_history):
            st.markdown(f"**Q{i+1}:** {qa['question']}")
            st.markdown(f"**A{i+1}:** {qa['answer']}")

        # Show sources
        with st.expander("📄 Sources"):
            for i, doc in enumerate(docs):
                st.markdown(f"**Source {i+1}:**\n```\n{doc.page_content[:500]}...\n```")
