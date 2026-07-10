# AveMariaGPT: Seu Guia de Inteligência Artificial para a Fé Católica 🕊️

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-FFC107?style=for-the-badge&logo=langchain&logoColor=black)
![LangGraph](https://img.shields.io/badge/LangGraph-2196F3?style=for-the-badge&logo=langchain&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-0366D6?style=for-the-badge&logo=ollama&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-6453A8?style=for-the-badge&logo=chroma&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Progresso-yellow?style=for-the-badge)

## 📖 Sobre o Projeto

O **AveMariaGPT** é um projeto ambicioso que visa criar um agente de Inteligência Artificial conversacional especializado na fé católica. Utilizando a arquitetura **Retrieval-Augmented Generation (RAG)** e modelos de linguagem grandes (LLMs) executados localmente via Ollama, o MariaGPT consulta uma vasta base de conhecimento composta por diferentes versões da Bíblia, o Catecismo da Igreja Católica e, futuramente, transcrições de ensinamentos de líderes religiosos.

Nosso objetivo é fornecer respostas precisas, contextualizadas e teologicamente alinhadas, sempre citando as fontes (versículos bíblicos e passagens do Catecismo) na íntegra.

## ✨ Funcionalidades Principais

As funcionalidades do AveMariaGPT são divididas em categorias, indicando seu status de desenvolvimento:

### 1. Aquisição e Preparação de Dados da Bíblia (Ave Maria)

Esta seção foca na ingestão e formatação de uma versão específica da Bíblia Católica.

- **Extração de Texto de PDF (Bíblia Ave Maria)**
  - **Status:** ✅ Completa.
  - **Descrição:** Extrai texto de PDF para `.txt`, ignorando cabeçalhos/rodapés.
  - **Arquivos:** `src/Bíblia VectorStore/1. Format.ipynb`
- **Limpeza e Normalização de Texto (Bíblia Ave Maria)**
  - **Status:** ✅ Completa.
  - **Descrição:** Remove linhas indesejadas e caracteres de processamento.
  - **Arquivos:** `src/Bíblia VectorStore/1. Format.ipynb`
- **Estruturação de Versículos da Bíblia (Ave Maria)**
  - **Status:** ✅ Completa.
  - **Descrição:** Formata texto bruto em "Livro Capítulo:Versículo Texto do versículo".
  - **Arquivos:** `src/Bíblia VectorStore/1. Format.ipynb`
- **Criação de Vector Store para a Bíblia (Ave Maria)**
  - **Status:** ✅ Completa.
  - **Descrição:** Gera embeddings com `HuggingFaceEmbeddings` e armazena em `ChromaDB`.
  - **Arquivos:** `src/Bíblia VectorStore/2. Vector database.ipynb`
- **Criação de Banco de Dados Relacional para a Bíblia (Ave Maria)**
  - **Status:** ✅ Completa.
  - **Descrição:** Armazena metadados dos versículos em SQLite (`biblia.db`) para recuperação precisa.
  - **Arquivos:** `src/Bíblia VectorStore/2. Vector database.ipynb`

### 2. Aquisição e Preparação de Dados Genéricos (Bíblia Matos Soares & Catecismo)

Foca em uma abordagem mais genérica de processamento de PDFs para Markdown.

- **Conversão de PDF para Markdown em Lotes (`marker-pdf`)**
  - **Status:** ✅ Completa e funcional como script.
  - **Descrição:** Script Bash que usa `marker_single` para converter PDFs grandes para Markdown, evitando estouro de memória e permitindo OCR/análise aprimorados com Ollama.
  - **Arquivos:** `src/1. Preprocessing/pdf_to_markdown_convert_in_batches.sh`
- **Quebra de Texto Estruturado (Markdown Header Splitter)**
  - **Status:** ✅ Completa.
  - **Descrição:** Divide textos Markdown em "chunks" baseados em cabeçalhos, mantendo o contexto estrutural para o RAG.
  - **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb`
- **Setup de Modelos de Embedding e LLM com Ollama**
  - **Status:** ✅ Completa.
  - **Descrição:** Configura e verifica a instalação de modelos LLM e Embedding no Ollama.
  - **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb`
- **Criação de Vector Store Unificada (Bíblia Matos Soares e Catecismo)**
  - **Status:** ✅ Completa (em memória).
  - **Descrição:** Inicializa uma `InMemoryVectorStore` (com `OllamaEmbeddings`) e adiciona documentos processados da Bíblia Matos Soares e do Catecismo.
  - **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb`

### 3. Agente Conversacional (RAG)

A funcionalidade central do MariaGPT.

- **Engenharia de Prompt para Agente Católico**
  - **Status:** ✅ Completa (definição do prompt).
  - **Descrição:** Define `SYSTEM_TEMPLATE` e `RAG_TEMPLATE` para instruir o LLM a atuar como um assistente católico, citando passagens bíblicas e do catecismo na íntegra, com referências, e respondendo em português brasileiro.
  - **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb`
- **Orquestração de RAG com LangGraph (Pipeline Principal)**
  - **Status:** ✅ Funcional e em demonstração.
  - **Descrição:** Implementa um pipeline de RAG com LangGraph (`analyze_query`, `retrieve`, `generate`) para processar e responder perguntas.
  - **Arquivos:** `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb`

### 4. Generalização da Ingestão de Conhecimento

Permite a adição contínua de novos materiais.

- **Processo de Ingestão de Novos Materiais**
  - **Status:** 🚧 Em progresso (conceitual, baseando-se em ferramentas existentes).
  - **Descrição:** Define e refina o processo para converter novos documentos em formato estruturado (Markdown), extrair conteúdos e metadados, e indexá-los no vector store principal.
  - **Arquivos:** `src/1. Preprocessing/process_pdf_batches.sh`, `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb` (bases)

### 5. Processamento de Conteúdo Específico (Lives do Frei Gilson)

Processamento de transcrições de lives católicas para extrair ensinamentos.

- **Detecção de Passagens Bíblicas em Texto Arbitrário**
  - **Status:** 🚧 Em progresso (funcionalidade testada, mas não totalmente integrada).
  - **Descrição:** Módulo que usa `ChromaDB` da Bíblia e LLM para identificar referências bíblicas em transcrições.
  - **Arquivos:** `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb`
- **Sumarização e Extração de Informações de Transcrições de Lives (Santo Rosário)**
  - **Status:** 🚧 Em progresso.
  - **Descrição:** Define um `system_message` para LLM extrair temáticas, versículos, músicas e agenda de transcrições de lives do Frei Gilson.
  - **Arquivos:** `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb`

## ⚙️ Como Funciona (Visão Geral)

O AveMariaGPT opera com base em um pipeline RAG sofisticado:

1.  **Preparação de Dados:** Documentos católicos (Bíblia, Catecismo, Lives do Frei Gilson) são extraídos de PDFs, limpos, normalizados e estruturados (muitas vezes em Markdown).
2.  **Geração de Embeddings:** Os textos estruturados são convertidos em representações numéricas (embeddings) usando modelos de embedding (e.g., `mxbai-embed-large` via Ollama ou `sentence-transformers/all-MiniLM-L6-v2`).
3.  **Armazenamento em Vector Store:** Esses embeddings são armazenados em uma base de dados vetorial (`ChromaDB` para dados persistentes, `InMemoryVectorStore` para testes) e, para a Bíblia Ave Maria, também em um banco de dados relacional (`SQLite`) para metadados e recuperação precisa.
4.  **Orquestração RAG (LangGraph):**
    - **Análise da Query:** A pergunta do usuário é analisada e decomposta em sub-perguntas se for complexa.
    - **Recuperação de Contexto (Retrieval):** Documentos relevantes são recuperados da vector store unificada com base nas (sub)perguntas.
    - **Geração de Resposta (Generation):** Um LLM (e.g., `gemma3:12b` ou `llama3.1:8b` via Ollama) recebe o contexto recuperado e a pergunta do usuário. Guiado por prompts cuidadosamente elaborados, o LLM gera uma resposta precisa, teologicamente alinhada, em português brasileiro, e com citações completas das fontes.

## 🚀 Roadmap do Projeto

O projeto está dividido em fases claras para garantir um desenvolvimento estruturado:

- **Fase 0: Fundação e Ingestão de Dados Iniciais (Concluída ✅)**
  - Instalação e Configuração do Ollama, pré-processamento e estruturação das Bíblias (Ave Maria e Matos Soares), Catecismo, e criação das Vector Stores iniciais (ChromaDB e In-Memory). Definição inicial dos prompts do agente RAG.

- **Fase 1: Processamento Detalhado das Lives do Frei Gilson (Prioridade Atual 🚧)**
  - **Objetivo:** Concluir a extração de conhecimento das transcrições das lives, tornando-as uma fonte de dados valiosa.
  - **Etapas Principais:** Aprimorar a detecção de versículos bíblicos, refinar prompts para sumarização e extração de ensinamentos, implementar pipeline de processamento em lotes e integrar o conhecimento das lives ao vector store principal.
  - **Estimativa:** 78 horas

- **Fase 2: Refinamento e Otimização do Agente Conversacional Core (MariaGPT) (A Seguir ⏳)**
  - **Objetivo:** Otimizar o coração do MariaGPT.
  - **Etapas Principais:** Substituir `InMemoryVectorStore` por uma persistente (ChromaDB/FAISS), melhorar o módulo retriever (MultiQuery, Compressão), validar e ajustar prompts finais, implementar gerenciamento de memória conversacional, e desenvolver testes de qualidade.
  - **Estimativa:** 82 horas

- **Fase 3: Desenvolvimento do Front-end (Interface do Chatbot) (A Seguir ⏳)**
  - **Objetivo:** Criar a interface de usuário para interação com o MariaGPT.
  - **Etapas Principais:** Escolher e configurar a stack de front-end (React/Next.js/HTML/CSS), criar API REST (Flask/FastAPI) para comunicação e implementar a lógica e UI do chatbot.
  - **Estimativa:** 68 horas

- **Fase 4: Deploy e Testes com Usuários (A Seguir ⏳)**
  - **Objetivo:** Disponibilizar o MariaGPT para uso e coletar feedback.
  - **Etapas Principais:** Containerização do backend (Dockerfile), orquestração com Docker Compose, testes finais em ambiente local, e opcionalmente, configuração de serviço de hospedagem e testes com usuários.
  - **Estimativa:** 83 horas

- **Fase 5: Melhorias Futuras (Versão 2.0) (Longo Prazo 💡)**
  - **Objetivo:** Expandir as capacidades do MariaGPT.
  - **Ideias:** Suporte a voz (STT+TTS), resumos automáticos, modo devocional (leituras diárias/orações), exploração de modelos fine-tuned com corpus católico, e generalização da ingestão de novos materiais (EPUB, TXT, HTML).
  - **Estimativa:** 225 horas

**Total Estimado para Concluir o MVP (Fases 1 a 4): ~311 horas.**

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python (3.9+)
- **Orquestração de LLMs:** LangChain, LangGraph
- **LLMs e Embeddings Locais:** Ollama (`gemma3:12b`, `llama3.1:8b-instruct-q5_K_M`, `mxbai-embed-large:latest`)
- **Bases Vetoriais:** ChromaDB (persistente), InMemoryVectorStore (para testes)
- **Banco de Dados Relacional:** SQLite
- **Processamento de PDFs:** `pdfplumber`, `marker-pdf` (`marker_single`)
- **Processamento de Texto:** `langchain-text-splitters` (MarkdownHeaderTextSplitter, CharacterTextSplitter)
- **Gerenciamento de Ambiente:** `conda`, `pip`
- **Utilitários:** `python-dotenv`, `tqdm`, `rich`, `pydantic`
- **Scripting:** Bash

## 🚀 Primeiros Passos e Como Usar

Para configurar e executar o AveMariaGPT, siga estas etapas:

### Pré-requisitos

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/AveMariaGPT.git # Substitua pelo link real do seu repo
    cd AveMariaGPT
    ```
2.  **Crie e Ative o Ambiente Virtual (recomendado):**
    ```bash
    conda create -n mariagpt python=3.9 -y
    conda activate mariagpt
    ```
    Ou com `venv`:
    ```bash
    python3.9 -m venv .venv
    source .venv/bin/activate
    ```
3.  **Instale as Dependências Python:**
    ```bash
    pip install langchain-ollama langchain-chroma langchain-huggingface langchain-core langchain-text-splitters langchain-community langgraph python-dotenv pydantic rich tqdm pdfplumber unstructured
    pip install marker-pdf # Para a conversão de PDF para Markdown
    ```
4.  **Instale `poppler-utils` (para `pdfinfo`):**
    ```bash
    # No Ubuntu/Debian
    sudo apt update
    sudo apt install poppler-utils
    # No macOS com Homebrew
    brew install poppler
    ```
5.  **Instale e Configure o Ollama:**
    Baixe e instale o Ollama em [ollama.ai](https://ollama.ai/). Após a instalação, puxe os modelos necessários:
    ```bash
    ollama pull gemma3:12b
    ollama pull mxbai-embed-large:latest
    ollama pull llama3.1:8b-instruct-q5_K_M
    # E qualquer outro modelo LLM que você pretenda testar
    ```
6.  **Organize os Dados Brutos:**
    Certifique-se de que seus arquivos PDF da Bíblia (Ave Maria e Matos Soares) e do Catecismo estão nas pastas `data/raw/biblia/Ave Maria/`, `data/raw/biblia/` e `data/raw/catecismo/`, respectivamente, conforme as variáveis de caminho nos notebooks.

### Ordem de Execução das Funcionalidades

As funcionalidades devem ser executadas em uma ordem específica para preparar a base de conhecimento e o agente RAG:

1.  **Preparação da Bíblia Matos Soares e Catecismo (PDF para Markdown):**
    - Navegue até o diretório do script:
      ```bash
      cd src/1.\ Preprocessing
      ```
    - Dê permissão de execução ao script:
      ```bash
      chmod +x pdf_to_markdown_convert_in_batches.sh
      ```
    - Execute o script para converter os PDFs para Markdown. **Ajuste os caminhos conforme a localização dos seus arquivos:**

      ```bash
      # Exemplo para Bíblia Matos Soares (ajuste o nome do arquivo conforme o seu)
      bash pdf_to_markdown_convert_in_batches.sh ../../data/raw/biblia/"Bíblia Sagrada O Antigo e Novo Testamento - 4 volumes - Vulgata Latina por Pe. Matos Soares 1927-1950.pdf" 100 ../../data/processed/biblia/pdf_to_markdown_using_marker-pdf true

      # Exemplo para Catecismo (ajuste o nome do arquivo conforme o seu)
      bash pdf_to_markdown_convert_in_batches.sh ../../data/raw/catecismo/"Catecismo da Igreja Católica.pdf" 50 ../../data/processed/catecismo/pdf_to_markdown_using_marker true
      ```

    - _Volte para o diretório raiz do projeto para os próximos passos baseados em notebooks:_
      ```bash
      cd ../../
      ```

2.  **Preparação da Bíblia Ave Maria e Vector Store Dedicada:**
    - Abra e execute as células do notebook:
      `src/Bíblia VectorStore/1. Format.ipynb` (para extração, limpeza e estruturação da Bíblia Ave Maria).
    - Em seguida, execute o notebook:
      `src/Bíblia VectorStore/2. Vector database.ipynb` (para criar o `ChromaDB` dedicado (`biblia_vectorstore`) e o `SQLite` (`biblia.db`)).

3.  **Construção do Agente RAG Principal (Unificação de Conhecimento):**
    - Abra e execute todas as células do notebook:
      `src/1. Preprocessing/2. Data Ingestion for RAG.ipynb`
      Este notebook:
      - Usa os arquivos Markdown da Bíblia Matos Soares e do Catecismo (gerados no passo 1).
      - Divide o texto em chunks estruturados.
      - Configura os modelos Ollama (LLM e Embeddings).
      - Cria uma **vector store unificada (em memória neste notebook)** contendo ambos os corpos de texto.
      - Constrói e demonstra o pipeline de RAG com LangGraph.
    - **Após a execução deste notebook, o pipeline RAG estará pronto para demonstração de perguntas.**

4.  **Processamento das Transcrições das Lives (Funcionalidade Secundária/Especializada):**
    - Abra e execute as células do notebook:
      `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb`
      Este notebook:
      - Reutiliza a `biblia_vectorstore` para detecção de versículos.
      - Está em progresso para sumarização e extração de informações das lives do Frei Gilson.
      - Contém um `assert False` em uma célula de loop, que deve ser removido para processar todos os arquivos quando a lógica estiver finalizada.

## 🤝 Como Contribuir

Ficou interessado em colaborar? Seja bem-vindo(a)! Siga estas etapas:

1.  Faça um fork do projeto.
2.  Crie uma nova branch (`git checkout -b feature/sua-feature`).
3.  Faça suas alterações e commit-as (`git commit -m 'feat: adicione sua nova feature'`).
4.  Envie suas alterações para o seu fork (`git push origin feature/sua-feature`).
5.  Abra um Pull Request descrevendo suas mudanças.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

Para dúvidas ou sugestões, entre em contato com o autor:

- **Bruno Conterato** - [Seu Perfil do GitHub](https://github.com/brunoconterato)
- **Email:** [seu.email@example.com](mailto:seu.email@example.com)

---

🙏 **Deus abençoe seu trabalho e sua jornada na fé!** 🙏
