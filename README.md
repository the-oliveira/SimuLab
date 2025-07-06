# SimuLab - Simulador de Gestão para Laboratórios de Análises Clínicas 🔬

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

## 📍 Status do Projeto
**Em Desenvolvimento Ativo.** A base do backend está funcional e a próxima fase de desenvolvimento será focada na criação da interface de usuário e na expansão das funcionalidades.

---

## 📄 Descrição
O SimuLab é um sistema de gestão para laboratórios de análises clínicas, desenvolvido em Python e fundamentado nos princípios da Programação Orientada a Objetos. O projeto visa modelar e gerenciar o ciclo de vida completo de um exame, desde o cadastro inicial do paciente até a entrega do resultado.

## ✨ Funcionalidades Atuais
A fundação do projeto está concluída, com um backend robusto e funcional que inclui:

* **✔️ Backend com Persistência de Dados:** Conexão funcional com um banco de dados para armazenar e gerenciar todas as informações de forma segura.
* **✔️ CRUD de Pacientes e Exames:** Lógica implementada para Criar (INSERT) e Ler (SELECT) registros de pacientes e seus respectivos exames no banco de dados.
* **✔️ Arquitetura Orientada a Objetos:** Código estruturado em classes (`Paciente`, `Exame`, etc.), garantindo uma base modular, coesa e pronta para ser expandida.

## 🛠️ Tecnologias Utilizadas
* **Linguagem Principal:** Python
* **Banco de Dados:** MySQL

## 🗺️ Roadmap de Desenvolvimento
O futuro do SimuLab está planejado em fases para garantir um desenvolvimento estruturado e incremental.

### Fase 1: Interface e Funcionalidades Essenciais
-   [ ] **Desenvolvimento da Interface de Usuário (UI):** Criar uma interface gráfica (GUI) com **Tkinter** ou **PyQT** para permitir a interação visual do usuário com o sistema.
-   [ ] **Implementação do CRUD Completo:** Adicionar as funcionalidades de Atualizar (Update) e Deletar (Delete) registros através da nova interface.
-   [ ] **Ciclo de Vida do Exame:** Implementar a lógica para atualizar o **status** de um exame (ex: 'Aguardando Coleta', 'Em Análise', 'Concluído').

### Fase 2: Enriquecimento da Experiência
-   [ ] **Geração de Laudos:** Criar uma funcionalidade para gerar um relatório/laudo fictício do exame em formato **PDF**, contendo os dados do paciente e o resultado.
-   [ ] **Painel de Controle (Dashboard):** Desenvolver uma tela principal que exiba um resumo visual dos exames (em andamento, concluídos, pendentes) para uma visão geral da operação.
-   [ ] **Busca e Filtros Avançados:** Implementar na UI um sistema de busca de pacientes (por nome/CPF) e filtros de exames (por status/data).

### Fase 3: Arquitetura Avançada e Escalabilidade
-   [ ] **Sistema de Autenticação:** Implementar um sistema de login para diferenciar perfis de usuário (`Recepcionista`, `Técnico`, `Administrador`), cada um com suas respectivas permissões.
-   [ ] **Refatoração para API RESTful:** Desacoplar o backend, transformando-o em uma API com **Flask** ou **FastAPI**, permitindo que futuras interfaces (Web, Mobile) possam consumir os dados.
-   [ ] **Sistema de Notificações:** Adicionar uma funcionalidade simulada para notificar o paciente (via e-mail ou SMS) quando seu laudo estiver disponível.
