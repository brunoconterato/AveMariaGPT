# MAP

Mapa rápido do teor das pastas do repositório, com base nos arquivos presentes e nos notebooks/scripts que os processam.

## Visão Geral

- `data/raw`: fontes originais e transcrições brutas.
- `data/processed`: saídas já tratadas, convertidas ou sumarizadas.
- `src`: notebooks, scripts e utilitários que fazem o pré-processamento e a ingestão.

## `data/raw`

### `data/raw/biblia`

- Contém a Bíblia em diferentes formatos de origem.
- `Ave Maria`: PDF e TXT da Bíblia Católica Ave-Maria.
- `Full text of _Bíblia Sagrada O Antigo E Novo Testamento 4 Volumes Vulgata Latina Por Pe. Matos Soares 1927-1950__files`: arquivos auxiliares de uma captura HTML/Internet Archive do texto da Bíblia de Pe. Matos Soares.

### `data/raw/catecismo`

- PDF(s) do Catecismo da Igreja Católica.
- Material-base para consultas teológicas e RAG.

### `data/raw/missal`

- PDFs do Missal Romano e da Instrução Geral do Missal Romano.
- Conteúdo litúrgico e normativo da missa.

### `data/raw/batismo`

- PDF `Baptismo.pdf`.
- Conteúdo sacramental sobre o Batismo.

### `data/raw/Notas do Vaticano`

- Documento do Vaticano sobre títulos marianos e cooperação de Maria.
- Arquivo focado em mariologia e doutrina.

### `data/raw/Santo Rosário | Quaresma 2025`

- Transcrições e fontes variadas das lives do Frei Gilson durante a Quaresma de 2025.
- Subpastas:
  - `Youtube to Text`: transcrições do YouTube em texto puro, organizadas por dia da quaresma.
  - `Youtube Transcript`: outra fonte de transcrição do YouTube, possivelmente em formato original/alternativo.
  - `Tactiq`: transcrições exportadas do Tactiq.
  - `NoteGPT`: uma transcrição/resumo alternativo para ao menos um dia.
- O foco é a análise do Santo Rosário das lives de Quaresma, com conteúdo de oração, reflexão e eventuais músicas/intenções.

### `data/raw/Santo Rosário | Sextas feiras normais`

- Transcrição de lives do Santo Rosário em sextas-feiras comuns, fora da Quaresma.
- Subpasta `YouTube To Text` contém a transcrição bruta em `.txt`.

## `data/processed`

### `data/processed/biblia`

- Saídas já processadas da Bíblia para formatos úteis ao RAG.
- `Ave Maria`: texto limpo/extraído da Bíblia Ave-Maria.
- `pdf_to_markdown_using_marker-pdf`: versão em Markdown da Bíblia de Pe. Matos Soares gerada por conversão automatizada.

### `data/processed/catecismo`

- Versões processadas do Catecismo em Markdown.
- `pdf_to_markdown_using_marker`: saídas geradas a partir do PDF, com variantes como `WithoutLLM` e `WithLLM`.

### `data/processed/Santo Rosário | Quaresma 2025`

- Saídas processadas das transcrições das lives da Quaresma de 2025.
- `Youtube to Text`: arquivos `.md` com resumo/análise produzidos por LLM a partir das transcrições brutas.
- O arquivo processado tenta organizar:
  - temática principal
  - temáticas secundárias
  - versículos bíblicos citados
  - músicas
  - eventos/intenções mencionadas

## `src`

### `src/1. Preprocessing`

- Etapa de pré-processamento da Bíblia e ingestão para RAG.
- `pdf_to_markdown_convert_in_batches.sh`: script de conversão de PDF para Markdown em lotes.
- `2. Data Ingestion for RAG.ipynb`: notebook para dividir/ingerir Markdown em vector store.
- `README.md`: documentação do fluxo de pré-processamento da Bíblia.

### `src/Bíblia VectorStore`

- Construção da base vetorial da Bíblia.
- `1. Format.ipynb`: normalização do texto bíblico e montagem de documentos/versículos.
- `2. Vector database.ipynb`: criação da ChromaDB e do banco SQLite com os versículos.

### `src/Rosários Quaresma Frei Gilson 2025`

- Pipeline de análise das transcrições das lives do Frei Gilson na Quaresma de 2025.
- `1. Preprocessing.ipynb`: notebook principal que:
  - limpa texto
  - detecta possíveis passagens bíblicas
  - envia a transcrição para LLM
  - estrutura a resposta em Markdown
- `utils.py`: enums e utilitários usados no pipeline, incluindo livros bíblicos e respostas binárias.
- `README.md`: visão geral do objetivo da compilação dos ensinamentos do Frei Gilson.
- `todo.md`: checklist de evolução do pipeline e pendências.

## Observações

- A pasta `data/processed/Santo Rosário | Quaresma 2025/Youtube to Text` não contém transcrições brutas, mas sim análises/sínteses geradas a partir delas.
- Em `src/Rosários Quaresma Frei Gilson 2025/1. Preprocessing.ipynb`, o salvamento automático do Markdown está comentado no trecho atual do notebook.
- Os nomes das pastas seguem a origem do conteúdo, então várias classificações acima são inferências confirmadas pelos arquivos internos e pelos notebooks de processamento.
