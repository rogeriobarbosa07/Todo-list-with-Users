from django.shortcuts import render, redirect
from .admin import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

# Create your views here.

def register(request):
        form = CustomUserCreationForm()
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
    
            if form.is_valid():
                user = form.save(commit=False)
                user.is_valid = False
                user.save()
                messages.success(request, 'Registrado. Agora faça o login para começar!')
                return redirect('index')

            else:
                print('invalid registration details')
                
        return render(request, "registration/register.html",{"form": form})

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user-name')
        pass_word = request.POST.get('pass-word')

        # inserindo informações do form para autenticar um usuário
        user = authenticate(username=user_name, password=pass_word)

        if user: # se a autenticação retornar um usuário
            login_django(request, user) # função que loga de fato o usuário no sistema
            return redirect('home')
        
        # se a autenticação não retornar um usuário
        messages.warning('Usuário ou senha incorretos! Tente novamente')
        return redirect('login') # recarrega a página
    
    return render(request, 'registration/login.html', {})