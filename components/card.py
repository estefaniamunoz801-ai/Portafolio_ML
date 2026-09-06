import streamlit as st
from components.card import render_ml_card
from styles import load_css


st.set_page_config(
    page_title="Aplicaciones de Machine Learning",
    layout="wide"
)

load_css()

with st.sidebar:

    st.subheader("Aplicaciones de Machine Learning.")

    parrafo = (
        "El Machine Learning permite a los sistemas aprender de los datos para "
        "identificar patrones, hacer predicciones y clasificar información sin "
        "ser programados explícitamente para cada tarea."
    )

    st.write(parrafo)


st.markdown(
    '<div class="main-title">Aplicaciones de Machine Learning</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Portafolio de aplicaciones prácticas desarrolladas con Python y Machine Learning.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title-line"></div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="section-title">Recursos y ejercicios prácticos</div>',
    unsafe_allow_html=True
)

url_ml = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown(
    f"En el siguiente enlace puedes encontrar páginas y ejercicios prácticos: "
    f"[Enlace]({url_ml})"
)


st.markdown(
    '<div class="section-title">Aplicaciones</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3, gap="large")

with col1:
    render_ml_card(
        "Regresión Lineal",
        "imag/regresion_lineal.png",
        "En el siguiente enlace veremos cómo usar la regresión lineal para predecir datos.",
        "https://predictor-en-vivo.streamlit.app/",
        "Regresión Lineal"
    )


with col2:
    render_ml_card(
        "Regresión Logística",
        "imag/regresion_logistica.png",
        "En el siguiente enlace veremos cómo usar la regresión logística para clasificar datos.",
        "https://app-seguros-python.streamlit.app/",
        "Regresión Logística"
    )


with col3:
    render_ml_card(
        "Clasificación con KNN",
        "imag/knn_clasificacion.png",
        "En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.",
        "https://ml-clasificacion-k-means-svm.streamlit.app/",
        "KNN"
    )

st.write("")

col4, col5, col6 = st.columns(3, gap="large")

with col4:
    render_ml_card(
        "Agrupamiento con K-Means",
        "imag/kmeans_consumo_electrico_v2.png",
        "En el siguiente enlace veremos cómo agrupar datos usando K-Means en una app de consumo electrico.",
        "https://app-consumo-ml.streamlit.app/",
        "K-Means"
    )


with col5:
    render_ml_card(
        "Árboles de Decisión",
        "imag/arboles_decision_v2.png",
        "En el siguiente enlace veremos cómo funciona un árbol de decisión.",
        "https://sistema-de-riego-inteligente-ml-arboles-decision.streamlit.app/",
        "Árbol de Decisión"
    )


with col6:
    render_ml_card(
        "Medidor de energia con ML",
        "imag/consumo_electrico_influxdb.png",
        "En el siguiente enlace veremos un dashboard interactivo para análisis y modelado con Machine Learning de datos de consumo eléctrico almacenados en InfluxDB.",
        "https://medidor-energia-ml.streamlit.app/",
        "Medidor de Energía con ML"
    )