from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class house(models.Model):
    HOUSE_TYPES = (
        ('1', 'Жилой'), 
        ('2', 'Жилой дом блокированной застройки'), 
        ('3', 'Многоквартирный')
    )
    ESTSTATUSES = (
        ('1', 'Владение'), 
        ('2', 'Дом'), 
        ('3', 'Домовладение'),
        ('4', 'Участок')
    )
    STRSTATUSES = (
        ('1', 'Строение'), 
        ('2', 'Сооружение'), 
        ('3', 'Литер')
    )
    title = models.CharField(max_length = 200)      #   Адрес строкой
    houseguid = models.CharField(max_length = 36)   #   Глобальный уникальный идентификатор дома
    aoguid = models.CharField(max_length = 36)      #   Guid записи родительского объекта (улицы, города, населенного пункта и т.п.)
    management_org = models.ForeignKey(             #   Управляющая организация
        'organization',
        models.PROTECT
    )
    house_type = models.CharField(
        max_length = 50,
        choices = HOUSE_TYPES,
        default = '3'
    )
    housenum = models.CharField(max_length = 20)    #	Номер дома – Строка, содержащая номер дома, до 20 символов
    buildnum = models.CharField(max_length = 10, blank = True)    #	Номер корпуса – Строка, содержащая номер корпуса, до 10 символов
    strucnum = models.CharField(max_length = 10, blank = True)    #	Номер строения – Строка, содержащая номер строения, до 10 символов
    eststatus = models.CharField(                   #   Признак владения
        max_length = 20,
        choices = ESTSTATUSES,
        default = '2'
    )
    strstatus = models.CharField(                   #   Признак строения
        max_length = 20,
        choices = STRSTATUSES,
        blank = True
    )
    cadnum = models.CharField(max_length = 40)      #   Кадастровый номер
    created_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
   
    #def add(self):
    #    self.save()

    def __str__(self):
        return self.title


class organization(models.Model):
    ogrn = models.CharField(max_length = 15)
    kpp = models.CharField(max_length = 9)
    name = models.CharField(max_length = 160)
    short_name = models.CharField(max_length = 100)
    created_date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)

    #def save(self):
    #    self.save()

    def __str__(self):
        return self.short_name
