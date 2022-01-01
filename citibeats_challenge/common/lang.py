from enum import Enum


class LanguageISO(str, Enum):
    """
    Language ISO 639-1 standard
    """

    English = "en"
    Spanish = "es"
    Portuguese = "pt"
    French = "fr"
    Catalan = "ca"
