from rest_framework import serializers
from .models import Keyword

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword # 모델 설정
        fields = ('title','content') # 필드 설정