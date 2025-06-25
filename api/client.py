import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",json={"input":{"topic":input_text}})

    return response.json()['output']

def get_olama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",json={"input":{"topic":input_text}})

    return response.json()['output']


st.title('Langchain Demo with LLAMA2 API')
input_text = st.text_input("Write an essay on")
input_test1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_test1:
    st.write(get_olama_response(input_test1))

