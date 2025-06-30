# ✅ Checklist Interativo — Projeto MariaGPT

## 🏗️ 1. Coleta e Preparação de Dados

### 📖 1.1. Seleção de Fontes de Conhecimento

- [x] Obter uma versão livre da Bíblia Católica
  - [x] Matos Soares
  - [x] Bíblia Ave Maria
- [x] Obter o Catecismo da Igreja Católica em formato estruturado (EPUB, PDF ou TXT)
- [ ] Buscar documentos adicionais (encíclicas, concílios, escritos dos santos) → **Mover para Fase 5.5**

### 📂 1.2. Processamento e Estruturação dos Dados

- [x] Conversão dos PDFs para Markdown
- [x] Quebra dos textos em chunks com cabeçalhos e metadados
- [x] Criação da Vector Store temporária (InMemoryVectorStore)
- [ ] Migrar para uma Vector Store persistente (ChromaDB ou FAISS) → **Fase 2.1**

---

## 💡 2. Processamento das Lives do Frei Gilson (Quaresma 2025) → **Prioridade Atual**

### 🔧 2.1. Preparação e Refinamento dos Dados das Lives

- [x] Definir e validar prompts para sumarização e extração dos ensinamentos
- [x] Refinar prompt para:
  - Ignorar a parte da reflexão
  - Focar no conteúdo da oração do Santo Rosário
  - Gerar relatório estruturado em Markdown
- [x] Implementar detecção de versículos bíblicos (`get_bible_passages`)
- [ ] Melhorar robustez da detecção de versículos: [Ver `src/Rosários Quaresma Frei Gilson 2025/todo.md`](./src/Rosários%20Quaresma%20Frei%20Gilson%202025/todo.md)

### 🔍 2.2. Pipeline de Processamento das Transcrições

- [x] Criar lógica de carregamento dos arquivos
- [~] Implementar loop de processamento em lotes (`for i in tqdm(range(13, 41))`)
  - [x] Leitura dos arquivos
  - [x] Teste para um arquivo

### 💾 2.3. Armazenamento e Indexação

- [ ] Armazenar resumos e metadados extraídos das lives:
  - Arquivos Markdown estruturados
  - E/ou banco (ChromaDB ou SQLite) junto com Bíblia e Catecismo
- [ ] Indexar versículos, temáticas e ensinamentos das lives no vector store principal

### 🧪 2.4. Testes e Validação Específicos das Lives

- [x] Testar diferentes modelos (Llama3, Mistral, Qwen, Gemma)
- [x] Validar qualidade dos modelos na detecção de versículos
- [ ] Validar se o split correto entre oração e reflexão funciona
- [ ] Testar pipeline completo em lotes
- [ ] Validar se todos os versículos e ensinamentos são corretamente extraídos

---

## 🤖 3. Construção e Refinamento do Agente Conversacional

### 🧠 3.1. Configuração de Modelos e Embeddings

- [x] Instalar e configurar Ollama (LLMs + embeddings locais)
- [x] Testar modelos open-source (Gemma, Mistral, Llama 3)

### 🔍 3.2. Implementação do Pipeline RAG

- [x] Implementar pipeline RAG básico (LangChain + LangGraph)
- [ ] Otimizar o retriever com:
  - MultiQueryRetriever
  - Filtros por metadados
  - Compressão → **Fase 2.2**
- [ ] Refinar o prompt principal para alinhamento teológico → **Fase 2.3**
- [ ] Implementar memória conversacional → **Fase 2.4**

---

## 🌐 4. Desenvolvimento do Front-end e API

### 💬 4.1. Interface de Chat

- [ ] Escolher stack de front-end (React + Tailwind, Next.js ou HTML/CSS)
- [ ] Implementar UI minimalista do chatbot
- [ ] Criar API REST (Flask ou FastAPI) para comunicação com backend

### 🚀 4.2. Deploy e Infraestrutura

- [ ] Criar Dockerfile do backend (API + RAG)
- [ ] Criar docker-compose.yml para orquestração (backend + frontend)
- [ ] Testar aplicação localmente (frontend + backend)
- [ ] (Opcional) Configurar deploy (VPS, Railway, Fly.io)

---

## 🧪 5. Testes e Validação Geral

### 🔍 5.1. Testes Técnicos

- [ ] Implementar testes unitários e de integração para:
  - Pipelines de RAG
  - Recuperação de documentos
  - Formatação de respostas (citações, markdown)
- [ ] Implementar logging robusto para monitoramento e depuração

### 👥 5.2. Testes com Usuários

- [ ] Criar MVP funcional para feedback
- [ ] Coletar feedback dos usuários
- [ ] Iterar e ajustar com base no feedback

---

## 🎯 6. Melhorias Futuras (Versão 2.0)

- [ ] Suporte a voz (STT + TTS)
- [ ] Modo devocional com leituras diárias e orações
- [ ] Criação de resumos automáticos
- [ ] Explorar modelos fine-tuned com corpus católico
- [ ] Pipeline genérico para ingestão de novos materiais (PDF, EPUB, HTML)

---

## 🚩 Próximo Passo Imediato:

➡️ **Finalizar a Fase 2 (Processamento das Lives do Frei Gilson)**:

- Refinar detecção de versículos
- Ativar pipeline completo em lotes
- Iniciar armazenamento e indexação no vector store principal
