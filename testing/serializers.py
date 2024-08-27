from rest_framework import serializers

from testing.models import Questions, Answers, Tests


class QuestionsSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Questions """

    class Meta:
        model = Questions
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):
    """ Cериализатор для контроллеров Answers """

    class Meta:
        model = Answers
        fields = ('answer',)


class TestsSerializer(serializers.ModelSerializer):
    """ Сериализатор для контроллеров Tests """

    class Meta:
        model = Tests
        fields = '__all__'
