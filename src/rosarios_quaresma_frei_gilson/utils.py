from enum import Enum
import re


def clean_tags(text: str) -> str:
    """Remove bracketed and parenthesized tags from ``text``.

    Both the delimiters and their contents are removed.  For example,
    ``"Olá [Música] mundo (aplausos)!"`` becomes ``"Olá  mundo !"``.

    Args:
        text: Text containing tags such as ``[anything]`` or ``(anything)``.

    Returns:
        The text with bracketed and parenthesized segments removed.
    """
    return re.sub(r"\[[^\]]*\]|\([^)]*\)", "", text)


def normalize_whitespace(text: str) -> str:
    """Normalize whitespace in ``text`` while preserving line breaks.

    Multiple spaces on a line become one space. Single tabs are preserved,
    while consecutive tabs are collapsed to one tab. Multiple consecutive
    newlines become one newline.

    Args:
        text: Text to be cleaned.

    Returns:
        The cleaned text with normalized spaces, tabs, and line breaks.
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r" +", " ", text)
    text = re.sub(r"\t{2,}", "\t", text)
    text = "\n".join(line.strip() for line in text.split("\n"))
    return re.sub(r"\n{2,}", "\n", text).strip()


def trim_line_whitespace(text):
    """
    Remove todos os tabs e espaços em branco do início e do final de cada linha do texto.
    """
    lines = text.split("\n")
    cleaned_lines = [line.strip() for line in lines]
    return "\n".join(cleaned_lines)

class BinaryResponse(Enum):
    YES = "Sim."
    NO = "Não."
