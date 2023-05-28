from collections import namedtuple
import html, json, os, urllib.parse
from typing import Iterable, Optional, Tuple
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from .html import html_unsafe, marked_container


def ChatAvatar(name: str, images: Iterable[str], is_viewer: bool):
    return {
        'name': name,
        'images': images,
        'is_viewer': is_viewer
    }

def ChatMessage(sender: str, content: str):
    return {
        'sender': sender,
        'content': content
    }

class ChatBox():

    def __init__(self, file:str):
        self.file = file
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                json.dump({
                    'avatars': {},
                    'messages': []
                }, f)
        
        self.container = marked_container('chat-box')
        with self.container:
            self.messages = marked_container('chat-messages')
            self.input = marked_container('chat-input')            
    
        with open(self.file, 'r') as f:
            data = json.load(f)
        for message in data['messages']:
            sender = data['avatars'].get(message['sender'])
            content = message['content']
            self._render_post(sender, content)
    
    def post(self, sender : ChatAvatar, content : str):
        with open(self.file, 'r') as f:
            data = json.load(f)
        data['avatars'][sender['name']] = sender
        data['messages'].append(ChatMessage(sender['name'], content))
        with open(self.file, 'w') as f:
            json.dump(data, f)

    def _render_post(self, sender : ChatAvatar, content : str) -> DeltaGenerator:
        with self.container:
            post_container = marked_container(
                'chat-message stu-row viewer' if sender['is_viewer'] else 'chat-message stu-row'
            )
        with post_container:
            self._render_avatar(sender)
            content_container = marked_container('content')
        with content_container:
            html_unsafe(f"""
                <div class="username-title">
                    {html.escape(sender['name'])}
                </div>
            """)
            st.markdown(content)
    
    def _render_avatar(self, avatar : ChatAvatar):
        avatar_html = ''.join([
            f"""<img src="{urllib.parse.quote(i)}" />"""
            for i in avatar['images']
        ])
        html_unsafe(f'<div class="avatar">{avatar_html}</div>')


def create_avatar(
    name: str,
    type: str,
    src: str = 'generic',
    is_viewer: bool = False
):
    return ChatAvatar(
        name = name,
        images = [
            f"/app/static/icons/src-{src}.png",
            f"/app/static/icons/{type}.png"
        ],
        is_viewer = is_viewer
    )


viewer_avatar = create_avatar('You', 'chat-user', 'userland', is_viewer = True)
generic_bot_avatar = create_avatar('Bot', 'llm-bot')


__all__ = [
    'ChatBox',
    'viewer_avatar',
    'generic_bot_avatar'
]
