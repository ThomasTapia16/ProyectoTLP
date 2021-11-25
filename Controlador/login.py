from django.core.checks import messages
from django.shortcuts import render
from Modelo.models import Funcionario

#user gaston.marquez
#pwd profegaston
def logging(request):

    if request.method == 'POST':
        
        try:
            datosFuncionario = Funcionario.objects.get(usuario = request.POST['username'], contrasena = request.POST['pwd'])
            print("usuario",datosFuncionario)
            request.session['usuario'] = datosFuncionario.usuario
            return render(request,'login/home.html')
        except datosFuncionario.DoesNotExist as e:
            messages.succes(request,'Datos incorrectos aweonao culiao...')
    
    return render(request,'login/login.html')
