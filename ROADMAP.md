# Roadmap do Projeto MariaGPT

## 📌 **Fase 0: Fundação e Ingestão de Dados Iniciais (Concluído)**

Esta fase estabeleceu as bases do projeto, incluindo a extração e estruturação inicial dos dados da Bíblia e do Catecismo, além do setup do ambiente LLM.

- **0.1. Instalação e Configuração do Ambiente Ollama**
  - **Descrição:** Verificação e instalação dos modelos LLM (`gemma3:12b`) e de Embedding (`mxbai-embed-large:latest`) no Ollama.
  - **Status:** ✅ Concluído
  - **Arquivos Relevantes:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (células `d61c542a`, `e724bf19`)
  - **Estimativa:** 0 horas (já feito)

- **0.2. Pré-processamento e Estruturação da Bíblia (Ave Maria)**
  - **Descrição:** Extração, limpeza e formatação da Bíblia Ave Maria em versículos individualizados.
  - **Status:** ✅ Concluído
  - **Arquivos Relevantes:** `src/Bíblia VectorStore/1. Format.ipynb`
  - **Estimativa:** 0 horas (já feito)

- **0.3. Criação de Vector Store e DB Relacional da Bíblia (Ave Maria)**
  - **Descrição:** Indexação dos versículos da Bíblia Ave Maria em uma `ChromaDB` e armazenamento em um banco de dados SQLite para consulta detalhada.
  - **Status:** ✅ Concluído
  - **Arquivos Relevantes:** `src/Bíblia VectorStore/2. Vector database.ipynb`
  - **Estimativa:** 0 horas (já feito)

- **0.4. Conversão de PDF para Markdown (Bíblia Matos Soares & Catecismo)**
  - **Descrição:** Utilização do script `process_pdf_batches.sh` para converter PDFs da Bíblia Matos Soares e do Catecismo para Markdown, preparando-os para o split.
  - **Status:** ✅ Concluído
  - **Arquivos Relevantes:** `src/1. Preprocessing/process_pdf_batches.sh`, `src/1. Preprocessing/README.md`
  - **Estimativa:** 0 horas (já feito)

- **0.5. Quebra de Texto por Cabeçalhos (Bíblia Matos Soares & Catecismo)**
  - **Descrição:** Implementação do `MarkdownHeaderTextSplitter` para segmentar os textos Markdown em chunks com metadados de cabeçalho.
  - **Status:** ✅ Concluído
  - **Arquivos Relevantes:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (células `399f989b`, `13d68cc0`)
  - **Estimativa:** 0 horas (já feito)

- **0.6. Criação da Vector Store Unificada (Bíblia Matos Soares & Catecismo - In-Memory)**
  - **Descrição:** Adição dos chunks processados da Bíblia Matos Soares e do Catecismo a uma `InMemoryVectorStore` para testes iniciais do RAG.
  - **Status:** ✅ Concluído
  - **Arquivos Relevantes:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (células `5ec25d1d`, `c9acb7d2`)
  - **Estimativa:** 0 horas (já feito)

- **0.7. Definição Inicial do Prompt para o Agente RAG**
  - **Descrição:** Criação das templates de `SystemMessage` e `HumanMessage` para guiar o LLM na geração de respostas católicas.
  - **Status:** ✅ Concluído
  - **Arquivos Relevantes:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (célula `e724bf19`)
  - **Estimativa:** 0 horas (já feito)

---

## 🚀 **Fase 1: Processamento Detalhado das Lives do Frei Gilson (Prioridade)**

Esta fase foca em concluir a extração de conhecimento das transcrições das lives, tornando-as uma fonte de dados valiosa para o MariaGPT.

- **1.1. Extração Confiável de Referências Bíblicas em Transcrições**
  - **Descrição:** Executar a implementação em ordem de prioridade P0–P4: (P0) auditar/reconstruir a base bíblica, criar IDs canônicos, certificar SQLite–Chroma, definir o contrato de seleção e o gold set; (P1) implementar aliases, parser determinístico, ocorrências com offsets/timestamps, separação oração/reflexão e resolução direta de referências anunciadas; (P2) limitar a seleção do LLM a 3–5 candidatos estruturados, validar allow-list/existência/consecutividade e consolidar intervalos por ocorrência; (P3) adicionar detector de citações sem endereço, busca BM25+dense/híbrida, reranking, alinhamento ASR, calibração e abstinência; (P4) comparar Gemma quantizado, GPT 5.* e Gemini 3.*, habilitar revisão humana, provenance, ablações e regressões.
  - **Dependência:** Fonte bíblica licenciada/versionada e `src/Bíblia VectorStore/2. Vector database.ipynb` como referência para reconstrução da base e do índice.
  - **Arquivos Relevantes:** `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb`, `src/Rosários Quaresma Frei Gilson 2025/utils.py`, `src/Bíblia VectorStore/2. Vector database.ipynb`, `src/Rosários Quaresma Frei Gilson 2025/research-extracao-referencias-biblicas.md` e `src/Rosários Quaresma Frei Gilson 2025/todo-extracao-confiavel-referencias-biblicas.md`
  - **Critérios de aceite:** zero referência inexistente, intervalo invertido ou `id`/`line_number` tratado como versículo; deduplicação técnica sem apagar repetições reais; métricas do gold set superiores ao baseline; decisões reproduzíveis por provenance.
  - **Estimativa:** 55 horas

- **1.2. Refinamento do Prompt para Sumarização e Extração de Ensinamentos das Lives**
  - **Descrição:** Ajustar o `system_message` para a LLM extrair de forma precisa temáticas, subtemas, músicas e eventos, garantindo que apenas o conteúdo relevante do "Santo Rosário" seja considerado, ignorando a parte da "Reflexão".
  - **Arquivos Relevantes:** `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb` (células `75aa5ce7`, `e724bf19`)
  - **Estimativa:** 20 horas

- **1.3. Implementação do Pipeline de Processamento em Lotes das Transcrições**
  - **Descrição:** Concluir a lógica do loop em `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb` para processar todas as transcrições das lives (`for i in tqdm(range(13, 41))`), persistindo os resultados extraídos em um formato estruturado (e.g., Markdown ou JSON) por live. Remover o `assert False`.
  - **Dependência:** 1.1 e 1.2
  - **Arquivos Relevantes:** `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb` (célula `2240fa7d`)
  - **Estimativa:** 25 horas

- **1.4. Armazenamento e Indexação do Conhecimento das Lives para RAG**
  - **Descrição:** Integrar o conhecimento estruturado extraído das lives (temáticas, versículos, etc.) ao vector store principal do MariaGPT ou criar um vector store dedicado. Isso permitirá que o agente RAG responda a perguntas sobre os ensinamentos do Frei Gilson.
  - **Dependência:** 1.3
  - **Arquivos Relevantes:** (Novo script/notebook ou extensão de `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb`)
  - **Estimativa:** 18 horas

**Total Estimado para Fase 1:** 118 horas

---

## ⚙️ **Fase 2: Refinamento e Otimização do Agente Conversacional Core (MariaGPT)**

Com as fontes de dados completas, esta fase otimizará o coração do MariaGPT.

- **2.1. Otimização e Persistência da Vector Store Principal**
  - **Descrição:** Substituir a `InMemoryVectorStore` por uma solução persistente (e.g., `ChromaDB` em disco ou `FAISS`) para armazenar os embeddings da Bíblia Matos Soares, Catecismo e as informações das Lives.
  - **Dependência:** Todas as etapas de ingestão de dados.
  - **Arquivos Relevantes:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (modificação)
  - **Estimativa:** 10 horas

- **2.2. Melhoria do Módulo Retriever**
  - **Descrição:** Explorar e implementar estratégias de recuperação avançadas (e.g., `MultiQueryRetriever`, `ContextualCompressionRetriever`, ajuste de `k` e filtros de metadados) para garantir que os chunks mais relevantes sejam retornados ao LLM.
  - **Dependência:** 2.1
  - **Arquivos Relevantes:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (modificação da função `retrieve`)
  - **Estimativa:** 15 horas

- **2.3. Validação e Ajustes Finais do Prompt Principal do Agente**
  - **Descrição:** Realizar testes exaustivos com diversas perguntas para refinar os prompts do sistema e do RAG, garantindo que as respostas sejam teologicamente precisas, completas (com citações integrais de versículos e catecismo) e no tom desejado.
  - **Arquivos Relevantes:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (célula `e724bf19`)
  - **Estimativa:** 20 horas

- **2.4. Implementação de Gerenciamento de Memória Conversacional**
  - **Descrição:** Integrar módulos de memória do Langchain (e.g., `ConversationBufferWindowMemory`) para permitir que o chatbot mantenha o contexto de conversas multi-turn.
  - **Arquivos Relevantes:** (Novo arquivo ou extensão de `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` para integrar a memória ao LangGraph)
  - **Estimativa:** 12 horas

- **2.5. Desenvolvimento de Testes de Qualidade (Unitários e de Integração)**
  - **Descrição:** Criar testes automatizados para verificar a acurácia do retriever, a coerência e relevância das respostas do LLM e a aderência aos requisitos de formatação (e.g., citação de versículos).
  - **Arquivos Relevantes:** (Novo diretório `tests/`)
  - **Estimativa:** 25 horas

**Total Estimado para Fase 2:** 82 horas

---

## 💬 **Fase 3: Desenvolvimento do Front-end (Interface do Chatbot)**

Esta fase concentra-se na criação da interface do usuário que permitirá a interação com o MariaGPT.

- **3.1. Escolha e Configuração da Interface do Chatbot**
  - **Descrição:** Selecionar a tecnologia de front-end (ex: React, Next.js, ou HTML/CSS/JS puro) e uma biblioteca/componente de UI de chatbot, configurando o ambiente de desenvolvimento.
  - **Arquivos Relevantes:** (Novo diretório `frontend/`)
  - **Estimativa:** 20 horas

- **3.2. Criação da API REST para Comunicação Back-end/Front-end**
  - **Descrição:** Desenvolver uma API leve (ex: com Flask ou FastAPI) que exponha o agente RAG (desenvolvido na Fase 2) como um serviço, permitindo que o front-end envie perguntas e receba respostas.
  - **Arquivos Relevantes:** (Novo diretório `backend/api/`)
  - **Estimativa:** 18 horas

- **3.3. Implementação da Lógica e UI do Chatbot**
  - **Descrição:** Construir os componentes da interface do usuário, incluindo a caixa de entrada, a área de exibição de mensagens, botões, e a lógica de comunicação com a API REST.
  - **Dependência:** 3.1 e 3.2
  - **Arquivos Relevantes:** `frontend/`
  - **Estimativa:** 30 horas

**Total Estimado para Fase 3:** 68 horas

---

## 🚀 **Fase 4: Deploy e Testes com Usuários**

Esta fase visa disponibilizar o MariaGPT para uso e coletar feedback para futuras melhorias.

- **4.1. Containerização do Agente Conversacional (Dockerfile)**
  - **Descrição:** Criar um `Dockerfile` para empacotar o back-end (agente RAG e API) em uma imagem Docker, garantindo portabilidade e ambiente consistente.
  - **Arquivos Relevantes:** `backend/Dockerfile`
  - **Estimativa:** 10 horas

- **4.2. Orquestração da Aplicação com Docker Compose**
  - **Descrição:** Configurar um `docker-compose.yml` para facilmente levantar e gerenciar os serviços do back-end (agente RAG) e front-end (chatbot UI) em um ambiente de desenvolvimento ou produção local.
  - **Arquivos Relevantes:** `docker-compose.yml` (na raiz do projeto)
  - **Estimativa:** 8 horas

- **4.3. Testes Finais em Ambiente Local e Preparação do MVP**
  - **Descrição:** Realizar testes de integração completos do sistema localmente, verificando a comunicação entre front-end e back-end, e preparando uma versão MVP para ser compartilhada com um grupo seleto de usuários.
  - **Estimativa:** 20 horas

- **4.4. Opcional: Configuração de Serviço de Hospedagem (VPS, Railway, Fly.io)**
  - **Descrição:** Selecionar e configurar um provedor de hospedagem para o deploy público da aplicação MariaGPT.
  - **Estimativa:** 30 horas (Variável dependendo da plataforma escolhida e complexidade da infra)

- **4.5. Testes com Usuários e Coleta de Feedback**
  - **Descrição:** Lançar o MVP para um grupo de usuários, coletar feedback qualitativo e quantitativo sobre a qualidade das respostas, usabilidade da interface e desempenho geral.
  - **Estimativa:** 15 horas

**Total Estimado para Fase 4:** 83 horas (considerando a etapa opcional de hospedagem)

---

## 💡 **Fase 5: Melhorias Futuras (Versão 2.0)**

Estas são as etapas para expandir as capacidades do MariaGPT após a versão inicial.

- **5.1. Implementação de Suporte a Voz (TTS e STT)**
  - **Descrição:** Adicionar capacidades de entrada de voz (Speech-to-Text) e saída de voz (Text-to-Speech) para maior acessibilidade.
  - **Estimativa:** 40 horas

- **5.2. Criação de Resumos Automáticos para Explicações Concisas**
  - **Descrição:** Desenvolver um módulo que gere resumos mais curtos e diretos para respostas que tendem a ser muito extensas, otimizando a experiência do usuário.
  - **Estimativa:** 15 horas

- **5.3. Adição de Modo Devocional com Leituras Diárias e Orações Guiadas**
  - **Descrição:** Implementar uma funcionalidade que ofereça leituras bíblicas diárias, orações guiadas e reflexões devocionais.
  - **Estimativa:** 30 horas

- **5.4. Exploração de Modelos Fine-tuned com Conhecimento Católico Específico**
  - **Descrição:** Pesquisar e, se viável, treinar um modelo LLM open-source com um corpus de dados católicos ainda mais específico para melhorar a precisão e profundidade das respostas.
  - **Estimativa:** 80 horas (P&D intenso)

- **5.5. Generalização da Ingestão de Novos Livros e Materiais**
  - **Descrição:** Desenvolver um processo robusto e flexível para ingestão contínua de novos documentos (livros, encíclicas, documentos conciliares, escritos de santos, etc.) em diferentes formatos (PDF, EPUB, TXT, HTML). Isso incluirá:
    - Análise e adaptação das ferramentas existentes para lidar com a variedade de formatos e estruturas de documentos.
    - Desenvolvimento de lógicas de "splitting" e extração de metadados configuráveis para cada tipo de material.
    - Criação de um pipeline automatizado para ingestão e indexação desses novos conhecimentos na vector store principal do MariaGPT, garantindo a atualização e expansão contínua da base de conhecimento.
  - **Estimativa:** 60 horas

**Total Estimado para Fase 5:** 225 horas

---

**Total Estimado Geral para Concluir o MVP (Fases 1 a 4):** 78 + 82 + 68 + 83 = **311 horas**

**Observações:**

- As estimativas são para o tempo de _desenvolvimento_. O tempo total do projeto incluirá tempo para planejamento, reuniões, testes adicionais, documentação e possíveis iterações.
- A complexidade de algumas tarefas (e.g., fine-tuning de LLMs, deploy em cloud) pode variar muito.
- A "Conclusão" de uma etapa significa que a funcionalidade está implementada e testada para o propósito atual, não necessariamente "perfeita". Iterações e melhorias podem ocorrer em fases futuras.
