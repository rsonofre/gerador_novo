async function gerarBusca() {
    const populacao = document.getElementById("populacao").value;
    const intervencao = document.getElementById("intervencao").value;
    const comparacao = document.getElementById("comparacao").value;
    const desfecho = document.getElementById("desfecho").value;

    try {
        const resposta = await fetch("https://gerador-novo.onrender.com/gerar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ populacao, intervencao, comparacao, desfecho })
        });

        if (!resposta.ok) {
            throw new Error(`Erro ${resposta.status}: ${resposta.statusText}`);
        }

        const data = await resposta.json();
        document.getElementById("resultado").textContent = data.resultado || data.erro;
    } catch (erro) {
        console.error("Erro ao buscar dados:", erro);
        document.getElementById("resultado").textContent = "Erro ao gerar a estratégia de busca.";
    }
}
