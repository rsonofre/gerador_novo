
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/gerar_busca", methods=["POST"])
def gerar_busca():
    data = request.get_json()

    populacao = data.get("populacao", "")
    intervencao = data.get("intervencao", "")
    comparacao = data.get("comparacao", "")
    desfecho = data.get("desfecho", "")

    prompt = f"""
    Você é um especialista em estratégias de busca no PubMed. Com base nos dados fornecidos, elabore:

    1. Uma pergunta de pesquisa estruturada no formato PICO.
    2. Uma estratégia de busca otimizada para PubMed, com uso de termos MeSH, operadores booleanos e truncamentos.

    População: {populacao}
    Intervenção: {intervencao}
    Comparação: {comparacao}
    Desfecho: {desfecho}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=700
        )

        resultado = response['choices'][0]['message']['content']
        return jsonify({"resposta": resultado})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
