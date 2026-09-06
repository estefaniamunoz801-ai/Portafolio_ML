import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Aplicaciones de Machine Learning",
    page_icon="🤖",
    layout="wide",
)

#Estilos personalizados
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    .app-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }

    .app-subtitle {
        text-align: center;
        color: #6B7280;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
        padding: 0.5rem;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    }

    .card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1F2937;
        margin-bottom: 0.4rem;
        text-align: center;
    }

    .card-text {
        font-size: 0.92rem;
        color: #4B5563;
        min-height: 78px;
    }

    .link-button {
        display: block;
        text-align: center;
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        color: white !important;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-decoration: none !important;
        font-weight: 600;
        margin-top: 0.6rem;
        transition: opacity 0.15s ease;
    }

    .link-button:hover {
        opacity: 0.85;
    }

    .sidebar-box {
        background-color: rgba(79, 70, 229, 0.07);
        padding: 1rem;
        border-radius: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.subheader("🤖 Aplicaciones de Machine Learning")
    parrafo = (
        "El Machine Learning permite a los sistemas aprender de los datos para "
        "identificar patrones, hacer predicciones y clasificar información sin "
        "ser programados explícitamente para cada tarea."
    )
    st.write(parrafo)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Encabezado ----------
st.markdown('<div class="app-title">Aplicaciones de Machine Learning</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Explora ejemplos prácticos e interactivos de distintos algoritmos de ML</div>',
    unsafe_allow_html=True,
)

url_ml = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("📚 En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.markdown(f'<a class="link-button" href="{url_ml}" target="_blank">Enlace para páginas y ejercicios</a>', unsafe_allow_html=True)

st.divider()


def app_card(icon, titulo, imagen_path, descripcion, url, texto_link):
    with st.container(border=True):
        st.markdown(f'<div class="card-title">{icon} {titulo}</div>', unsafe_allow_html=True)
        image = Image.open(imagen_path)
        st.image(image, width=210, use_container_width=False)
        st.markdown(f'<div class="card-text">{descripcion}</div>', unsafe_allow_html=True)
        st.markdown(f'<a class="link-button" href="{url}" target="_blank">{texto_link}</a>', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3, gap="large")

with col1:
    app_card(
        "Regresión Lineal",
        "imag/regresion_lineal.png",
        "En el siguiente enlace veremos cómo usar la regresión lineal para predecir datos.",
        "https://predictor-en-vivo.streamlit.app/",
        "Ver Regresión Lineal",
    )

with col2:
    app_card(
        "Regresión Logística",
        "imag/regresion_logistica.png",
        "En el siguiente enlace veremos cómo usar la regresión logística para clasificar datos.",
        "https://app-seguros-python.streamlit.app/",
        "Ver Regresión Logística",
    )

with col3:
    app_card(
        "Clasificación con KNN",
        "imag/knn_clasificacion.png",
        "En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.",
        "https://ml-clasificacion-k-means-svm.streamlit.app/",
        "Ver KNN",
    )

st.write("")


col4, col5, col6 = st.columns(3, gap="large")

with col4:
    app_card(
        "Agrupamiento con K-Means",
        "imag/kmeans_consumo_electrico_v2.png",
        "En el siguiente enlace veremos cómo agrupar datos usando K-Means en una app de consumo eléctrico.",
        "https://app-consumo-ml.streamlit.app/",
        "Ver K-Means",
    )

with col5:
    app_card(
        "Árboles de Decisión",
        "imag/arboles_decision_v2.png",
        "En el siguiente enlace veremos cómo funciona un árbol de decisión.",
        "https://sistema-de-riego-inteligente-ml-arboles-decision.streamlit.app/",
        "Ver Árbol de Decisión",
    )

with col6:
    app_card(
        "Medidor de energía con ML",
        "imag/consumo_electrico_influxdb.png",
        "En el siguiente enlace veremos un dashboard interactivo para análisis y modelado con Machine Learning de datos de consumo eléctrico almacenados en InfluxDB.",
        "https://medidor-energia-ml.streamlit.app/",
        "Ver Medidor de Energía",
    )