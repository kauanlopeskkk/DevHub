const API_URL = "http://127.0.0.1:8000";

const formulario = document.getElementById("cadastro-form");

formulario.addEventListener("submit", async (event) => {
  event.preventDefault();

  const nome = document.getElementById("nome").value.trim();
  const email = document.getElementById("email").value.trim();
  const senha = document.getElementById("senha").value;
  const cfsenha = document.getElementById("confirmar-senha").value;

  if (senha !== cfsenha) {
    alert("As senhas não coincidem.");
    return;
  }

  const dadosUsuarios = { nome, email, senha };

  try {
    const resposta = await fetch(`${API_URL}/usuarios/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dadosUsuarios),
    });

    if (!resposta.ok) {
      const erro = await resposta.json().catch(() => ({}));
      alert("Erro ao cadastrar: " + (erro.detail || erro.message || "Tente novamente"));
      return;
    }

    try {
      const data = await resposta.json();
      alert("Conta criada com sucesso! Faça login.");
      window.location.href = "login.html";
    } catch (erro) {
      alert("Erro ao analisar a resposta do servidor: " + erro.message);
      console.error("Erro ao analisar a resposta JSON:", erro);
    }

  } catch (erro) {
    alert("Erro ao conectar ao servidor. Tente novamente.");
    console.error("Erro na requisição:", erro);
  }
});