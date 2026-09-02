import requests
import streamlit as st

st.set_page_config(
    page_title="Detección de Intrusiones - KDD Cup 1999",
    page_icon="🛡️",
    layout="centered"
)


# Estilos CSS para centrar y estilizar la interfaz
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #00d2ff !important;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #8a99ad;
        font-weight: 400;
        margin-top: 5px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Títulos centrados
st.markdown("<h1 class='main-title'>🛡️ Pipeline MLOps: Detección de Intrusiones</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Interfaz web interactiva conectada a la API de FastAPI para inferencia en tiempo real</h3>", unsafe_allow_html=True)


# Campo de texto para ingresar las características separadas por comas
features_text = st.text_area(
    "Características de la red (separadas por comas):",
    (
        "0, 181, 5450, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"
        " 0, 8, 8, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 255, 10, 0.04, 0.06,"
        " 0.00, 0.00, 0.00, 0.00, 0.00, 0.00"
    ),
)
if st.button("Ejecutar Predicción"):
  try:
    # Convertir el texto ingresado en una lista de números decimales
    features_list = [float(x.strip()) for x in features_text.split(",")]

    # Enviar la petición POST al contenedor de FastAPI en el puerto 8000
    payload = {"features": features_list}
    response = requests.post("https://kdd-intrusion-mlops.onrender.com/predict", json=payload)

    if response.status_code == 200:
      data = response.json()
      st.success("¡Inferencia realizada con éxito!")

      # Mostrar resultados visuales destacados
      label = data.get("prediction_label")
      prob = data.get("probability")

      st.markdown(f"### Clasificación: **{label}**")
      st.metric(label="Probabilidad del Modelo", value=f"{prob * 100:.2f}%")

      with st.expander("Ver respuesta completa en JSON"):
        st.json(data)
    else:
      st.error(
          f"Error en el servidor ({response.status_code}): {response.text}"
      )

  except Exception as e:
    st.error(f"Error al procesar los datos de entrada: {e}")
