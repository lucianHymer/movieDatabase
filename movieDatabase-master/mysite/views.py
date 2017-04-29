from django.shortcuts import render, redirect
from django.http import HttpResponse  
import datetime
from movies.models import *
from mysite.forms import *


def is_manager(request):
	return 'manager' in request.session
def must_be_manager_response():
	return HttpResponse('Must be logged in as a manager to complete this function')


def edit_movie(request,movie_id=None):
	if is_manager(request):
		if request.method == 'POST':
			if movie_id:
				movie_instance = Movie.objects.get(id=movie_id)
			else:
				movie_instance = None
				
			if 'action' in request.POST:
				movie_form = MovieForm(request.POST,instance=movie_instance)
				if request.POST['action'] == 'Submit Movie':
					genre_form = GenreForm()
					disable_empty_checks(genre_form)
					tag_form = TagForm()
					disable_empty_checks(tag_form)
					force_empty_checks(movie_form,'tag')
					if movie_form.is_valid():
						new_movie = movie_form.save()
						return redirect('/movie/?id=%s'%new_movie.id, request)

				elif request.POST['action'] == 'Add Tag': 
					disable_empty_checks(movie_form)
					genre_form = GenreForm(request.POST)
					disable_empty_checks(genre_form)
					tag_form = TagForm(request.POST)
					force_empty_checks(tag_form)
					if tag_form.is_valid():
						tag_form.save()
						tag_form=TagForm()
						disable_empty_checks(tag_form)

				elif request.POST['action'] == 'Add Genre': 
					disable_empty_checks(movie_form)
					tag_form  = TagForm(request.POST)
					disable_empty_checks(tag_form)
					genre_form = GenreForm(request.POST)
					force_empty_checks(genre_form)
					if genre_form.is_valid():
						genre_form.save()
						genre_form=GenreForm()
						disable_empty_checks(genre_form)
			else:
				movie_form = MovieForm(instance=movie_instance)
				genre_form = GenreForm()
				tag_form   = TagForm()
				disable_empty_checks(genre_form)
				disable_empty_checks(tag_form  )

		else:
			genre_form = GenreForm()
			movie_form = MovieForm()
			tag_form   = TagForm()
			disable_empty_checks(movie_form)
			disable_empty_checks(genre_form)
			disable_empty_checks(tag_form  )

		options = {'movie_form':movie_form,'genre_form':genre_form,'tag_form':tag_form, 'is_manager': is_manager(request)}
		if movie_id:
			options['movie_id'] = movie_id
		return render(request,'edit_movie.html',options)
	else:
		return HttpResponse('Must be logged in as a manager to edit movies')

def home_page(request):
	return render(request, 'home_page.html', { 'is_manager': is_manager(request)})
	
def contributions(request):
	return render(request, 'contributions.html', { 'is_manager': is_manager(request)})

def manager_page(request):
	if is_manager(request):
		return render(request, 'manager_page.html',{ 'is_manager': is_manager(request)})
	else:
		return HttpResponse('Must be logged in as a manager to access this page.')

def log_in(request):
	errors = []
	if 'email' in request.session:
		return log_out(request)
	else:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				user = User.objects.filter(email=form.cleaned_data['email'])
				if not user:
					errors.append('User not found.')
					return render(request, 'log_in.html', {'errors': errors})
				else:
					user = user.filter(password=form.cleaned_data['password'])
					if not user:
						errors.append('password is incorrect')
						return render(request, 'log_in.html', {'errors': errors})
					else:
						user = user.get()
						request.session['email'] = user.email
						request.session['userID'] = user.id
						request.session['username'] = user.first_name + ' ' + user.last_name
						response_string = "Hello %s!"%user.first_name
						if user.manager:
						    request.session['manager'] = True
						    response_string += " You are a manager."
						elif 'manager' in request.session:
						    # If prviously logged in as manager,
						    # need to delete key and mark as modified
						    del request.session['manager']
						    request.session.modified = True
						# Cookies will expire when browser closes
						request.session.set_expiry(0)
#						return render(request, home_page(request), {'is_manager': is_manager(request)})
						return home_page(request)
		else:
        		form = LoginForm();
		return render(request,'log_in.html', {'form':form})

def log_out(request):
	if 'manager' in request.session:
		del request.session['manager']
	if 'email' in request.session:
		del request.session['email']
	request.session.modified = True
	return redirect('/login/',request)

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			login_form = LoginForm(request.POST)
			return render(request,'log_in.html', {'form':login_form})
	else:
		form = RegisterForm()

	return render(request,'register.html', {'form':form})


def edit_crew(request,crew_id=None):
	if is_manager(request):
		if crew_id:
			crew_instance = Crew.objects.get(id=crew_id)
		else:
			crew_instance = None
		if request.method == 'POST' and request.POST.get('action','') == 'Submit Crew Member':
			crew_form = CrewForm(request.POST,instance=crew_instance);
			if crew_form.is_valid():
				crew_form.save()
			else:
				return HttpResponse('Invalid form input')
		else:
			crew_form = CrewForm(instance=crew_instance)

		return render(request,'edit_crew.html',{'crew_form':crew_form,'crew_id':crew_id,
							'is_manager': is_manager(request)})
	else:

		return HttpResponse('Must be logged in as a manager to edit crew')

def modify_crew(request):
	if is_manager(request):
		if request.method == "POST":
			if 'crew_id' in request.POST:
				crew_id = request.POST['crew_id']
				if request.POST['operation'] == 'Modify':
					return edit_crew(request,crew_id);
				elif request.POST['operation'] == 'Remove':
					Crew.objects.filter(id=crew_id).delete()
					
		crew_members = Crew.objects.all().order_by('crew_last_name')
		return render(request, 'modify_crew.html',{'crew_members':crew_members, 'is_manager': is_manager(request)})
	else:
		return HttpResponse('Must be logged in as a manager to edit crew')


def disable_empty_checks(form):
	for field in form.fields:
	    form.fields[field].required = False

def force_empty_checks(form,except_for=[]):
	for field in form.fields:
		if field not in except_for:
			form.fields[field].required = True


def search(request):
	errors = []
	g_ids = []
	if 'Search' in request.GET:
		movies = Movie.objects.all()
		if 'sort_by' in request.GET:
			sort_by = request.GET['sort_by']
			if sort_by == 'title':
				movies = movies.order_by('title')
			elif sort_by == 'runtime':
				movies = movies.order_by('duration')
			elif sort_by == 'year':
				movies = movies.order_by('release_date')
		if 'g_id' in request.GET:
			g_ids = request.GET.getlist('g_id')
			if g_ids:
				movies = movies.filter(genre__id__in=g_ids)
		if 'tag_q' in request.GET:
			tag_q = request.GET['tag_q']
			if tag_q:
				movies = movies.filter(tag__t_name__icontains=tag_q)
		if 'crew_q' in request.GET:
			crew_q = request.GET['crew_q']
			if crew_q:
				movies = movies.filter(crew__crew_first_name__icontains=crew_q)
		if 'crew_q2' in request.GET:
			crew_q2 = request.GET['crew_q2']
			if crew_q2:
				movies = movies.filter(crew__crew_last_name__icontains=crew_q2)
		if 'title_q' in request.GET:
			title_q = request.GET['title_q']
			if title_q:
				movies = movies.filter(title__icontains=title_q)
		return render(request, 'search_results.html', {'genre': Genre.objects.filter(id__in=g_ids), 
								'tag': tag_q,
								'crew': crew_q,
								'title': title_q,
								'movies': movies.distinct,
								'is_manager': is_manager(request)})

	else:

		genres = Genre.objects.all()	
		return render(request, 'search_form.html', {'errors': errors,
							    'genres': genres,
							    'is_manager': is_manager(request)})

							



def movie(request):

	if 'id' in request.GET:
		ID = request.GET['id']
		results = Movie.objects.get(pk=ID)
		genre = Genre.objects.filter(movie__id=ID)
		tags = Tag.objects.filter(movie__id=ID)
		crew = Crew.objects.filter(m_id=ID)
		review = Review.objects.filter(movie__id=ID)
		
		user_id = request.session['userID']
		review_form = ReviewForm(initial={'movie': ID, 'user': user_id})
		tag_form = TagForm()

		
		return render(request, 'movie_info.html',
                             {'movie': results, 'genre': genre,
			      'tags': tags, 'crew': crew, 'ID': ID,
			      'reviews': review, 'is_manager': is_manager(request), 'review_form': review_form, 'tag_form': tag_form})

def add_review(request):

	if request.method == "POST":
		review_instance = None
		review_form = ReviewForm(request.POST, instance=review_instance)

		if review_form.is_valid():
			review_form.save()
		else:
			return HttpResponse('Invalid form input')
	return HttpResponse("Thanks for the comment. Go back and refresh to see your comment!")

def add_tag(request):
	if request.method == "POST":
		if 'movie_id' in request.POST:
			movie_id = request.POST['movie_id']
			tag_form = TagForm(request.POST)
			results = Movie.objects.get(pk=movie_id)
			if tag_form.is_valid():
				tag_form.save()
				genre_form = GenreForm()
				disable_empty_checks(genre_form)
				tag_form = TagForm()
				disable_empty_checks(tag_form)
				movie_instance = Movie.objects.get(id=movie_id)
				movie_instance.tag.add(Tag.objects.get(t_name=request.POST['t_name']))
				movie_form = MovieForm(instance=movie_instance)
				
		else:
			return HttpResponse('Invalid form input')
	return redirect('/movie/?id=%s'%movie_instance.id, request)


def promote(request):
	if is_manager(request):
		if request.method == "POST":
			if 'to_be_promoted' in request.POST:
				new_manager_emails = request.POST.getlist('to_be_promoted')
				for email in new_manager_emails:
					new_manager = User.objects.get(email=email)
					new_manager.manager = True
					new_manager.save()
				return HttpResponse('Successfully promoted %s'%', '.join(new_manager_emails))
		else:
			normal_users = User.objects.filter(manager=False).order_by('email')
			return render(request, 'promote.html',{'users':normal_users, 'is_manager': is_manager(request)})
	else:
		return HttpResponse('Must be logged in as a manager to promote')

def modify_movie(request):
	if is_manager(request):
		if request.method == "POST":
			if 'movie_id' in request.POST:
				movie_id = request.POST['movie_id']
				if request.POST['operation'] == 'Modify':
					return edit_movie(request,movie_id);
				elif request.POST['operation'] == 'Remove':
					Movie.objects.filter(id=movie_id).delete()
					
		movies = Movie.objects.all().order_by('title')
		return render(request, 'modify_movie.html',{'movies':movies, 'is_manager': is_manager(request)})
	else:
		return HttpResponse('Must be logged in as a manager to edit movies')
