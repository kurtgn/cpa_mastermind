from django.db import models

# Create your models here.


class AdNetwork(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.name)


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.name)


class Offer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.name)


class AffiliateNetwork(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.name)


class Advert(models.Model):
    forum_name = models.CharField(max_length=30)
    skype_name = models.CharField(max_length=30)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '{}'.format(self.forum_name)


class Post(models.Model):
    details = models.TextField(max_length=500)
    url = models.URLField(max_length=500)
    ad_networks = models.ManyToManyField(AdNetwork)
    advert = models.ForeignKey(Advert)
    offers = models.ManyToManyField(Offer)
    affiliate_networks = models.ManyToManyField(AffiliateNetwork)
    countries = models.ManyToManyField(Country)
