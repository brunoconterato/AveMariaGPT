# Extração Confiável de Referências Bíblicas — Lista Única de Tarefas Priorizadas

Checklist revisada contra `research-extracao-referencias-biblicas.md`. As prioridades indicam dependência e risco: P0 bloqueia a confiabilidade; P1 entrega o caminho explícito; P2 fecha a seleção e consolidação; P3 trata citações sem endereço; P4 cobre comparação, operação e evolução.

## [P0] Epic — Base de verdade e avaliação mínima

- [ ] [Bug] [P0] Auditar e reconstruir `biblia.db` a partir de fonte católica licenciada/versionada, corrigindo números corrompidos, duplicatas, capítulos/versículos impossíveis e diferenças de versificação.
- [ ] [Feature] [P0] Criar IDs estáveis por `(tradução, livro, capítulo, versículo)`, separar IDs canônicos de `id`/`line_number`, aplicar unicidade, gerar manifesto/checksum e recriar o Chroma somente com essa base, retornando JSON mínimo (ID, texto, metadados e score) e testando a correspondência SQLite–Chroma.
- [ ] [Feature] [P0] Definir o contrato do pipeline e criar gold set estratificado, revisado/adjudicado e dividido em desenvolvimento, validação e teste; incluir explícitas, ASR, paráfrases, negativos temáticos, repetições e versificação especial.
- [ ] [Test] [P0] Bloquear por testes de integridade duplicatas, coordenadas inexistentes, intervalos invertidos, IDs técnicos expostos e qualquer divergência entre a base e o índice.

## [P1] Epic — Detecção explícita e segmentação por ocorrência

- [ ] [Feature] [P1] Implementar catálogo normalizado de livros/aliases e parser determinístico para endereços, intervalos e continuações, tolerando acentos, pontuação, livros numerados e erros de ASR; validar no gold set com precision, recall e F1.
- [ ] [Feature] [P1] Substituir chunks globais com overlap por ocorrências: sentenças com offsets/timestamps, marcadores de anúncio, janela adaptativa e separação entre oração/reflexão; medir IoU dos limites no gold set.
- [ ] [Feature] [P1] Resolver endereços explícitos diretamente na base; casos inexistentes ou ambíguos viram `NEEDS_REVIEW`, sem correção silenciosa por LLM.

## [P2] Epic — Seleção controlada, validação e consolidação

- [ ] [Bug] [P2] Remover geração livre de livro/capítulo/versículo e tool choice autônoma; a aplicação controla detector, recuperação, seleção e validação, e o LLM pode escolher apenas candidatos oferecidos.
- [ ] [Feature] [P2] Usar saída estruturada com `occurrence_id`, IDs selecionados, confiança, evidência curta e `NONE`; oferecer 3–5 candidatos, aplicar JSON Schema/Pydantic no Ollama e temperatura zero.
- [ ] [Feature] [P2] Validar allow-list, existência, limites e consecutividade; materializar localização/texto somente pela base canônica, registrar rejeições e encaminhar baixa confiança/margem para revisão.
- [ ] [Feature] [P2] Consolidar cada ocorrência como conjunto de IDs, unindo sobreposições, recomprimindo apenas sequências consecutivas, preservando lacunas, ordem temporal, provenance e repetições reais; comprovar isso ao reprocessar o artefato atual.

## [P3] Epic — Citações sem endereço e recuperação híbrida

- [ ] [Feature] [P3] Criar detector de citações textuais sem endereço com janela candidata e abstinência, usando marcadores, mudança discursiva e evidência textual; não aceitar semelhança apenas temática.
- [ ] [Feature] [P3] Comparar BM25, embedding multilíngue/BGE-M3 e busca híbrida; recuperar candidatos com filtros canônicos, alinhamento tolerante a ASR e expansão somente para vizinhos válidos.
- [ ] [Feature] [P3] Avaliar reranking por cross-encoder/late interaction (incluindo ColBERT quando justificável), calibrar `top_k`, scores, margem, cobertura/abstinência e cachear por versão; aprovar somente se superar o baseline em Recall@k, MRR/nDCG, F1 por versículo e taxa de candidato correto ausente.

## [P4] Epic — Modelos, revisão humana e operação

- [ ] [Feature] [P4] Avaliar Gemma e2b/e4b quantizado em qualidade, estabilidade, memória, latência, abstinência e allow-list; comparar adaptadores equivalentes para GPT 5.* e Gemini 3.* e definir modelos aceitáveis por custo/benefício.
- [ ] [Feature] [P4] Implementar revisão humana para baixa confiança, conflitos, endereços inválidos e ausência de evidência; registrar decisão e provenance completo (arquivo, offsets, candidatos/scores, modelos, versões, IDs e rejeições).
- [ ] [Test] [P4] Executar ablações (parser, overlap, sparse/dense/híbrido, reranker e LLMs), bootstrap, relatórios reproduzíveis e suíte de regressão; bloquear promoção se uma invariante de integridade regredir.

## Critérios globais de conclusão

- [ ] [Test] [P0] Toda referência exportada existe na base certificada; nenhum `id`/`line_number` é tratado como versículo.
- [ ] [Test] [P2] A saída preserva ordem temporal, evidência, provenance e distingue duplicatas técnicas de repetições reais.
- [ ] [Test] [P4] O pipeline supera o baseline no gold set, abstém-se de casos ambíguos dentro do limite definido e permite auditar cada decisão.
