import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_RCTS_chunks(text, chunk_size, chunk_overlap):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_text(text)
    return chunks

def vectorStore(chunks, api_key):
    embeddings = OpenAIEmbeddings(api_key=api_key)
    try:
        vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    except Exception as e:
        st.error(f"Error creating vectorstore: {e}")
        return None
    return vectorstore

def main():
    st.title("Chunker")

    st.sidebar.title("Configuration")
    
    api_key = st.sidebar.text_input("Paste your OpenAI API key here", type="password")
    
    if api_key:
        chunk_size = st.sidebar.slider("Select chunk size", min_value=50, max_value=1000, value=100, step=50)
        chunk_overlap = st.sidebar.slider("Select chunk overlap", min_value=0, max_value=100, value=20, step=10)
        num_chunks = st.sidebar.number_input("Number of chunks to display", min_value=1, max_value=20, value=5, step=1)
        
        docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        
        if docs:
            text = get_pdf_text(docs)
            #st.write("Extracted Text:", text[:1000])  # Display the first 1000 characters of the extracted text for verification
            
            chunks = get_RCTS_chunks(text, chunk_size, chunk_overlap)
            #st.write("Text Chunks:", chunks[:10])  # Display the first 10 chunks for verification
            
            vectorstore = vectorStore(chunks, api_key)
            
            if vectorstore:
                user_input = st.text_input("Enter text here")
                if user_input:
                    output = vectorstore.similarity_search_with_score(user_input, k=num_chunks)
                    for idx, (result, score) in enumerate(output):
                        with st.expander(f"Match {idx+1} (Score: {score})"):
                            st.write(result.page_content)
            else:
                st.error("Failed to create vectorstore. Please check the logs for details.")
    else:
        st.sidebar.warning("Please enter your OpenAI API key.")

if __name__ == "__main__":
    main()
