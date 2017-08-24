from django import forms
from django.forms import ModelForm
from movies.models import User, Movie, Crew, Genre,Tag, Review

class LoginForm(forms.Form):
	email = forms.EmailField(label='Email', max_length=30)
	password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('username','email','password')


class RegisterForm(ModelForm):
	confirm_password=forms.CharField(label='Confirm password', max_length=20, widget=forms.PasswordInput())


	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm password does not match"
				)

	class Meta:
		model = User
		widgets = {
		'password': forms.PasswordInput(),
		}

		fields = ['middle_name','last_name','email','password',
                  'confirm_password', 'date_of_birth','sex']
		#fields = ['first_name','middle_name','last_name','email','password',
                 # 'confirm_password', 'date_of_birth','sex']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title','description','release_date','language', 'duration', 'genre','tag']

class CrewForm(ModelForm):
	class Meta:
		model = Crew
		labels = {'m_id': 'Movies'}
		fields = ['crew_first_name','crew_last_name','role','m_id']

class GenreForm(ModelForm):
	class Meta:
		model = Genre
		labels = {'g_name': ''}
		fields = ['g_name']

class TagForm(ModelForm):
	class Meta:
		model = Tag
		labels = {'t_name': ''}
		fields = ['t_name']

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		labels = {'user': 'User', 'movie': 'Movie'}
		fields = ['description', 'rating', 'user', 'movie']

#class RegisterForm(forms.Form):
#	GENDER_CHOICES = (
#		('M', 'Male'),
#		('F', 'Female'),
#		('O', 'Other'),
#	)
#	u_first_name = forms.CharField(label='First Name',max_length=15)
#	u_middle_name = forms.CharField(label='Middle Name',max_length=15,required=False)
#	u_last_name = forms.CharField(label='Last Name',max_length=15)
#	email = forms.EmailField(label='Email',max_length=30)
#	password = forms.CharField(label='Password',max_length=20)
#	dob = forms.DateField(label='Date of Birth')
#	sex = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
