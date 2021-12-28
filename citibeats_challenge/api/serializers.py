from typing import List

from rest_framework import serializers

from common import lang
from const import tokenizer


class TextSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=tokenizer.MAX_CHARS_PER_TEXT, allow_blank=False)
    lang = serializers.CharField(max_length=tokenizer.MAX_CHARS_LANG, allow_blank=True)

    def validate_lang(self, value):
        value = value.lower()
        try:
            lang.LanguageISO(value)
        except ValueError:
            raise serializers.ValidationError(f"Language {value} not supported")
        return value


class TokenSerializer(serializers.Serializer):

    def to_representation(self, tokens: List[str]):
        return {
            "tokens" : tokens,
        }
