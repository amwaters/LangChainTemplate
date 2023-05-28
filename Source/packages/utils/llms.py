import streamlit as st

available_llms = {
    "(none)": lambda: None
}

def _add_llm(name):
    def decorator(f):
        available_llms[name] = f
        return f
    return decorator

@st.cache_data
def get_llm(model, **kwargs):
    return available_llms[model](**kwargs)

def llm_selectbox(selectbox_kwargs={}, llm_kwargs={}):
    import streamlit as st
    selected_model = st.selectbox(
        label = "Select a model:",
        options = list(available_llms.keys()),
        **selectbox_kwargs
    )
    return get_llm(selected_model, **llm_kwargs)


@_add_llm("OpenAI GPT-3.5 Turbo")
def _gpt3_5_turbo(**kwargs):
    from langchain.chat_models import ChatOpenAI
    return ChatOpenAI(model_name = "gpt-3.5-turbo", **kwargs)

@_add_llm("OpenAI GPT-4")
def _gpt4(**kwargs):
    from langchain.chat_models import ChatOpenAI
    return ChatOpenAI(model_name = "gpt-4", **kwargs)

@_add_llm("OpenAI GPT-4 (32k context)")
def _gpt4_32k(**kwargs):
    from langchain.chat_models import ChatOpenAI
    return ChatOpenAI(model_name = "gpt-4-32k", **kwargs)
