from django.shortcuts import render, redirect
from django.core.cache import cache

def index(request):
    status = cache.get('site_status', 'off')
    return render(request, 'status_app/index.html', {'status': status})

def set_on(request):
    cache.set('site_status', 'on')
    return redirect('index')

def set_off(request):
    cache.set('site_status', 'off')
    return redirect('index')