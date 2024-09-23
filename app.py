from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import retrieval_qa
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_ollama.llms import OllamaLLM
from langchain_ollama.chat_models import ChatOllama

import streamlit as st

llm = OllamaLLM(model="llama3.1:8b")

# Initialize message array
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

# Display chat box
prompt = st.chat_input("Pass your prompt here")

if prompt:
    # Display and save user prompt
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({ "role": "user", "content": prompt })

    # Generate and save AI response
    response = llm.invoke(st.session_state.messages)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({ "role": "assistant", "content": response })