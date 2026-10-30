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

col10, col11, col12 = st.columns(3, gap="large")

with col10:
    st.subheader("Recomendador semántico con embeddings")
    image = Image.open("imag/busqueda_semantica_embeddings.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos cómo utilizar Sentence Transformers y embeddings para encontrar respuestas mediante similitud semántica.")
    url = "https://app-recomendador-semantico-ml.streamlit.app/"
    st.write(f"Recomendador semántico: [Enlace]({url})")

with col11:
    st.subheader("Conversor de Texto a Audio")
    image = Image.open("imag/conversor_texto_audio.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace convertiremos textos en audio mediante gTTS")
    url = "https://app-conversor-texto-audio-ml.streamlit.app/"
    st.write(f"Conversor de Texto a Audio: [Enlace]({url})")

with col12:
    st.subheader("Traductor de Voz Multilenguaje")

    image = Image.open("imag/traductor_voz_multilenguaje.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos cómo convertir voz en texto, traducirlo a diferentes idiomas y generar audio mediante reconocimiento de voz.")
    url = "https://app-translate-ml.streamlit.app/"
    st.write(f"Traductor de Voz Multilenguaje: [Enlace]({url})")

col13, col14, col15 = st.columns(3, gap="large")

with col13:
    st.subheader("RNN-consumo de energía semanal")
    image = Image.open("imag/rnn_consumo_energia_semanal.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos cómo una red neuronal recurrente (RNN) aprende patrones semanales de consumo energético.")
    url = "https://app-rnn-energy-consumption-ml.streamlit.app/"
    st.write(f"RNN-consumo de energía semanal: [Enlace]({url})")

with col14:
    st.subheader("Generador de Texto con LSTM")
    image = Image.open("imag/generador_texto_lstm.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos cómo utilizar una red neuronal LSTM para generar texto.")
    url = "https://generador-texto-con-lstm-ml.streamlit.app/"
    st.write(f"Generador de Texto con LSTM: [Enlace]({url})")

with col15:
    st.subheader("Reconocimiento de Personas mediante Visión Artificial")

    image = Image.open("imag/reconocimiento_personas.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos cómo utilizar un modelo de clasificación de imágenes entrenado con Teachable Machine.")
    url = "https://computer-vision-ml.streamlit.app/"
    st.write(f"Reconocimiento de Personas: [Enlace]({url})")

col16, col17, col18 = st.columns(3, gap="large")

with col16:
    st.subheader("Detección en Tiempo Real de Objetos")
    image = Image.open("imag/imag/deteccion_objetos_yolov5.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos la detección de objetos en tiempo real usando YOLOv5")
    url = "https://real-time-object-detection-ml.streamlit.app/"
    st.write(f"Detección en Tiempo Real de Objetos: [Enlace]({url})")

with col17:
    st.subheader("Multipages de Machine Learning")
    image = Image.open("imag/multipagina_machine_learning.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos una plataforma web multipágina que integra diferentes aplicaciones de Machine Learning.")
    url = "https://multipages-ml.streamlit.app/"
    st.write(f"Multipages de Machine Learning: [Enlace]({url})")

with col18:
    st.subheader("Asistente RAG para Análisis de Documentos PDF")

    image = Image.open("imag/asistente_rag_pdf.png")
    st.image(image, width=250)
    st.write("En el siguiente enlace exploraremos cómo consultar documentos PDF mediante RAG, combinando búsqueda semántica y modelos de lenguaje para generar respuestas.")
    url = "https://chat-pdf-ml.streamlit.app/"
    st.write(f"Asistente RAG: [Enlace]({url})")