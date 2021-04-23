import django_filters.rest_framework
from rest_framework import viewsets
from core.serializers import QuestionSerializer, OptionSerializer, MemberSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend

from core.models import Question, Option, Member


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = QuestionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question', 'correct']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('-score')
    serializer_class = MemberSerializer
