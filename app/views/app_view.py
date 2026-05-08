import streamlit as st
import os
import requests


st.set_page_config(page_title='Biblioteca de livros')

API_URL = os.getenv('API_URL')

st.title('Gestor de Livros')

with st.sidebar:
    st.header('novo livro')
    titulo = st.text_input('Digite o livro')
    autor = st.text_input('Autor')
    if st.button('Cadastrar'):
        if titulo and autor:
            res = requests.post(API_URL, json={'titulo': titulo, 'autor':autor})
            if res.status_code == 200:
                st.sucess('Livro Salvo')
            else:
                st.error('Ocorreu um erro')

st.subheader('livros disponiveis')
if st.button('Livro disponíveis'):
    try:
        livros = requests.get(API_URL).json
        for l in livros:
            st.info(f'{l['titulo']} : {['autor']}')
    except:
        st.error('não foi possivel concectar a api - verifique.....o serviço')
        
