# Etapa de Pré-Processamento

## Objetivo

O objetivo desta etapa é converter a **Bíblia Sagrada - O Antigo e Novo Testamento - 4 volumes - Vulgata Latina por Pe. Matos Soares (1927-1950)**, disponível em formato PDF, para o formato Markdown. Essa conversão é essencial para o desenvolvimento de um agente **RAG (Retrieval-Augmented Generation)** católico, que utilizará a Bíblia como referência principal.

A estrutura em Markdown facilita a manipulação, indexação e consulta do texto, permitindo que o agente acesse informações de forma eficiente.

---

## Estrutura de Pastas

A estrutura atual do projeto, com foco nos arquivos essenciais à etapa de pré-processamento, é a seguinte:

```
├── data
│   ├── processed
│   │   └── bible-from-pdf-using-pdf-to-text.txt
│   └── raw
│       ├── biblia
│       │   ├── Bíblia Sagrada O Antigo e Novo Testamento - 4 volumes - Vulgata Latina por Pe. Matos Soares 1927-1950.pdf
│       │   ├── pdf_to_markdown_output
│       |   ├── combined_output.md
│       |   └── process_log.txt
│       └── ...
├── src
│   └── 1. Preprocessing
│       ├── process_pdf_batches.sh
│       └── README.md
|       ├── ...
└── ...
```

---

## Pré-Requisitos

Antes de executar o script de pré-processamento, é necessário instalar algumas dependências:

### 1. Instalar o `marker-pdf`

O `marker-pdf` é uma biblioteca Python utilizada para processar arquivos PDF e convertê-los para Markdown. Para instalá-la, siga os passos abaixo:

#### Usando Anaconda:
```bash
conda create -n maria-gpt python=3.9 -y
conda activate maria-gpt
pip install marker-pdf
```

#### Alternativamente, usando `pip` diretamente:
```bash
pip install marker-pdf
```

### 2. Instalar o `poppler-utils`

O script utiliza o comando `pdfinfo` para obter informações sobre o PDF. Certifique-se de que o `poppler-utils` está instalado:

#### No Ubuntu/Debian:
```bash
sudo apt update
sudo apt install poppler-utils
```

---

## Configuração de Permissões

Antes de executar o script `process_pdf_batches.sh`, é necessário garantir que ele tenha permissões de execução. Para isso, utilize o comando `chmod`:

```bash
chmod +x process_pdf_batches.sh
```

### Explicação

- **`chmod +x`**: Adiciona permissão de execução ao arquivo.
- **`process_pdf_batches.sh`**: Nome do script que será configurado.

Esse passo é essencial para evitar erros de permissão ao tentar executar o script.

---

## Explicação do Script `process_pdf_batches.sh`

O script `process_pdf_batches.sh` processa o PDF em lotes (batches) para evitar estouro de memória. Ele utiliza o `marker_single` (parte do `marker-pdf`) para converter páginas específicas do PDF em arquivos Markdown.

### Parâmetros do Script

- **`PDF_FILE`**: Caminho para o arquivo PDF a ser processado.
- **`BATCH_SIZE`**: Número de páginas por lote (padrão: 10).
- **`OUTPUT_DIR`**: Diretório de saída para os arquivos gerados (padrão: `output`).

### Fluxo de Execução

1. Validações iniciais:
   - Verifica se o arquivo PDF existe.
   - Confirma se o `marker_single` e `pdfinfo` estão instalados.
2. Obtém o número total de páginas do PDF.
3. Processa o PDF em lotes, gerando arquivos Markdown para cada intervalo de páginas.
4. Combina os arquivos Markdown em um único arquivo (`combined_output.md`).

---

## Exemplo de Uso

Para processar o PDF da Bíblia em lotes de 50 páginas, execute o seguinte comando:

```bash
bash process_pdf_batches.sh \
    ../data/raw/biblia/Bíblia\ Sagrada\ O\ Antigo\ e\ Novo\ Testamento\ -\ 4\ volumes\ -\ Vulgata\ Latina\ por\ Pe.\ Matos\ Soares\ 1927-1950.pdf \
    50 \
    ../data/raw/biblia/pdf_to_markdown_output
```

### Explicação

- **`../data/raw/biblia/Bíblia Sagrada...pdf`**: Caminho para o PDF da Bíblia.
- **`50`**: Tamanho do lote (50 páginas por vez).
- **`../data/raw/biblia/pdf_to_markdown_output`**: Diretório onde os arquivos Markdown e logs serão salvos.

---

## Benefícios do Processamento em Lotes

O processamento em lotes evita o consumo excessivo de memória, especialmente para arquivos PDF grandes como a Bíblia. Isso garante que o script possa ser executado em máquinas com recursos limitados.

---

## Saída Esperada

Após a execução do script, os seguintes arquivos serão gerados no diretório de saída:

- **`combined_output.md`**: Arquivo Markdown consolidado com todo o conteúdo do PDF.
- **`process_log.txt`**: Log detalhado do processamento.

---

## Conclusão

A etapa de pré-processamento é fundamental para transformar o conteúdo da Bíblia em um formato adequado para o agente RAG. Com o uso do `marker-pdf` e do script `process_pdf_batches.sh`, é possível realizar essa conversão de forma eficiente e organizada.