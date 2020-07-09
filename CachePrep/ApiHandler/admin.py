from django.contrib import admin
from ApiHandler.models import Questions


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id','text','tag']


admin.site.register(Questions,QuestionsAdmin)