from django.db import models

# Create your models here.

class Tag(models.Model):
    isim = models.CharField(max_length=20)

    def __unicode__(self):
        return self.isim


class Yazar(models.Model):
    isim = models.CharField(max_length=20)

    def __unicode__(self):
        return self.isim


class Kitap(models.Model):
    isbn = models.CharField(max_length=10)
    isim = models.CharField(max_length=100)
    aciklama = models.CharField(max_length=250)
    yazarlar = models.ManyToManyField(Yazar)
    taglar = models.ManyToManyField(Tag)
    eklenme_tarihi = models.DateTimeField('Eklenme tarihi')

    def __unicode__(self):
        return self.isim

