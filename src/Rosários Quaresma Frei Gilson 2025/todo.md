# TODO - Pré-processamento das Lives do Frei Gilson

Este arquivo detalha as tarefas para o pré-processamento e análise das transcrições das lives do Frei Gilson, conforme implementado no notebook `1. Preprocessing.ipynb`.

## 1. Configuração e Ambiente

- [x] Importar bibliotecas essenciais (langchain, dotenv, etc.)
- [x] Implementar seleção de modelo de LLM e provedor dinamicamente.
- [x] Carregar variáveis de ambiente para chaves de API e configurações.

## 2. Engenharia de Prompt

- [x] Criar função utilitária para limpar texto (`remove_starting_tabs`).
- [x] Desenvolver um prompt de sistema detalhado para guiar o LLM na tarefa de sumarização e extração de informações do Santo Rosário.
- [x] Refinar o prompt do sistema para ser mais robusto e funcionar melhor com LLMs menores, utilizando uma estrutura clara e instruções diretas.

## 3. Detecção de Versículos Bíblicos (RAG)

- [x] Configurar o `RecursiveCharacterTextSplitter` para dividir as transcrições em chunks.
- [x] Carregar o modelo de embeddings `sentence-transformers/all-MiniLM-L6-v2`.
- [x] Conectar à base de dados vetorial persistente `ChromaDB` que contém a Bíblia.
- [x] Implementar uma cadeia RAG para identificar possíveis referências bíblicas nos textos.
  - [x] Criar um prompt específico para a tarefa de classificação binária (se o trecho contém ou não uma citação bíblica).
  - [x] Definir a cadeia `rag_chain` que combina o retriever, o prompt e o LLM para uma verificação inicial.
- [ ] Melhorar robustez da detecção de versículos:
  - [ ] Transformar o processo de trazer trechos similarem em método, de nome: `get_similar_bible_passages`
  - [ ] Adicionar um hyperparâmetro `MIN_SIMILARITY` para ajustar a sensibilidade dos trechos retornados pelo Retriever.
  - [ ] O método `get_similar_bible_passages` deve receber um trecho e a similaridade mínima e retornar uma lista de dicionários, onde cada dicionário contém:
    - `passage`: o trecho da bíblia
    - `similarity_score`: o score de similaridade do trecho com o texto analisado
    - `verse`: o versículo correspondente (se aplicável)
    - `chapter`: o capítulo correspondente (se aplicável)
    - `book`: o livro da bíblia correspondente (se aplicável)
- [x] Implementar o método `get_bible_passages` para orquestrar o processo de detecção.
- [ ] Ajustar o método `get_bible_passages` para lidar com essa nova estrutura de dados.
- [ ] Testar se funciona melhor trazendo capítulos inteiros da bíblia ou somente os trechos retornados pelo método `get_similar_bible_passages`.

## 4. Pipeline de Processamento em Lote

- [x] Criar lógica para carregar os arquivos de transcrição em sequência a partir de um diretório.
- [x] Implementar um loop de processamento para iterar sobre os arquivos (`for i in tqdm(...)`).
- [x] Realizar um teste inicial do pipeline completo para um único arquivo.
- [ ] Remover a instrução `assert False` que atualmente bloqueia o processamento em lote.
- [ ] Ativar o salvamento automático dos resultados gerados em arquivos Markdown estruturados.
- [ ] Implementar tratamento de erros para casos de arquivos vazios ou não encontrados, com logs claros.
