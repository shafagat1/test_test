from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Платена"
        verbose_name_plural = u"Планета"
        db_table = u"Планета"

class Questions(models.Model):
    name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Вопрос')

class Answer(models.Model):
    result = models.BooleanField(default=False, verbose_name='Ответ')
    # author = models.ForeignKey(Recruit, on_delete=models.CASCADE, related_name='answer_author',
    #                            verbose_name='Автор ответа', null=False)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answer_questions', verbose_name='Вопрос', null=False)

class Recruit(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete=models.SET_NULL, related_name='rectuit_planet',
                               verbose_name='Планета обитания', null=True)
    email = models.EmailField( unique=True)
    age = models.IntegerField(verbose_name='Возраст', null=False, blank=False)
    activate = models.BooleanField(default=False)
    answer = models.ManyToManyField(Answer, related_name='answer_author', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["planet"]
        verbose_name = u"Рекрут"
        verbose_name_plural = u"Рекруты"
        db_table = u"Рекруты"

class Sith(models.Model):
    PlANET_CHOICES = (
        ('', u"мужской"),
        ('w', u"женский"),
    )
    planet = models.ForeignKey(Planet, on_delete=models.SET_NULL, related_name='sith_planet',
                               verbose_name='Планета обучения', null=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    recruits = models.ManyToManyField(Recruit, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["planet", 'name']
        verbose_name = u"Ситх"
        verbose_name_plural = u"Ситхи"
        db_table = u"Ситхи"











# Create your models here.
