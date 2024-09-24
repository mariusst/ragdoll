# ragdoll 🪆
Implementing Retrieval Augmented Generation (not quite) from scratch. For more information see the [project page](https://bibliotecaarad.ro/devops-arad-ai/).

To contribute, join the [Arad Makerspace](https://bibliotecaarad.ro/makerspace) or just open an issue/pull request.

*Currently the retrieval system returns mostly irrelevant information and the project is barely useable.*  
*I'm experimenting with different ways to structure and retrieve indexed data.*

## Installation
At the current time, the language model is run locally using [ollama](https://ollama.com), so you'll need a GPU.

1. Start by [downloading ollama](https://ollama.com/download), or if you're on linux, run:
```sh
curl -fsSL https://ollama.com/install.sh | sh
```

2. Setup the environment. We assume python, pip and git are already installed.
```sh
git clone https://github.com/mark-veres/ragdoll
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
1. Create the `input.txt` file where your document will be located.

2. Before being able to chat with your dataset, you have to index it. Simply run:  
*Note that it may take a while to index your document depending on its size.*
```bash
python index.py
```

3. Start them app using streamlit
```sh
streamlit run app.py
```

## Notes
**🚧 UNDER CONSTRUCTION 🚧**  
- documents: PDFs, docx, html, excel, images, plain text
- each document type has its own parser
- parsers returns features (eg. title, author, date, paragraphs, entities)
- prompt is first turned into database queries
- data is ranked by relevance
- LLM is left to respond to initial query using the context it gained through the queries