from django.contrib import admin
from .models import Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # show 4 blank option rows by default

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text',)

admin.site.register(Question, QuestionAdmin)
