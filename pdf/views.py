#encoding: utf-8
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'inicio.html')


def pdf(request):
    nombre = request.POST['nombre']
    nota = request.POST['nota']

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="factura.pdf"'

    p = canvas.Canvas(response)


    p.drawString(50, 800, "nombre: "+nombre)
    p.drawString(50, 785, "nota: "+nota)

    p.showPage()
    p.save()
    return response