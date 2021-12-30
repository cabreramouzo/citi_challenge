from typing import List, Optional

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


def _add_contraction_rules(nlp: Language, lang: Optional[str] = "en") -> Language:
        # add special case rules
        if lang == "en":
            special_case_we_have = [{ORTH: "we"}, {ORTH: "'ve", NORM: "have"}]
            nlp.tokenizer.add_special_case("we've", special_case_we_have)

            '''contractions_to_phrase = {
                "ain't": "are not",
                "aren't": "are not",
                "can't": "cannot",
                "can't've": "cannot have",
                "'cause": "because",
                "could've": "could have",
                "couldn't": "could not",
                "couldn't've": "could not have",
                "didn't": "did not",
                "doesn't": "does not",
                "don't": "do not",
                "hadn't": "had not",
                "hadn't've": "had not have",
                "hasn't": "has not",
                "haven't": "have not",
                "he'd": "he would",
                "he'd've": "he would have",
                "he'll": "he will",
                "he'll've": "he will have",
                "he's": "he is",
                "how'd": "how did",
                "how'd'y": "how do you",
                "how'll": "how will",
                "how's": "how is",
                "I'd": "I would",
                "I'd've": "I would have",
                "I'll": "I will",
                "I'll've": "I will have",
                "I'm": "I am",
                "I've": "I have",
                "isn't": "is not",
                "it'd": "it would",
                "it'd've": "it would have",
                "it'll": "it will",
                "it'll've": "it will have",
                "it's": "it is",
                "let's": "let us",
                "ma'am": "madam",
                "mayn't": "may not",
                "might've": "might have",
                "mightn't": "might not",
                "mightn't've": "might not have",
                "must've": "must have",
                "mustn't": "must not",
                "mustn't've": "must not have",
                "needn't": "need not",
                "needn't've": "need not have",
                "o'clock": "of the clock",
                "oughtn't": "ought not",
                "oughtn't've": "ought not have",
                "shan't": "shall not",
                "sha'n't": "shall not",
                "shan't've": "shall not have",
                "she'd": "she would",
                "she'd've": "she would have",
                "she'll": "she will",
                "she'll've": "she will have",
                "she's": "she is",
                "should've": "should have",
                "shouldn't": "should not",
                "shouldn't've": "should not have",
                "so've": "so have",
                "so's": "so is",
                "that'd": "that would",
                "that'd've": "that would have",
                "that's": "that is",
                "there'd": "there would",
                "there'd've": "there would have",
                "there's": "there is",
                "they'd": "they would",
                "they'd've": "they would have",
                "they'll": "they will",
                "they'll've": "they will have",
                "they're": "they are",
                "they've": "they have",
                "to've": "to have",
                "wasn't": "was not",
                "we'd": "we would",
                "we'd've": "we would have",
                "we'll": "we will",
                "we'll've": "we will have",
                "we're": "we are",
                "we've": "we have",
                "weren't": "were not",
                "what'll": "what will",
                "what'll've": "what will have",
                "what're": "what are",
                "what's": "what is",
                "what've": "what have",
                "when's": "when is",
                "when've": "when have",
                "where'd": "where did",
                "where's": "where is",
                "where've": "where have",
                "who'll": "who will",
                "who'll've": "who will have",
                "who's": "who is",
                "who've": "who have",
                "why's": "why is",
                "why've": "why have",
                "will've": "will have",
                "won't": "will not",
                "won't've": "will not have",
                "would've": "would have",
                "wouldn't": "would not",
                "wouldn't've": "would not have",
                "y'all": "you all",
                "y'all'd": "you all would",
                "y'all'd've": "you all would have",
                "y'all're": "you all are",
                "y'all've": "you all have",
                "you'd": "you would",
                "you'd've": "you would have",
                "you'll": "you will",
                "you'll've": "you shall have",
                "you're": "you are",
                "you've": "you have",
                "doin'": "doing",
                "goin'": "going",
                "nothin'": "nothing",
                "somethin'": "something",
            }'''

            '''for k,v in contractions_to_phrase.items():
                case = [{ORTH: k, NORM: v}]
                nlp.tokenizer.add_special_case(k, case)'''



        """
        
        elif lang == "es":
            special_case_sr_senor = [{ORTH: "Sr.", NORM: "señor"}]
            special_case_ud_usted = [{ORTH: "Ud.", NORM: "usted"}]
            nlp.tokenizer.add_special_case("Sr.", special_case_sr_senor)
            nlp.tokenizer.add_special_case("Ud.", special_case_ud_usted)
        elif lang == "pt":
            special_case_sr_senhor = [{ORTH: "Sr.", NORM: "senhor"}]
            nlp.tokenizer.add_special_case("Sr.", special_case_sr_senhor)
        elif lang == "ca":
            special_case_sr_senyor = [{ORTH: "Sr.", NORM: "senyor"}]
            nlp.tokenizer.add_special_case("Sr.", special_case_sr_senyor)
        return nlp
        """

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
    result_tokens = _perform_tokenization_rules_by_lang(doc, lang)
    return result_tokens
    
    
    """
    
    print(core_web_sm)
    for token in doc:
        print(f"text: {token.text}, pos: {token.pos_}, dep: {token.dep_}, norm: {token.norm_}, lemma: {token.lemma_}, morph: {token.morph}")
        if not token.is_punct and not token.is_quote and token.pos != SYM:
            result_tokens.append(
                token.norm_
                if token.pos in TOKEN_NORMALIZED_CASES_EN
                else token.text
            )

    return result_tokens
    """
