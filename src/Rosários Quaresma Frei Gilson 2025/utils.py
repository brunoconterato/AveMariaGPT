from enum import Enum  # Add import for Enum


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


ORDERED_BOOKS = [
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
]
