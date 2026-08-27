import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc

st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
st.subheader("Módulo 1 – Python Fundamentals")
st.sidebar.title("Home")
st.write("Elaborado por: Carmela Contreras")

st.image("python.png", width = 300)
st.sidebar.image("dmc.png",width = 100)


modulos = st.sidebar.selectbox ("Selecione un módulo", ["Ejercicio1", "Ejercicio2", "Ejercicio3", "Ejercicio4"])

if modulos == "Ejercicio1":
  
  st.write("Bienvenido al Ejercicio1: Flujo de caja con listas")
  if "lista_flujo" not in st.session_state:
    st.session_state.lista_flujo = []
  concepto=st.text_input("Ingrese el concepto")
  tipo_movimiento=st.selectbox("Seleccione Tipo de movimiento",["Ingreso","Gasto"])
  valor = st.number_input("Ingrese el valor inicial")
  calcular=st.button("calcular")
  if calcular:
    st.session_state.lista_flujo.append({"concepto": concepto, "tipo":tipo_movimiento, "valor": valor})

  total_ingresos = sum(item["valor"] for item in st.session_state.lista_flujo if item["tipo"] == "Ingreso")
  st.write(st.session_state.lista_flujo)
  st.write("Total ingresos:", total_ingresos)
  
elif modulos == "Módulo Arreglos":
  
  st.write("Bienvenido al módulo de Arreglos")

  cantidad_elementos = st.slider("Selecione la cantidad de elementos de su arreglo", 1,100)
  cantidad_arreglo= np.arange(cantidad_elementos)
  st.write(cantidad_arreglo)

elif modulos == "Archivos":
  
  archivo = st.sidebar.file_uploader("Seleccione su archivo")

  if archivo is not None:
    st.write("Su archivo ha sido cargado")

    if archivo.name.endswith(".csv"):
      datos = pd.read_csv(archivo)
      st.write(datos)
    elif archivo.name.endswith(".xlsx"):
      datos = pd.read_excel(archivo)
      st.write(datos)

  else:
    st.write("Cargue su archivo")





else:
  
  st.write("Bienvenido al módulo de Funciones")

  capital_inicial = st.number_input("Capital inicial", min_value=0.0, value=1000.0)
  tiempo_meses = st.number_input("Tiempo en meses", min_value=1, value=12)
  tasa_porcentaje = st.number_input("Tasa de interés anual (%)", min_value=0.0, value=0.05)

  resultado_interes_simple = lf.interes_simple(capital_inicial, tiempo_meses,tasa_porcentaje )
  st.write(resultado_interes_simple)

  

