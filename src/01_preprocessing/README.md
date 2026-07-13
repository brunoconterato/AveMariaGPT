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
│   │   └── biblia
│   │       ├── pdf_to_markdown_using_marker-pdf
│   │       │   ├── Bíblia Sagrada O Antigo e Novo Testamento - 4 volumes - Vulgata Latina por Pe. Matos Soares 1927-1950.md
│   │       │   └── process_log.txt
│   └── raw
│       ├── biblia
│       │   ├── Bíblia Sagrada O Antigo e Novo Testamento - 4 volumes - Vulgata Latina por Pe. Matos Soares 1927-1950.pdf
│       │   └── ...
├── src
│   └── 1. Preprocessing
│       ├── pdf_to_markdown_convert_in_batches.sh
│       ├── 1. Preprocessing.ipynb
│       └── README.md
└── ...
```

### Explicação da Estrutura

- **`data`**: Diretório principal para armazenar os dados do projeto.

  - **`raw`**: Contém os arquivos originais, como PDFs, que ainda não foram processados.
    - **`biblia`**: Subdiretório específico para armazenar os arquivos da Bíblia em formato PDF.
  - **`processed`**: Contém os dados que já passaram por algum tipo de processamento.
    - **`biblia`**: Subdiretório para armazenar os resultados do processamento da Bíblia.
      - **`pdf_to_markdown_using_marker-pdf`**: Diretório onde os arquivos Markdown gerados e os logs do processamento são salvos.
        - **`Bíblia Sagrada O Antigo e Novo Testamento...md`**: Arquivo consolidado em formato Markdown contendo o conteúdo do PDF.
        - **`process_log.txt`**: Arquivo de log detalhando o processo de conversão.

- **`src`**: Diretório contendo os scripts e notebooks relacionados ao pré-processamento.

  - **`1. Preprocessing`**: Subdiretório específico para a etapa de pré-processamento.
    - **`pdf_to_markdown_convert_in_batches.sh`**: Script Bash para processar o PDF em lotes e convertê-lo para Markdown.
    - **`1. Preprocessing.ipynb`**: Notebook Jupyter para análises e testes relacionados ao pré-processamento.
    - **`README.md`**: Documento explicativo sobre a etapa de pré-processamento.

- **`...`**: Representa outros diretórios e arquivos que não são diretamente relevantes para esta etapa.

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

## Movendo-se para a Pasta Correta no Terminal

Para executar o script `pdf_to_markdown_convert_in_batches.sh`, é necessário navegar até o diretório correto no terminal. Utilize o seguinte comando:

```bash
cd src/1.\ Preprocessing
```

## Configuração de Permissões

Antes de executar o script `pdf_to_markdown_convert_in_batches.sh`, é necessário garantir que ele tenha permissões de execução. Para isso, utilize o comando `chmod`:

```bash
chmod +x pdf_to_markdown_convert_in_batches.sh
```

### Explicação

- **`chmod +x`**: Adiciona permissão de execução ao arquivo.
- **`pdf_to_markdown_convert_in_batches.sh`**: Nome do script que será configurado.

Esse passo é essencial para evitar erros de permissão ao tentar executar o script.

---

## Explicação do Script `pdf_to_markdown_convert_in_batches.sh`

O script `pdf_to_markdown_convert_in_batches.sh` processa o PDF em lotes (batches) para evitar estouro de memória. Ele utiliza o `marker_single` (parte do `marker-pdf`) para converter páginas específicas do PDF em arquivos Markdown.

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

## Uso do Ollama no Script `pdf_to_markdown_convert_in_batches.sh`

O script `pdf_to_markdown_convert_in_batches.sh` suporta o uso do **Ollama**, um serviço de LLM (Large Language Model) que melhora a qualidade do processamento de PDFs. O Ollama pode ser habilitado ou desabilitado, e o modelo utilizado pode ser configurado diretamente ao chamar o script.

### Parâmetros Relacionados ao Ollama

- **`USE_OLLAMA`**: Define se o Ollama será utilizado durante o processamento.
  - Valores possíveis:
    - `true`: Habilita o uso do Ollama.
    - `false`: Desabilita o uso do Ollama (padrão).
- **`OLLAMA_MODEL`**: Nome do modelo Ollama a ser utilizado.
  - Valor padrão: `"deepseek-r1:8b"`.

### Como Configurar o Uso do Ollama

Ao executar o script, você pode passar os valores para `USE_OLLAMA` e `OLLAMA_MODEL` como o quarto e quinto parâmetros, respectivamente. Por exemplo:

#### Exemplo 1: Habilitar o Ollama com o modelo padrão

```bash
bash pdf_to_markdown_convert_in_batches.sh ../../data/raw/biblia/Bíblia\ Sagrada\ O\ Antigo\ e\ Novo\ Testamento\ -\ 4\ volumes\ -\ Vulgata\ Latina\ por\ Pe.\ Matos\ Soares\ 1927-1950.pdf 100 ../../data/processed/biblia/pdf_to_markdown_using_marker-pdf true
```

#### Exemplo 2: Habilitar o Ollama com um modelo personalizado

```bash
bash pdf_to_markdown_convert_in_batches.sh ../../data/raw/biblia/Bíblia\ Sagrada\ O\ Antigo\ e\ Novo\ Testamento\ -\ 4\ volumes\ -\ Vulgata\ Latina\ por\ Pe.\ Matos\ Soares\ 1927-1950.pdf 100 ../../data/processed/biblia/pdf_to_markdown_using_marker-pdf true custom-model-name
```

#### Exemplo 3: Desabilitar o Ollama

```bash
bash pdf_to_markdown_convert_in_batches.sh ../../data/raw/biblia/Bíblia\ Sagrada\ O\ Antigo\ e\ Novo\ Testamento\ -\ 4\ volumes\ -\ Vulgata\ Latina\ por\ Pe.\ Matos\ Soares\ 1927-1950.pdf 100 ../../data/processed/biblia/pdf_to_markdown_using_marker-pdf false
```

### Vantagens do Uso do Ollama

- **Melhoria na Qualidade**: O Ollama utiliza modelos avançados para realizar OCR e análise de layout, resultando em uma conversão mais precisa e estruturada.
- **Configuração Flexível**: Permite escolher o modelo mais adequado para o tipo de documento sendo processado.
- **Processamento Avançado**: Habilita recursos como extração de tabelas e imagens com maior precisão.

### Considerações

- Certifique-se de que o serviço Ollama está configurado e acessível antes de habilitá-lo no script.
- O uso do Ollama pode aumentar o tempo de processamento, dependendo do modelo escolhido e do tamanho do PDF.

---

## Exemplo de Uso

Para processar o PDF da Bíblia em lotes de 50 páginas, sem utilizar o Ollama, execute o seguinte comando:

```bash
bash pdf_to_markdown_convert_in_batches.sh ../../data/raw/biblia/Bíblia\ Sagrada\ O\ Antigo\ e\ Novo\ Testamento\ -\ 4\ volumes\ -\ Vulgata\ Latina\ por\ Pe.\ Matos\ Soares\ 1927-1950.pdf 100 ../../data/processed/biblia/pdf_to_markdown_using_marker-pdf
```

### Explicação

- **`../../data/raw/biblia/Bíblia\ Sagrada...pdf`**: Caminho para o PDF da Bíblia.
- **`100`**: Tamanho do lote (100 páginas por vez).
- **`../../data/processed/biblia/pdf_to_markdown_using_marker-pdf`**: Diretório onde os arquivos Markdown e logs serão salvos.

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

A etapa de pré-processamento é fundamental para transformar o conteúdo da Bíblia em um formato adequado para o agente RAG. Com o uso do `marker-pdf` e do script `pdf_to_markdown_convert_in_batches.sh`, é possível realizar essa conversão de forma eficiente e organizada.
