# 💬 RAG Chatbot with LangGraph and Streamlit

A conversational AI chatbot application built with **LangGraph** for graph-based conversation workflows and **Streamlit** for an interactive web interface.

## ✨ Features

- **Interactive Chat Interface**: User-friendly Streamlit UI for seamless conversations
- **LangGraph Architecture**: Graph-based state management for robust conversation flows
- **OpenAI Integration**: Uses OpenAI's advanced language models
- **Conversation History**: Maintains message history throughout each session and across sessions
- **Persistent Storage**: Conversations are stored in a SQLite database using SqliteSaver, so they are not lost when the page is refreshed or the app is restarted
- **Streaming Responses**: Displays the model's reply token by token as it is generated, instead of waiting for the full response
- **Multiple Conversations**: Start a new conversation or resume existing conversations.
- **Tool Calling**: The chatbot can use tools when needed: web search (DuckDuckGo), a calculator for basic arithmetic, and current weather lookup for any city.
- **Document Q&A (RAG)**: Upload a PDF to a conversation and ask questions grounded in its content. The PDF is split into chunks, indexed in a FAISS vector store, and the most relevant chunks are retrieved to answer your questions.


## 📁 Project Structure
```
RAG-Chatbot/
├── aenv/ # Virtual environment folder
├── .env # Environment variables
├── chatbot.db # SQLite database for conversation storage (auto-created)
├── chatbot.py # LangGraph chatbot definition
├── main.py # Streamlit application entry point
├── README.md # README file
├── requirements.txt # Python dependencies
└── state.py # LangGraph state definition
```


## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key
- pip package manager

### Installation Steps

1. **Navigate to project directory**:
   ```bash
   cd RAG-Chatbot
   ```

2. **Create virtual environment**:
    ```bash
    python -m venv aenv
    ```

3. **Activate virtual environment**:
    ```bash
    aenv\Scripts\activate
    ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:
    
    Create a .env file in the project root:
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
    ```

6. **Run the application**:
    ```bash
    streamlit run main.py
    ```

    The application will open at http://localhost:8501 in your default browser.