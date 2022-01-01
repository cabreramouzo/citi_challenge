FROM python:3.9
LABEL author="Miguel A. Cabrera"

RUN apt update

WORKDIR /citibeats
COPY requirements.txt .

RUN pip install poetry
RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm && \
    python -m spacy download es_core_news_sm && \
    python -m spacy download pt_core_news_sm && \
    python -m spacy download fr_core_news_sm && \
    python -m spacy download ca_core_news_sm

## ARGS & Envs
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_PASSWORD
ARG DJANGO_SUPERUSER_EMAIL

ENV DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
ENV DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}

COPY . /citibeats

CMD ["./entrypoint.sh"]