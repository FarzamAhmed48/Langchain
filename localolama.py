from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=""
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=""


prompt =ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user  queries"),
        ("user","Question:{question}")
    ]
)


st.title("Langchain Demo With Ollama API")
input_text = st.text_input("Search the topic you want")

# llm= Ollama(model= "gemma3:1b")
llm = OllamaLLM(model="gemma3:1b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))