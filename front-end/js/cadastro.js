const API_URL = "http://127.0.0.1:8000";

const formulario = document.getElementById("cadastro-form");

formulario.addEventListener("submit", async (event) => {
  event.preventDefault();

  const nome = document.getElementById("nome").value;
  const email = document.getElementById("email").value;
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
        "Content-Type": "application/json"
      },
      body: JSON.stringify(dadosUsuarios)
    });

    if (resposta.ok) {
      console.log("Usuário cadastrado.");
    } else {
      console.error("Erro ao cadastrar usuário.");
    }
  } catch (erro) {
    console.error("Erro na requisição:", erro);
  }
});

