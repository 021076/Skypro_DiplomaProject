from django.contrib import admin
from testing.models import Tests, Questions, Answers


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    """ Админка для работы с моделей Tests """
    list_display = ('id', 'topic', 'description')
    search_fields = ('topic',)
    list_filter = ('topic',)


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    """ Админка для работы с моделей Questions """
    list_display = ('id', 'test', 'question')
    search_fields = ('test',)
    list_filter = ('test',)


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    """ Админка для работы с моделей Answers """
    list_display = ('id', 'question', 'answer')
    list_filter = ('id',)
