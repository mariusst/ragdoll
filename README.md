# ragdoll 🪆
Retrieval Augmented Generation

**🚧 UNDER CONSTRUCTION 🚧**  
**DO NOT BANG YOUR HEAD AGAINST THE IDEAS LAYING AROUND**

- documents: PDFs, docx, html, excel, images, plain text
- each document type has its own parser
- parsers returns features (eg. title, author, date, paragraphs, entities)
- prompt is first turned into database queries
- data is ranked by relevance
- LLM is left to respond to initial query using the context it gained through the queries

## installation
```sh
git clone https://github.com/mark-veres/ragdoll
python -m venv .venv
source .venv/bin/activate
pip install streamlit langchain langchain-ollama langchain-community
```

## usage
```sh
streamlit run app.py
```