from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app, origins=["https://illustrious-sable-2979ca.netlify.app"])

openai.api_key = "sua_chave_api_aqui"

@app.route("/gerar", methods=["POST"])
def gerar_busca():
    dados = request.get_json()
    populacao = dados.get("populacao", "")
    intervencao = dados.get("intervencao", "")
    comparacao = dados.get("comparacao", "")
    desfecho = dados.get("desfecho", "")

    prompt = f"""Você é um especialista em estratégias avançadas de busca científica, com experiência na construção de estratégias eficazes para o PubMed.

Com base nas informações abaixo, siga estas instruções:

1. Formule uma pergunta de pesquisa estruturada no formato PICO, claramente identificando os quatro elementos (População, Intervenção, Comparação e Desfecho).

2. Elabore uma estratégia de busca avançada para o PubMed, pronta para ser utilizada, com as seguintes características:
- Inclua termos MeSH e sinônimos relevantes.
- Use operadores booleanos (AND, OR), truncamentos (*) e parênteses de forma adequada.
- Seja o mais abrangente possível, sem comprometer a especificidade.
- Evite linguagem desnecessária — retorne apenas a pergunta PICO e a string da busca.

Informações fornecidas:
- População: {populacao}
- Intervenção: {intervencao}
- Comparação: {comparacao}
- Desfecho: {desfecho}"""

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em estratégias de busca científica no PubMed."},
                {"role": "user", "content": prompt}
            ]
        )
        resultado = resposta["choices"][0]["message"]["content"]
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
