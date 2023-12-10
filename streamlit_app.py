import streamlit as st
import requests

st.title("Respondedor de preguntas legales de Guatemala")

question = st.text_input("Escriba su pregunta sobre las leyes de Guatemala:")

if question:
    api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
    session_id = "65489d7c9ad727940f2ab26f" 
    data = {
        "apiKey": api_key,
        "sessionID": session_id,
        "history": [{"role": "user", "content": question}],
        "powerful": True,
        "google": True
    }

    response = requests.post("https://api.afforai.com/api/api_completion", json=data)

    if response.status_code == 200:
        answer = response.json()["choices"][0]["message"]["content"]
        st.write(answer)
    else:
        st.error("Error al obtener la respuesta de la API")
        
