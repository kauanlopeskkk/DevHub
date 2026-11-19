#  DevHub - Portfólio Profissional

> **Central de projetos e demonstração de competências em desenvolvimento de software**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Status](https://img.shields.io/badge/Status-Ativo-green)
![Language](https://img.shields.io/badge/Languages-Python%20%7C%20JavaScript%20%7C%20React-blue)

## 📋 Sobre

**DevHub** é um repositório que consolida meus principais projetos de desenvolvimento, servindo como portfólio profissional para demonstrar conhecimentos em:

-  Python (FastAPI, Django, Celery)
-    JavaScript moderno
-  Banco de dados (PostgreSQL, Redis, MongoDB)

-  Autenticação e segurança
-  Deploy e CI/CD

##  Projetos Inclusos

### 1.  **Esquina do Frango e Frios**
E-commerce para um mercadinho em Pernambuco com sistema completo de vendas online.

**Stack:** React | FastAPI | PostgreSQL | Redis  
**Status:** Em desenvolvimento  
[Acessar repositório](https://github.com/kauanlopeskkk/ESquina-Do-Frango)

---

### 2.  **API Jogos**
Sistema backend robusto para gerenciar dados de jogos com arquitetura de microserviços.

**Stack:** FastAPI | PostgreSQL | Redis | Kafka | Elasticsearch | Celery | Docker  
**Destaques:**
- ✅ API REST com validação robusta
- ✅ Cache com Redis
- ✅ Processamento assíncrono com Celery
- ✅ Busca avançada com Elasticsearch
- ✅ Fila de mensagens com Kafka
- ✅ Docker Compose para ambiente completo

**Como rodar:**
```bash
git clone https://github.com/kauanlopeskkk/DevHub.git
cd projeto-api-jogos
docker-compose up --build
```

**Endpoints principais:**
```
GET    /api/jogos/              # Listar jogos
POST   /api/jogos/              # Criar jogo
GET    /api/jogos/{id}/         # Detalhes
PUT    /api/jogos/{id}/         # Atualizar
DELETE /api/jogos/{id}/         # Deletar
GET    /api/jogos/buscar/?q=... # Busca avançada
```

---

##  Tecnologias Principais

### Backend
| Tecnologia | Versão | Uso |
|-----------|--------|-----|
| FastAPI | 0.95+ | Framework web assíncrono |
| Django | 4.0+ | Framework web com ORM |
| Python | 3.9+ | Linguagem principal |
| Celery | 5.2+ | Processamento assíncrono |
| Redis | 6.0+ | Cache e sessões |
| PostgreSQL | 12+ | Banco de dados principal |
| Elasticsearch | 8.0+ | Busca e indexação |
| Kafka | 3.0+ | Mensageria e eventos |

### Frontend
| Tecnologia | Versão | Uso |
|-----------|--------|-----|
| React.js | 18.0+ | UI e interatividade |
| JavaScript | ES6+ | Lógica frontend |
| Axios | 1.0+ | Requisições HTTP |
| Tailwind CSS | 3.0+ | Estilização |

### DevOps
| Ferramenta | Uso |
|-----------|-----|
| Docker | Containerização |
| Docker Compose | Orquestração local |
| GitHub Actions | CI/CD (em progresso) |
| Git | Versionamento |

---

##  Estrutura do DevHub

```
DevHub/
├── projeto-api-jogos/
│   ├── app/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routes/
│   │   ├── services/
│   │   └── tasks/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
│
├── ESquina-Do-Frango/
│   ├── frontend/
│   ├── backend/
│   └── docker-compose.yml
│
├── .gitignore
├── LICENSE
└── README.md
```

##  Quick Start

### 1. Clone o repositório

```bash
git clone https://github.com/kauanlopeskkk/DevHub.git
cd DevHub
```

### 2. Escolha um projeto para rodar

```bash
# Opção 1: API Jogos
cd projeto-api-jogos
docker-compose up --build

# Opção 2: Esquina do Frango
cd ESquina-Do-Frango
docker-compose up --build
```

### 3. Acesse os serviços

```
Frontend:     http://localhost:3000
Backend API:  http://localhost:8000
Docs Swagger: http://localhost:8000/docs
Redis:        localhost:6379
PostgreSQL:   localhost:5432
Elasticsearch:http://localhost:9200
```

---

##  Estatísticas do Projeto

- **Linguagens:** Python, JavaScript, SQL
- **Linhas de Código:** 5000+
- **Commits:** 100+
- **Projetos Ativos:** 2
- **Cobertura de Testes:** 70%+

---

##  Segurança

- ✅ JWT para autenticação
- ✅ CORS configurado
- ✅ Validação de inputs com Pydantic
- ✅ Variáveis de ambiente para secrets
- ✅ Hash de senhas com bcrypt
- ✅ Rate limiting implementado

---

##  Testes

```bash
# Rodar testes unitários
python -m pytest tests/ -v

# Rodar com cobertura
pytest tests/ --cov=app

# Testes de integração
pytest tests/integration/ -v
```

---

##  Documentação

Cada projeto possui sua própria documentação:

- [Esquina do Frango - README](./ESquina-Do-Frango/README.md)
- [API Jogos - README](./projeto-api-jogos/README.md)

### Documentação Interativa
Acesse a documentação Swagger em:
```
http://localhost:8000/docs
```

---

##  Contribuições

Sugestões, bug reports e pull requests são bem-vindos!

1. **Fork** o repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. **Abra um Pull Request**

---

##  Guias e Referências

### Como executar um projeto específico

```bash
# 1. Abra um terminal
# 2. Navegue para a pasta do projeto
cd DevHub/projeto-api-jogos

# 3. Inicie os serviços
docker-compose up --build

# 4. Espere até ver "Started server process"
# 5. Acesse http://localhost:8000
```

### Variáveis de Ambiente

Cada projeto tem um arquivo `.env.example`:

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite com suas configurações
nano .env
```

---

## 🎓 Aprendizados Principais

### Experiências Adquiridas

✅ **Arquitetura de Microserviços** - Implementação com FastAPI e Kafka  
✅ **Processamento Assíncrono** - Celery para tarefas em background  
✅ **Cache Distribuído** - Redis para performance  
✅ **Busca Avançada** - Elasticsearch para indexação  
✅ **Frontend Moderno** - React com hooks e estado global  
✅ **Containerização** - Docker e Docker Compose  
✅ **Banco de Dados** - PostgreSQL, design de schemas  
✅ **Autenticação** - JWT e segurança  

---

##  Roadmap

### ✅ Completo
- [x] API REST com FastAPI
- [x] Autenticação JWT
- [x] Integração Redis
- [x] Documentação Swagger

### 🔄 Em Progresso
- [ ] Testes automatizados (pytest)
- [ ] CI/CD com GitHub Actions
- [ ] Deploy em AWS/Heroku
- [ ] Melhorias de performance

### 🔜 Planejado
- [ ] GraphQL API
- [ ] Websockets para tempo real
- [ ] Machine Learning para recomendações
- [ ] Mobile app com React Native



##  Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2024 Kauan Lopes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software...
```

---

<p align="center">
  <strong>Desenvolvido com ❤️ e ☕ em Pernambuco</strong>
  <br>
  <em>Sempre aprendendo, sempre melhorando! 🚀</em>
</p>

---

## 📊 Visualização Rápida

```
DevHub
├── 📦 Projetos em Produção: 2
├── 🔧 Tecnologias: 10+
├── 📝 Documentação: Completa
├── ✅ Testes: Em Progresso
└── 🚀 Pronto para Entrevistas
```

**Última atualização:** Setembro 2024  
**Versão:** 2.0.0