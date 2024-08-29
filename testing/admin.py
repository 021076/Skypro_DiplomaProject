from django.contrib import admin
from testing.models import Test, Question, Answer
import nested_admin


# Мульти-админка с вложенными строками
class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 0


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]
    extra = 0


class TestAdmin(nested_admin.NestedModelAdmin):
    model = Test
    inlines = [QuestionInline]
    extra = 0


admin.site.register(Test, TestAdmin)

# Обычная админка
# @admin.register(Tests)
# class TestsAdmin(admin.ModelAdmin):
#     """ Админка для работы с моделей Tests """
#     list_display = ('id', 'topic', 'description')
#     search_fields = ('topic',)
#     list_filter = ('topic',)
#
#
# @admin.register(Questions)
# class QuestionsAdmin(admin.ModelAdmin):
#     """ Админка для работы с моделей Questions """
#     list_display = ('id', 'test', 'question')
#     search_fields = ('test',)
#     list_filter = ('test',)
#
#
# @admin.register(Answers)
# class AnswersAdmin(admin.ModelAdmin):
#     """ Админка для работы с моделей Answers """
#     list_display = ('id', 'question', 'answer')
#     list_filter = ('id',)
