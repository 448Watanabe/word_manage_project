# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Word

from django.http import HttpResponse
from django.template import loader
from django.http import Http404



def index(request):
	word_list = Word.objects.all()
	"""
	output = '¥n, '.join([w.meaning for w in word_list])
	"""
	template = loader.get_template('word_manage_app/index.html')
	
	context = {
		'word_list' : word_list,
	}

	return HttpResponse(template.render(context, request))

def staticTest(request):

	template = loader.get_template('word_manage_app/staticTest.html')
	context = {}
	
	return HttpResponse(template.render(context, request))

def detail(request, word_id):
	"try,exceptの中身はget_object_or_404(Word, pk=word_id)で補えるが、理解の為に以下のように書く"
	try:
		word = Word.objects.get(pk = word_id)

	except Word.DoesNotExist:
		raise Http404("Word does not exist")

	context = {'word' : word}
	return render(request, 'word_manage_app/detail.html', context)
