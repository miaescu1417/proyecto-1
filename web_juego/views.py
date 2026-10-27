from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Página principal (CON CANDADITO)
@login_required
def index(request):
    return render(request, 'web_juego/index.html')

# Iniciar sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'web_juego/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'web_juego/login.html')

# Cerrar sesión
def logout_view(request):
    auth_logout(request)
    return redirect('login')

# Registrar
def registrar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'web_juego/registrar.html', {'error': 'Ese nombre de usuario ya existe'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'web_juego/registrar.html')

# Ver usuarios (CON CANDADITO)
@login_required
def usuarios(request):
    lista_usuarios = User.objects.all()
    return render(request, 'web_juego/usuarios.html', {'usuarios': lista_usuarios})