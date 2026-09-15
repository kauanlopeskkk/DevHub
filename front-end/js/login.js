const API_URL = "http://127.0.0.1:8000";

const form1 = getElementById("login-form").value;

const form2 = addEventListener("submit", async(event) =>{

event.preventDefault();

const email = document.getElementById("iemail").value
const senha = document.getElementById("isenha").value

const credencias = {
    email: email,
    senha: senha,
};
    try{
        fetch(`${API_URL}/usuario/login`,{
          method: "POST",
          headers: {
            "Content-Type":
            "application/json"
          },

        body: JSON.stringify(credencias),
        });
        if (Response.ok){

        const data = await Response.json();
        alert("Login bem sucedido");
        console.log(data);

        window.location.href = "dashboard.html"
     }
     else {
        const error = await Response.json();
        alert("Erro ao conectar ao servidor. Tente Novamente")
        console.error(error);
     }
    }catch (error) {
        alert("Erro ao conectar ao servidor. Tente novamente")
        console.error(error);    }



});



