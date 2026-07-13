# Pesquisa técnica: extração confiável de referências bíblicas

Data da auditoria: 11 de julho de 2026.

## Resumo executivo

A saída defeituosa não decorre de um único prompt ruim. Ela é produzida pela combinação de quatro falhas: a base bíblica já contém números de versículo corrompidos; a segmentação por tamanho fixo e com sobreposição reapresenta as mesmas citações; a recuperação puramente densa traz passagens apenas tematicamente parecidas; e o LLM recebe documentos serializados e pode transformar qualquer inteiro de metadados (`id`/`line_number`) em capítulo ou versículo. Ao final, o código somente remove tuplas idênticas, sem validar a referência nem consolidar intervalos sobrepostos.

A correção confiável é uma arquitetura híbrida e verificável. Referências anunciadas (“Mateus capítulo 27 versículo 46”) devem ser extraídas por parser determinístico e normalização de aliases. Citações sem endereço explícito devem passar por recuperação híbrida, reranking e alinhamento lexical. Em ambos os caminhos, o LLM só pode escolher entre IDs canônicos fornecidos pela aplicação; a aplicação converte o ID escolhido em livro/capítulo/versículo e rejeita qualquer valor ausente da base. A consolidação final deve operar sobre conjuntos de versículos, não sobre intervalos textuais gerados pelo modelo.

## 1. Escopo e pipeline auditado

Foram examinados o notebook `1. Preprocessing.ipynb`, `utils.py`, o `biblia.db`, o índice Chroma e a saída anexada.

O pipeline atual é:

1. remove marcações e normaliza espaços;
2. divide a transcrição com `RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)`;
3. um Gemma local decide quais partes parecem bíblicas e faz tool calls;
4. cada parte é buscada no Chroma por similaridade densa (`all-MiniLM-L6-v2`, `k=3`, limiar 0,65);
5. o resultado da ferramenta é convertido em `str(Document(...))` e entregue novamente ao LLM;
6. `with_structured_output(BibleExcerpts)` solicita livro e números ao LLM;
7. `sort_and_deduplicate()` ordena e elimina somente tuplas exatamente iguais.

O prompt diz que os textos bíblicos “são sempre anunciados”, mas o algoritmo não implementa essa regra: o modelo pode enviar qualquer trecho semanticamente bíblico à busca. Também há código e prompts antigos comentados, o que torna difícil saber qual experimento é a especificação vigente.

## 2. Evidências e problemas encontrados

### 2.1 Base de verdade corrompida

O SQLite tem 35.497 linhas, mas somente 35.495 chaves distintas `(book, chapter, verse)`. Há duas duplicatas canônicas. Mais grave: a própria coluna `verse` contém valores impossíveis, por exemplo `Josué 15:4860`, `Josué 19:4146`, `Esdras 2:3639` e `1 Crônicas 9:3544`. O índice Chroma replica os metadados `book`, `chapter`, `verse` e `line_number`; `line_number` varia de 0 a 35.496.

Isso mostra duas origens para os números enormes da saída:

- números como `27690`, `31322` e `35187` coincidem com a escala de `line_number`/ID global e podem ser copiados pelo LLM do `Document` serializado;
- outros números grandes podem vir diretamente da coluna `verse` já corrompida, provavelmente por falha do parser usado para criar o banco (concatenação de números/listas no texto de certos versículos).

Consequência: o Chroma recupera e apresenta metadados que não são uma verdade canônica confiável. Nenhuma melhoria de prompt resolve isso.

### 2.2 Ausência de validação estrutural e referencial

O Pydantic declara quatro inteiros, mas não impõe `ge=1`, não verifica `verse_start <= verse_end`, não consulta se o capítulo existe no livro, nem se o versículo existe no capítulo. Por isso aparecem:

- capítulo inexistente ou atribuição errada: `Números 40`, `Lamentações 31`, `Filipenses 15`;
- zero: `Lamentações 19:0-25`;
- intervalos invertidos: `Judite 1:8-3`, `Romanos 8:40-39`;
- finais maiores que o capítulo: `Apocalipse 21:4-70`;
- IDs globais tratados como versículos: `Mateus 6:27690-27691`.

Na amostra anexada foram reconhecidas 295 referências: 48 têm início maior que o fim, uma contém versículo zero e 57 têm ao menos uma extremidade maior que 200. Esses contadores são triagem por invariantes óbvias, não uma estimativa completa de erro; referências numericamente plausíveis também podem apontar para livro, capítulo ou texto incorretos.

Saída estruturada garante forma, não veracidade dos valores. A própria explicação oficial da OpenAI ressalva que Structured Outputs ainda pode errar valores; o mesmo princípio vale para outros fornecedores [S1].

### 2.3 Recuperação com baixa precisão para esta tarefa

`all-MiniLM-L6-v2` é usado sobre fala em português, mas não há no notebook uma avaliação que demonstre adequação ao idioma, à tradução bíblica ou ao domínio. Uma única busca densa, `k=3` e limiar fixo mistura similaridade temática com identidade textual. Trechos sobre fé, oração, amor ou sofrimento têm muitos falsos vizinhos bíblicos.

O sistema pede ao LLM que “ignore resultados apenas semanticamente parecidos”, mas não fornece distância, alinhamento textual, evidência palavra a palavra, nem uma opção estruturada e explícita `NONE`. Assim, a decisão final continua sendo uma geração aberta ancorada em candidatos frágeis.

### 2.4 Segmentação e repetição

O overlap de 200 caracteres reapresenta a mesma passagem em chunks adjacentes. Além disso, o modelo seleciona trechos com inícios/finais variáveis; cada variante recupera candidatos diferentes. Na amostra há 295 tuplas e todas são distintas exatamente, portanto a deduplicação atual não remove nenhuma. Há 30 pares `(livro, capítulo)` com intervalos distintos sobrepostos; `Lamentações 31` sozinho tem 25 variantes.

O método atual deduplica `(book, chapter, start, end)`. Logo, `Romanos 8:28-39`, `8:28-30` e `8:29-30` são considerados três itens, embora compartilhem versículos. Também não há identidade da ocorrência na transcrição (`start_char`, `end_char`, timestamp), impossibilitando distinguir repetição técnica da repetição real do orador.

### 2.5 Erros adicionais de implementação

- O validator de `verse_end` recebe o parâmetro `values`, mas referencia `info`, que não existe no corpo. Se `verse_end=None`, esse caminho tende a falhar.
- O prompt não pede confiança, evidência, offsets ou ID do candidato.
- A aplicação passa `str(tool_result)`, expondo representação interna e todos os inteiros dos metadados. O contrato deveria ser JSON mínimo e controlado.
- A ordenação canônica no fim destrói a ordem temporal da transcrição, importante para associar ensinamentos e detectar ocorrências.
- Não há versionamento da tradução/versificação. Salmos e livros deuterocanônicos exigem atenção especial, pois traduções/tradições podem divergir em numeração.
- A mesma LLM pequena executa segmentação, tool use, verificação e extração numérica em contexto relativamente grande; isso aumenta a carga composta e a propagação de erros.

## 3. Arquitetura recomendada

### 3.1 Etapa zero — reconstruir e certificar a base canônica

Esta é uma condição de entrada, não uma otimização.

1. Reimporte a Bíblia de uma fonte licenciada e versionada, preservando `translation_id`, tradição/versificação e checksum da fonte.
2. Crie uma tabela canônica com chave única `(translation_id, book_id, chapter, verse)` e um `canonical_verse_id` opaco, por exemplo `ave_maria:MAT:27:46`.
3. Separe identificadores técnicos (`row_id`, `line_number`) da referência; não os envie ao LLM.
4. Valide na ingestão: capítulo e versículo positivos, unicidade, continuidade esperada e limites por capítulo. Registros suspeitos vão para quarentena; nunca para o índice produtivo.
5. Gere o Chroma exclusivamente dessa tabela certificada e teste uma amostra Chroma ↔ SQLite por checksum.

Fonte técnica usada: a documentação do Chroma confirma que metadados estruturados podem filtrar consultas e que resultados podem retornar separadamente documentos, metadados e distâncias [S2, S3]. Aqui isso permite filtrar por livro/capítulo detectado, sem serializar objetos internos.

### 3.2 Dois caminhos de detecção

#### Caminho A — endereço explicitamente anunciado

Use regex/gramática e um dicionário normalizado de livros e aliases (“João”, “São João”, “primeira aos Coríntios”, abreviações). Extraia formas faladas como:

- `livro + capítulo + versículo(s)`;
- `Mateus 27 46`, `Mateus 27:46`;
- `versículos 42 a 46`, `do 42 ao 46`, `42 até 46`;
- continuação anafórica: “agora versículo 34”, mantendo livro/capítulo somente numa janela local segura.

O parser produz offsets e os números ou `NEEDS_REVIEW`; em seguida, consulta diretamente o SQLite. Se a referência não existir, não a “corrija” silenciosamente com LLM. Use busca aproximada somente para o nome do livro e exija margem clara entre o melhor e o segundo alias.

Para esse caminho não há motivo para RAG semântico: o endereço anunciado é a evidência primária. O LLM pode auxiliar apenas quando o ASR tornou o anúncio ambíguo, escolhendo entre 2–5 parses válidos.

#### Caminho B — citação textual sem endereço

1. Detecte uma janela candidata por marcadores discursivos e mudança de estilo, preservando offsets. Não fragmente toda a transcrição cegamente.
2. Faça busca híbrida: BM25/sparse para palavras exatas + embedding multilíngue para paráfrases/erros de ASR.
3. Recupere mais candidatos (por exemplo 20–50), depois aplique cross-encoder/late-interaction e alinhamento lexical robusto a ASR.
4. Expanda apenas os vizinhos canônicos do melhor candidato para decidir início/fim; não peça ao modelo que invente o intervalo.
5. Aceite somente se houver limiares calibrados de ranking, margem para o segundo colocado e cobertura textual. Caso contrário, retorne `NONE`/revisão humana.

BGE-M3 é uma opção a avaliar porque suporta português e combina recuperação densa, sparse e multi-vetor [S4]. ColBERT fornece late interaction para reranking/recuperação fina [S5]. Essas técnicas são candidatas, não garantias: devem vencer o baseline no conjunto rotulado local.

### 3.3 O LLM seleciona IDs; a aplicação materializa referências

O modelo nunca deve devolver números livres. Forneça candidatos assim:

```json
{
  "occurrence_id": "day13:char_10420_10610",
  "candidate_ids": ["MAT:27:46", "MRK:15:34", "NONE"],
  "candidate_texts": ["...", "...", ""]
}
```

Resposta permitida:

```json
{
  "selected_id": "MAT:27:46",
  "confidence": "high",
  "evidence": "meu Deus meu Deus por que me abandonaste"
}
```

A aplicação verifica que `selected_id` pertence à lista, resolve a referência pelo SQLite e salva score/evidência/proveniência. Para intervalos, o modelo escolhe uma lista de IDs consecutivos já fornecidos; a aplicação verifica consecutividade.

OpenAI Structured Outputs com schema estrito usa decodificação restrita, mas não elimina erros semânticos [S1]. Gemini oferece JSON Schema, inclusive `minimum`, `maximum`, `enum` e limites de array [S6]. Ollama aceita JSON Schema no campo `format`, recomenda Pydantic, schema também no prompt e temperatura baixa [S7]. Essas fontes sustentam o contrato de saída, enquanto a checagem de pertencimento continua obrigatoriamente determinística.

### 3.4 Consolidação correta de ocorrências e intervalos

Mantenha dois conceitos separados:

- **ocorrência**: posição/timestamp em que o orador anunciou ou citou a passagem;
- **referência canônica**: conjunto de IDs de versículos reconhecidos nessa ocorrência.

Por ocorrência, converta cada intervalo validado em conjunto de IDs, faça união e volte a comprimir somente IDs consecutivos do mesmo livro/capítulo. Entre ocorrências, não apague automaticamente uma repetição real: associe ocorrências próximas com alta sobreposição de offsets e conteúdo como duplicata técnica de chunk; preserve citações repetidas em momentos diferentes.

Exemplo: `{Rm 8:28–30, Rm 8:29–30}` vira `Rm 8:28–30` na mesma ocorrência. `{Rm 8:28–30, Rm 8:35–39}` permanece em dois intervalos. Não use regra de “menor” ou “maior” intervalo sem evidência textual.

### 3.5 Segmentação orientada a ocorrência

Troque chunks globais com overlap por janelas com identidade:

1. sentence split com offsets/timestamps;
2. alta-revocação para localizar anúncios e candidatos;
3. janela curta antes/depois do marcador;
4. expansão adaptativa até mudança discursiva ou limite;
5. supressão não máxima (NMS) de janelas sobrepostas que apontem para o mesmo anúncio.

Chunking orientado ao conteúdo preserva unidades coerentes; expansão posterior pode acrescentar contexto apenas quando necessário [S8]. Neste corpus, “unidade coerente” deve ser a ocorrência anunciada, não um bloco arbitrário de 1.000 caracteres.

## 4. Estratégia por tamanho de modelo

### Modelos locais pequenos e quantizados (Gemma e2b/e4b QAT)

- Divida o trabalho: detector → candidatos → seletor. Uma chamada curta por decisão.
- Faça o Caminho A sem LLM sempre que possível.
- Passe no máximo 3–5 candidatos reranqueados, com textos curtos e IDs opacos.
- Use Ollama `format=<Pydantic.model_json_schema()>`, temperatura 0, `enum` dinâmico de IDs e `NONE` obrigatório [S7].
- Evite tool choice autônoma e chamadas paralelas; a aplicação chama o retriever deterministically.
- Não peça cadeia de raciocínio. Peça apenas seleção e pequena evidência copiável.
- Use embedding realmente multilíngue e compare BM25, BGE-M3 e um reranker pequeno quantizado. Cache embeddings e resultados.
- Encaminhe ambiguidades e baixa margem para revisão, em vez de aumentar a criatividade do modelo.

Essas restrições reduzem espaço de busca e carga cognitiva. A literatura de structured RAG também observa que um retriever pequeno e bem treinado pode reduzir a necessidade de um LLM maior [S9].

### GPT 5.* e Gemini 3.*

- Use o mesmo pipeline determinístico; modelos maiores não devem contornar a base canônica.
- Eles podem melhorar segmentação ambígua, reranking de top-20 e decisão conjunta com evidências, especialmente em paráfrases longas.
- Use Structured Outputs estrito/JSON Schema e IDs enumerados [S1, S6]. No Gemini 3, structured outputs podem ser combinados com ferramentas, segundo a documentação atual [S10].
- Execute uma segunda verificação independente apenas nos casos ambíguos, sem mostrar a primeira resposta, e aceite por consenso + validação canônica.
- Compare custo/latência/qualidade contra o pipeline local; não presuma superioridade sem avaliação.

## 5. Plano incremental de implementação

### P0 — bloquear corrupção

1. Criar auditor de `biblia.db` e relatório de duplicatas, capítulos/versículos fora dos limites e checksums.
2. Reconstruir a fonte e o Chroma.
3. Adicionar constraints/índices únicos e testes de integridade.
4. Remover `line_number`, `id` e representação `Document(...)` dos prompts.
5. Adicionar validação canônica obrigatória antes de qualquer saída.

Critério de aceite: zero referência emitida que não exista na tabela certificada; zero intervalo invertido; zero ID técnico exposto.

### P1 — corrigir explícitas e repetição

1. Implementar parser de anúncios com aliases, offsets e estados locais.
2. Processar ocorrências, não chunks globais.
3. Implementar união de conjuntos e compressão de consecutivos.
4. Preservar ordem temporal e provenance.

Critério de aceite: 100% de validade estrutural e redução mensurável de duplicatas técnicas, sem eliminar repetições reais.

### P2 — melhorar citações implícitas

1. Montar baseline BM25 e embedding multilíngue.
2. Avaliar busca híbrida + reranker.
3. Calibrar `top_k`, limiares e margem no conjunto de validação.
4. Permitir abstinência e revisão humana.

Critério de aceite: ganho de precisão/recall/F1 por ocorrência e Recall@k/MRR do retriever em relação ao baseline atual.

### P3 — observabilidade e operação

Salve por ocorrência: arquivo/dia, offsets/timestamps, texto candidato, anúncio, candidatos e scores, modelo/versão/quantização, versão do índice, ID escolhido, razão de rejeição e decisão humana. Isso torna cada erro reproduzível.

## 6. Avaliação científica e testes

Crie um gold set estratificado, revisado por pelo menos duas pessoas, contendo:

- referências explícitas simples, intervalos e continuações (“agora versículo…”);
- nomes/abreviações e erros de ASR;
- citações textuais exatas, paráfrases e negativas tematicamente parecidas;
- limites entre oração e reflexão;
- repetições reais e duplicatas de janela;
- casos de Salmos/deuterocanônicos e variação de versificação.

Meça separadamente:

- detecção de ocorrência: precision, recall, F1 e IoU dos offsets;
- recuperação: Recall@k, MRR/nDCG e taxa de candidato correto ausente;
- ligação canônica: exact match de livro/capítulo/versículo e F1 por versículo;
- intervalos: precision/recall do conjunto de IDs, não apenas string exata;
- operação: taxa de abstinência, erro entre casos aceitos, latência e memória;
- integridade: referências inexistentes e duplicatas técnicas (alvo zero).

RAGChecker propõe diagnosticar separadamente recuperação e geração e relata melhor correlação com avaliação humana que métricas agregadas [S11]. A recomendação aqui adapta essa separação à ligação bíblica: primeiro verificar se o candidato correto foi recuperado, depois se foi selecionado corretamente.

Faça ablações: sem overlap; parser explícito; BM25; dense; híbrido; +reranker; LLM pequeno; LLM grande. Fixe seeds/temperatura quando aplicável e informe intervalos de confiança por bootstrap. Não ajuste limiar no conjunto de teste.

## 7. Esqueleto de contrato recomendado

```python
class OccurrenceDecision(BaseModel):
    occurrence_id: str
    selected_ids: list[str]  # validada contra enum dinâmico/allow-list
    confidence: Literal["high", "medium", "low"]
    evidence: str

def materialize(decision, allowed_ids, canon_db):
    if not decision.selected_ids or not set(decision.selected_ids) <= set(allowed_ids):
        return reject("id_not_offered")
    verses = [canon_db.get_required(i) for i in decision.selected_ids]
    if not canonical_and_consecutive_where_ranged(verses):
        return reject("invalid_canonical_sequence")
    return verses
```

O validator do modelo é uma camada; `materialize` e as constraints do banco são as fronteiras de confiança.

## 8. Fontes e rastreabilidade das soluções

- **[S1] OpenAI — Structured Outputs.** Schema estrito, constrained decoding e limitação de que valores ainda podem estar errados. Usada em 2.2, 3.3 e estratégia GPT. <https://openai.com/index/introducing-structured-outputs-in-the-api/>
- **[S2] Chroma — Metadata Filtering.** Filtros por metadados e operadores lógicos. Usada em 3.1 e 3.2. <https://docs.trychroma.com/docs/querying-collections/metadata-filtering>
- **[S3] Chroma — Query and Get.** Retorno separado de IDs, documentos, metadados e distâncias. Usada em 3.1 e para eliminar `str(Document)`. <https://docs.trychroma.com/docs/querying-collections/query-and-get>
- **[S4] Chen et al. — BGE M3-Embedding (arXiv:2402.03216).** Recuperação multilíngue, sparse, dense e multi-vetor. Usada em 3.2 e modelos locais. <https://arxiv.org/abs/2402.03216>
- **[S5] Khattab e Zaharia — ColBERT (arXiv:2004.12832).** Late interaction eficiente para ranking fino. Usada em 3.2. <https://arxiv.org/abs/2004.12832>
- **[S6] Google AI for Developers — Structured outputs.** JSON Schema, enums e limites numéricos/de arrays. Usada em 3.3 e estratégia Gemini. <https://ai.google.dev/gemini-api/docs/structured-output>
- **[S7] Ollama — Structured Outputs.** Schema no `format`, Pydantic e temperatura baixa. Usada em 3.3 e estratégia local. <https://docs.ollama.com/capabilities/structured-outputs>
- **[S8] Pinecone — Chunking Strategies for LLM Applications.** Chunking consciente de conteúdo e expansão na recuperação. Blog empresarial técnico usado em 3.5. <https://www.pinecone.io/learn/chunking-strategies/>
- **[S9] Djavanmardi et al. — Reducing hallucination in structured outputs via RAG (arXiv:2404.08189).** Grounding de saída estruturada e retriever menor reduzindo exigência sobre o LLM. Usada na estratégia local. <https://arxiv.org/abs/2404.08189>
- **[S10] Google AI for Developers — Using Tools with Gemini API.** Distinção entre function calling e saída estruturada e combinação no Gemini 3. Usada na estratégia Gemini. <https://ai.google.dev/gemini-api/docs/tools>
- **[S11] Ru et al. — RAGChecker (arXiv:2408.08067).** Métricas diagnósticas separadas para retrieval e generation. Usada na seção 6. <https://arxiv.org/abs/2408.08067>
- **[S12] Pinecone — Retrieval Augmented Generation series, James Briggs.** Material técnico empresarial sobre recuperação em dois estágios, reranking e métricas. Apoia 3.2 e 6. <https://www.pinecone.io/learn/series/rag/>

### Nota sobre blogs e vídeos

A busca incluiu documentação oficial, arXiv e material técnico empresarial reconhecido (Pinecone). Não foi incorporado um vídeo como fundamento: os resultados de vídeo encontrados não ofereciam evidência primária adicional melhor que as documentações e artigos acima. Isso evita usar autoridade aparente de canal como substituto de método reproduzível. As recomendações dependem de fontes auditáveis por texto e, principalmente, de validação no gold set deste corpus.

## Conclusão

O maior ganho não virá de trocar Gemma por GPT ou Gemini. Virá de retirar do modelo a autoridade de fabricar coordenadas, sanear a base, separar referência explícita de citação implícita, preservar identidade da ocorrência e validar cada saída contra uma allow-list canônica. Modelos maiores ajudam nos casos ambíguos; modelos locais pequenos tornam-se viáveis quando recebem poucos candidatos válidos e uma decisão estreita. Em ambos os casos, a confiabilidade é resultado das invariantes determinísticas e da avaliação, não da eloquência do modelo.
