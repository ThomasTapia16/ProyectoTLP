from django.core.checks import messages
from django.http.request import HttpRequest
from django.shortcuts import render
from Clases.clases.Usuario import Usuario
from Modelo.models import Funcionario,Cliente
#user gaston.marquez
#pwd profegaston

# if request.method == 'POST':
#     datosFuncionario = Funcionario.objects.get(usuario = request.POST['username'], contrasena = request.POST['pwd'])
#     request.session['usuario'] = datosFuncionario.usuario
#     funcionario = Funcionario(datosFuncionario.rut,datosFuncionario.usuario,datosFuncionario.contrasena)

# print(funcionario.__str__)

def logging(request):
    if request.method == 'POST':
        
        try:
            datosFuncionario = Funcionario.objects.get(usuario = request.POST['username'], contrasena = request.POST['pwd'])
            request.session['usuario'] = datosFuncionario.usuario
            funcionario = Funcionario(datosFuncionario.rut,datosFuncionario.usuario,datosFuncionario.contrasena)
            return render(request,'login/home.html')
            
        except datosFuncionario.DoesNotExist:
            messages.succes(request,'Datos incorrectos, inténta nuevamente.')
   
    # funcActivo = Funcionario(datosFuncionario.rut,datosFuncionario.usuario,datosFuncionario.contrasena)
    return render(request,'login/login.html')

def adduser(request):
    if  request.method=="POST":
        rut=request.POST["rut"]
        correo=request.POST["correo"]
        nombre=request.POST["nombre"]
        deuda=request.POST["deuda"]
        telefono=request.POST["telefono"]

        a = Cliente(rut=rut,correo=correo,nombre=nombre,deuda=deuda,telefono=telefono)
        a.save()

        messages.success(request,"El cliente"+request.POST['nombre']+" se registro exitosamente")
        return render(request,'controlador/adduser.html')
    else:
        return render(request,'controlador/adduser.html')
    


    


