import streamlit as st
import requests

API_KEY = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"

st.title("Leyes de Guatemala")

question = st.text_input("Escribe tu pregunta:")

if st.button("Responder"):

    data = {
      "apiKey": API_KEY,
      "sessionID": "1", 
      "history": [{"role": "user", "content": question}],
      "powerful": True,
      "google": True
    }
    
    response = requests.post("https://api.afforai.com/api/api_completion", json=data)
    result = response.json()
    
    st.write("Respuesta:")
    st.write(result["completion"])
