import streamlit as st
import numpy as np

st.title("Especializacion  Python for Analytics")
st.sidebar.title("Parametros")
st.write("Elaborado por: Carmela Contreras")

st.image("python.png",width=300)
st.sidebar.image("dmc.png",width=100)

modulos=st.sidebar.selectbox("Seleccione un Modulo",["Modulo Listas","Modulo Arreglos","Modulo Funciones"])
if modulos=="Modulo Listas":
  st.write("Bienvenido al modulo Lista")
  valor_inicial=st.number_input("Ingrese el valor inicial")
  valor_final=st.number_input("Ingrese el valor final")
  lista_numeros=list(range(int(valor_inicial),int(valor_final)))
  st.write(lista_numeros)
elif modulos=="Modulo Arreglos":
  st.write("Bienvenido al modulo Arreglos")
  cantidad_elementos=st.slider("Seleccione la Cantidad de elementos de su arreglo",1,100)
  cantidad_arreglo=np.arange(cantidad_elementos)
  st.write(cantidad_arreglo)

else:
  st.write("Bienvenido al modulo Funciones")
