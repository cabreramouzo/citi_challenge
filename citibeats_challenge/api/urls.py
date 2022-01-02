
from django.urls import path

from api.views import TokensView

urlpatterns = [
    path("tokenize", TokensView.as_view(), name=TokensView.name)
]
