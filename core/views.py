from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'core/home.html', {'user': request.user})