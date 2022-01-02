import pytest


def test_tokenize_status_ok(client):
    """
    test that the endpoint exists
    """
    response = client.post(
        "/api/tokenize",
        data={"text": "a", "lang": "en"},
        content_type="application/json",
    )
    expected = 200
    assert response.status_code == expected


def test_tokenize_english_text(client):
    response = client.post(
        "/api/tokenize",
        data={"text": "I am a test", "lang": "en"},
        content_type="application/json",
    )
    expected = {"tokens": ["I", "am", "a", "test"]}
    assert response.json() == expected


def test_tokenize_missing_text(client):
    response = client.post(
        "/api/tokenize", data={"lang": "en"}, content_type="application/json"
    )
    expected = {"text": ["This field is required."]}
    assert response.json() == expected


def xtest_tokenize_missing_lang(client):
    response = client.post(
        "/api/tokenize", data={"text": "some text"}, content_type="application/json"
    )
    expected = {"lang": ["This field is required."]}
    assert response.json() == expected


def test_tokenize_missing_lang_en(client):
    response = client.post(
        "/api/tokenize", data={"text": "Some text in English"}, content_type="application/json"
    )
    expected = {"tokens": ["Some", "text", "in", "English"]}
    assert response.json() == expected

def test_tokenize_missing_lang_es(client):
    response = client.post(
        "/api/tokenize", data={"text": "Un texto en Español."}, content_type="application/json"
    )
    expected = {"tokens": ["Un", "texto", "en", "Español"]}
    assert response.json() == expected


def test_tokenize_missing_lang_fr(client):
    response = client.post(
        "/api/tokenize", data={"text": "Un texte en français."}, content_type="application/json"
    )
    expected = {"tokens": ["Un", "texte", "en", "français"]}
    assert response.json() == expected


def test_tokenize_missing_lang_pt(client):
    response = client.post(
        "/api/tokenize", data={"text": "Un texte en portugais."}, content_type="application/json"
    )
    expected = {"tokens": ["Un", "texte", "en", "portugais"]}
    assert response.json() == expected


def test_tokenize_missing_lang_ca(client):
    response = client.post(
        "/api/tokenize", data={"text": "Un text en Català"}, content_type="application/json"
    )
    expected = {"tokens": ["Un", "text", "en", "Català"]}
    assert response.json() == expected

@pytest.mark.skip("Now supporting lang as optional param")
def test_tokenize_missing_lang(client):
    response = client.post(
        "/api/tokenize", data={"text": "some text"}, content_type="application/json"
    )
    expected = {"lang": ["This field is required."]}
    assert response.json() == expected

@pytest.mark.skip("Now supporting lang as empty param")
def test_tokenize_lang_is_empty(client):
    response = client.post(
        "/api/tokenize",
        data={"text": "some text", "lang": ""},
        content_type="application/json",
    )
    expected = {"lang": ["Language  not supported"]}
    assert response.json() == expected


def test_tokenize_lang_is_not_supported(client):
    unsupported_lang = "ch"
    response = client.post(
        "/api/tokenize",
        data={"text": "some text", "lang": unsupported_lang},
        content_type="application/json",
    )
    expected = {"lang": [f"Language {unsupported_lang} not supported"]}
    assert response.json() == expected


def test_tokenize_invalid_data(client):
    response = client.post(
        "/api/tokenize",
        data='{"text"="some text", "lang": "en"}',
        content_type="application/json",
    )
    expected = 400
    assert response.status_code == expected
