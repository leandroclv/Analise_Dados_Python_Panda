import streamlit as st
import plotly.express as px 
from dataset import df


st.set_page_config(layout='wide')
st.title('Dashoboard de Vendas :shopping_cart:')

aba1,aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

with aba1:
    st.dataframe(df)

#pip install --upgrade plotly