function converter(baseOrigem, baseDestino, inputId, resultadoId) {
  const numero = document.getElementById(inputId).value;

  // Limpa mensagens anteriores
  document.getElementById(resultadoId).textContent = '';
  document.getElementById(`${baseOrigem}Erro`).textContent = '';

  if (!numero) {
    document.getElementById(`${baseOrigem}Erro`).textContent = "Digite um número!";
    return;
  }

  fetch('/converter', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `numero=${encodeURIComponent(numero)}&base_origem=${encodeURIComponent(baseOrigem)}&base_destino=${encodeURIComponent(baseDestino)}`
  })
  .then(response => response.json())
  .then(data => {
    if (data.erro) {
      document.getElementById(`${baseOrigem}Erro`).textContent = data.erro;
    } else {
      document.getElementById(resultadoId).textContent = `${baseDestino.charAt(0).toUpperCase() + baseDestino.slice(1)}: ${data.resultado}`;
    }
  })
  .catch(error => {
    console.error("Erro:", error);
    document.getElementById(`${baseOrigem}Erro`).textContent = "Erro ao processar a conversão.";
  });
}
