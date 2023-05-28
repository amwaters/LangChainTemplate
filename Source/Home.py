import streamlit as st
from utils.chatbox import ChatBox
from utils.chatbox import viewer_avatar as user
from utils.chatbox import generic_bot_avatar as bot
from utils.css import load_style

load_style()

# consider putting this in the sidebar as an 'add bot' or 'add tool'
# or perhaps have this as the default 'Dispatcher'

from utils import llm_selectbox
llm = llm_selectbox()

@st.cache_resource
def get_docs():
    from utils import create_document_store
    return create_document_store(
        "SRD-OGL_V5.1.pdf",
        #"quick.txt"
    )
docs = get_docs()

chain = None
if llm is not None:
    from langchain.chains.qa_with_sources import load_qa_with_sources_chain
    chain = load_qa_with_sources_chain(llm, chain_type="map_rerank")

def query(input):
    shortlist = docs.as_retriever().get_relevant_documents(input)
    return chain(
        {
            'input_documents': shortlist,
            'question': input
        },
        return_only_outputs=True
    )['output_text']

chatbox = ChatBox('chat.json')

with st.form(
    key="chat_form",
    clear_on_submit=True
):
    input = st.text_area(label="Chat", height=100, max_chars=500, key="chat")
    submitted = st.form_submit_button("Submit")

if submitted:
    chatbox.post(user, input)
    if (chain is not None):
        chatbox.post(bot, query(input))
    else:
        chatbox.post(bot, "No LLM selected.")
    st.experimental_rerun()
