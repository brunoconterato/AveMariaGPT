# MAP

Mapa rápido para localizar código, dados, documentação e artefatos do repositório.

```text
.
├── AGENTS.md                         Regras de trabalho do agente
├── README.md                         Visão geral e arquitetura do projeto
├── MAP.md                            Este mapa
├── ROADMAP.md / TODO.md              Planejamento e pendências
├── features.md                       Funcionalidades e status
├── Biblia.session.sql                Sessão/exportação SQL
├── conda_env.yaml / requirements.txt Dependências e ambiente
│
├── data/
│   ├── raw/                          Fontes originais
│   │   ├── biblia/                   Bíblias em PDF, EPUB, HTML e TXT
│   │   ├── catecismo/                PDFs do Catecismo
│   │   ├── missal/                   PDFs do Missal Romano
│   │   ├── batismo/                  Baptismo.pdf
│   │   ├── Notas do Vaticano/        Documentos do Vaticano
│   │   ├── Santo Rosário | Quaresma 2025/  Transcrições das lives
│   │   └── Santo Rosário | Sextas feiras normais/  Transcrições fora da Quaresma
│   └── processed/                    Dados extraídos e analisados
│       ├── biblia/                   Texto e versículos estruturados
│       ├── catecismo/                Catecismo convertido para Markdown
│       └── Santo Rosário | Quaresma 2025/  Análises das transcrições
│
├── src/
│   ├── 01_preprocessing/             Conversão de PDFs e ingestão para RAG
│   │   ├── pdf_to_markdown_convert_in_batches.sh  Script de conversão
│   │   ├── 2. Data Ingestion for RAG.ipynb         Pipeline genérico de RAG
│   │   └── README.md                  Documentação do fluxo
│   ├── bible_vectorstore/            Pipeline da Bíblia e banco vetorial
│   │   ├── 01_structure_bible_verses.ipynb  Estrutura o texto em versículos
│   │   ├── 02_vector_database.ipynb         Cria SQLite e ChromaDB
│   │   ├── bible_model.py              Modelos e enums bíblicos
│   │   ├── biblia.db                   Banco SQLite gerado
│   │   └── biblia_vectorstore*/        Vector store e backup gerados
│   ├── Bíblia VectorStore/            Diretório legado com biblia.db
│   └── rosarios_quaresma_frei_gilson/ Pipeline das transcrições dos rosários
│       ├── 01_preprocessing.ipynb     Limpeza, referências e análises
│       ├── utils.py                    Utilitários e enums
│       ├── README.md                   Documentação do pipeline
│       ├── research-*.md               Investigações técnicas
│       └── todo*.md                    Pendências do pipeline
│
└── docs/
    └── bible_vectorstore/             Documentação dos notebooks da Bíblia
```

## Fluxos principais

- **Bíblia:** `data/raw/biblia` → `01_structure_bible_verses.ipynb` → `data/processed/biblia` → `02_vector_database.ipynb` → `src/bible_vectorstore`.
- **RAG genérico:** fontes em `data/processed` → `src/01_preprocessing/2. Data Ingestion for RAG.ipynb`.
- **Rosários:** transcrições em `data/raw/Santo Rosário*` → `src/rosarios_quaresma_frei_gilson` → `data/processed/Santo Rosário | Quaresma 2025`.

> Mantenha este mapa atualizado quando arquivos ou pastas forem criados, removidos, movidos ou mudarem de finalidade. Agrupe arquivos gerados em massa por pasta.
