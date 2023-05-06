import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessage

_callback = print

if os.environ.get('STREAMLIT', None) is not None:
    import streamlit as st
    _callback = st.write

def say_hello():
    """
    A simple demo function that says says "Hello!" to an AI.
    Handy to check everything's working.
    """
    llm = ChatOpenAI(**{
        'model_name': 'gpt-3.5-turbo',
        'temperature': 0.7
    })

    request = "Hello, friend! How are you?"
    _callback(f"Operator: {request}")
    response = llm([HumanMessage(content=request)])
    _callback(f"Consultant: {response.content}")
