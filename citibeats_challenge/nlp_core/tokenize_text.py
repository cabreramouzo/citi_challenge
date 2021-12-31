from logging import debug
from typing import List, Optional
import pdb

import spacy
from spacy import Language
from spacy import language
from spacy.symbols import ORTH, LEMMA, POS, TAG, NORM
from spacy.symbols import NOUN, ADV, ADP, AUX, DET, ADJ, PRON, SYM
from spacy.lang import en

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
        repr = [token.text, token.lemma_, token.norm_, token.orth_]
        #breakpoint()
        if token.is_punct or token.is_quote or token.pos == SYM:
            continue
        for r in repr:
            if "'" not in r:
                result_tokens.append(r)
                break

    return result_tokens
