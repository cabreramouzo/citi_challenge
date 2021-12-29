from typing import List, Optional

import spacy
from spacy import Language
from spacy.symbols import ORTH, LEMMA, POS, TAG, NORM
from spacy.lang import en
import contractions


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

    spacy_tokens = []
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.norm_, token.lemma_)
        print(token.text)
        print(token.norm_)
        print(contractions.fix(token.text))
        print(contractions.fix(token.norm_))
        if token.pos_ != "PUNCT" and token.pos_ != "SYM":
            if token.pos_ == "AUX" or (token.pos_ == "PRON" and token.dep_ == "nsubj"):
                spacy_tokens.append(contractions.fix(token.norm_))
            elif token.pos_ == "NOUN" and token.dep_ == "appos":
                spacy_tokens.append(contractions.fix(token.norm_))
            elif token.pos_ == "ADV" and token.dep_ == "advmod":
                spacy_tokens.append(contractions.fix(token.norm_))
            else:
                spacy_tokens.append(contractions.fix(token.text))

    return spacy_tokens

def _perform_tokenization_rules_for_es(doc) -> List[str]:

    spacy_tokens = []
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.norm_, token.lemma_)
        if token.pos_ != "PUNCT" and token.pos_ != "SYM":
            if token.pos_ == "AUX" or (token.pos_ == "PRON" and token.dep_ == "nsubj"):
                spacy_tokens.append(token.norm_)
            elif token.pos_ == "NOUN" and token.dep_ == "appos":
                spacy_tokens.append(token.norm_)
            elif token.pos_ == "ADV" and token.dep_ == "advmod":
                spacy_tokens.append(token.norm_)
            else:
                spacy_tokens.append(token.text)

    return spacy_tokens

def _perform_tokenization_rules_for_fr(doc) -> List[str]:

    spacy_tokens = []
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.norm_, token.lemma_)
        if token.pos_ != "PUNCT" and token.pos_ != "SYM":
            if token.pos_ == "AUX" or (token.pos_ == "PRON" and token.dep_ == "nsubj"):
                spacy_tokens.append(token.norm_)
            elif token.pos_ == "NOUN" and token.dep_ == "appos":
                spacy_tokens.append(token.norm_)
            elif token.pos_ == "ADV" and token.dep_ == "advmod":
                spacy_tokens.append(token.norm_)
            else:
                spacy_tokens.append(token.text)

    return spacy_tokens

def _perform_tokenization_rules_for_pt(doc) -> List[str]:
    spacy_tokens = []
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.norm_, token.lemma_)
        if token.pos_ != "PUNCT" and token.pos_ != "SYM":
            if token.pos_ == "AUX" or (token.pos_ == "PRON" and token.dep_ == "nsubj"):
                spacy_tokens.append(token.norm_)
            elif token.pos_ == "NOUN" and token.dep_ == "appos":
                spacy_tokens.append(token.norm_)
            else:
                spacy_tokens.append(token.text)

    return spacy_tokens

def _perform_tokenization_rules_for_ca(doc) -> List[str]:

    spacy_tokens = []
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.norm_, token.lemma_)
        if token.pos_ != "PUNCT" and token.pos_ != "SYM":
            if token.pos_ == "AUX" or (token.pos_ == "PRON" and token.dep_ == "nsubj"):
                spacy_tokens.append(token.norm_)
            elif token.pos_ == "NOUN" and token.dep_ == "appos":
                spacy_tokens.append(token.norm_)
            elif token.pos_ == "ADV" and token.dep_ == "advmod":
                spacy_tokens.append(token.norm_)
            else:
                spacy_tokens.append(token.text)

    return spacy_tokens

def _perform_tokenization_rules_by_lang(doc, lang = "en") -> List[str]:

    spacy_tokens = []
    if lang == "en":
        spacy_tokens = _perform_tokenization_rules_for_en(doc)
    elif lang == "es":
        spacy_tokens = _perform_tokenization_rules_for_es(doc)
    elif lang == "fr":
        spacy_tokens = _perform_tokenization_rules_for_fr(doc)
    elif lang == "pt":
        spacy_tokens = _perform_tokenization_rules_for_pt(doc)
    elif lang == "ca":
        spacy_tokens = _perform_tokenization_rules_for_ca(doc)

    return spacy_tokens

def perform_contractions_expansion_en(text: str) -> str:
    l = text.split()
    s = ""
    for w in l:
        s += contractions.fix(w) + " "
    return s

def _perform_contractions_expansion_by_lang(lang = "en", text = "") -> str:

    if lang == "en":
        return perform_contractions_expansion_en(text)
    elif lang == "es":
        return text
    elif lang == "pt":
        return text
    elif lang == "fr":
        return text
    elif lang == "ca":
        return text


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
    nlp = _add_contraction_rules(nlp, lang)

    text_expanded = _perform_contractions_expansion_by_lang(lang, text)

    doc = nlp(text_expanded)
    spacy_tokens = []
    spacy_tokens = _perform_tokenization_rules_by_lang(doc, lang)

    return spacy_tokens
