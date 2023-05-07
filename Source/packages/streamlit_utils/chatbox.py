import html, urllib.parse
import streamlit as st

from streamlit_utils.html import html_unsafe


class ChatPoster():
    def __init__(self, name, avatar, is_user=False):
        self.name = name
        self.avatar = avatar
        self.is_user = is_user

    def avatar_html(self):
        avatar = self.avatar
        if isinstance(avatar, str):
            avatar = [avatar]
        
        tags = [
            f"""<img src="{urllib.parse.quote(i)}" />"""
            for i in avatar
        ]

        return f"""<div class="avatar">{''.join(tags)}</div>"""


class ChatBox():

    def __init__(self):
        self.container = st.container()

    def post(self, poster : ChatPoster, message : str, is_user=False):
        with self.container:
            message = html.escape(message)
            username = html.escape(poster.name)
            html_unsafe(
                f"""
                    <div class="chat-post {'is-user' if poster.is_user else ''}">
                        {poster.avatar_html()}
                        <div class="message">
                            <div class="username">{html.escape(username)}</div>
                            {html.escape(message)}
                        </div>
                    </div>
                """
            )

__all__ = [
    'ChatBox',
    'ChatPoster'
]
