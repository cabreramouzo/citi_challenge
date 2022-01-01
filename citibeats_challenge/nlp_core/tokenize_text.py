from typing import List, Optional

import spacy
from spacy.tokens import Token
from spacy.symbols import SYM

from nlp_core.exceptions import NLPCoreException
from common.lang import LanguageISO

_MAPPING_LANG_SM = {
    LanguageISO.English: "en_core_web_sm",
    LanguageISO.Spanish: "es_core_news_sm",
    LanguageISO.Portuguese: "pt_core_news_sm",
    LanguageISO.French: "fr_core_news_sm",
    LanguageISO.Catalan: "ca_core_news_sm"
}

def _get_core_web_sm_by_lang(lang: Optional[str] = "en") -> str:
    """
    Map between lang and core_web_sm, returns english by default 
    if there is invalid lang.
    """
    return _MAPPING_LANG_SM.get(lang, "en_core_web_sm")

def _get_token_representation(token: Token) -> Optional[str]:
    """
    Returns the token representation. The function will try to match the proper
    contraction of the passed token, if there isn't any, it will return its
    text representation.
    """
    if token.is_punct or token.is_quote or token.pos == SYM:
        return

    token_repr = [
        token.text, 
        token.lemma_, 
        token.norm_, 
        token.orth_
    ]
    for repr in token_repr:
        if "'" not in repr:
            return repr 
    return token_repr[0]

def get_tokens(*, text: str, lang: Optional[str] = "en") -> List[str]:
    """
    Returns a list of tokens from a given text and language params.
    :param text: The text to tokenize in English, Spanish, Portuguese or French.
    :param lang: The ISO code of the lenguage (optional).
    :return: A list of tokens of the input text.
    """
    # Load English tokenizer, tagger, parser and NER
    core_web_sm = _get_core_web_sm_by_lang(lang)
    try:
        nlp = spacy.load(core_web_sm)
    except (IOError, ImportError, ValueError):
        raise NLPCoreException("Could not load spaCy lang module")

    doc = nlp(text)
    result_tokens = []
    for token in doc:
        token_repr = _get_token_representation(token)
        if token_repr:
            result_tokens.append(token_repr)
    return result_tokens
