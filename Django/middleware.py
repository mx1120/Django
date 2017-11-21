#coding:utf-8
import logging, traceback
import simplejson as json

from django.conf import settings
from django.http.request import QueryDict
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, Http404


log = logging.getLogger(__name__)

class AuthenticationMiddleware(object):
	def process_request(self, request):
		try:
			return self._process_request(request)
		except:
			exc = traceback.format_exc()
			log.error(exc)

	def cross_domain(self, request, response=None):
		origin = request.META.get('HTTP_ORIGIN', '*')
		if request.method == 'OPTIONS' and not response:
			response = HttpResponse()
		if not response:
			return
		response['Access-Control-Allow-Origin'] = origin
		response['Access-Control-Allow-Methods'] = 'GET,POST'
		response['Access-Control-Allow-Credentials'] = 'true'
		response['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,Tbkt-Token,App-Type'
		response['Access-Control-Max-Age'] = '1728000'
		return response

	def _process_request(self, request):
		paths = request.path.split('/', 2)
		rootdir = paths[1]
		# REQUEST过期, 使用QUERY代替
		query = request.GET.copy()
		query.update(request.POST)
		# 把body参数合并到QUERY
		try:
			body = json.loads(request.body)
			query.update(body)
		except:
			pass
		request.QUERY = query

		r = self.cross_domain(request)
		if r:
			return r

