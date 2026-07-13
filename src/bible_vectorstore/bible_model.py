from typing import List
from enum import Enum

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class BookEnum(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_

    Got books list using query:

    ```sql
    SELECT DISTINCT book
    FROM versiculos
    ORDER BY line_number

    ```
    """

    GENESIS = "Gênesis"
    EXODUS = "Êxodo"
    LEVITICUS = "Levítico"
    NUMBERS = "Números"
    DEUTERONOMY = "Deuteronômio"
    JOSHUA = "Josué"
    JUDGES = "Juízes"
    RUTH = "Rute"
    FIRST_SAMUEL = "1 Samuel"
    SECOND_SAMUEL = "2 Samuel"
    FIRST_KINGS = "1 Reis"
    SECOND_KINGS = "2 Reis"
    FIRST_CHRONICLES = "1 Crônicas"
    SECOND_CHRONICLES = "2 Crônicas"
    EZRA = "Esdras"
    NEHEMIAH = "Neemias"
    TOBIT = "Tobias"
    JUDITH = "Judite"
    ESTHER = "Ester"
    JOB = "Jó"
    PSALMS = "Salmos"
    FIRST_MACCABEES = "1 Macabeus"
    SECOND_MACCABEES = "2 Macabeus"
    PROVERBS = "Provérbios"
    ECCLESIASTES = "Eclesiastes"
    SONG_OF_SONGS = "Cântico dos Cânticos"
    WISDOM = "Sabedoria"
    ECCLESIASTICUS = "Eclesiástico"
    ISAIAH = "Isaías"
    JEREMIAH = "Jeremias"
    LAMENTATIONS = "Lamentações de Jeremias"
    BARUCH = "Baruc"
    EZEKIEL = "Ezequiel"
    DANIEL = "Daniel"
    HOSEA = "Oseias"
    JOEL = "Joel"
    AMOS = "Amós"
    ABDIAS = "Abdias"
    JONAS = "Jonas"
    MIQUEIAS = "Miqueias"
    NAUM = "Naum"
    HABACUC = "Habacuc"
    SOFONIAS = "Sofonias"
    AGEU = "Ageu"
    ZACARIAS = "Zacarias"
    MALAQUIAS = "Malaquias"
    SÃO_MATEUS = "São Mateus"
    SÃO_MARCOS = "São Marcos"
    SÃO_LUCAS = "São Lucas"
    SÃO_JOÃO = "São João"
    ATOS = "Atos"
    ROMANOS = "Romanos"
    PRIMEIRA_CORINTIOS = "1 Coríntios"
    SEGUNDA_CORINTIOS = "2 Coríntios"
    GALATAS = "Gálatas"
    EFESIOS = "Efésios"
    FILIPENSES = "Filipenses"
    COLOSSENSES = "Colossenses"
    PRIMEIRA_TESSALONICENSES = "1 Tessalonicenses"
    SEGUNDA_TESSALONICENSES = "2 Tessalonicenses"
    PRIMEIRA_TIMOTEO = "1 Timóteo"
    SEGUNDA_TIMOTEO = "2 Timóteo"
    TITO = "Tito"
    FILEMON = "Filemon"
    HEBREUS = "Hebreus"
    TIAGO = "Tiago"
    PRIMEIRA_SAO_PEDRO = "1 São Pedro"
    SEGUNDA_SAO_PEDRO = "2 São Pedro"
    PRIMEIRA_SAO_JOAO = "1 São João"
    SEGUNDA_SAO_JOAO = "2 São João"
    TERCEIRA_SAO_JOAO = "3 São João"
    SAO_JUDAS = "São Judas"
    APOCALIPSE = "Apocalipse"


ORDERED_BOOKS: List[BookEnum] = [
    BookEnum.GENESIS,
    BookEnum.EXODUS,
    BookEnum.LEVITICUS,
    BookEnum.NUMBERS,
    BookEnum.DEUTERONOMY,
    BookEnum.JOSHUA,
    BookEnum.JUDGES,
    BookEnum.RUTH,
    BookEnum.FIRST_SAMUEL,
    BookEnum.SECOND_SAMUEL,
    BookEnum.FIRST_KINGS,
    BookEnum.SECOND_KINGS,
    BookEnum.FIRST_CHRONICLES,
    BookEnum.SECOND_CHRONICLES,
    BookEnum.EZRA,
    BookEnum.NEHEMIAH,
    BookEnum.TOBIT,
    BookEnum.JUDITH,
    BookEnum.ESTHER,
    BookEnum.JOB,
    BookEnum.PSALMS,
    BookEnum.FIRST_MACCABEES,
    BookEnum.SECOND_MACCABEES,
    BookEnum.PROVERBS,
    BookEnum.ECCLESIASTES,
    BookEnum.SONG_OF_SONGS,
    BookEnum.WISDOM,
    BookEnum.ECCLESIASTICUS,
    BookEnum.ISAIAH,
    BookEnum.JEREMIAH,
    BookEnum.LAMENTATIONS,
    BookEnum.BARUCH,
    BookEnum.EZEKIEL,
    BookEnum.DANIEL,
    BookEnum.HOSEA,
    BookEnum.JOEL,
    BookEnum.AMOS,
    BookEnum.ABDIAS,
    BookEnum.JONAS,
    BookEnum.MIQUEIAS,
    BookEnum.NAUM,
    BookEnum.HABACUC,
    BookEnum.SOFONIAS,
    BookEnum.AGEU,
    BookEnum.ZACARIAS,
    BookEnum.MALAQUIAS,
    BookEnum.SÃO_MATEUS,
    BookEnum.SÃO_MARCOS,
    BookEnum.SÃO_LUCAS,
    BookEnum.SÃO_JOÃO,
    BookEnum.ATOS,
    BookEnum.ROMANOS,
    BookEnum.PRIMEIRA_CORINTIOS,
    BookEnum.SEGUNDA_CORINTIOS,
    BookEnum.GALATAS,
    BookEnum.EFESIOS,
    BookEnum.FILIPENSES,
    BookEnum.COLOSSENSES,
    BookEnum.PRIMEIRA_TESSALONICENSES,
    BookEnum.SEGUNDA_TESSALONICENSES,
    BookEnum.PRIMEIRA_TIMOTEO,
    BookEnum.SEGUNDA_TIMOTEO,
    BookEnum.TITO,
    BookEnum.FILEMON,
    BookEnum.HEBREUS,
    BookEnum.TIAGO,
    BookEnum.PRIMEIRA_SAO_PEDRO,
    BookEnum.SEGUNDA_SAO_PEDRO,
    BookEnum.PRIMEIRA_SAO_JOAO,
    BookEnum.SEGUNDA_SAO_JOAO,
    BookEnum.TERCEIRA_SAO_JOAO,
    BookEnum.SAO_JUDAS,
    BookEnum.APOCALIPSE,
]



class BibleExcerpt(BaseModel):
    book: BookEnum = Field(
        ...,
        description="Nome do livro da Bíblia explicitamente anunciado. Não deve conter número do capítulo.",
        examples=ORDERED_BOOKS,
    )
    chapter: int = Field(
        ...,
        description="Número do capítulo explicitamente anunciado. Não deve conter número de versículos.",
    )
    verse_start: int = Field(
        ...,
        description="Número do primeiro versículo do intervalo explicitamente anunciado, se for um único versículo. Se for um intervalo, é o primeiro versículo do intervalo.",
    )
    verse_end: int = Field(
        ...,
        description="Número do último versículo do intervalo explicitamente anunciado, se for um intervalo. Se não houver intervalo, igual ao verse_start.",
    )

    @field_validator("verse_end", mode="before")
    @classmethod
    def set_verse_end(cls, v, info: ValidationInfo):
        if v is None:
            return info.data.get("verse_start")
        return v


class BibleExcerpts(BaseModel):
    bible_excerpts: List[BibleExcerpt] = Field(
        ..., description="Lista com todos os trechos da bíblia identificados"
    )

    def sort_and_deduplicate(self):
        self.bible_excerpts.sort(
            key=lambda x: (
                ORDERED_BOOKS.index(x.book),
                x.chapter,
                x.verse_start,
            )
        )
        
        unique_excerpts = []
        seen = set()
        
        for excerpt in self.bible_excerpts:
            identifier = (
                excerpt.book,
                excerpt.chapter,
                excerpt.verse_start,
                excerpt.verse_end,
            )
            if identifier not in seen:
                seen.add(identifier)
                unique_excerpts.append(excerpt)
                
        self.bible_excerpts = unique_excerpts

    def __str__(self):
        return "\t".join(
            f"{excerpt.book} "
            f"{excerpt.chapter}:"
            f"{excerpt.verse_start}-"
            f"{excerpt.verse_end}"
            for excerpt in self.bible_excerpts
        )
