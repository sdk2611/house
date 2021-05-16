from django.db import models
from django.utils import timezone
from django.conf import settings

# МКД
class house(models.Model):
    '''
    СПРАВОЧНИКИ
    '''
    #   Тип дома
    HOUSE_TYPES = (
        ('1', 'Жилой'), 
        ('2', 'Жилой дом блокированной застройки'), 
        ('3', 'Многоквартирный')
    )
    #   Признак владения
    ESTSTATUSES = (
        ('1', 'Владение'), 
        ('2', 'Дом'), 
        ('3', 'Домовладение'),
        ('4', 'Участок')
    )
    #   Признак строения
    STRSTATUSES = (
        ('1', 'Строение'), 
        ('2', 'Сооружение'), 
        ('3', 'Литер')
    )
    #   Состояние (НСИ 24)
    STATES = (
        ('1', 'Аварийный'), 
        ('2', 'Исправный'), 
        ('3', 'Ветхий')
    )
    #   Стадия жизненного цикла (НСИ 338)
    LIFECYCLESTAGES = (
        ('1', 'Эксплуатация'), 
        ('2', 'Реконструкция'), 
        ('3', 'Капитальный ремонт с отселением'),
        ('4', 'Капитальный ремонт без отселения')
    )
    year_now = timezone.now().year
    YEARS = [(year, year) for year in range(year_now, year_now - 200, -1)]
    '''
    ОБЩИЕ ХАРАКТЕРИСТИКИ МКД
    '''
    #   Адрес строкой
    address = models.CharField(max_length = 200, null = True, verbose_name='Адрес')
    #   Полный Адрес строкой
    fullAddress = models.CharField(max_length = 200, verbose_name='Полный адрес')
    #   Глобальный уникальный идентификатор дома
    houseguid = models.CharField(max_length = 36, unique=True, verbose_name = 'Идентификатор в ФИАС')   
    #   Уникальный номер дома в ГИС ЖКХ (например, MBp00381)
    UniqueNumber = models.CharField(max_length = 10, unique=True, blank = True, null = True, verbose_name = 'Идентификатор в ГИС ЖКХ')
    #   Guid записи родительского объекта (улицы, города, населенного пункта и т.п.)
    aoguid = models.CharField(max_length = 36, verbose_name = 'Идентификатор улицы в ФИАС')
    #   Код ОКТМО
    oktmo = models.CharField(max_length = 11, verbose_name = 'Код ОКТМО')
    #	Номер дома – Строка, содержащая номер дома, до 20 символов
    housenum = models.CharField(max_length = 20, verbose_name = 'Номер дома')
    #	Номер корпуса – Строка, содержащая номер корпуса, до 10 символов
    buildnum = models.CharField(max_length = 10, blank = True, null = True, verbose_name = 'Номер корпуса')
    #	Номер строения – Строка, содержащая номер строения, до 10 символов
    strucnum = models.CharField(max_length = 10, blank = True, null = True, verbose_name = 'Номер строения')
    #   Тип дома
    house_type = models.CharField(
        max_length = 1,
        choices = HOUSE_TYPES,
        default = '3',
        verbose_name = 'Тип дома',
    )
    #   Признак владения
    eststatus = models.CharField(                   
        max_length = 1,
        choices = ESTSTATUSES,
        default = '2',
        verbose_name = 'Признак владения',
    )
    #   Признак строения
    strstatus = models.CharField(                   
        max_length = 1,
        choices = STRSTATUSES,
        blank = True,
        null = True, 
        verbose_name = 'Признак строения',
    )
    #   Кадастровый номер
    cadnum = models.CharField(max_length = 40, verbose_name = 'Кадастровый номер')      
    #   TotalSquare 	PremisesAreaType 	1..1 	Общая площадь здания
    TotalSquare = models.DecimalField(max_digits=25,decimal_places=4, null=True, verbose_name = 'Общая площадь')   
    #   State 	nsiRef 	1..1 	Состояние (НСИ 24)
    State = models.CharField(                       
        max_length = 1,
        choices = STATES,
        default = '2',
        verbose_name = 'Состояние',
    )
    #   LifeCycleStage 	nsiRef 	0..1 	Стадия жизненного цикла (НСИ 338)
    LifeCycleStage = models.CharField(              
        max_length = 1,
        choices = LIFECYCLESTAGES,
        default = '1',
        blank = True,
        null = True, 
        verbose_name = 'Стадия жизненного цикла',
    )
    #   UsedYear 	UsedYearType 	1..1 	Год ввода в эксплуатацию
    # UsedYear = models.DateField(null=True, verbose_name = 'Год ввода в эксплуатацию')
    UsedYear = models.CharField(
        max_length = 4,
        choices = YEARS,
        null=True, 
        verbose_name = 'Год ввода в эксплуатацию',
    )
    #   FloorCount 	FloorType 	1..1 	Количество этажей
    FloorCount = models.PositiveSmallIntegerField(null = True, verbose_name = 'Количество этажей')
    #    UndergroundFloorCount 	UndergroundFloorType 	1..1 	Количество подземных этажей
    UndergroundFloorCount = models.PositiveSmallIntegerField(null = True, verbose_name = 'Количество подземных этажей')
    #    OlsonTZ 	nsiRef 	1..1 	Часовая зона
    OlsonTZ = models.CharField(
        max_length = 50,
        default = 'Москва',
        verbose_name = 'Часовая зона',
    )
    #    CulturalHeritage 	boolean 	1..1 	Наличие у дома статуса объекта культурного наследия
    CulturalHeritage = models.BooleanField(default = False, verbose_name = 'Статус объекта культурного наследия')

    #   Управляющая организация
    management_org = models.ForeignKey(             
        'organization',
        on_delete = models.PROTECT,
        verbose_name = 'Управляющая организация',
    )
    #   Дата создания
    created_date = models.DateTimeField(default = timezone.now, verbose_name = 'Когда создано')
    #   Автор
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, verbose_name = 'Кем создано')

    def __str__(self):
        return self.address

# ПОДЪЕЗДЫ
class Entrance(models.Model):
    #   EntranceNum 	string (ограничение) 	1..1 	Номер подъезда
    EntranceNum = models.CharField(max_length = 10, verbose_name = 'Номер подъезда')
    #   ID дома
    house = models.ForeignKey(             
        'house',
        on_delete=models.CASCADE,
        verbose_name = 'Дом',
    )
    #   StoreysCount 	byte (ограничение) 	0..1 	Этажность
    StoreysCount = models.PositiveSmallIntegerField(blank = True, verbose_name = 'Этажность')
    #   CreationYear 	YearType 	0..1 	Год постройки
    CreationYear = models.DateField(blank = True, verbose_name = 'Год постройки')

    def __str__(self):
        return self.EntranceNum


# ЖИЛЫЕ ПОМЕЩЕНИЯ
class ResidentialPremises(models.Model):
    '''
    СПРАВОЧНИКИ
    '''
    #   Характеристики помещения
    PREMISESCHARACTERISTICS = (
        ('1', 'Отдельная квартира'), 
        ('2', 'Квартира коммунального заселения'), 
        ('3', 'Общежитие')
    )
    #   PremisesNum 	Номер помещения
    PremisesNum = models.CharField(max_length = 10, verbose_name = 'Номер помещения')
    #   Уникальный номер помещения в ГИС ЖКХ (например, MBp00381)
    UniqueNumber = models.CharField(max_length = 10, unique=True, blank = True, null = True, verbose_name = 'Идентификатор в ГИС ЖКХ')
    #   ID дома
    house = models.ForeignKey(             
        'house',
        on_delete=models.CASCADE,
        verbose_name = 'Дом',
    )
    #   ID подъезда
    Entrance = models.ForeignKey(
        'Entrance', 
        on_delete = models.CASCADE,
        null = True,
        verbose_name = 'Подъезд',
    )
    #   Характеристика помещения
    PremisesCharacteristic = models.CharField(              
        max_length = 1,
        choices = PREMISESCHARACTERISTICS,
        default = '1',
        blank = True,
        verbose_name = 'Характеристика',
    )
    #   TotalArea Общая площадь жилого помещения по паспорту помещения
    TotalArea = models.DecimalField(max_digits=25, decimal_places=4, blank = True, verbose_name = 'Общая площадь')
    #   GrossArea 	Жилая площадь жилого помещения по паспорту помещения
    GrossArea = models.DecimalField(max_digits=25, decimal_places=4, blank = True, verbose_name = 'Жилая площадь')
    #   Кадастровый номер
    CadastralNumber = models.CharField(max_length = 40, blank = True, verbose_name = 'Кадастровый номер')
    #   Дата создания
    created_date = models.DateTimeField(default = timezone.now, verbose_name = 'Когда создано')
    #   Автор
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, verbose_name = 'Кем создано')

    def __str__(self):
        return self.PremisesNum

# КОМНАТЫ
class LivingRoom(models.Model):
    #   RoomNumber 	PremisesNumType 	1..1 	Номер комнаты
    RoomNumber = models.CharField(max_length = 10, blank = True, verbose_name = 'Номер комнаты')
    #   Уникальный номер комнаты в ГИС ЖКХ (например, MBp00381)
    UniqueNumber = models.CharField(max_length = 10, unique=True, blank = True, null = True, verbose_name = 'Идентификатор в ГИС ЖКХ')
    #   ID дома
    house = models.ForeignKey(             
        'house',
        on_delete=models.CASCADE,
        verbose_name = 'Дом',
    )
    #   ID помещения
    ResidentialPremises = models.ForeignKey(
        'ResidentialPremises', 
        on_delete = models.CASCADE,
        verbose_name = 'Помещение',
    )
    #   Square 	PremisesAreaType 	0..1 	Площадь
    Square = models.DecimalField(max_digits=25, decimal_places=4, blank = True, verbose_name = 'Площадь')
    #   Кадастровый номер
    CadastralNumber = models.CharField(max_length = 40, blank = True, verbose_name = 'Кадастровый номер')
    #   Дата создания
    created_date = models.DateTimeField(default = timezone.now, verbose_name = 'Когда создано')
    #   Автор
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, verbose_name = 'Кем создано')

    def __str__(self):
        return self.RoomNumber

#   ЛИФТЫ
class Lift(models.Model):
    '''
    СПРАВОЧНИКИ
    '''
    #   Типы лифтов
    LIFTTYPES = (
        ('1', 'Грузовой'), 
        ('2', 'Пассажирский'), 
        ('3', 'Грузопассажирский')
    )
    #   FactoryNum 	string 	0..1 	Заводской номер
    FactoryNum = models.CharField(max_length = 20, blank = True, verbose_name = 'Заводской номер')
    #   Type 	nsiRef 	0..1 	Тип лифта. Ссылка на НСИ "Тип лифта" (реестровый номер 192)
    Type = models.CharField(              
        max_length = 1,
        choices = LIFTTYPES,
        default = '2',
        blank = True,
        verbose_name = 'Тип лифта',
    )
    #   ID дома
    house = models.ForeignKey(             
        'house',
        on_delete=models.CASCADE,
        verbose_name = 'Дом',
    )
    #   ID подъезда
    Entrance = models.ForeignKey(
        'Entrance', 
        on_delete = models.CASCADE,
        verbose_name = 'Подъезд',
    )
    #   Дата создания
    created_date = models.DateTimeField(default = timezone.now, verbose_name = 'Когда создано')
    #   Автор
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, verbose_name = 'Кем создано')

    def __str__(self):
        return self.FactoryNum
 

class organization(models.Model):
    inn = models.CharField(max_length = 12, verbose_name = 'ИНН')
    ogrn = models.CharField(max_length = 15, verbose_name = 'ОГРН')
    kpp = models.CharField(max_length = 9, blank = True, verbose_name = 'КПП')
    name = models.CharField(max_length = 160, verbose_name = 'Полное наименование')
    short_name = models.CharField(max_length = 100, blank = True, verbose_name = 'Сокращенное наименование')
    created_date = models.DateTimeField(default = timezone.now, verbose_name = 'Когда создано')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, verbose_name = 'Кем создано')

    def __str__(self):
        return self.short_name
