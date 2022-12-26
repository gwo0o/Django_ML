from rest_framework import viewsets
from .serializers import KeywordSerializer
from .models import Keyword

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer