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

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.subheader("Regresión Lineal")
    image = Image.open("imag/regresion_lineal.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace veremos cómo usar la regresión lineal para predecir datos.")
    url = "https://predictor-en-vivo.streamlit.app/"
    st.write(f"Regresión Lineal: [Enlace]({url})")

with col2:
    st.subheader("Regresión Logística")
    image = Image.open("imag/regresion_logistica.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace veremos cómo usar la regresión logística para clasificar datos.")
    url = "https://app-seguros-python.streamlit.app/"
    st.write(f"Regresión Logística: [Enlace]({url})")

with col3:
    st.subheader("Clasificación con KNN")
    image = Image.open("imag/knn_clasificacion.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.")
    url = "https://ml-clasificacion-k-means-svm.streamlit.app/"
    st.write(f"KNN: [Enlace]({url})")

col4, col5, col6 = st.columns(3, gap="large")

with col4:
    st.subheader("Agrupamiento con K-Means")
    image = Image.open("imag/kmeans_consumo_electrico_v2.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace veremos cómo agrupar datos usando K-Means en una app de consumo electrico.")
    url = "https://app-consumo-ml.streamlit.app/"
    st.write(f"K-Means: [Enlace]({url})")

with col5:
    st.subheader("Árboles de Decisión")

    image = Image.open("imag/arboles_decision_v2.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    url = "https://sistema-de-riego-inteligente-ml-arboles-decision.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")

with col6:
    st.subheader("Medidor de energia con ML")

    image = Image.open("imag/consumo_electrico_influxdb.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace veremos un dashboard interactivo para análisis y modelado con Machine Learning de datos de consumo eléctrico almacenados en InfluxDB.")
    url = "https://medidor-energia-ml.streamlit.app/"
    st.write(f"Medidor de Energía con ML: [Enlace]({url})")


col7, col8, col9 = st.columns(3, gap="large")

with col7:
    st.subheader("Redes Neuronales vs Regresión")
    image = Image.open("imag/redes_neuronales_vs_regresion.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos cómo funciona una neurona artificial, su relación con la regresión lineal y logística.")
    url = "https://de-la-regresion-a-la-red-neuronal.streamlit.app/"
    st.write(f"Redes Neuronales vs Regresión: [Enlace]({url})")

with col8:
    st.subheader("Reconocimiento de Dígitos")

    image = Image.open("imag/reconocimiento_de_digitos.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos cómo una red neuronal reconoce dígitos escritos a mano mediante el conjunto de datos MNIST.")
    url = "https://reconocimientodedigitos.streamlit.app/"
    st.write(f"Reconocimiento de Dígitos: [Enlace]({url})")

with col9:
    st.subheader("Análisis de Sentimientos")

    image = Image.open("imag/analisis_sentimientos_texto.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace analizaremos textos para identificar su polaridad y subjetividad, clasificando los sentimientos como positivos, negativos o neutrales.")
    url = "https://representaciones-del-lenguaje-ml.streamlit.app/"
    st.write(f"Análisis de Sentimientos: [Enlace]({url})")