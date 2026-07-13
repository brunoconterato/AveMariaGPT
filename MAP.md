# MAP

Mapa rápido do repositório AveMariaGPT, organizado por finalidade e pelos arquivos atualmente presentes.

## Visão geral

- `data/raw`: fontes originais usadas como base de conhecimento.
- `data/processed`: textos extraídos, normalizados e estruturados para uso posterior.
- `src/01_preprocessing`: conversão de PDFs e ingestão genérica para RAG.
- `src/bible_vectorstore`: estruturação dos versículos e criação do vector store da Bíblia.
- `src/rosarios_quaresma_frei_gilson`: processamento e investigação das transcrições dos rosários.
- `docs`: documentação de notebooks e fluxos específicos.
- `script`: espaço reservado para scripts auxiliares; atualmente não contém arquivos rastreados.

## Arquivos de referência na raiz

- `README.md`: visão geral do projeto, arquitetura RAG, tecnologias e roadmap.
- `features.md`: funcionalidades, status e relação entre os pipelines.
- `roadmap.md`: planejamento de evolução do projeto.
- `TODO.md`: pendências gerais.
- `conda_env.yaml` e `requirements.txt`: dependências do ambiente.
- `Biblia.session.sql`: sessão/exportação SQL auxiliar.
- `all.txt` e `all_code.py`: arquivos auxiliares agregados.

## `data/raw`

### `data/raw/biblia`

- `Ave Maria/`: PDF e texto extraído da Bíblia Ave-Maria.
- Bíblia de Pe. Matos Soares: PDF, EPUB e captura HTML acompanhada de arquivos auxiliares.

### `data/raw/catecismo`

- PDFs do Catecismo da Igreja Católica, incluindo versões duplicadas da fonte.

### `data/raw/missal`

- PDFs do Missal Romano e da Instrução Geral do Missal Romano.

### `data/raw/batismo`

- `Baptismo.pdf`, com conteúdo sacramental sobre o Batismo.

### `data/raw/Notas do Vaticano`

- Documento `Mater Populi fidelis`, sobre títulos marianos e a cooperação de Maria.

### `data/raw/Santo Rosário | Quaresma 2025`

- Transcrições brutas das lives do Frei Gilson durante a Quaresma de 2025.
- `Youtube to Text/`: transcrições principais em `.txt`, incluindo os 40 dias e o show de Páscoa.
- `Youtube Transcript/`: fonte alternativa de transcrição.
- `Tactiq/`: transcrições exportadas do Tactiq.
- `NoteGPT/`: transcrição alternativa do 29º dia.

### `data/raw/Santo Rosário | Sextas feiras normais`

- Transcrição de uma live de sexta-feira fora da Quaresma, em `YouTube To Text/`.

## `data/processed`

### `data/processed/biblia`

- `Ave Maria/Portugues-Catolica-AVM-All-Bible.txt`: texto extraído da Bíblia Ave-Maria.
- `Ave Maria/Portugues-Catolica-AVM-All-Bible-verses.csv`: versículos estruturados com metadados de parsing e revisão.
- `pdf_to_markdown_using_marker-pdf/`: Bíblia de Pe. Matos Soares convertida para Markdown, com `process_log.txt`.
- `bible-from-pdf-using-pdf-to-text.txt`: saída adicional de extração de texto.

### `data/processed/catecismo`

- `pdf_to_markdown_using_marker/`: Catecismo convertido para Markdown nas variantes `WithLLM` e `WithoutLLM`, além do log de processamento.

### `data/processed/Santo Rosário | Quaresma 2025`

- `Youtube to Text/`: análises em Markdown das transcrições processadas.
- Os documentos organizam tema central, subtemas, referências bíblicas, músicas e eventos/intenções mencionados.

## `src/01_preprocessing`

- `pdf_to_markdown_convert_in_batches.sh`: converte PDFs grandes para Markdown em lotes usando `marker_single`.
- `2. Data Ingestion for RAG.ipynb`: divide Markdown em chunks, configura embeddings/LLM via Ollama, cria uma vector store unificada em memória e demonstra o pipeline RAG.
- `README.md`: documentação do fluxo de pré-processamento.

## `src/bible_vectorstore`

- `01_structure_bible_verses.ipynb`: estrutura o texto da Bíblia Ave-Maria em versículos e exporta os dados processados.
- `02_vector_database.ipynb`: cria o vector store persistente e o banco SQLite a partir dos versículos.
- `bible_model.py`: modelos e enumerações para versículos, livros bíblicos e trechos identificados por LLM.
- `biblia.db`: banco SQLite persistido com os versículos e metadados.
- `biblia_vectorstore/`: dados persistidos do ChromaDB.
- `biblia_vectorstore_bkp/`: cópia de segurança do vector store.

### `src/Bíblia VectorStore`

- Diretório legado que ainda contém uma cópia do banco `biblia.db`; o fluxo de desenvolvimento atual está em `src/bible_vectorstore`.

## `src/rosarios_quaresma_frei_gilson`

- `01_preprocessing.ipynb`: notebook de desenvolvimento para limpar transcrições, identificar referências bíblicas e gerar análises estruturadas.
- `utils.py`: enums e utilitários do pipeline, incluindo livros bíblicos e respostas binárias.
- `README.md`: objetivo, metodologia e estrutura esperada das compilações.
- `todo.md`: pendências gerais do pipeline.
- `research-extracao-referencias-biblicas.md`: investigação sobre extração de referências bíblicas.
- `todo-extracao-confiavel-referencias-biblicas.md`: tarefas para tornar a extração confiável.
- `research-artifact-saida-defeituosa.md`: registro de problema em uma saída gerada.

## `docs`

- `docs/bible_vectorstore/01_structure_bible_verses.md`: documentação do notebook de estruturação dos versículos.

## Fluxo resumido

1. Fontes em `data/raw` são extraídas e convertidas pelos scripts ou notebooks de `src/01_preprocessing`.
2. A Bíblia Ave-Maria passa pelo notebook de estruturação e gera o CSV de versículos em `data/processed/biblia/Ave Maria`.
3. O notebook `02_vector_database.ipynb` usa esses versículos para criar o SQLite e o ChromaDB em `src/bible_vectorstore`.
4. A ingestão genérica usa a Bíblia de Pe. Matos Soares e o Catecismo em Markdown para montar uma vector store unificada e demonstrar o RAG.
5. O pipeline de rosários processa as transcrições de Quaresma e produz análises em `data/processed/Santo Rosário | Quaresma 2025`.

## Observações

- As saídas processadas dos rosários são análises em Markdown; as transcrições brutas permanecem em `data/raw`.
- O vector store e o banco SQLite são artefatos gerados, não código-fonte.
- Os notebooks de `src/rosarios_quaresma_frei_gilson` ainda representam um pipeline em desenvolvimento, conforme as pesquisas e listas de tarefas do diretório.
