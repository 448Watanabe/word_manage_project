# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Word, Expression, Reference

"""
このクラスを追加する事で、Modelクラスのaccessというフィールドを
adminページから見れて、且つ編集不可の状態にする

"""
class WordAdmin(admin.ModelAdmin):
    readonly_fields=('access',)

# 以下により管理ページでワードのaddなどをする事が出来るようになる
admin.site.register(Word, WordAdmin)
admin.site.register(Expression)
admin.site.register(Reference)
