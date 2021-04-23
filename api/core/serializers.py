from rest_framework import serializers
from rest_framework.authtoken.models import Token
from core.models import Question, Option, Member

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['question', 'correct', 'choice_text']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['q', 'xtraInfo', 'image']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['username', 'score']
