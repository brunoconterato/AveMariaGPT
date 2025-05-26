## Mapeamento de Funcionalidades

As funcionalidades são categorizadas abaixo com base em seu propósito, e cada uma delas indica seu status (completa, em progresso) e os arquivos de código relevantes.

### 1. Aquisição e Preparação de Dados da Bíblia (Ave Maria)

Esta seção lida com a ingestão e formatação de uma versão específica da Bíblia Católica.

*   **Extração de Texto de PDF (Bíblia Ave Maria)**
    *   **Status:** Completa para a versão específica.
    *   **Descrição:** Extrai o texto de um arquivo PDF (`.pdf`) da Bíblia (Ave Maria) para um arquivo de texto limpo (`.txt`). Ignora páginas de cabeçalho/rodapé e corta páginas finais irrelevantes.
    *   **Arquivos:** `src/Bíblia VectorStore/1. Format.ipynb` (célula `9530d1fc`)

*   **Limpeza e Normalização de Texto (Bíblia Ave Maria)**
    *   **Status:** Completa para a versão específica.
    *   **Descrição:** Remove linhas indesejadas (cabeçalhos, direitos autorais) e outros caracteres que podem atrapalhar o processamento.
    *   **Arquivos:** `src/Bíblia VectorStore/1. Format.ipynb` (células `399f989b`, `13d68cc0`)

*   **Estruturação de Versículos da Bíblia (Ave Maria)**
    *   **Status:** Completa para a versão específica.
    *   **Descrição:** Transforma o texto bruto da Bíblia em um formato linha-a-linha, onde cada linha representa um versículo formatado como "Livro Capítulo:Versículo Texto do versículo".
    *   **Arquivos:** `src/Bíblia VectorStore/1. Format.ipynb` (célula `5ec25d1d`)

*   **Criação de Vector Store para a Bíblia (Ave Maria)**
    *   **Status:** Completa.
    *   **Descrição:** Converte os versículos estruturados da Bíblia em documentos (`langchain.schema.Document`), gera embeddings usando `HuggingFaceEmbeddings` (`sentence-transformers/all-MiniLM-L6-v2`) e os armazena em uma base vetorial `ChromaDB`.
    *   **Arquivos:** `src/Bíblia VectorStore/2. Vector database.ipynb` (células `a111732f`, `92a78804`)

*   **Criação de Banco de Dados Relacional para a Bíblia (Ave Maria)**
    *   **Status:** Completa.
    *   **Descrição:** Além do vector store, cria um banco de dados SQLite (`biblia.db`) para armazenar os metadados dos versículos (livro, capítulo, versículo, texto, número da linha), o que pode ser útil para recuperação precisa ou navegação.
    *   **Arquivos:** `src/Bíblia VectorStore/2. Vector database.ipynb` (célula `a80d317d`)

### 2. Aquisição e Preparação de Dados Genéricos (Matos Soares Bible & Catechism)

Esta seção foca em uma abordagem mais genérica de processamento de PDFs para Markdown, utilizada para a Bíblia Matos Soares e o Catecismo.

*   **Conversão de PDF para Markdown em Lotes (`marker-pdf`)**
    *   **Status:** Completa e funcional como script.
    *   **Descrição:** Um script Bash que utiliza a ferramenta `marker_single` para converter PDFs grandes para Markdown em lotes, prevenindo estouro de memória e permitindo a integração opcional com Ollama para OCR/análise de layout aprimorados.
    *   **Arquivos:** `src/1. Preprocessing/process_pdf_batches.sh`
    *   **Documentação:** `src/1. Preprocessing/README.md`

*   **Quebra de Texto Estruturado (Markdown Header Splitter)**
    *   **Status:** Completa.
    *   **Descrição:** Divide os textos Markdown (Bíblia Matos Soares e Catecismo) em "chunks" menores baseados em cabeçalhos (ex: `#`, `##`, `####`), mantendo o contexto estrutural. Isso é crucial para o RAG.
    *   **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (células `399f989b`, `13d68cc0`)

*   **Setup de Modelos de Embedding e LLM com Ollama**
    *   **Status:** Completa.
    *   **Descrição:** Configura e verifica a instalação de modelos de LLM e Embedding no Ollama (ex: `gemma3:12b` para LLM, `mxbai-embed-large:latest` para embeddings), puxando-os se necessário.
    *   **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (células `d61c542a`, `e724bf19`)

*   **Criação de Vector Store Unificada (Bíblia e Catecismo)**
    *   **Status:** Completa.
    *   **Descrição:** Inicializa uma `InMemoryVectorStore` (usando `OllamaEmbeddings`) e adiciona os documentos processados tanto da Bíblia Matos Soares quanto do Catecismo, criando uma base de conhecimento combinada para o RAG.
    *   **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (células `399f989b`, `13d68cc0`)

### 3. Agente Conversacional (RAG)

Esta é a funcionalidade central do MariaGPT, utilizando os dados preparados.

*   **Engenharia de Prompt para Agente Católico**
    *   **Status:** Completa (definição do prompt).
    *   **Descrição:** Define um `SYSTEM_TEMPLATE` detalhado e um `RAG_TEMPLATE` que instruem o LLM a atuar como um assistente católico, citando passagens bíblicas e ensinamentos do catecismo na íntegra, com referências, e respondendo em português brasileiro de forma educada e respeitosa.
    *   **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (célula `e724bf19`)

*   **Orquestração de RAG com LangGraph (Pipeline Principal)**
    *   **Status:** Funcional e em demonstração.
    *   **Descrição:** Implementa um pipeline de RAG usando `LangGraph` com três etapas principais:
        1.  `analyze_query`: Decompõe a pergunta do usuário em sub-perguntas se for complexa.
        2.  `retrieve`: Recupera documentos relevantes da vector store unificada para as (sub)perguntas.
        3.  `generate`: Gera a resposta final usando o LLM e o contexto recuperado, seguindo as instruções do prompt.
    *   **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (células `a111732f`, `a80d317d`, `bb4a367b`)

### 4. Processamento de Conteúdo Específico (Lives do Frei Gilson)

Esta seção visa processar transcrições de lives católicas para extrair ensinamentos.

*   **Detecção de Passagens Bíblicas em Texto Arbitrário**
    *   **Status:** Em progresso (funcionalidade testada, mas não totalmente integrada ao fluxo principal de summarização).
    *   **Descrição:** Um módulo que utiliza a `ChromaDB` da Bíblia (construída no `src/Bíblia VectorStore/2. Vector database.ipynb`) e um LLM para identificar se trechos de texto (e.g., de uma transcrição) contêm referências ou citações bíblicas, e qual versículo específico é.
    *   **Arquivos:** `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb` (células `c9acb7d2`, `fb19f6be`)

*   **Sumarização e Extração de Informações de Transcrições de Lives (Santo Rosário)**
    *   **Status:** Em progresso.
    *   **Descrição:** Define um `system_message` complexo para um LLM extrair temáticas, versículos citados, músicas e eventos de agenda de transcrições de lives do Frei Gilson, focando apenas na parte do Santo Rosário. A implementação no notebook está pausada (`assert False`, `break`).
    *   **Arquivos:** `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb` (células `75aa5ce7`, `e724bf19`, `2240fa7d`)
    *   **Documentação:** `src/Rosários Quaresma Frei Gilson 2025/README.md`

## Relação entre as Funcionalidades e Ordem de Execução

As funcionalidades se interligam para construir o agente RAG e para processar conteúdo específico. A ordem de execução é crucial para a preparação dos dados que alimentam os modelos.

1.  **Preparação da Bíblia Matos Soares e Catecismo:**
    *   Primeiro, o script `src/1. Preprocessing/process_pdf_batches.sh` (ou um processo similar) deve ser executado para converter os PDFs da **Bíblia Sagrada O Antigo e Novo Testamento - Vulgata Latina por Pe. Matos Soares** e do **Catecismo da Igreja Católica** para o formato Markdown. Estes são os arquivos de entrada para a etapa de ingestão do RAG principal.
    *   **Dependência:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` depende dos arquivos Markdown gerados por `src/1. Preprocessing/process_pdf_batches.sh`.

2.  **Preparação da Bíblia Ave Maria e Vector Store Dedicada:**
    *   Em paralelo (ou como uma alternativa/complemento ao Matos Soares), `src/Bíblia VectorStore/1. Format.ipynb` pode ser executado para extrair, limpar e estruturar a Bíblia Ave Maria.
    *   Em seguida, `src/Bíblia VectorStore/2. Vector database.ipynb` utiliza o output do passo anterior para criar um **vector store `ChromaDB` dedicado à Bíblia Ave Maria** (`biblia_vectorstore`) e um banco de dados SQLite (`biblia.db`).
    *   **Dependência:** `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb` (funcionalidade de detecção de passagens bíblicas) depende diretamente do `biblia_vectorstore` criado aqui.

3.  **Construção do Agente RAG Principal:**
    *   `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` é o coração do setup do RAG. Ele usa os arquivos Markdown da Bíblia Matos Soares e do Catecismo (resultantes do passo 1) para:
        *   Dividir o texto em chunks estruturados.
        *   Configurar os modelos Ollama (LLM e Embeddings).
        *   Criar uma **vector store unificada (em memória neste notebook)** contendo *ambos* os corpos de texto.
        *   Construir e demonstrar o pipeline de RAG com LangGraph (análise de query, recuperação de contexto, geração de resposta).
    *   **Dependência:** Esta é a etapa final para que o agente RAG possa receber perguntas e gerar respostas com base nos dados preparados. O **agente conversacional do projeto MariaGPT** (mencionado no `todo.md`) dependerá deste pipeline.

4.  **Processamento das Transcrições das Lives (Funcionalidade Secundária/Especializada):**
    *   `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb` é um notebook de desenvolvimento para processar transcrições de lives específicas.
    *   Ele *reutiliza* a `biblia_vectorstore` criada em `src/Bíblia VectorStore/2. Vector database.ipynb` para a detecção de versículos.
    *   A sumarização e extração de informações das lives é uma funcionalidade paralela ao agente conversacional principal, mas que visa enriquecer o conhecimento sobre os ensinamentos do Frei Gilson.
    *   **Não é uma dependência direta** para o funcionamento do agente RAG principal, mas é uma funcionalidade que agrega valor ao projeto.
