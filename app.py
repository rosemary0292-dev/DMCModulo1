import streamlit as st
import numpy as np
import libreria_funciones as lf
import pandas as pd

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
elif modulo=="Archivos" :
  archivo = st.sidebar.file_uploader("Seleccione su archivo")
  if archivo is not None:
    st.write("Su archivo ha sido Cargado")
    if archivo.name.endwith(".csv"):
      datos=pd.read_csv(archivo)
    elif archivo.name.endwith(".xlsx"):
      datos=pd.read_excel(archivo)
    else:
      st.write("No es un archivo compatible")
  else:
     st.write("Cargue su archivo")
else:
  st.write("Bienvenido al módulo de Funciones")
  capital_inicial = st.number_input("Capital inicial", min_value=0.0, value=1000.0)
  tiempo_meses = st.number_input("Tiempo en meses", min_value=1, value=12)
  tasa_porcentaje = st.number_input("Tasa de interés anual (%)", min_value=0.0, value=0.05)
  resultado_interes_simple = lf.interes_simple(capital_inicial, tiempo_meses,tasa_porcentaje )
  st.write(resultado_interes_simple)
