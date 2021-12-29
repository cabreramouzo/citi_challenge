import pytest
from nlp_core.tokenize_text import get_tokens

def test_text_tokenize_sample_en():
    text = "Agent Smith: As you can see, we've had our eye on you for some time now, Mr. Anderson."
    tkns = get_tokens(text=text, lang="en")
    res = ["Agent","Smith","As","you","can","see","we","have","had","our","eye","on","you","for","some","time","now","Mr.","Anderson"]
    print(tkns)
    print(res)
    assert( tkns == res)

def test_text_tokenize_sample_es():
    text = "Agente Smith: Cómo Ud. puede ver, le hemos echado un ojo desde hace algún tiempo, Sr. Anderson."
    tkns = get_tokens(text=text, lang="es")
    res = ["Agente","Smith","Cómo","usted","puede","ver","le","hemos","echado","un","ojo","desde","hace","algún","tiempo","señor","Anderson"]
    print("Output->", tkns)
    print("Sample ->", res)
    assert( tkns == res)

def test_text_tokenize_sample_fr():
    text = "Agent Smith : Comme vous pouvez le voir, nous vous surveillons depuis un certain temps, M. Anderson."
    tkns = get_tokens(text=text, lang="fr")
    res = ["Agent","Smith","Comme","vous","pouvez","le","voir","nous","vous","surveillons","depuis","un","certain","temps","M.","Anderson"]
    print("Output->", tkns)
    print("Sample ->", res)
    assert( tkns == res)

    def xtest_text_tokenize_sample_fr_le_petit_prince():
        text = '''Lorsque j'avais six ans j'ai vu, une fois, une magnifique image, dans un livre sur la Forêt Vierge qui s'appelait "Histoires Vécues". Ça représentait un serpent boa qui avalait un fauve. Voilà la copie du dessin.'''
        tkns = get_tokens(text=text, lang="es")
        res = ["Agente","Smith","Cómo","usted","puede","ver","le","hemos","echado","un","ojo","desde","hace","algún","tiempo","señor","Anderson"]
        print("Output->", tkns)
        print("Sample ->", res)
        assert( tkns == res)

