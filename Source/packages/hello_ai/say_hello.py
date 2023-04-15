from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessage

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
    print(f"Operator: {request}")
    response = llm([HumanMessage(content=request)])
    print(f"Consultant: {response.content}")
