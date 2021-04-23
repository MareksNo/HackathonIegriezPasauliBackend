from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

from core.serializers import QuestionSerializer, OptionSerializer, MemberSerializer
from core.models import Question, Option, Member


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    authentication_classes = [TokenAuthentication] # Autentifikācija ar token
    permission_classes = [IsAuthenticatedOrReadOnly] # Iespējams GET bes auth, bet POST nepieciešams auth

    serializer_class = QuestionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question', 'correct']
    authentication_classes = [TokenAuthentication] # Autentifikācija ar token
    permission_classes = [IsAuthenticatedOrReadOnly] # Iespējams GET bes auth, bet POST nepieciešams auth


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('-score')
    serializer_class = MemberSerializer 
