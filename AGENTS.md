# AGENTS.md

## Ambiente de trabalho

- Repositório: `/home/bruno/Workspace/MariaGPT`
- Shell padrão: `bash`
- Conda base: `/home/bruno/anaconda3`
- Ambiente principal: `mariagpt`

## Como ativar o ambiente

Use este comando no terminal antes de rodar notebooks, testes ou scripts que dependam de `pandas`:

```bash
source /home/bruno/anaconda3/etc/profile.d/conda.sh && conda activate mariagpt
```

## Observações úteis

- O notebook `src/bible_vectorstore/01_structure_bible_verses.ipynb` depende de `pandas`.
- Se `conda activate mariagpt` falhar direto, carregue primeiro `conda.sh` como acima.
- Evite assumir que o ambiente do shell já está ativo.

## Documentação

- Toda documentação criada ou atualizada em `docs/` deve iniciar pela seção `# Visão geral`, antes de detalhes técnicos, instruções ou referências.

## Commits

- Comite apenas modificações dentro do escopo da tarefa atual.
- Quando houver mais de um subescopo independente, divida as alterações em commits menores.
- Não faça push sem solicitação explícita do usuário.
- Use título curto e intuitivo; no corpo, detalhe as alterações relevantes.
