from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from dotenv import load_dotenv
from state import ChatState
import sqlite3
import requests
import os

# Load environment variables from .env file
load_dotenv()

# Define the LLM
llm = ChatOpenAI()

# Define tools for LLM
search_tool = DuckDuckGoSearchRun(region="us-en")

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """
    try:
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num
        else:
            return {"error": f"Unsupported operation '{operation}'"}
        
        return {"first_num": first_num, "second_num": second_num, "operation": operation, "result": result}
    except Exception as e:
        return {"error": str(e)}

@tool
def get_weather_data(city: str) -> dict:
    """
    Fetch the current weather for a given city (e.g. 'London', 'Tokyo').
    Returns temperature, humidity and a short description of the conditions.
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return {"error": "OPENWEATHERMAP_API_KEY is not set in the .env file"}

    try:
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": api_key, "units": "metric"},
            timeout=10,
        )

        if r.status_code == 404:
            return {"error": f"City '{city}' not found"}
        if r.status_code == 401:
            return {"error": "Invalid or not-yet-activated OpenWeatherMap API key"}
        r.raise_for_status()

        data = r.json()
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature_c": data["main"]["temp"],
            "humidity_percent": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
        }
    except Exception as e:
        return {"error": str(e)}
    
tools = [search_tool, calculator, get_weather_data]
llm_with_tools = llm.bind_tools(tools)

# Nodes
def chat_node(state: ChatState):
    """LLM node that may answer or request a tool call."""
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)

# In-memory checkpointer
conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn = conn)


# Build a simple graph
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", tools_condition)
graph.add_edge("tools", "chat_node")

# Compile the graph
chatbot = graph.compile(checkpointer=checkpointer)


# ----------- Utility Functions -----------
def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config["configurable"]["thread_id"])
    
    return list(all_threads)