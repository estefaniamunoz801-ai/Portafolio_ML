import streamlit as st
from PIL import Image

st.title("Aplicaciones de Machine Learning.")

with st.sidebar:
    st.subheader("Aplicaciones de Machine Learning.")
    parrafo = (
        "El Machine Learning permite a los sistemas aprender de los datos para "
        "identificar patrones, hacer predicciones y clasificar información sin "
        "ser programados explícitamente para cada tarea."
    )
    st.write(parrafo)

url_ml = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ml})")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.subheader("Regresión Lineal")
    image = Image.open("imag/regresion_lineal.png")
    st.image(image, width=210)
    st.write("En el siguiente enlace veremos cómo usar la regresión lineal para predecir datos.")
    url = "https://predictor-en-vivo.streamlit.app/"
    st.write(f"Regresión Lineal: [Enlace]({url})")

with col2:
    st.subheader("Regresión Logística")
    image = Image.open("imag/regresion_logistica.png")
    st.image(image, width=210)
    st.write("En el siguiente enlace veremos cómo usar la regresión logística para clasificar datos.")
    url = "https://app-seguros-python.streamlit.app/"
    st.write(f"Regresión Logística: [Enlace]({url})")

with col3:
    st.subheader("Clasificación con KNN")
    image = Image.open("imag/knn_clasificacion.png")
    st.image(image, width=210)
    st.write("En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.")
    url = "https://ml-clasificacion-k-means-svm.streamlit.app/"
    st.write(f"KNN: [Enlace]({url})")
    

with col4:
    st.subheader("Agrupamiento con K-Means")
    image = Image.open("imag/kmeans_consumo_electrico_v2.png")
    st.image(image, width=210)
    st.write("En el siguiente enlace veremos cómo agrupar datos usando K-Means en una app de consumo electrico.")
    url = "https://app-consumo-ml.streamlit.app/"
    st.write(f"K-Means: [Enlace]({url})")

with col5:
    st.subheader("Árboles de Decisión")

    image = Image.open("imag/arboles_decision_v2.png")
    st.image(image, width=210)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    url = "https://sistema-de-riego-inteligente-ml-arboles-decision.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")

with col6:
    st.subheader("Medidor de energia con ML")

    image = Image.open("imag/consumo_electrico_influxdb.png")
    st.image(image, width=210)
    st.write("En el siguiente enlace veremos un dashboard interactivo para análisis y modelado con Machine Learning de datos de consumo eléctrico almacenados en InfluxDB.")
    url = "https://medidor-energia-ml.streamlit.app/"
    st.write(f"Medidor de Energía con ML: [Enlace]({url})")