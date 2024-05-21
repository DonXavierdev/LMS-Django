from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.views.decorators.cache import never_cache
def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")
def test_view(request):
    return render(request, 'index.html')
@never_cache
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')
@never_cache
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'home.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Redirect logged-in users to the home page
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)