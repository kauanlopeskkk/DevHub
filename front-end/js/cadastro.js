const API_URL = "http://127.0.0.1:8000";

const formulario = document.getElementById("cadastro-form");

formulario.addEventListener("submit", async (event) => {

event.preventDefault();

})


const nome = document.getElementById("nome").value
const email = document.getElementById("email").value
const senha = document.getElementById("senha").value
const cfsenha = document.getElementById("confirmar-senha").value;

if (senha !== cfsenha){
    alert("As senhas não estar completamente errado")
}
return;

const dadosUsuarios = {

nome: nome,
email: email,
senha: senha

};

