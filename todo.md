# ✅ Checklist Completo para o Projeto MariaGPT

## 🏗️ 1. Coleta e Preparação de Dados  
### 📖 1.1. Seleção de Fontes de Conhecimento
- [x] Obter uma versão **livre** da Bíblia Católica (ex.: Bíblia Matos Soares 1927-1950)
- [x] Obter o **Catecismo da Igreja Católica** em formato reutilizável (ex.: EPUB, PDF, TXT)
- [ ] Buscar documentos adicionais relevantes (ex.: encíclicas, concílios, santos)

### 📂 1.2. Processamento dos Dados  
- [ ] Extrair o texto limpo das fontes disponíveis (EPUB, PDF, HTML, TXT)  
- [ ] Estruturar a Bíblia em versículos e capítulos indexáveis  
- [ ] Indexar o Catecismo por parágrafos e tópicos  
- [ ] Normalizar a formatação do texto (remoção de caracteres indesejados, espaçamentos, etc.)  
- [ ] Criar uma base vetorial para **Recuperação Aumentada por Geração (RAG)**  

---

## 🏗️ 2. Construção do Agente Conversacional  
### 🧠 2.1. Implementação do RAG com Langchain  
- [ ] Configurar **Langchain** para consulta eficiente às fontes de dados  
- [ ] Escolher e configurar um **Vector Store** (ex.: FAISS, ChromaDB, Weaviate)  
- [ ] Criar um **retriever** otimizado para busca eficiente na Bíblia e Catecismo  
- [ ] Implementar um **pipeline de RAG** para alimentar a LLM com dados relevantes  

### 🤖 2.2. Configuração da LLM Local  
- [ ] Instalar e configurar **Ollama** para rodar uma LLM localmente  
- [ ] Testar diferentes modelos **open-source** (ex.: Mistral, Llama 3)  
- [ ] Ajustar o prompt engineering para respostas mais alinhadas com o contexto católico  
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
### ✅ 4.1. Testes de Qualidade  
- [ ] Validar a qualidade das respostas da LLM  
- [ ] Ajustar recuperação de trechos bíblicos e catequéticos para precisão teológica  
- [ ] Implementar logging para monitoramento de conversas  

### 📢 4.2. Testes com Usuários  
- [ ] Criar um **MVP** para feedback inicial  
- [ ] Melhorar a interface com base no feedback dos usuários  
- [ ] Iterar na curadoria das fontes de conhecimento  

---

## 🎯 5. Melhorias Futuras (Versão 2.0)  
- [ ] Implementar suporte a **voz (TTS e STT)** para acessibilidade  
- [ ] Criar **resumos** automáticos para explicações mais concisas  
- [ ] Adicionar **modo devocional** com leituras diárias e orações guiadas  
- [ ] Explorar modelos **fine-tuned** com conhecimento católico específico  

---

💡 **Meta:** Criar um chatbot funcional e útil para responder dúvidas sobre a fé católica, utilizando fontes confiáveis e garantindo respostas precisas.  
📌 **Tecnologias-chave:** Langchain, Ollama, FAISS/ChromaDB, React/HTML, Docker.  

🚀 **Próximo Passo:** Implementação do pipeline de RAG e configuração do Ollama.  
