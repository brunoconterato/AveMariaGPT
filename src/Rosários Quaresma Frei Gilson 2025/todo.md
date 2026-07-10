# Pré-processamento das Lives do Frei Gilson

Este arquivo detalha as tarefas para o pré-processamento e análise das transcrições das lives do Frei Gilson, conforme implementado no notebook `1. Preprocessing.ipynb`.

## 1. Configuração e Ambiente

- [x] Importar bibliotecas essenciais (langchain, dotenv, etc.)
- [x] Implementar seleção de modelo de LLM e provedor dinamicamente.
- [x] Carregar variáveis de ambiente para chaves de API e configurações.

## 2. Engenharia de Prompt

- [x] Criar função utilitária para limpar texto (`remove_starting_tabs`).
- [x] Desenvolver um prompt de sistema detalhado para guiar o LLM na tarefa de sumarização e extração de informações do Santo Rosário.
- [x] Refinar o prompt do sistema para ser mais robusto e funcionar melhor com LLMs menores, utilizando uma estrutura clara e instruções diretas.
  - [ ] Solicitar que a LLM traga todas as citações relevantes, de outras pessoas ou por meio de suas obras, que são relevantes às temáticas específicas do dia.

## 3. Detecção de Versículos Bíblicos (RAG)

- [x] Configurar o `RecursiveCharacterTextSplitter` para dividir as transcrições em chunks.
- [x] Carregar o modelo de embeddings `sentence-transformers/all-MiniLM-L6-v2`.
- [x] Conectar à base de dados vetorial persistente `ChromaDB` que contém a Bíblia.
- [x] Implementar uma cadeia RAG para identificar possíveis referências bíblicas nos textos.
  - [x] Criar um prompt específico para a tarefa de classificação binária (se o trecho contém ou não uma citação bíblica).
  - [x] Definir a cadeia `rag_chain` que combina o retriever, o prompt e o LLM para uma verificação inicial.
- [ ] Melhorar robustez da detecção de versículos:
  - [x] Transformar o processo de trazer trechos similarem em método, de nome: `retrieve_similar_bible_passages`
  - [x] Adicionar um hyperparâmetro `MIN_SIMILARITY_THRESHOULD` para ajustar a sensibilidade dos trechos retornados pelo Retriever.
- [x] Implementar o método `get_bible_passages` para orquestrar o processo de detecção.
- [x] Ajustar o método `get_bible_passages` para lidar com essa nova estrutura de dados.
- [ ] Descobrir um jeito de fazer funcionar em LLMs pequenas.
  - [x] Testar: `get_bible_passages` enviando os versículos de contexto
  - [x] Testar: `get_bible_passages` enviando os capítulos inteiros de contexto
  - [ ] Testar: `get_bible_passages` obtendo os versículos apenas a partir da anunciação, sem nenhum contexto (apenas com a query)
- [ ] [2026] Tornar o processo de procurar trechos da bíblia mais agêntico:
  - [ ] Agente: identificar trechos candidatos a serem versículos bíblicos. Trechos candidatos geralmente são antes anunciados por expressões como "leitura da bíblia", "leitura do evangelho", "leitura do livro de", "leitura do capítulo", "leitura do versículo", etc, etc, etc.
  - [ ] Fazer RAG para cada trecho candidato, trazendo os versículos mais similares da bíblia
  - [ ] Agente: identificar se o trecho candidato é realmente um versículo bíblico, com base nos versículos mais similares encontrados

## 4. Pipeline de Processamento em Lote

Retomar esta etapa após a implementação da detecção de versículos bíblicos estiver funcional.

- [x] Criar lógica para carregar os arquivos de transcrição em sequência a partir de um diretório.
- [x] Implementar um loop de processamento para iterar sobre os arquivos (`for i in tqdm(...)`).
- [x] Realizar um teste inicial do pipeline completo para um único arquivo.
- [ ] Implementar lógica de detecção de versículos bíblicos dentro do loop de processamento.
  - [ ] Implementar extração dos ensinamentos transmitidos durante o Santo Rosário a partir dos versículos bíblicos detectados.
- [ ] Ativar o salvamento automático dos resultados gerados em arquivos Markdown estruturados.u
