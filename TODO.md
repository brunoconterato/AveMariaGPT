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
- [ ] [P0] Reconstruir e certificar a base bíblica e o índice Chroma: corrigir referências corrompidas/duplicadas, criar IDs canônicos, separar `id`/`line_number`, versionar base/embedding/índice e validar a correspondência SQLite–Chroma.
- [ ] [P0] Definir o contrato de extração e o gold set: o LLM só seleciona candidatos oferecidos, a aplicação materializa a referência pela base, e `NONE`/`NEEDS_REVIEW` são respostas válidas.
- [ ] [P1] Implementar catálogo de aliases e parser determinístico para livros, capítulos, versículos, intervalos e continuações; segmentar ocorrências com offsets/timestamps, marcadores, janela adaptativa e separação oração/reflexão.
- [ ] [P1] Resolver referências explicitamente anunciadas diretamente na base e encaminhar endereços ambíguos ou inexistentes para revisão.
- [ ] [P2] Substituir geração livre de coordenadas e tool choice autônoma por seleção estruturada de 3–5 candidatos, validação de allow-list/existência/consecutividade e consolidação de intervalos por ocorrência.
- [ ] [P3] Implementar detecção de citações sem endereço e comparar BM25, embeddings multilíngues/BGE-M3, busca híbrida, reranking e abstinência calibrada.
- [ ] [P4] Avaliar Gemma quantizado, GPT 5.* e Gemini 3.*, implementar revisão humana/provenance e executar ablações e regressões sem permitir violação das invariantes de integridade.

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

- [ ] [P4] Avaliar Gemma quantizado, GPT 5.* e Gemini 3.* com métricas comparáveis de qualidade, estabilidade, latência, memória e abstinência.
- [ ] Validar o gold set com métricas de ocorrência (precision, recall, F1, IoU), recuperação (Recall@k, MRR/nDCG) e ligação por versículo.
- [ ] Testar integridade: zero referência inexistente, intervalo invertido, ID técnico tratado como versículo ou divergência entre base e índice.
- [ ] Validar o split entre oração/reflexão, a deduplicação técnica, a preservação de repetições reais e a ordem temporal/provenance.
- [ ] Testar o pipeline completo em lotes e executar a suíte de regressão após mudanças de base, parser, embedding, reranker ou modelo.

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

- Executar a reconstrução P0 e implementar os caminhos P1–P4 da extração confiável de referências
- Ativar pipeline completo em lotes
- Iniciar armazenamento e indexação no vector store principal
