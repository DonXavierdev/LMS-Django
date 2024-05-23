from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.views.decorators.cache import never_cache
from .models import Course,Section
@never_cache
def index(request):
    return render(request, 'index.html')

def test_view(request):
    return render(request, 'index.html')
@never_cache
def home(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')
@never_cache
def course_list(request):
    if request.user.is_authenticated:
        courses = Course.objects.all()
        return render(request, 'Course/courses.html', {'courses': courses})
    else:
        return redirect('login')
def course_detail(request, pk):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, pk=pk)
        sections = course.section_set.all() 
        return render(request, 'Course/course_detail.html', {'course': course, 'sections': sections})
    else:
        return redirect('login')
def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'dashboard.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)