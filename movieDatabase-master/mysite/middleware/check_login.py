from django.shortcuts import render, redirect
from mysite.views import log_in

def CheckLogin(get_response):
	def middleware(request):
		if '/register/' in request.path or '/admin/' in request.path or '/login/' in request.path or 'email' in request.session:
			response = get_response(request)
		#option to display homepage without login if we want it later
			"""
		elif request.path == "/":
			print(request.path)
			response = get_response(request)
			"""
		else:
			response = redirect('/login/',request)
		
		return response
	return middleware
