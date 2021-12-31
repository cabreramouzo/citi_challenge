FROM python:3.9
LABEL author="Miguel A. Cabrera"

RUN apt update

WORKDIR /citibeats
COPY requirements.txt .

RUN pip install spacy
RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm && \
    python -m spacy download es_core_news_sm && \
    python -m spacy download pt_core_news_sm && \
    python -m spacy download fr_core_news_sm && \
    python -m spacy download ca_core_news_sm

COPY . /citibeats

EXPOSE 8080
CMD ["./entrypoint.sh"]
