#coding:utf-8
from Django.libs.utils import ajax
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {}
	context['hello'] = 'Hello World!'
	return render(request, 'index/index.html', context)

def login(request):
	print 1111111
	# return HttpResponse('this is login API')
	username = request.POST.get('username')
	password = request.POST.get('password')
	context = {}
	context['username'] = username
	context['password'] = password
	return render(request, 'login.html', context)
	# args = request.QUERY.casts(username=str,password=str)
	# username = args.username
	# password = args.password
	# if username == 'test' and password == 'yuzhouwudishuai':
	# 	res = ajax.ajax_ok()
	# else:
	# 	res = ajax.ajax_fail(message='账号密码错误')
	# return res