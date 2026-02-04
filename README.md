# 💬 RAG Chatbot with LangGraph and Streamlit

A conversational AI chatbot application built with **LangGraph** for graph-based conversation workflows and **Streamlit** for an interactive web interface.

## ✨ Features

- **Interactive Chat Interface**: User-friendly Streamlit UI for seamless conversations
- **LangGraph Architecture**: Graph-based state management for robust conversation flows
- **OpenAI Integration**: Uses OpenAI's advanced language models
- **Conversation History**: Maintains message history throughout each session
- **Stateful Processing**: In-memory checkpointing for conversation persistence


## 📁 Project Structure
```
RAG-Chatbot/
├── aenv/ # Virtual environment folder
├── .env # Environment variables
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
