#coding:utf-8
from Django.libs.utils import ajax
import json
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {}
	context['hello'] = 'Hello World!'
	context['user'] = 'mx'
	context['list'] = [
		{'name':'1', 'tell':'175'},
		{'name':'2', 'tell':'177'},
		{'name':'3', 'tell':'179'},
		{'name':'4', 'tell':'181'}
	]
	return render(request, 'index/index.html', context)

def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	rsp = ''
	if username == 'mengxiang' and password == 'zuishuai':
		rsp = 'ok'
		message = ''
	else:
		rsp = 'fail'
		message = '账号密码错误'
	return HttpResponse(json.dumps({'response':rsp, 'message':message}))