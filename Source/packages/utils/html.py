import streamlit as st
import re


css_rx = re.compile(r'^[-_a-zA-Z][-_a-zA-Z0-9]*$')
def validate_css_class(name : str):
    """
    Validates a CSS class name.
    """
    if css_rx.match(name) is None:
        raise ValueError(f"Invalid CSS class name: {name}")
    return name


def html_unsafe(content : str = None):
    """
    Renders HTML content.
    This is unsafe, and should only be used with trusted content.
    """
    st.write(content, unsafe_allow_html=True)


def marked_container(marker_name : str = None):
    """
    Creates a streamlit container with a classed marker.
    This is useful for styling.
    CSS usage: `:has(.marker_name) { ... }`
    """
    for i in marker_name.split():
        validate_css_class(i)
    c = st.container()
    with c:
        html_unsafe(f'<div class="stu-marker {marker_name}"></div>')
    return c


__all__ = [
    'html_unsafe',
    'marked_container'
]
