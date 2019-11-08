from django.contrib import admin
from .models import Sith, Planet, Recruit, Questions, Answer


class SithAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'planet' )

class PlanetAdmin(admin.ModelAdmin):
    list_display = ( 'name',  )

class RecruitAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'planet' )
class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'name', )
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('questions', 'result')
admin.site.register(Sith, SithAdmin)
admin.site.register(Planet, PlanetAdmin)
admin.site.register(Recruit, RecruitAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)


# Register your models here.
