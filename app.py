import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos con manejo de errores
try:
    df = pd.read_csv('vehicles_us.csv')
    st.write("Datos cargados correctamente. Aquí una vista previa:")
    st.write(df.head())  # Muestra las primeras 5 filas como prueba
except Exception as e:
    st.error(f"❌ Error al cargar el archivo CSV: {e}")
    st.stop()  # Detiene la app si falla la carga

# Encabezado
st.header('Análisis de anuncios de autos usados en EE.UU.')

# Botón para histograma
if st.button('Mostrar histograma de odómetro'):
    st.write('Histograma del kilometraje recorrido')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para scatter plot
if st.button('Mostrar diagrama de dispersión (precio vs. año)'):
    st.write('Gráfico de dispersión entre precio y año del modelo')
    fig = px.scatter(df, x='model_year', y='price')
    st.plotly_chart(fig, use_container_width=True)
