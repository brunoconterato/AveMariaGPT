# ✅ Checklist Completo para o Projeto MariaGPT

## 🏗️ 1. Coleta e Preparação de Dados

### 📖 1.1. Seleção de Fontes de Conhecimento

- [x] Obter uma versão **livre** da Bíblia Católica (ex.: Bíblia Matos Soares 1927-1950)
- [x] Obter o **Catecismo da Igreja Católica** em formato reutilizável (ex.: EPUB, PDF, TXT)
- [ ] Buscar documentos adicionais relevantes (ex.: encíclicas, concílios, santos)

### 📂 1.2. Processamento e Estruturação dos Dados Iniciais (Bíblia e Catecismo)

- [x] Extrair e estruturar texto das fontes (PDF para Markdown, TXT)
- [x] Estruturar a Bíblia em versículos/seções e o Catecismo por parágrafos/tópicos (indexáveis)
- [x] Normalizar a formatação do texto (remoção de caracteres indesejados, espaçamentos, etc.)
- [~] Criar e persistir uma base vetorial (Vector Store) para **Recuperação Aumentada por Geração (RAG)** (Atual: `InMemoryVectorStore` em uso, precisa de persistência)

### 💡 1.3. Processamento e Indexação das Lives do Frei Gilson

- [~] Aprimorar e testar a detecção de versículos bíblicos em transcrições das lives
- [~] Refinar o prompt para sumarização e extração de ensinamentos das lives
- [~] Implementar e executar o pipeline de processamento em lotes das transcrições das lives
- [ ] Armazenar e indexar o conhecimento extraído das lives no Vector Store principal

---

## 🏗️ 2. Construção e Refinamento do Agente Conversacional

### 🧠 2.1. Configuração de LLM e Embeddings

- [x] Instalar e configurar **Ollama** para rodar LLMs e modelos de embedding localmente
- [x] Testar diferentes modelos **open-source** (ex.: Mistral, Llama 3) no Ollama

### 🤖 2.2. Implementação e Otimização do RAG

- [x] Configurar **Langchain/LangGraph** para consulta eficiente às fontes de dados
- [~] Ajustar o prompt engineering para respostas mais alinhadas com o contexto católico e citações explícitas
- [~] Otimizar o **retriever** para busca eficiente e precisa na base de conhecimento unificada
- [x] Implementar o **pipeline de RAG** com decomposição de query (ex: LangGraph)
- [ ] Implementar **memory management** para conversas mais naturais

---

## 🌐 3. Desenvolvimento do Front-end

### 💬 3.1. Escolha e Implementação do Chatbot

- [ ] Selecionar uma interface pré-programada de chatbot (ex.: **Botpress**, **React chatbot kit**)
- [ ] Implementar um front-end minimalista (ex.: React, Next.js ou HTML/CSS puro)
- [ ] Criar comunicação entre o front-end e o back-end do agente via API REST

### 🚀 3.2. Deploy e Infraestrutura

- [ ] Criar um **Dockerfile** para o agente conversacional
- [ ] Configurar **docker-compose** para rodar a aplicação completa
- [ ] Testar o sistema em ambiente local antes do deploy
- [ ] Opcional: Configurar um serviço de hospedagem (ex.: VPS, Railway, Fly.io)

---

## 🧪 4. Testes e Ajustes

### ✅ 4.1. Testes de Qualidade Internos

- [ ] Validar a qualidade das respostas da LLM (acurácia teológica, formatação)
- [~] Ajustar recuperação de trechos bíblicos e catequéticos para precisão teológica
- [ ] Implementar logging para monitoramento de conversas e depuração
- [ ] Desenvolver testes unitários e de integração para os componentes do RAG

### 📢 4.2. Testes com Usuários e Iteração

- [ ] Criar um **MVP** para feedback inicial
- [ ] Melhorar a interface com base no feedback dos usuários
- [ ] Iterar na curadoria e expansão das fontes de conhecimento

---

## 🎯 5. Melhorias Futuras (Versão 2.0)

- [ ] Implementar suporte a **voz (TTS e STT)** para acessibilidade
- [ ] Criar **resumos** automáticos para explicações mais concisas
- [ ] Adicionar **modo devocional** com leituras diárias e orações guiadas
- [ ] Explorar modelos **fine-tuned** com conhecimento católico específico
- [ ] Generalizar o processo de ingestão de novos livros e materiais (PDF, EPUB, TXT, HTML)

---

💡 **Meta:** Criar um chatbot funcional e útil para responder dúvidas sobre a fé católica, utilizando fontes confiáveis e garantindo respostas precisas.  
📌 **Tecnologias-chave:** Langchain, Ollama, FAISS/ChromaDB, React/HTML, Docker.

🚀 **Próximo Passo:** Concluir o processamento e indexação das lives do Frei Gilson.
