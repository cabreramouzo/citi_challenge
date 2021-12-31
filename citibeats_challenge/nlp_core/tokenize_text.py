from typing import List, Optional

import spacy
from spacy.tokens import Token
from spacy.symbols import SYM

from common.lang import LanguageISO

def _get_core_web_sm_by_lang(lang: Optional[str] = "en") -> str:

    if lang == "en":
        return "en_core_web_sm"
    elif lang == "es":
        return "es_core_news_sm"
    elif lang == "pt":
        return "pt_core_news_sm"
    elif lang == "fr":
        return "fr_core_news_sm"
    elif lang == "ca":
        return "ca_core_news_sm"

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
    nlp = spacy.load(core_web_sm)

    doc = nlp(text)
    result_tokens = []
    for token in doc:
        token_repr = _get_token_representation(token)
        if token_repr:
            result_tokens.append(token_repr)
    return result_tokens
