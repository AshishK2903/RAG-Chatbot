import streamlit as st
from chatbot import chatbot
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="LangGraph Chatbot", page_icon="💬")

# --------------------- Session Setup ---------------------
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# --------------------- Sidebar ---------------------
st.sidebar.title("RAG Chatbot")
st.sidebar.markdown("""RAG Chatbot built with LangGraph and Streamlit.""")

# --------------------- Main UI ---------------------
st.header("💬 RAG Chatbot")

# Loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])


# User input
user_input = st.chat_input("Type here...")

if user_input:

    # Add User message to message history
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable': {'thread_id': 'thread-1'}}

    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config = CONFIG,
                stream_mode = 'messages'
            )
        )

    # Add AI message to message history
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})