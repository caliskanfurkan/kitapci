#!/usr/bin/python
# -*- coding: utf-8 -*-

from kitapci.app.models import Kitap, Tag, Yazar
from django.contrib import admin

class TagInline(admin.StackedInline):
    model = Tag
    extra = 5

class KitapAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Kitap adı", {'fields': ['isim']}),
            ("Kitap detayları", {'fields': ["isbn","aciklama","yazarlar","eklenme_tarihi"]}),
            ("Anahtar kelimeler",{'fields':["taglar"]}),
            ]
    inlines= [TagInline]


admin.site.register(Kitap, KitapAdmin)
admin.site.register(Tag)
