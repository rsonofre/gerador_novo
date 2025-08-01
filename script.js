async function gerarBusca() {
    const populacao = document.getElementById("populacao").value;
    const intervencao = document.getElementById("intervencao").value;
    const comparacao = document.getElementById("comparacao").value;
    const desfecho = document.getElementById("desfecho").value;

    const resposta = await fetch("https://gerador-novo.onrender.com/gerar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ populacao, intervencao, comparacao, desfecho })
    });

    const data = await resposta.json();
    document.getElementById("resultado").textContent = data.resultado || data.erro;
}
