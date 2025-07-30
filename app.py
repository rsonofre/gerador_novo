
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/gerar_busca", methods=["POST"])
def gerar_busca():
    data = request.get_json()

    populacao = data.get("populacao", "")
    intervencao = data.get("intervencao", "")
    comparacao = data.get("comparacao", "")
    desfecho = data.get("desfecho", "")

    prompt = f"""
Você é um especialista em estratégias avançadas de busca científica, com experiência na construção de estratégias eficazes para o PubMed.

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
- Desfecho: {desfecho}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=600
        )

        resultado = response.choices[0].message.content.strip()
        return jsonify({"resposta": resultado})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
