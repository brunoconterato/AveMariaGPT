# Extração Confiável de Referências Bíblicas — Lista Única de Tarefas Priorizadas

Documento de origem: `research-extracao-referencias-biblicas.md`.

Legenda de prioridade:

- **P0:** bloqueia resultados inválidos ou o desenvolvimento seguro das etapas seguintes.
- **P1:** compõe o fluxo funcional mínimo para referências explicitamente anunciadas.
- **P2:** melhora a cobertura de citações implícitas e a qualidade da recuperação.
- **P3:** consolida operação, comparação entre modelos e evolução contínua.

## [P0] Epic — Definir a especificação e as fronteiras de confiança

- [ ] [Feature] [P0] Documentar formalmente os conceitos de ocorrência, referência canônica, intervalo, candidato, duplicata técnica, repetição real, abstinência e revisão humana.
- [ ] [Feature] [P0] Definir que somente a base canônica pode materializar livro, capítulo e versículo na saída final.
- [ ] [Feature] [P0] Definir que LLMs podem selecionar apenas IDs canônicos previamente oferecidos e nunca gerar coordenadas bíblicas livres.
- [ ] [Feature] [P0] Definir os contratos de entrada e saída de cada etapa: detecção, parsing explícito, recuperação, reranking, seleção, validação, consolidação e exportação.
- [ ] [Feature] [P0] Definir uma resposta explícita de abstinência, como `NONE`, e uma resposta de encaminhamento, como `NEEDS_REVIEW`.
- [ ] [Feature] [P0] Definir a política de versificação e tradução, incluindo tratamento de Salmos e livros deuterocanônicos.
- [ ] [Feature] [P0] Registrar decisões arquiteturais e remover da especificação vigente os fluxos experimentais ou prompts antigos que não serão mais utilizados.

## [P0] Epic — Auditar e reconstruir a base bíblica canônica

- [ ] [Bug] [P0] Criar uma auditoria reproduzível do `biblia.db` que liste chaves duplicadas `(book, chapter, verse)`.
- [ ] [Bug] [P0] Identificar a origem dos números de versículo corrompidos, como `Josué 15:4860` e `Esdras 2:3639`, no processo que gerou o banco.
- [ ] [Bug] [P0] Detectar capítulos e versículos inexistentes, valores menores que 1, descontinuidades inesperadas e registros fora dos limites de cada capítulo.
- [ ] [Bug] [P0] Produzir um relatório de integridade contendo totais, exemplos, causas conhecidas e registros enviados para quarentena.
- [ ] [Feature] [P0] Selecionar e documentar uma fonte bíblica licenciada, versionada e adequada à tradição católica utilizada no projeto.
- [ ] [Feature] [P0] Preservar na ingestão a tradução, a tradição de versificação, a versão da fonte e seu checksum.
- [ ] [Feature] [P0] Reconstruir a tabela bíblica a partir da fonte certificada, sem reutilizar registros corrompidos.
- [ ] [Feature] [P0] Criar um `canonical_verse_id` estável e opaco para cada versículo.
- [ ] [Feature] [P0] Separar os IDs canônicos dos identificadores técnicos, como `row_id`, `id` e `line_number`.
- [ ] [Feature] [P0] Aplicar unicidade a `(translation_id, book_id, chapter, verse)`.
- [ ] [Feature] [P0] Impedir que registros reprovados pela auditoria sejam inseridos na tabela ou no índice produtivo.
- [ ] [Feature] [P0] Gerar um manifesto versionado da base com quantidade de livros, capítulos, versículos, checksum e data de construção.
- [ ] [Test] [P0] Criar testes de integridade que falhem diante de duplicatas, coordenadas inválidas ou divergências de checksum.
- [ ] [Test] [P0] Confirmar que a nova base contém zero referência inválida segundo a versificação escolhida.

## [P0] Epic — Reconstruir e certificar o índice de recuperação

- [ ] [Bug] [P0] Remover do contexto enviado ao LLM qualquer `id`, `line_number` ou representação serializada de `Document(...)`.
- [ ] [Feature] [P0] Reconstruir o Chroma exclusivamente a partir da base canônica certificada.
- [ ] [Feature] [P0] Indexar somente metadados necessários e semanticamente inequívocos, como `canonical_verse_id`, `book_id`, `chapter`, `verse` e `translation_id`.
- [ ] [Feature] [P0] Definir IDs determinísticos para os registros do Chroma.
- [ ] [Feature] [P0] Retornar documentos, metadados e scores em JSON mínimo e controlado, sem usar `str()` de objetos internos.
- [ ] [Feature] [P0] Implementar filtros de metadados por tradução, livro e capítulo quando essas informações já forem conhecidas.
- [ ] [Feature] [P0] Versionar conjuntamente a base SQLite, o modelo de embedding e o índice vetorial.
- [ ] [Test] [P0] Comparar uma amostra do Chroma com o SQLite por ID e checksum.
- [ ] [Test] [P0] Garantir que nenhum identificador técnico seja exposto nos contratos de recuperação ou nos prompts.
- [ ] [Test] [P0] Garantir que todo item recuperado possa ser resolvido para exatamente um registro canônico.

## [P0] Epic — Implementar validação estrutural e referencial obrigatória

- [ ] [Bug] [P0] Corrigir o validator de `verse_end` que referencia `info` sem recebê-lo corretamente.
- [ ] [Bug] [P0] Rejeitar capítulo, início e fim de versículo menores que 1.
- [ ] [Bug] [P0] Rejeitar intervalos em que `verse_start > verse_end`.
- [ ] [Bug] [P0] Rejeitar capítulos inexistentes para o livro selecionado.
- [ ] [Bug] [P0] Rejeitar versículos inexistentes para o livro e capítulo selecionados.
- [ ] [Bug] [P0] Rejeitar qualquer ID selecionado que não pertença à allow-list oferecida ao modelo.
- [ ] [Feature] [P0] Resolver referências exclusivamente pelo `canonical_verse_id` na base certificada.
- [ ] [Feature] [P0] Verificar que listas usadas como intervalo contêm somente versículos canonicamente consecutivos do mesmo livro e capítulo.
- [ ] [Feature] [P0] Registrar a razão estruturada de cada rejeição.
- [ ] [Feature] [P0] Bloquear a exportação caso alguma referência não tenha passado pela validação canônica.
- [ ] [Test] [P0] Cobrir regressões presentes no artefato defeituoso: versículo zero, números globais, capítulos inexistentes, intervalos invertidos e finais acima do capítulo.
- [ ] [Test] [P0] Estabelecer como critério de aceite zero referência inexistente, zero intervalo invertido e zero ID técnico na saída.

## [P0] Epic — Criar o conjunto de avaliação e o baseline reproduzível

- [ ] [Feature] [P0] Definir um esquema de anotação para ocorrência, offsets ou timestamps, anúncio explícito, texto citado e referência canônica esperada.
- [ ] [Feature] [P0] Selecionar uma amostra estratificada de diferentes dias e partes das transcrições.
- [ ] [Feature] [P0] Incluir referências explícitas simples, intervalos, continuações anafóricas e nomes abreviados de livros.
- [ ] [Feature] [P0] Incluir erros de ASR, citações exatas, paráfrases e negativos tematicamente semelhantes.
- [ ] [Feature] [P0] Incluir limites entre oração e reflexão, repetições reais e duplicatas provocadas por janelas.
- [ ] [Feature] [P0] Incluir casos de Salmos, deuterocanônicos e possíveis diferenças de versificação.
- [ ] [Feature] [P0] Fazer cada exemplo ser revisado independentemente por pelo menos duas pessoas.
- [ ] [Feature] [P0] Definir um processo de adjudicação para divergências entre anotadores.
- [ ] [Feature] [P0] Separar conjuntos de desenvolvimento, validação e teste, impedindo ajuste de limiares no teste.
- [ ] [Feature] [P0] Congelar e versionar a primeira versão do gold set.
- [ ] [Feature] [P0] Reexecutar o pipeline atual no gold set e registrar o baseline antes das mudanças.
- [ ] [Test] [P0] Medir validade estrutural, precision, recall e F1 por ocorrência e por versículo no baseline.
- [ ] [Test] [P0] Medir Recall@k, MRR ou nDCG da recuperação atual.
- [ ] [Test] [P0] Medir duplicatas técnicas, taxa de referências inexistentes, latência e memória do baseline.

## [P1] Epic — Extrair referências explicitamente anunciadas sem RAG

- [ ] [Feature] [P1] Criar um catálogo normalizado de livros bíblicos, abreviações, variantes faladas e aliases em português.
- [ ] [Feature] [P1] Diferenciar corretamente livros numerados, como 1 João, 2 João, 1 Coríntios e 2 Coríntios.
- [ ] [Feature] [P1] Implementar normalização tolerante a acentos, pontuação, caixa e variações comuns do ASR.
- [ ] [Feature] [P1] Implementar parser para `livro + capítulo + versículo`.
- [ ] [Feature] [P1] Implementar parser para intervalos anunciados com “a”, “ao”, “até”, hífen e formas equivalentes.
- [ ] [Feature] [P1] Implementar parser para formas compactas, como `Mateus 27:46` e variações sem pontuação.
- [ ] [Feature] [P1] Implementar estado local seguro para continuações como “agora versículo 34”.
- [ ] [Feature] [P1] Limitar temporalmente ou por distância textual a herança de livro e capítulo nas continuações.
- [ ] [Feature] [P1] Preservar offsets de caracteres e timestamps, quando disponíveis, para cada anúncio reconhecido.
- [ ] [Feature] [P1] Consultar diretamente o SQLite após o parsing, sem busca semântica para referências válidas e explícitas.
- [ ] [Feature] [P1] Usar fuzzy matching somente no nome do livro e exigir margem mínima entre o primeiro e o segundo alias.
- [ ] [Feature] [P1] Retornar `NEEDS_REVIEW` quando mais de um parse canônico continuar plausível.
- [ ] [Bug] [P1] Impedir correção silenciosa por LLM quando o endereço anunciado não existir na base.
- [ ] [Test] [P1] Criar testes unitários para todas as formas explícitas presentes no gold set.
- [ ] [Test] [P1] Comparar o parser determinístico com o pipeline atual em precision, recall, latência e uso de memória.

## [P1] Epic — Segmentar a transcrição por ocorrências

- [ ] [Bug] [P1] Substituir o overlap global de 200 caracteres como mecanismo principal de descoberta de citações.
- [ ] [Feature] [P1] Segmentar a transcrição em sentenças preservando offsets e timestamps.
- [ ] [Feature] [P1] Detectar marcadores de anúncio bíblico com alta cobertura.
- [ ] [Feature] [P1] Criar uma janela identificável ao redor de cada anúncio.
- [ ] [Feature] [P1] Expandir a janela de forma adaptativa até mudança discursiva ou limite configurável.
- [ ] [Feature] [P1] Gerar um `occurrence_id` determinístico a partir do arquivo e dos offsets ou timestamps.
- [ ] [Feature] [P1] Aplicar supressão de janelas sobrepostas que apontem para o mesmo anúncio.
- [ ] [Feature] [P1] Preservar a ordem temporal das ocorrências durante todo o pipeline.
- [ ] [Feature] [P1] Identificar explicitamente a seção da oração e a seção da reflexão para permitir regras distintas.
- [ ] [Test] [P1] Medir precision, recall, F1 e IoU dos limites das ocorrências.
- [ ] [Test] [P1] Demonstrar redução de duplicatas técnicas sem perda de repetições reais.

## [P1] Epic — Redesenhar a seleção assistida por LLM

- [ ] [Bug] [P1] Remover a geração livre de `book`, `chapter`, `verse_start` e `verse_end` pelo modelo.
- [ ] [Bug] [P1] Remover a decisão autônoma do modelo sobre quando chamar a ferramenta de recuperação.
- [ ] [Feature] [P1] Fazer a aplicação controlar deterministicamente a sequência detector → recuperação → seleção → validação.
- [ ] [Feature] [P1] Definir uma saída estruturada contendo `occurrence_id`, IDs selecionados, confiança, evidência curta e opção `NONE`.
- [ ] [Feature] [P1] Criar um enum dinâmico ou allow-list contendo somente IDs efetivamente oferecidos naquela ocorrência.
- [ ] [Feature] [P1] Exigir que a evidência seja um trecho curto verificável da transcrição.
- [ ] [Feature] [P1] Materializar livro, capítulo, versículos e texto bíblico somente depois da seleção validada.
- [ ] [Feature] [P1] Configurar JSON Schema/Pydantic no Ollama e temperatura zero para modelos locais.
- [ ] [Feature] [P1] Passar para o modelo local no máximo 3–5 candidatos curtos e reranqueados.
- [ ] [Feature] [P1] Separar tarefas complexas em chamadas curtas, sem solicitar cadeia de raciocínio.
- [ ] [Feature] [P1] Encaminhar baixa confiança, baixa margem ou conflito de evidência para revisão humana.
- [ ] [Test] [P1] Testar tentativas de selecionar IDs que não foram oferecidos.
- [ ] [Test] [P1] Testar resposta vazia, truncada, malformada, `NONE` e `NEEDS_REVIEW`.
- [ ] [Test] [P1] Confirmar que erros semânticos do LLM não conseguem produzir uma referência canônica inexistente.

## [P1] Epic — Consolidar intervalos e deduplicar corretamente

- [ ] [Bug] [P1] Substituir a deduplicação por igualdade exata de `(book, chapter, start, end)`.
- [ ] [Feature] [P1] Representar internamente cada referência como conjunto ordenado de IDs canônicos.
- [ ] [Feature] [P1] Fazer a união de versículos sobrepostos dentro da mesma ocorrência.
- [ ] [Feature] [P1] Comprimir novamente somente IDs consecutivos do mesmo livro e capítulo.
- [ ] [Feature] [P1] Manter intervalos separados quando houver lacunas entre versículos.
- [ ] [Feature] [P1] Deduplicar janelas técnicas usando proximidade de offsets, sobreposição textual e identidade do anúncio.
- [ ] [Feature] [P1] Preservar citações repetidas em momentos diferentes como ocorrências reais distintas.
- [ ] [Feature] [P1] Associar todas as evidências e janelas de origem ao item consolidado.
- [ ] [Feature] [P1] Manter ordem temporal na saída principal e oferecer ordenação canônica somente como visualização alternativa.
- [ ] [Test] [P1] Garantir que `Rm 8:28–30` e `Rm 8:29–30` virem `Rm 8:28–30` na mesma ocorrência.
- [ ] [Test] [P1] Garantir que `Rm 8:28–30` e `Rm 8:35–39` permaneçam separados.
- [ ] [Test] [P1] Garantir que duas citações reais iguais em timestamps diferentes não sejam apagadas.

## [P1] Epic — Integrar o fluxo mínimo e bloquear regressões

- [ ] [Feature] [P1] Integrar base certificada, parser explícito, ocorrências, seleção limitada, validação e consolidação em um fluxo de ponta a ponta.
- [ ] [Feature] [P1] Gerar saída com referência canônica, texto bíblico, ocorrência, evidência e provenance.
- [ ] [Feature] [P1] Manter compatibilidade de exportação com a etapa posterior de extração de ensinamentos.
- [ ] [Bug] [P1] Impedir que referências da reflexão sejam misturadas às referências da oração quando essa separação for requisito do produto.
- [ ] [Test] [P1] Reprocessar o artefato defeituoso e verificar zero coordenada inexistente.
- [ ] [Test] [P1] Confirmar que nenhum `line_number` ou ID global aparece como versículo.
- [ ] [Test] [P1] Confirmar 100% de validade estrutural da saída.
- [ ] [Test] [P1] Comparar as duplicatas antes e depois sem usar somente igualdade textual.
- [ ] [Test] [P1] Executar regressão completa no gold set antes de iniciar o caminho de citações implícitas.

## [P2] Epic — Detectar citações textuais sem endereço explícito

- [ ] [Feature] [P2] Definir regras de alta cobertura para localizar possíveis citações sem endereço.
- [ ] [Feature] [P2] Detectar mudanças de estilo, vocabulário bíblico, fórmulas de leitura e transições para explicação.
- [ ] [Feature] [P2] Produzir janelas candidatas com offsets e contexto anterior suficiente.
- [ ] [Feature] [P2] Separar detector de ocorrência e identificador da passagem para permitir avaliação isolada.
- [ ] [Feature] [P2] Implementar abstinência para textos apenas tematicamente bíblicos.
- [ ] [Feature] [P2] Encaminhar candidatos ambíguos para revisão em vez de forçar uma referência.
- [ ] [Test] [P2] Avaliar o detector contra positivos, paráfrases e negativos tematicamente semelhantes.

## [P2] Epic — Implementar recuperação híbrida e reranking

- [ ] [Feature] [P2] Implementar um baseline lexical BM25 ou sparse sobre os versículos canônicos.
- [ ] [Feature] [P2] Selecionar embeddings multilíngues candidatos adequados ao português.
- [ ] [Feature] [P2] Avaliar BGE-M3 como candidato dense/sparse/multi-vetor.
- [ ] [Feature] [P2] Comparar o embedding atual `all-MiniLM-L6-v2` com os candidatos multilíngues no gold set.
- [ ] [Feature] [P2] Combinar resultados sparse e dense por estratégia de fusão documentada.
- [ ] [Feature] [P2] Recuperar um conjunto inicial maior, como top 20–50, antes do reranking.
- [ ] [Feature] [P2] Avaliar um cross-encoder multilíngue pequeno para reranking.
- [ ] [Feature] [P2] Avaliar late interaction/ColBERT quando o custo de índice e inferência for aceitável.
- [ ] [Feature] [P2] Adicionar score de alinhamento lexical tolerante a erros de ASR.
- [ ] [Feature] [P2] Expandir somente versículos canônicos vizinhos ao melhor candidato para determinar os limites da passagem.
- [ ] [Feature] [P2] Calibrar `top_k`, score mínimo, margem para o segundo colocado e cobertura textual no conjunto de validação.
- [ ] [Feature] [P2] Cachear embeddings, candidatos e resultados de reranking por versão do pipeline.
- [ ] [Test] [P2] Medir Recall@k, MRR/nDCG, precision e taxa de ausência do candidato correto.
- [ ] [Test] [P2] Aprovar a busca híbrida somente se superar o baseline com ganho estatisticamente documentado.

## [P2] Epic — Avaliar modelos locais pequenos e quantizados

- [ ] [Feature] [P2] Definir uma matriz de avaliação para Gemma e2b/e4b QAT e quantizações relevantes.
- [ ] [Feature] [P2] Padronizar temperatura, seed quando disponível, tamanho de contexto e schema entre execuções.
- [ ] [Feature] [P2] Avaliar separadamente detector, seletor de candidatos e verificador.
- [ ] [Feature] [P2] Medir o impacto de 3, 5 e mais candidatos sobre precisão, latência e memória.
- [ ] [Feature] [P2] Avaliar prompts curtos com exemplos mínimos e sem tool choice autônoma.
- [ ] [Feature] [P2] Quantificar respostas malformadas, abstinências, falsos positivos e seleções fora da allow-list.
- [ ] [Feature] [P2] Definir o menor modelo que atinge os critérios de qualidade do produto.
- [ ] [Test] [P2] Executar múltiplas repetições para medir estabilidade mesmo com temperatura zero.
- [ ] [Test] [P2] Confirmar que a quantização não altera as invariantes determinísticas do pipeline.

## [P2] Epic — Implementar revisão humana dos casos ambíguos

- [ ] [Feature] [P2] Definir os gatilhos de revisão: baixa confiança, baixa margem, conflito entre recuperadores, endereço inválido ou ausência de evidência.
- [ ] [Feature] [P2] Exibir ao revisor a ocorrência, contexto, anúncio, candidatos, scores, texto bíblico e razão do encaminhamento.
- [ ] [Feature] [P2] Permitir aceitar candidato, escolher outro candidato canônico, rejeitar todos ou marcar problema da transcrição/base.
- [ ] [Feature] [P2] Registrar decisão, responsável, data e versão do pipeline.
- [ ] [Feature] [P2] Incorporar decisões adjudicadas em versões futuras do gold set sem contaminar o teste congelado.
- [ ] [Test] [P2] Medir taxa de encaminhamento, tempo de revisão e erro residual entre casos aceitos automaticamente.

## [P3] Epic — Observabilidade, provenance e reprodutibilidade

- [ ] [Feature] [P3] Registrar arquivo, dia, offsets, timestamps, occurrence ID, anúncio e texto candidato.
- [ ] [Feature] [P3] Registrar candidatos, scores dense/sparse/reranker, margens e evidência selecionada.
- [ ] [Feature] [P3] Registrar modelo, provedor, versão, quantização, parâmetros e schema usado.
- [ ] [Feature] [P3] Registrar versões da base, tradução, índice, embedding e código do pipeline.
- [ ] [Feature] [P3] Registrar ID selecionado, referências materializadas, razão de abstinência ou rejeição e decisão humana.
- [ ] [Feature] [P3] Criar relatório agregado por execução com métricas de qualidade, integridade, custo, latência e memória.
- [ ] [Feature] [P3] Permitir reproduzir uma decisão individual a partir do seu registro de provenance.
- [ ] [Feature] [P3] Alertar quando qualquer invariante P0 for violada.
- [ ] [Test] [P3] Verificar que duas execuções com o mesmo manifesto são comparáveis e rastreáveis.

## [P3] Epic — Comparar modelos grandes sem enfraquecer as invariantes

- [ ] [Feature] [P3] Criar adaptadores equivalentes para GPT 5.* e Gemini 3.* com Structured Outputs/JSON Schema.
- [ ] [Feature] [P3] Manter para modelos grandes a mesma allow-list canônica e a mesma validação determinística.
- [ ] [Feature] [P3] Avaliar modelos grandes somente em segmentação ambígua, reranking e seleção de candidatos.
- [ ] [Feature] [P3] Implementar segunda verificação independente apenas para casos ambíguos selecionados.
- [ ] [Feature] [P3] Impedir que a segunda verificação veja a primeira resposta antes de produzir sua decisão.
- [ ] [Feature] [P3] Definir uma regra de consenso combinada com validação canônica.
- [ ] [Feature] [P3] Comparar modelos locais e grandes por qualidade, abstinência, custo, latência e privacidade.
- [ ] [Test] [P3] Aprovar o uso de modelo grande somente quando houver ganho mensurável no gold set ou nos casos encaminhados.

## [P3] Epic — Experimentação científica e melhoria contínua

- [ ] [Feature] [P3] Criar uma matriz de ablação: pipeline atual, sem overlap, parser explícito, BM25, dense multilíngue, híbrido e híbrido com reranker.
- [ ] [Feature] [P3] Comparar LLM pequeno, LLM grande e nenhuma LLM no caminho explícito.
- [ ] [Feature] [P3] Fixar seeds e parâmetros quando suportados.
- [ ] [Feature] [P3] Calcular intervalos de confiança por bootstrap para as métricas principais.
- [ ] [Feature] [P3] Avaliar métricas de recuperação e seleção separadamente, seguindo a decomposição proposta no research.
- [ ] [Feature] [P3] Versionar resultados de experimentos junto aos manifestos de dados e modelos.
- [ ] [Feature] [P3] Definir um processo de promoção de configuração baseado em métricas e não em inspeção anedótica.
- [ ] [Feature] [P3] Criar uma suíte de regressão executada sempre que base, parser, embedding, reranker, prompt ou modelo mudar.
- [ ] [Test] [P3] Bloquear promoção quando houver regressão de integridade, mesmo que outra métrica média melhore.

## [P3] Epic — Documentação e operação do pipeline definitivo

- [ ] [Feature] [P3] Documentar a arquitetura final e a responsabilidade de cada componente.
- [ ] [Feature] [P3] Documentar como reconstruir e certificar a base e o índice.
- [ ] [Feature] [P3] Documentar como criar, revisar e versionar o gold set.
- [ ] [Feature] [P3] Documentar como calibrar limiares sem usar o conjunto de teste.
- [ ] [Feature] [P3] Documentar como investigar uma referência incorreta usando provenance.
- [ ] [Feature] [P3] Documentar como executar modelos locais e grandes com contratos equivalentes.
- [ ] [Feature] [P3] Documentar critérios de rollback para base, índice, modelo e configuração.
- [ ] [Feature] [P3] Arquivar ou marcar claramente os experimentos antigos para evitar execução acidental do pipeline defeituoso.

## Critérios globais de conclusão

- [ ] [Test] [P0] Toda referência exportada existe na base canônica certificada.
- [ ] [Test] [P0] Nenhum ID técnico ou `line_number` é interpretado ou exibido como versículo.
- [ ] [Test] [P0] Não existem capítulos ou versículos iguais a zero, intervalos invertidos ou limites inexistentes na saída.
- [ ] [Test] [P1] Duplicatas técnicas são consolidadas e repetições reais permanecem representadas como ocorrências distintas.
- [ ] [Test] [P1] A ordem temporal e a evidência de cada ocorrência são preservadas.
- [ ] [Test] [P2] O fluxo novo supera o baseline documentado nas métricas prioritárias do gold set.
- [ ] [Test] [P2] A taxa de erro entre resultados aceitos automaticamente está dentro do limite definido pelo produto.
- [ ] [Test] [P3] Cada resultado pode ser reproduzido e auditado por meio do manifesto e dos dados de provenance.
