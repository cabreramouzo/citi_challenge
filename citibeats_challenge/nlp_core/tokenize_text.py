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

TOKEN_NORMALIZED_CASES_EN = (
    NOUN,
    ADV,
    AUX,
    ADJ,
    PRON,
)

TOKEN_LEMMA_CASES_FR = (
    PRON,
    ADP,
    DET,
)

TOKEN_NORMALIZED_CASES_FR = (
    AUX,
)

TOKEN_NORMALIZED_CASES_PT = (
    ADV,
    AUX,
    ADJ,
    PRON,
)

TOKEN_LEMMA_CASES_PT = (
    ADV,
)

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

def _perform_tokenization_rules_for_en(doc) -> List[str]:
    """Perform tokenization rules for English, this should be the base for other languages
    when Spacy refines its tokenization algorithm for other languages."""
    result_tokens = []
    for token in doc:
        print(f"text: {token.text}, pos: {token.pos_}, dep: {token.dep_}, norm: {token.norm_}, lemma: {token.lemma_}, morph: {token.morph}")
        if not token.is_punct and not token.is_quote and token.pos != SYM:
            result_tokens.append(
                token.norm_
                if token.pos in TOKEN_NORMALIZED_CASES_EN
                else token.text
            )
    return result_tokens


def _perform_tokenization_rules_for_es(doc) -> List[str]:

    result_tokens = []
    for token in doc:
        print(f"text: {token.text}, pos: {token.pos_}, dep: {token.dep_}, norm: {token.norm_}, lemma: {token.lemma_}, morph: {token.morph}")
        if not token.is_punct and not token.is_quote and token.pos != SYM:
            result_tokens.append(
                token.norm_
                if token.pos in TOKEN_NORMALIZED_CASES_EN
                else token.text
            )
    return result_tokens


def _perform_tokenization_rules_for_fr(doc) -> List[str]:
    """Perform specific rules for French due for pronouns Spacy's treatment 
    is different than the English one."""

    result_tokens = []
    for token in doc:
        print(f"text: {token.text}, pos: {token.pos_}, dep: {token.dep_}, norm: {token.norm_}, lemma: {token.lemma_}, morph: {token.morph}")
        if not token.is_punct and not token.is_quote and token.pos != SYM:
            if token.pos in TOKEN_LEMMA_CASES_FR:
                result_tokens.append(token.lemma_)
            elif token.pos in TOKEN_NORMALIZED_CASES_FR:
                result_tokens.append(token.norm_)
            else: result_tokens.append(token.text)
    return result_tokens


def _perform_tokenization_rules_for_pt(doc) -> List[str]:
    result_tokens = []
    for token in doc:
        print(f"text: {token.text}, pos: {token.pos_}, dep: {token.dep_}, norm: {token.norm_}, lemma: {token.lemma_}, morph: {token.morph}")
        if not token.is_punct and not token.is_quote and token.pos != SYM:
            if token.pos in TOKEN_LEMMA_CASES_PT:
                result_tokens.append(token.lemma_)
            elif token.pos in TOKEN_NORMALIZED_CASES_PT:
                result_tokens.append(token.norm_)
            else: result_tokens.append(token.text)
    return result_tokens

def _perform_tokenization_rules_for_ca(doc) -> List[str]:

    result_tokens = []
    for token in doc:
        print(f"text: {token.text}, pos: {token.pos_}, dep: {token.dep_}, norm: {token.norm_}, lemma: {token.lemma_}, morph: {token.morph}")
        if not token.is_punct and not token.is_quote and token.pos != SYM:
            result_tokens.append(
                token.norm_
                if token.pos in TOKEN_NORMALIZED_CASES_EN
                else token.text
            )
    return result_tokens

def _perform_tokenization_rules_by_lang(doc: spacy.tokens.Doc, lang = LanguageISO.English) -> List[str]:

    result_tokens = []
    if lang == LanguageISO.English:
        result_tokens = _perform_tokenization_rules_for_en(doc)
    elif lang == LanguageISO.Spanish:
        result_tokens = _perform_tokenization_rules_for_es(doc)
    elif lang == LanguageISO.French:
        result_tokens = _perform_tokenization_rules_for_fr(doc)
    elif lang == LanguageISO.Portuguese:
        result_tokens = _perform_tokenization_rules_for_pt(doc)
    elif lang == LanguageISO.Catalan:
        result_tokens = _perform_tokenization_rules_for_ca(doc)
    else: 
        result_tokens = _perform_tokenization_rules_for_en(doc)

    return result_tokens


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
