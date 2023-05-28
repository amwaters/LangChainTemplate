import streamlit as st
from langchain.vectorstores import VectorStore
from langchain.embeddings.openai import OpenAIEmbeddings

_extension_map = {}
def _extension(*ext):
    def decorator(f):
        for e in ext:
            _extension_map[e] = f
        return f
    return decorator

@_extension("txt")
def load_txt(docs : VectorStore, path : str):
    from langchain.document_loaders import TextLoader
    loader = TextLoader(path)
    docs.add_documents(loader.load())

@_extension("pdf")
def load_pdf(docs : VectorStore, path : str):
    from langchain.document_loaders import PyPDFLoader
    loader = PyPDFLoader(path)
    docs.add_documents(loader.load())


_CHROMA_INDEX = ".chroma-index.txt"

def create_document_store(*files):
    from langchain.vectorstores import Chroma
    docs = Chroma(
        embedding_function=OpenAIEmbeddings(),
        persist_directory="chroma"
    )

    import os
    preloaded = []
    if os.path.exists(_CHROMA_INDEX):
        with open(_CHROMA_INDEX, 'r') as f:
            preloaded = [l.strip() for l in f.readlines()]

    for file in files:
        if file in preloaded: continue

        f = _extension_map.get(file.split(".")[-1], None)
        if f is None:
            raise ValueError(f"Unknown file extension: {file}")
        
        with st.spinner(f"Loading {file}..."):
            f(docs, file)
            with open(_CHROMA_INDEX, 'a') as f:
                f.write(f'{file}\n')
    docs.persist()

    return docs
