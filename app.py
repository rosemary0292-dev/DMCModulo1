import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc

st.title("PROYECTO 1 – APLICACIÓN EN STREAMLIT")
st.subheader("Módulo 1 – Python Fundamentals")
st.sidebar.title("Home")
st.write("Elaborado por: Rosemary Contreras Roque")
st.write("2026")
st.write("El proyecto busca mostrar las dieferentes herramientas aprendidas en el modulo 1 de python")
st.write("Las tecnologías usadas son: listas, arreglos, funciones y clases")
st.image("python.png", width = 300)
st.sidebar.image("dmc.png",width = 100)


modulos = st.sidebar.selectbox ("Selecione un módulo", ["Ejercicio1", "Ejercicio2", "Ejercicio3", "Ejercicio4"])

if modulos == "Ejercicio1":
  
  st.write("Bienvenido al Ejercicio1: Flujo de caja con listas")
  st.markdown("El ejercicio busca registrar los ingresos, gastos y saldo")
  if "lista_flujo" not in st.session_state:
    st.session_state.lista_flujo = []
  concepto=st.text_input("Ingrese el concepto")
  tipo_movimiento=st.selectbox("Seleccione Tipo de movimiento",["Ingreso","Gasto"])
  valor = st.number_input("Ingrese el valor inicial")
  calcular=st.button("calcular")
  if calcular:
    st.session_state.lista_flujo.append({"concepto": concepto, "tipo":tipo_movimiento, "valor": valor})

  total_ingresos = sum(item["valor"] for item in st.session_state.lista_flujo if item["tipo"] == "Ingreso")
  total_gastos = sum(item["valor"] for item in st.session_state.lista_flujo if item["tipo"] == "Gasto")
  saldo=total_ingresos - total_gastos
  st.write(st.session_state.lista_flujo)
  st.write("Total ingresos:", total_ingresos)
  st.write("Total Gastos:", total_gastos)
  st.write("Saldo:", saldo)
  
elif modulos == "Ejercicio2":
  
  st.write("Ejercicio 2 – Registro con NumPy, arrays y DataFrame")
  st.markdown("El ejercicio busca registrar los productos en dataframe")
  if "productos" not in st.session_state:
    st.session_state.productos = np.empty((0, 5), dtype=object)
  Nombrepro=st.text_input("Ingrese el Nombre Producto")
  Categoria=st.selectbox("Seleccione la Categoria",["Ropa","Alemnto","Abarrote"])
  precio = st.number_input("Ingrese el precio")
  cantidad = st.number_input("Ingrese la cantidad")
  total=precio*cantidad
  agregar=st.button("agregar")
  if agregar:
    nuevo_producto = np.array([[Nombrepro, Categoria, precio, cantidad, total]], dtype=object)
    st.session_state.productos = np.vstack([st.session_state.productos, nuevo_producto])
  df_productos = pd.DataFrame(st.session_state.productos,columns=["Nombre", "Categoría", "Precio", "Cantidad", "Total"])
  st.write("Productos registrados:")
  st.dataframe(df_productos)

elif  modulos == "Ejercicio3":
  st.write("Ejercicio 3 – Uso de funciones desde una librería externa")
  st.markdown("El ejercicio utiliza la funcion disponibilidad del sistema")
  if "historico_funciones" not in st.session_state:
    st.session_state.historico_funciones = []

  funcion = st.selectbox("Seleccione una función",["Disponibilidad del sistema"])
  if funcion == "Disponibilidad del sistema":
    tiempo_total = st.number_input("Ingrese el tiempo total del sistema en horas")
    tiempo_caida = st.number_input("Ingrese el tiempo de caída en horas")
    ejecutar = st.button("Ejecutar función")
    if ejecutar:
      resultado = lf.calcular_disponibilidad_sistema(tiempo_total,tiempo_caida)
      disponibilidad = resultado["disponibilidad_pct"]
      st.write("Disponibilidad del sistema:",disponibilidad,"%")
      st.session_state.historico_funciones.append({"Función": funcion,"Tiempo total": tiempo_total,"Tiempo caída": tiempo_caida, "Disponibilidad (%)": disponibilidad})
      df_historico = pd.DataFrame(st.session_state.historico_funciones)
      st.write("Histórico de resultados:")
      st.dataframe(df_historico)
      
else:
  st.write("Ejercicio 4 – Uso de clases desde una librería externa con CRUD")
  st.markdown("El ejercicio utiliza clases de una libreria externa")
  if "servidores" not in st.session_state:
    st.session_state.servidores = []
    
  st.subheader("Crear servidor")
  nombre = st.text_input("Nombre del servidor")
  tiempo_total = st.number_input("Tiempo total en horas")
  tiempo_caida = st.number_input("Tiempo de caída en horas")
  almacenamiento_total = st.number_input("Almacenamiento total GB")
  almacenamiento_usado = st.number_input("Almacenamiento usado GB")
  crear = st.button("Crear")
  if crear:
    servidor = lc.Servidor(nombre,tiempo_total,tiempo_caida,almacenamiento_total,almacenamiento_usado)
    st.session_state.servidores.append(servidor)
  st.subheader("Servidores registrados")
  datos = []
  for servidor in st.session_state.servidores:
    datos.append(servidor.resumen())
  df_servidores = pd.DataFrame(datos)
  st.dataframe(df_servidores)
  if len(st.session_state.servidores) > 0:
    st.subheader("Actualizar servidor")
    nombres = [servidor.nombre for servidor in st.session_state.servidores]
    servidor_actualizar = st.selectbox( "Seleccione servidor a actualizar",nombres)
    nuevo_tiempo_caida = st.number_input("Nuevo tiempo de caída")
    nuevo_almacenamiento_usado = st.number_input("Nuevo almacenamiento usado",)
    actualizar = st.button( "Actualizar")
    if actualizar:
      for servidor in st.session_state.servidores:
        if servidor.nombre == servidor_actualizar:
          servidor.tiempo_caida_h = nuevo_tiempo_caida
          servidor.almacenamiento_usado_gb = nuevo_almacenamiento_usado
          
    st.subheader("Eliminar servidor")
    servidor_eliminar = st.selectbox("Seleccione servidor a eliminar", nombres)
    eliminar = st.button("Eliminar")
    if eliminar:
      for servidor in st.session_state.servidores:
        if servidor.nombre == servidor_eliminar:
          st.session_state.servidores.remove(servidor)
          break






  

