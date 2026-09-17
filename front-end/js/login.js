const API_URL = "http://127.0.0.1:8000";

const form = document.getElementById("login-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const email = document.getElementById("iemail").value.trim();
  const senha = document.getElementById("isenha").value.trim();

  const credenciais = { email, senha };

  try {
    const resp = await fetch(`${API_URL}/usuarios/login`, { // Corrigido
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(credenciais),
    });

    if (!resp.ok) {
      const error = await resp.json().catch(() => ({}));
      throw new Error(error.detail || "Falha no login");
    }

    const data = await resp.json();
    localStorage.setItem("usuarioLogado", JSON.stringify(data));
    alert("Login bem-sucedido!");
    window.location.href = "dashboard.html";
  } catch (error) {
    alert("Erro ao fazer login: " + error.message);
    console.error("Erro:", error);
  }
});