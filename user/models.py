from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=20, verbose_name='Язык программирование')
    month_to_learn = models.IntegerField(verbose_name='продолжительность курса')

    def __str__(self):
        return self.name

class AbstractPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    email = models.EmailField(unique=True, verbose_name='почта')
    phone_number = models.CharField(max_length=13, verbose_name='номер телефона')


    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        abstract = True

class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=20, verbose_name='место учебы/работы', null=True, blank=True)
    has_own_notebook = models.BooleanField(default=True)
    preferred_os = models.CharField(max_length=20, verbose_name='предпочтительная опер сист')

    def __str__(self):
        return self.name

class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=20, verbose_name='основное место работы', null=True)
    experience = models.DateField(auto_now_add=True, verbose_name='опыт работы')
    student = models.ManyToManyField(Student, related_name='mentor', through='Course')

    def __str__(self):
        return f'{self.main_work} - {self.experience}'

class Course(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='наименование курса')
    date_started = models.DateField(auto_now_add=True, verbose_name='Дата начало курсов')

    def __str__(self):
        return f'{self.name} - {self.date_started}'


