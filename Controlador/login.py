from django.core.checks import messages
from django.http.request import HttpRequest
from django.shortcuts import render
from Modelo.models import Funcionario
#user gaston.marquez
#pwd profegaston

def logging(request):
    if request.method == 'POST':
        
        try:
            
            datosFuncionario = Funcionario.objects.get(usuario = request.POST['username'], contrasena = request.POST['pwd'])
            request.session['usuario'] = datosFuncionario.usuario
            funcionario = Funcionario(datosFuncionario.rut,datosFuncionario.usuario,datosFuncionario.contrasena)
            
            
            return render(request,'login/home.html')
            
        except datosFuncionario.DoesNotExist:
            messages.succes(request,'Datos incorrectos, inténta nuevamente.')
    
    #funcActivo = Funcionario(datosFuncionario.rut,datosFuncionario.usuario,datosFuncionario.contrasena)
    return render(request,'login/login.html')

