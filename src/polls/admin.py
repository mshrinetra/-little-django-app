from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # Change the order of items in admin edit view
    fields = ['question_text', 'pub_date']

    # # Split the view using fieldsets
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    inlines = [ChoiceInline]

    # Names and order of columns in admin list view
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Define how to filter
    list_filter = ['pub_date']

    # Define how to search
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
