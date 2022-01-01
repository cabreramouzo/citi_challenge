from rest_framework import status, views
from rest_framework.response import Response

from api.serializers import TokenSerializer, TextSerializer
from nlp_core.exceptions import NLPCoreException
from nlp_core import tokenize_text


class TokensView(views.APIView):
    """
    API endpoint that allows request for tokenize a text.
    """
    name = "tokens-viewset"

    def post(self, request, *args, **kwargs):
        text_lang = TextSerializer(data=request.data)
        text_lang.is_valid(raise_exception=True)
        try:
            tokens = tokenize_text.get_tokens(**text_lang.data)
        except NLPCoreException as e:
            return Response({"error": f"{e}"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        tokens = TokenSerializer(tokens).data
        return Response(tokens, status=status.HTTP_200_OK)
