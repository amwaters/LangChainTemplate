import streamlit as st
from streamlit_utils.chatbox import ChatBox, ChatPoster
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

chatbox = ChatBox()

user = ChatPoster("User", [
    "/app/static/icons/src-userland.png",
    "/app/static/icons/chat-user.png"
], is_user=True)

bot = ChatPoster("Dispatcher", [
    "/app/static/icons/src-generic.png",
    "/app/static/icons/chat-commander.png"
])

chatbox.post(user, "Hello, world!")
chatbox.post(bot, "Greetings!")

# TODO: have chatbox.post return a container that we can fill with our content
# TODO: hook into llm to get thoughts

form = st.form(
    key="chat_form",
    clear_on_submit=True
)

with form:
    input = st.text_area(label="Chat", height=100, max_chars=500, key="chat")
    submitted = st.form_submit_button("Submit")

if not submitted: exit()

#st.image("//app/static/icons/user.png", width=50, caption="User")

with chatbox:

    st.text(input)

    #st.image("//app/static/icons/bot.png", width=50, caption="Bot")

    st.text(f"I received: {input}")
