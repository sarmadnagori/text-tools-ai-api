from fastapi import FastAPI
from pydantic import BaseModel
import requests



app = FastAPI()



class write (BaseModel):
    text : str


def ask_model(prompt):
    try:
        response = requests.post("http://localhost:11434/api/chat", json={
        "model": "llama3.2",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    })
        return response.json()["message"]["content"]
    except requests.exceptions.RequestException:
        return "Could not reach Ollama — is the server running?"


@app.post("/summarize")

def get_summary(summarize:write):

    prompt= f"Summarize this:\n\n{summarize.text}"

    reply = ask_model(prompt)
    return reply


@app.post("/translate")

def get_translate(translate:write):
    prompt= f"Translate this in Urdu language:\n\n{translate.text}"

    reply = ask_model(prompt)
    return reply

@app.post("/explain")

def get_explain(explain:write):
    prompt= f"Explain in simple:\n\n{explain.text}"

    reply = ask_model(prompt)
    return reply