# -*- coding: utf-8 -*-
"""research_agent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HRuRhqJqOO1-KnfzPKk4QsuYWIEhw8Ou
"""

from langgraph.graph import Graph
from llm.groq_wrapper import load_groq_llm
from memory.langmem_tools import get_memory_tools

def create_agent():
    llm = load_groq_llm()
    memory_tools = get_memory_tools()

    graph = Graph()
    # Add your memory and llm nodes here
    # For simplicity, you can compose a ReAct-style agent

    return graph.compile()