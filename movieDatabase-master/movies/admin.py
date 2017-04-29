from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')

	search_fields = ('first_name', 'last_name')

class MovieAdmin(admin.ModelAdmin):
	list_display = ('title',  'release_date', 'language' )
	list_filter = ('release_date',)
	ordering = ('title', 'release_date', 'language', 'genre',)
	search_fields = ('title', )
	filter_horizontal = ('genre', 'tag', )
#	raw_id_fields = ('genre',)

class CrewAdmin(admin.ModelAdmin):
	list_display = ('crew_first_name', 'crew_last_name', 'role')
	search_fields = ('crew_first_name', 'crew_last_name', 'role',)

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('description', 'rating')
	search_fields = ('description',)
	

class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'middle_name', 'last_name', 'email', 'manager')
	ordering = ('first_name', 'last_name',)
	search_fields = ('first_name', 'middle_name', 'last_name', 'email',)

class GenreAdmin(admin.ModelAdmin):
	search_fields = ('g_name',)

class TagAdmin(admin.ModelAdmin):
	search_fields = ('t_name',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Review)