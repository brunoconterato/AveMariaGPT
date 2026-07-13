# Visão geral

O notebook `src/bible_vectorstore/01_structure_bible_verses.ipynb` transforma o texto bruto da Bíblia Ave-Maria em um `DataFrame` orientado a referências bíblicas. Ele preserva blocos de texto que não podem ser divididos com segurança entre versículos e marca situações que exigem revisão.

O processamento usa a fonte em `data/raw/biblia/Ave Maria/Portugues-Catolica-AVM-All-Bible.txt`. Cabeçalhos, rodapés e números de página são reconhecidos antes dos marcadores de versículo para evitar que sejam tratados como conteúdo bíblico.

## Execução

Ative o ambiente antes de executar o notebook:

```bash
source /home/bruno/anaconda3/etc/profile.d/conda.sh && conda activate mariagpt
```

No notebook, `PROCESSAR_PDF` controla a extração do PDF e `PROCESSAR_TXT` controla a estruturação do TXT. Com `PROCESSAR_PDF=False` e `PROCESSAR_TXT=True`, o fluxo reutiliza o texto bruto existente, remove as três primeiras linhas para criar um arquivo temporário e chama `transformar_biblia_versiculo_a_versiculo`.

A função retorna o `DataFrame` `df_verse`. Apesar de receber `caminho_saida`, ela ainda não serializa o DataFrame nesse caminho; a persistência é uma etapa futura.

## Estrutura do DataFrame

| Coluna | Descrição |
| --- | --- |
| `book` | Livro identificado pelo parser. |
| `chapter` | Capítulo identificado no cabeçalho do texto. |
| `verse_start` | Primeiro versículo coberto pelo bloco; nulo quando o marcador não pode ser interpretado. |
| `verse_end` | Último versículo coberto pelo bloco; igual a `verse_start` para um versículo simples. |
| `text` | Texto do bloco, preservando quebras de linha internas. |
| `verse_acc` | Ordinal global do primeiro versículo lógico do bloco; não é chave persistente. |
| `pdf_page` | Página detectada no rodapé do PDF. |
| `need_review` | Indica uma exceção que exige revisão, como intervalo, duplicação, salto ou marcador não interpretado. |
| `raw_verse_marker` | Marcador original encontrado na fonte; concatena os marcadores quando dois blocos são mesclados. |
| `parse_issue` | Motivo da revisão; nulo para marcador simples válido. |

## Marcadores suportados

| Fonte | Resultado | Revisão |
| --- | --- | --- |
| `34` | `verse_start=34`, `verse_end=34` | Não. |
| `115`, no início do capítulo | Intervalo `1–15`; o início é obtido pela sequência inicial do capítulo e o restante do marcador representa o fim. | Sim: `merged_verse_marker`. |
| `924`, após o verso 8 | Intervalo `9–24`; o início é obtido pela sequência e o restante do marcador representa o fim. | Sim: `merged_verse_marker`. |
| `38`, após o verso 7 | Verso `38`; os números 8–37 não geram registros porque seus marcadores não estão na fonte. | Sim: `skipped_verse_marker`. |
| `12`, após o verso 10, seguido de `13` | Verso `12`; o verso 11 fica ausente porque seu marcador não está na fonte. | Sim: `skipped_verse_marker`. |
| `35-39`, após o verso 34 | Intervalo explícito `35–39`; o texto permanece em um único bloco. | Sim: `explicit_verse_range`. |
| `...: 19-32 Dentre ...`, após o verso 18 | Separa o texto anterior como verso 18 e preserva o restante como intervalo `19–32`. | Sim: `explicit_verse_range`. |
| `10`, `10`, após o verso 8 | Um único bloco `10`, com os dois textos concatenados; o versículo 9 não é inferido. | Sim: `merged_duplicate_marker`. |
| Marcador sem sequência válida, como `6` após o verso 8 | Referência e acumulador nulos; o texto é preservado. | Sim: `unexpected_marker`. |

Um marcador de intervalo explícito deve ocupar toda a linha, seguir o formato `início-fim`, iniciar no próximo versículo esperado e ter fim maior ou igual ao início. Assim, hifens presentes no texto normal não são interpretados como referência.

Uma faixa explícita também pode ser separada quando foi extraída após dois-pontos na mesma linha do versículo anterior, desde que comece exatamente no próximo versículo esperado. O texto antes da faixa permanece no versículo anterior; o restante forma o bloco de intervalo.

## Ordem e acumulador

`verse_acc` registra a posição global do primeiro versículo coberto por uma linha. Para um intervalo `start..end`, o acumulador avança `end - start + 1` posições. Por exemplo, um bloco `9–24` ocupa 16 posições; o próximo versículo lógico começa 15 posições depois da contagem que existiria se o bloco fosse unitário.

Marcadores com `unexpected_marker` não avançam o acumulador, pois o número de versículos cobertos não é conhecido. Eles devem ser revisados antes de usar o resultado como base canônica ou de indexação.

Para um salto de apenas um versículo, o parser aguarda o próximo marcador. Se ele retomar exatamente a sequência, o marcador adiantado é aceito como versículo simples com `skipped_verse_marker`; o número ausente não gera registro. Um marcador repetido tem prioridade e usa `merged_duplicate_marker`, sem criar o versículo ausente.

Para um salto de dois ou mais versículos, o marcador numérico explícito também é aceito como versículo simples com `skipped_verse_marker` e atualiza a sequência a partir dele. Os números ausentes não geram registros nem intervalos implícitos.

Quando um marcador adiantado é repetido imediatamente, o parser recupera a sequência sem inferir o número ausente. O registro resultante recebe `merged_duplicate_marker`, preserva os dois marcadores em `raw_verse_marker` e concatena os respectivos textos. Esse bloco não é atômico e não deve ser usado como transcrição canônica isolada do versículo indicado sem revisão.

## Revisão de qualidade

Use as células finais do notebook para listar linhas com `need_review=True` e visualizar o contexto anterior e posterior. A revisão deve confirmar que o intervalo representa o bloco inteiro e que o próximo marcador retoma uma sequência coerente.

Os marcadores `merged_verse_marker`, `explicit_verse_range`, `merged_duplicate_marker` e `skipped_verse_marker` exigem revisão. Os dois primeiros preservam intervalos válidos, mas o texto não traz fronteiras internas confiáveis entre todos os versículos. O parser não inventa essa separação.
