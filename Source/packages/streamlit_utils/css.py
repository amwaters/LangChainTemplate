import streamlit as st


def load_style(file : str = '/app/default.css'):
    """
    Loads a CSS file into a style tag.
    Note that this can be unsafe, and should only be used with trusted files.
    """
    with open(file, 'r') as f:
        unsafe_run_style(f.read())


def unsafe_run_style(css : str):
    """
    Adds CSS styling to the page.
    Note that this can be unsafe, and should only be used with trusted CSS.
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


__all__ = [
    'load_style',
    'unsafe_run_style'
]
