# citi_challenge
NLP tokenizer challenge. Based on the [spaCy](https://spacy.io) NLP library. The challenge consists in develop a system to handle a text and tokenize it.

# TODO:
- [x] NLP core
- [x] API
- [x] Test API and nlp core.
- [x] Docker
- [x] gunicorn 
- [x] Heroku
- [ ] Detect language

# Learns:
This project allowed me to understand better how to create a system as a micro-service, dockerize it and deploy it in Heroku. Also I learn a lot about NLP and how to handle with text tokenization. For me was a big challenge beacause I never build a docker project before and also was my first project deployed in Heroku.

I also have some difficulties, mainly with NLP tokenization and handling with spaCy library, because it has a pretty amount of things to understand how the library manages tokenization and how it performs categorization. Due to every language is different, for me was pretty difficult to develop a single code to manage all languages supported by this system.

I needed to adapt to new thigs, tools and frameworks for me like software architecture, virtual enviroments for python, [Django REST framework](https://www.django-rest-framework.org), [docker](https://www.docker.com), [poetry](https://python-poetry.org), testing, [Heroku](https://id.heroku.com/login), django apps inside project, and many more :)

# Requeriments

- poetry
- python >=3.9
- docker

# Installation
Local development
```bash
poetry install
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm
python -m spacy download pt_core_news_sm
python -m spacy download fr_core_news_sm
python -m spacy download ca_core_news_sm
python citibeats_challenge/manage.py migrate
python citibeats_challenge/manage.py runserver
```
Testing
```bash
cd citi_challenge/citibeats_challenge
pytest
```


Docker
```
docker build . -t citibeats_challenge:local_dev
docker run --rm -p 8080:8080 citibeats_challenge:local_dev
```

# Usage and supported languages
```bash
curl -XPOST -H 'Content-Type: application/json' \
--data '{"text": "this is a sample", "lang": "en"}' \
'http://localhost:8080/api/tokenize'
```
Caution with single cuotes in `curl` command:
```bash
curl -XPOST -H 'Content-Type: '{"text": "Let'\''s go now people!"}'
```
> [!NOTE]
> Note that `lang` param in the request is optional and spaCy will try to detect it, but the `text` should be in English, Spanish, French, Portuguese or Catalan.

# Endpoints
|endpoint|method|data|
|---------|---------|---------|
|/api/tokenize | POST | {"text": "En un lugar de la Mancha", "lang": "es"}|


# NOTES:
- Optimization with generator and https://docs.djangoproject.com/en/4.0/ref/request-response/#django.http.StreamingHttpResponse
- Add [CORS](https://pypi.org/project/django-cors-headers/) headers.
- spaCy has missfunctions with some contractions like what've in english or je l'ai in French. In this cases tokenization will be as good as possible but can contain tokens without the correct contractions expansion.