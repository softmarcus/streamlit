import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

st.title ("Meu Primeiro App :sunglasses:")

st.image('https://softgraf.com/icones/logo_softgraf.png', width=200)

st.header('Este é um header com divisor', divider='rainbow')

st.subheader('Este é um subheader:   _Streamlit_ é legal')

st.write('Este é um *Texto* comum')

"Texto Mágico"
texto  = "Texto na Variavel"
texto

x = 10 
'x', x

st.markdown('Markdown: *Streamlit* é **realmente** ***legal***.')
st.markdown("""
    :red[Streamlit] :orange[pode]:green[escrever] :blue[texto]: violet [em]:gray[muitas]:rainbow[cores] e :blue-blackground[texto destacado]""")

multi = """Se terminar a linha com dois espaços
uma quebra de linha suave é usada para a proxima linha
Dois ou mais enter resulta em apenas uma quebra de linha
 """
st.markdown(multi)
#--------------------------------------------------------------------------
st.subheader('Abas',divider='red')
aba1,aba2, aba3 = st.tabs(['Tabelas','Graficos','Histogramas'])
with aba1:
    st.write('Exibindo DataFrame com Streamlit')
    df = pd.read_excel('https://softgraf.com/cursodatascience/produtos.xlsx')
    df
with aba2:
    st.write('Exibindo um grafico de linhas')
    #cria um array de 20 linhas x 3 colunas, com valores randomicos (distribuiçao padrao)
    arr = np.random.randn(20,3)
    tabela = pd.DataFrame(arr,columns=['a','b','c'])
    st.line_chart(tabela)
with aba3:
    st.write('Exibindo um histograma')
    arr = np.random.normal(1,1, size = 40)
    fig, ax = plt.subplots()
    ax.hist(arr,bins=20)
    fig
    #-----------------------------------------------------------------------------
    st.subheader('Input widgets', divider='red')
    col1,col2,col3 = st.columns(3)

    with col1:
        st.button('Reset',type='primary')
        aceito = st.checkbox('Aceito os termos')
        if aceito:
            st.write('Aceitou!')
        
with col2:
    if st.button('Salvar'):
        st.write('Voce clicou salvar')
    else:
        st.write('Reiniciou')

    on = st.toggle('Ligar recurso')
    if on:
        st.write('Recurso ativado')

with col3:
    st.link_button('Ir para galeria','https://streamlit.io/gallery')
    cor = st.color_picker('Escolha umca cor','#00f900')
    st.write('A cor escolhida foi:',cor)

cidades = ['Ponta Grossa','Curitiba','Castro','Carambei','Pirai do Sul']
padroes = ['Curitiba','Castro','Carambei']
with st.expander('Expander  cidades'):
    escolhidas = st.multiselect('Selecione as cidades',cidades,padroes)

st.write('Cidades escolhidas:', escolhidas)

#===== barra lateral =====
with st.sidebar:
    mensagens = st.container(height=300)
    if prompt := st.chat_input('Digite algo'):
        mensagens.chat_message('usuario').write(prompt)