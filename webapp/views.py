from django.shortcuts import render, redirect
from .models import Reservas, Login
import openpyxl
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request, "index.html")

def reservar(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        cancha = request.POST.get("cancha")
        fecha = request.POST.get("fecha")
        hora = request.POST.get("hora")
        duracion = request.POST.get("duracion")
        cel = request.POST.get("cel")
        
        reservas_existente = Reservas.objects.filter(cancha=cancha,fecha=fecha,hora=hora).exists()

        if reservas_existente:
            return render(request, 'reservar.html', {'mensaje': 'Ya hay una reserva para esta cancha en la misma fecha y hora'})
        else:
            # Asignar el valor de pago antes de la verificación
            pago = request.POST.get("pago")
            if pago == 'on':
                pago = True
            else:
                pago = False
            
            # Guardar la reserva
            reserva = Reservas(nombre=nombre, apellido=apellido, cancha=cancha, fecha=fecha, hora=hora, duracion=1, cel=cel, pago=pago)
            reserva.save()
            return render(request, 'reservar.html', {'mensaje': 'Se generó una reserva a nombre de: ' + nombre + ' recuerda realizar el pago y enviar el comprobante'})
    return render(request, "reservar.html")

def reservas(request):
    if request.method == 'POST':
        # Obtener el ID de la reserva y el valor del checkbox de pago
        reserva_id = request.POST.get("reserva_id")
        pago = request.POST.get("pago")

        # Buscar la reserva por ID
        reserva = Reservas.objects.get(id=reserva_id)

        # Actualizar el valor de pago
        reserva.pago = True if pago == 'on' else False
        reserva.save()

    reservas = Reservas.objects.all()
    datos = {'reservas': reservas}
    return render(request, "reservas.html", datos)

def login(request):
    mensaje = ''  # Inicializar mensaje en caso de que no haya ningún mensaje específico
    
    if request.method == 'POST':
        usuario = request.POST.get("usuario")
        password = request.POST.get("password")
        
        try:
            user = Login.objects.filter(usuario=usuario, password=password).first()
        except Login.DoesNotExist:
            user = None
        
        if user is not None:
            return redirect('reservas')
        else: 
            mensaje = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
    return render(request, "login.html", {'mensaje': mensaje})


def exportar_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reservas.xlsx"'

    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = 'Reservas'

    headers = ['Nombre', 'Apellido', 'Cancha reservada', 'Fecha', 'Hora inicio', 'Duración','Celular','Pago']
    worksheet.append(headers)

    reservas = Reservas.objects.all()
    for reserva in reservas:
        row = [ reserva.nombre,reserva.apellido, reserva.cancha, reserva.fecha, reserva.hora, reserva.duracion, reserva.cel, reserva.pago]
        worksheet.append(row)

    workbook.save(response)
    return response
