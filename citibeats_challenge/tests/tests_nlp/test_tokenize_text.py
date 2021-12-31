import pytest

from nlp_core.tokenize_text import get_tokens

@pytest.fixture
def sample_en_agent_smith():
     text = "Agent Smith: As you can see, we've had our eye on you for some time now, Mr. Anderson."
     return text


@pytest.fixture
def sample_es_agent_smith():
    text = "Agente Smith: Cómo Ud. puede ver, le hemos echado un ojo desde hace algún tiempo, Sr. Anderson."
    return text

@pytest.fixture
def sample_fr_agent_smith():
     text = "Agent Smith : Comme vous pouvez le voir, nous vous surveillons depuis un certain temps, M. Anderson."
     return text


@pytest.fixture
def sample_pt_agent_smith():
     text = "Agente Smith: Como você pode ver, estamos de olho em você há algum tempo, Sr. Anderson."
     return text

@pytest.fixture
def sample_ca_agent_smith():
     text = "Agent Smith: Com vostè pot veure, li hem fet una ullada des de fa un temps, Sr. Anderson"
     return text
@pytest.fixture
def sample_fr_le_petit_prince():
    text = '''Lorsque j'avais six ans j'ai vu, une fois, une magnifique image, dans un livre sur la Forêt Vierge qui s'appelait 'Histoires Vécues'. Ça représentait un serpent boa qui avalait un fauve. Voilà la copie du dessin.'''
    return text

@pytest.fixture
def sample_es_quijote():
    text = ("En un lugar de la Mancha, de cuyo nombre no quiero acordarme, "
        "no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. "
        "Gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de «Quijada», o «Quesada»")
    return text

def xtest_text_tokenize_sample_en_what_ve():
    '''In this case Spacy tokenizer_exceptions does not have proper contraction expansion for what've.'''
    text = "Agent Smith: As you can see, what've had our eye on you for some time now, Mr. Anderson."
    tkns = get_tokens(text=text, lang="en")
    expected = ["Agent","Smith","As","you","can","see","what","have","had","our","eye","on","you","for","some","time","now","Mr.","Anderson"]
    assert(tkns == expected)

def test_text_tokenize_sample_en(sample_en_agent_smith):
    tkns = get_tokens(text=sample_en_agent_smith, lang="en")
    expected = ["Agent","Smith","As","you","can","see","we","have","had","our","eye","on","you","for","some","time","now","Mr.","Anderson"]
    assert(tkns == expected)

def test_text_tokenize_sample_es(sample_es_agent_smith):
    text = sample_es_agent_smith
    tkns = get_tokens(text=sample_es_agent_smith, lang="es")
    expected = ["Agente","Smith","Cómo","Ud.","puede","ver","le","hemos","echado","un","ojo","desde","hace","algún","tiempo","Sr.","Anderson"]
    assert(tkns == expected)

def test_text_tokenize_sample2_es(sample_es_quijote):
    tkns = get_tokens(text=sample_es_quijote, lang="es")
    expected = ["En", "un", "lugar", "de", "la", "Mancha", "de", "cuyo", "nombre", "no", "quiero", "acordarme", "no", "ha", "mucho", 
        "tiempo", "que", "vivía", "un", "hidalgo", "de", "los", "de", "lanza", "en", "astillero", "adarga", "antigua", "rocín", 
        "flaco", "y", "galgo", "corredor", "Gran", "madrugador", "y", "amigo", "de", "la", "caza", "Quieren", "decir", "que", 
        "tenía", "el", "sobrenombre", "de", "Quijada", "o", "Quesada"
    ]
    assert(tkns == expected)

def test_text_tokenize_sample_fr(sample_fr_agent_smith):
    '''Due spacy has some bugs in French mode, I change the test case. 'Smith' is a proper nound but spacy thinks that is an adjective.
    In this case 'Smith' should start with Capital letter but Spacy's engine normalized the token with lowercase letter'''

    tkns = get_tokens(text=sample_fr_agent_smith, lang="fr")
    expected = ["Agent","Smith","Comme","vous","pouvez","le","voir","nous","vous","surveillons","depuis","un","certain","temps","M.","Anderson"]
    print("Output->", tkns)
    print("Sample ->", expected)
    assert(tkns == expected)

def xtest_text_tokenize_contraction_je_l_ai_fr():
    """Bug je l'ai, sapcy treats as pronoun and is a preposition (in POS: ADP)"""
    #No treates properly by spacy: je l'ai
    text = "je l'ai mis sur liste noire"
    expected = ["je", "le", "ai", "mis", "sur", "liste", "noire"]
    tkns = get_tokens(text=text, lang="fr")
    assert(tkns == expected)

def test_text_tokenize_contraction_que_il_fr():
    text = "qu'il"
    expected = ["que", "il"]
    tkns = get_tokens(text=text, lang="fr")
    assert(tkns == expected)

def test_text_tokenize_contractions_fr():
    """Bug je l'ai, sapcy treats as pronoun and is a preposition (in POS: ADP)"""
    #No treates properly by spacy: je l'ai
    #text = "C'est d'amour j'habite je l'ai l'amie l'homme qu'il il s'apelle je t'aime"
    text = ["C'est", "d'amour", "j'habite", "l'amie", "l'homme", "il s'apelle", "je t'aime"]
    expected = [ ["ce", "est"], ["de", "amour"], ["je", "habite"], ["le", "amie"], ["le", "homme"], ["il", "se", "apelle"], ["je", "te", "aime"] ]
    tkns = [] 
    for phrase in text:
        tkns.append( get_tokens(text=phrase, lang="fr") )
    assert(tkns == expected)

def test_text_tokenize_sample_pt(sample_pt_agent_smith):
    '''Same case like Spanish or French,'''
    tkns = get_tokens(text=sample_pt_agent_smith, lang="pt")
    expected = ["Agente", "Smith", "Como", "você", "pode", "ver", "estamos", "de", "olho", "em", "você", "há", "algum", "tempo", "Sr.", "Anderson"]
    assert(tkns == expected)

def test_text_tokenize_sample_ca(sample_ca_agent_smith):
    tkns = get_tokens(text=sample_ca_agent_smith, lang="ca")
    expected = ["Agent", "Smith", "Com", "vostè", "pot", "veure", "li", "hem", "fet", "una", "ullada", "des", "de", "fa", "un", "temps", "Sr.", "Anderson"]
    assert(tkns == expected)

def test_text_tokenize_sample_fr_le_petit_prince(sample_fr_le_petit_prince):
    tkns = get_tokens(text=sample_fr_le_petit_prince, lang="fr")
    expected = ["Lorsque", "je", "avais", "six", "ans", "je", "ai", "vu", "une", "fois", "une", "magnifique", "image", "dans", "un", "livre", "sur", "la", "Forêt", "Vierge", "qui", "se", "appelait", "Histoires", "Vécues", "Ça", "représentait", "un", "serpent", "boa", "qui", "avalait", "un", "fauve", "Voilà", "la", "copie", "du", "dessin"]
    assert(tkns == expected)

