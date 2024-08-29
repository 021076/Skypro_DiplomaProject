from django.contrib import admin
from testing.models import Tests, Questions, Answers
import nested_admin


# Мульти-админка с вложенными строками
class AnswersInline(nested_admin.NestedTabularInline):
    model = Answers
    extra = 0


class QuestionsInline(nested_admin.NestedTabularInline):
    model = Questions
    inlines = [AnswersInline]
    extra = 0


class TestsAdmin(nested_admin.NestedModelAdmin):
    model = Tests
    inlines = [QuestionsInline]
    extra = 0


admin.site.register(Tests, TestsAdmin)

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
