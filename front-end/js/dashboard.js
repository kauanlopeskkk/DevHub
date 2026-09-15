const API_URL = "http://127.0.0.1:8000";

// 1. VERIFICA SE O USUÁRIO ESTÁ LOGADO
const usuarioSalvo = localStorage.getItem("usuarioLogado");

if (!usuarioSalvo) {
    alert("Você precisa fazer login primeiro!");
    window.location.href = "login.html";
}

const usuario = JSON.parse(usuarioSalvo);

// 2. QUANDO O DOCUMENTO CARREGAR
document.addEventListener("DOMContentLoaded", () => {
    configurarCabecalho();
    carregarDashboard();
    configurarBotoes();
});

// Atualiza a saudação com o nome do usuário e configura o botão Sair
function configurarCabecalho() {
    const tituloBoasVindas = document.querySelector(".boas-vindas h2");
    if (tituloBoasVindas && usuario.nome) {
        tituloBoasVindas.innerText = `Bem-vindo ao DevHub, ${usuario.nome}! 👋`;
    }

    // Botão de Sair (id="layout" no seu HTML)
    const btnSair = document.getElementById("layout");
    if (btnSair) {
        btnSair.addEventListener("click", () => {
            localStorage.removeItem("usuarioLogado");
            alert("Você saiu da sua conta.");
            window.location.href = "login.html";
        });
    }
}

// 3. CARREGA PROJETOS, TAREFAS E BUGS DA API
async function carregarDashboard() {
    try {
        const [resProjetos, resTarefas, resBugs] = await Promise.all([
            fetch(`${API_URL}/projetos/`),
            fetch(`${API_URL}/tarefas/`),
            fetch(`${API_URL}/bugs/`)
        ]);

        const projetos = resProjetos.ok ? await resProjetos.json() : [];
        const tarefas = resTarefas.ok ? await resTarefas.json() : [];
        const bugs = resBugs.ok ? await resBugs.json() : [];

        // Atualiza contadores dos cards
        document.getElementById("total--projetos").innerText = projetos.length;
        document.getElementById("total-tarefas").innerText = tarefas.length;
        document.getElementById("total-bugs").innerText = bugs.length;

        // Renderiza as listas na tela
        renderizarProjetos(projetos);
        renderizarTarefas(tarefas);
        renderizarBugs(bugs);

    } catch (erro) {
        console.error("Erro ao carregar dados do dashboard:", erro);
    }
}

// 4. RENDERIZAÇÃO DAS LISTAS NA TELA
function renderizarProjetos(projetos) {
    const container = document.querySelector(".listar-projetos");
    if (!container) return;

    if (projetos.length === 0) {
        container.innerHTML = "<p>Nenhum projeto encontrado.</p>";
        return;
    }

    container.innerHTML = projetos.map(p => `
        <div style="background: #f4f4f4; padding: 10px; margin-bottom: 8px; border-radius: 6px; border-left: 4px solid #007bff;">
            <strong>${p.nome}</strong> (ID: ${p.id})<br>
            <small>${p.descricao || "Sem descrição"}</small><br>
            <span style="font-size: 12px; color: #555;">Status: <b>${p.status}</b></span>
        </div>
    `).join("");
}

function renderizarTarefas(tarefas) {
    const container = document.querySelector(".listar-tarefa");
    if (!container) return;

    if (tarefas.length === 0) {
        container.innerHTML = "<p>Nenhuma tarefa encontrada.</p>";
        return;
    }

    container.innerHTML = tarefas.map(t => `
        <div style="background: #f4f4f4; padding: 10px; margin-bottom: 8px; border-radius: 6px; border-left: 4px solid #28a745;">
            <strong>${t.titulo}</strong> (Projeto ID: ${t.projeto_id})<br>
            <small>${t.descricao || "Sem descrição"}</small><br>
            <span style="font-size: 12px; color: #555;">Prioridade: <b>${t.prioridade}</b> | Status: <b>${t.status}</b></span>
        </div>
    `).join("");
}

function renderizarBugs(bugs) {
    const container = document.querySelector(".lista-bugs");
    if (!container) return;

    if (bugs.length === 0) {
        container.innerHTML = "<p>Nenhum bug encontrado.</p>";
        return;
    }

    container.innerHTML = bugs.map(b => `
        <div style="background: #f4f4f4; padding: 10px; margin-bottom: 8px; border-radius: 6px; border-left: 4px solid #dc3545;">
            <strong>${b.titulo}</strong> (Projeto ID: ${b.projeto_id})<br>
            <small>${b.descricao || "Sem descrição"}</small><br>
            <span style="font-size: 12px; color: #555;">Prioridade: <b>${b.prioridade}</b> | Status: <b>${b.status}</b></span>
        </div>
    `).join("");
}

// 5. CONFIGURAÇÃO DOS BOTÕES DE CRIAÇÃO RÁPIDA
function configurarBotoes() {
    // Criar Projeto
    const btnNovoProjeto = document.getElementById("novo-projeto");
    if (btnNovoProjeto) {
        btnNovoProjeto.addEventListener("click", async () => {
            const nome = prompt("Nome do Projeto:");
            if (!nome) return;

            const descricao = prompt("Descrição do Projeto:") || "";

            const resposta = await fetch(`${API_URL}/projetos/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    nome: nome,
                    descricao: descricao,
                    status: "Em andamento",
                    usuario_id: usuario.id
                })
            });

            if (resposta.ok) {
                alert("Projeto criado com sucesso!");
                carregarDashboard();
            } else {
                const erro = await resposta.json();
                alert("Erro ao criar projeto: " + (erro.detail || "Erro inesperado"));
            }
        });
    }

    // Criar Tarefa
    const btnNovaTarefa = document.getElementById("nova-tarefa");
    if (btnNovaTarefa) {
        btnNovaTarefa.addEventListener("click", async () => {
            const projetoId = prompt("ID do Projeto para esta tarefa:");
            if (!projetoId) return;

            const titulo = prompt("Título da Tarefa:");
            if (!titulo) return;

            const descricao = prompt("Descrição da Tarefa:") || "";
            const prioridade = prompt("Prioridade (Baixa, Média, Alta):") || "Média";

            const resposta = await fetch(`${API_URL}/tarefas/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    titulo: titulo,
                    descricao: descricao,
                    prioridade: prioridade,
                    status: "Pendente",
                    projeto_id: parseInt(projetoId)
                })
            });

            if (resposta.ok) {
                alert("Tarefa criada com sucesso!");
                carregarDashboard();
            } else {
                const erro = await resposta.json();
                alert("Erro ao criar tarefa: " + (erro.detail || "Erro inesperado"));
            }
        });
    }

    // Registrar Bug
    const btnNovoBug = document.getElementById("novo-bugs");
    if (btnNovoBug) {
        btnNovoBug.addEventListener("click", async () => {
            const projetoId = prompt("ID do Projeto com o Bug:");
            if (!projetoId) return;

            const titulo = prompt("Título do Bug:");
            if (!titulo) return;

            const descricao = prompt("Descrição do Bug:") || "";
            const prioridade = prompt("Gravidade/Prioridade (Baixa, Média, Alta):") || "Alta";

            const resposta = await fetch(`${API_URL}/bugs/`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    titulo: titulo,
                    descricao: descricao,
                    prioridade: prioridade,
                    status: "Aberto",
                    projeto_id: parseInt(projetoId)
                })
            });

            if (resposta.ok) {
                alert("Bug registrado com sucesso!");
                carregarDashboard();
            } else {
                const erro = await resposta.json();
                alert("Erro ao registrar bug: " + (erro.detail || "Erro inesperado"));
            }
        });
    }
}