import streamlit as st
import itertools

from index import collection, chain

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

    # Return similar documents by vector search
    results = collection.query(query_texts=[prompt], n_results=10)['documents']
    results = itertools.chain.from_iterable(results) # Flatten array

    # Generate and save AI response
    response = chain.invoke({
        "prompt": prompt,
        "results": "\n\n".join(results)
    })

    # Display and save chatbot response
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({ "role": "assistant", "content": response })