import pytest
from citi_challenge.nlp_core.tokenize_text import get_tokens

def test_text_tokenize_sample_en():
    text = "Agent Smith: As you can see, we've had our eye on you for some time now, Mr. Anderson."
    tkns = tokenizeText(text, "en")
    res = ["Agent","Smith","As","you","can","see","we","have","had","our","eye","on","you","for","some","time","now","Mr.","Anderson"]
    print(tkns)
    print(res)
    assert( tkns == res)

def test_text_tokenize_sample_es():
    text = "Agente Smith: Cómo ud. puede ver, le hemos echado un ojo desde hace algún tiempo, Sr. Anderson."
    tkns = tokenizeText(text, "es")
    res = ["Agente","Smith","Cómo","usted","puede","ver","le","hemos","echado","un","ojo","desde","hace","algún","tiempo","Señor","Anderson"]
    print(tkns)
    print(res)
    assert( tkns == res)