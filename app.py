import streamlit as st
import requests
import os

# Set page title
st.set_page_config(page_title="RAG Document Assistant")

# Title
st.title("RAG Document Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask a question about your documents..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send request to backend
    try:
        backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")
        response = requests.post(
            f"{backend_url}/api/query",
            json={"query": prompt}
        )
        
        if response.status_code == 200:
            answer = response.json()["response"]
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(answer)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})
        else:
            error_msg = f"Error: {response.status_code} - {response.text}"
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            
    except Exception as e:
        error_msg = f"Connection Error: {str(e)}"
        st.error(error_msg)
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
