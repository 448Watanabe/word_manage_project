# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reference(models.Model):
	reference = models.CharField(max_length=128, default = "english text reference.")
	# referenceにdefaultの引数がないとpython3 manage.py makemigrationsするとエラーが起きる

	def __str__(self):
		return self.reference[:20]


class Word(models.Model): #この時のmodelsはファイル名？Modelはクラス名?
	new_word = models.CharField('新しいワード', max_length=128)
	# 「新しい言葉」という引数を渡すと表記が「new_word」から「新しい言葉」に変わる
	meaning = models.TextField()
	# reference = models.ManyToManyField(Reference)
	reference = models.ForeignKey(Reference, null=True, on_delete=models.PROTECT)
	# verbose_name="参照"
	"""
	example = models.TextField(verbose_name = "例文")
	後から付け加えようとするとエラーが出る
	"""
	note = models.TextField()
	first_date = models.DateTimeField('first day registering this word.')
	access = models.IntegerField(default = 0, editable = False)
	
	def __str__(self):
		return self.new_word
	
class Expression(models.Model):
	expression = models.CharField(max_length=128)
	meaning = models.TextField()
	reference = models.ManyToManyField(Reference)
	note = models.TextField()

	def __str__(self):
		return self.expression




