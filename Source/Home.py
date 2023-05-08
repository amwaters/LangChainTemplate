import streamlit as st
from streamlit_utils.chatbox import ChatBox
from streamlit_utils.chatbox import viewer_avatar as user
from streamlit_utils.chatbox import generic_bot_avatar as bot
from streamlit_utils.css import load_style

load_style()

submitted = False

# consider putting this in the sidebar as an 'add bot' or 'add tool'
# or perhaps have this as the default 'Dispatcher'
st.selectbox(
    label = "Select a Dispatcher model:",
    options = [
        "OpenAI GPT-3-turbo",
        "OpenAI GPT-4",
        "LLaMa local \xA0 (\u2913 3.3 GB)",
    ]
)

chatbox = ChatBox('/home/user/chat.json')

form = st.form(
    key="chat_form",
    clear_on_submit=True
)

with form:
    input = st.text_area(label="Chat", height=100, max_chars=500, key="chat")
    submitted = st.form_submit_button("Submit")

if submitted:
    chatbox.post(user, input)
    chatbox.post(bot, f"I received: {input}")
    st.experimental_rerun()
