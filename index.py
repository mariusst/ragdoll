from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import retrieval_qa
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama.llms import OllamaLLM
from langchain_ollama.chat_models import ChatOllama

import chromadb
import nltk

# Initialize database
client = chromadb.PersistentClient(path="./data")
collection = client.get_or_create_collection("docs")

# Initialize language model
llm = OllamaLLM(model="llama3.1:8b")

# Only execute when run as script:
#  `python index.py`
if __name__ == "__main__":
    # Download NLP datasets
    nltk.download("punkt_tab")
    nltk.download("averaged_perceptron_tagger_eng")
    nltk.download("maxent_ne_chunker_tab")
    nltk.download("words")
    
    # Read text file as sentences
    f = open("input.txt", "r")
    sentences = nltk.sent_tokenize(f.read())

    # Insert sentences into database
    collection.add(
        documents=sentences,
        ids=list(map(str, range(len(sentences))))
    )

# Turns LLM outputs to strings
parser = StrOutputParser()

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are given the information below." +
               "Answer the user's questions using only this" +
               "data and avoid making things up.\n\n {results}"),
    ("user", "{prompt}")
])

chain = prompt_template | llm | parser