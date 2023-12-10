import streamlit as st
import requests

# Configurar la URL de la API
API_URL = "https://api.afforai.com/api/api_completion"

# Función para llamar a la API y obtener la respuesta
def obtener_respuesta_pregunta(pregunta):
    payload = {
        "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
        "sessionID": "65489d7c9ad727940f2ab26f",
        "history": [{"role": "user", "content": pregunta}],
        "powerful": True,
        "google": True
    }
    response = requests.post(API_URL, json=payload)
    respuesta = response.json()
    return respuesta["completions"][0]["choices"][0]["text"]

# Configurar la interfaz de la aplicación con Streamlit
def main():
    st.title("Preguntas sobre las leyes de Guatemala")
    pregunta = st.text_input("Haz tu pregunta aquí")
    if pregunta:
        respuesta = obtener_respuesta_pregunta(pregunta)
        st.markdown(f"**Respuesta:** {respuesta}")

if __name__ == "__main__":
    main()
