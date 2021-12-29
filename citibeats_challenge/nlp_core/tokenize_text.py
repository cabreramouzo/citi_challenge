from typing import List, Optional

import spacy
from spacy import Language
from spacy.symbols import ORTH, LEMMA, POS, TAG, NORM
from spacy.lang import en


def _add_contraction_rules(nlp: Language, lang: Optional[str] = "en") -> Language:
        # add special case rule
        if lang == "en":
            special_case_we_have = [{ORTH: "we"}, {ORTH: "'ve", NORM: "have"}]
            nlp.tokenizer.add_special_case("we've", special_case_we_have)
        elif lang == "es":
            special_case_sr_senor = [{ORTH: "Sr.", NORM: "señor"}]
            special_case_ud_usted = [{ORTH: "ud.", NORM: "usted"}]
            nlp.tokenizer.add_special_case("Sr.", special_case_sr_senor)
            nlp.tokenizer.add_special_case("ud.", special_case_ud_usted)
        return nlp

def _get_core_web_sm_by_lang(lang: Optional[str] = "en") -> str:

    if lang == "en":
        return "en_core_web_sm"
    elif lang == "es":
        return "es_core_news_sm"
    elif lang == "pt":
        return "pt_core_web_sm"
    elif lang == "fr":
        return "fr_core_web_sm"
    elif lang == "ca":
        return "ca_core_web_sm"


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
    nlp = _add_contraction_rules(nlp)
    doc = nlp(text)
    spacy_tokens = []
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.norm_)
        if token.pos_ != "PUNCT" and token.pos_ != "SYM":
            if token.pos_ == "AUX":
                spacy_tokens.append(token.norm_)
            else:
                spacy_tokens.append(token.text)

    return spacy_tokens
