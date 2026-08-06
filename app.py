import streamlit as st
st.title("Especializacion  Python for Analytics")
st.sidebar.title("Parametros")
st.write("Elaborado por: Carmela Contreras")
valor_inicial=st.number_input("Ingrese el valor inicial")
valor_final=st.number_input("Ingrese el valor final")
lista_numeros=list(range(valor_inicial,valor_final))
