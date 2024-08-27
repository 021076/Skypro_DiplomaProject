from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from testing.models import Tests, Questions, Answers
from testing.serializers import TestsSerializer, QuestionsSerializer


class TestsListAPIView(generics.ListAPIView):
    serializer_class = TestsSerializer
    queryset = Tests.objects.all()
    permission_classes = [IsAuthenticated]


class TestsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request) -> Response:
        answers = [Answers.answer for Answers in Answers.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1].lower()
        user_answer = request.data.get('user_answer')
        is_correct = user_answer == answer
        return Response({'is_correct': is_correct}, )


class QuestionsAPIView(APIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        question = [Questions.question for Questions in Questions.objects.all()]
        return Response({'questions': question}, )

    def post(self, request, *args, **kwargs):
        answer = [Answers.answer for Answers in Answers.objects.all()]
        user_answer = request.data.get('user_answer')

        is_correct = user_answer == answer
        return Response({'is_correct': is_correct})
