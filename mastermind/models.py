from django.contrib.auth.models import User, UserManager
from django.db import models

# Create your models here.


class AdNetwork(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Источник трафика'
        verbose_name_plural = 'Источники трафика'

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.name)


class Country(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Гео'
        verbose_name_plural = 'Гео'

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.name)


class Offer(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Оффер'
        verbose_name_plural = 'Офферы'

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.name)


class AffiliateNetwork(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Офферные сети'

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.name)


class CustomUser(User):
    """User with app settings."""
    skype_name = models.CharField(max_length=50)
    forum_name = models.CharField(max_length=50)
    objects = UserManager()

    class Meta:
        verbose_name = 'Адверт'
        verbose_name_plural = 'Адверты'


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    details = models.TextField(max_length=500, verbose_name="Комментарий")
    url = models.URLField(max_length=500, unique=True)
    ad_networks = models.ManyToManyField(AdNetwork)
    user = models.ForeignKey(CustomUser, verbose_name="Адверт")
    offers = models.ManyToManyField(Offer)
    affiliate_networks = models.ManyToManyField(AffiliateNetwork)
    countries = models.ManyToManyField(Country)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'