from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
from state import ChatState

# Load environment variables from .env file
load_dotenv()

# Define the LLM
llm = ChatOpenAI()

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {'messages': [response]}

# In-memory checkpointer
checkpointer = InMemorySaver()

# Build a simple graph
graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

# Compile the graph
chatbot = graph.compile(checkpointer=checkpointer)
