from django.shortcuts import redirect, render

from django.http import HttpResponse

def test_view(request):
    return render(request, 'index.html')
