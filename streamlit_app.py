import streamlit as st
import requests

def get_api_response(question):
    url = "https://api.afforai.com/api/api_completion"
    payload = {
        "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
        "sessionID": "65489d7c9ad727940f2ab26f",
        "history": [
            {
                "role": "user",
                "content": question
            }
        ],
        "powerful": True,
        "google": True
    }
    response = requests.post(url, json=payload)
    return response.json()

def main():
    st.title("Preguntas sobre las leyes de Guatemala")
    question = st.text_input("Escribe tu pregunta")
    if st.button("Enviar"):
        response = get_api_response(question)
        st.json(response)

if __name__ == "__main__":
    main()
