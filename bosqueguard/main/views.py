from django.shortcuts import render, redirect
from .forms import EvaluacionAmbientalForm
from time import sleep
from .models import EvaluacionAmbiental

# Create your views here.
def CalcularPuntajeSeccion1(seccion):
    puntaje = 0
    for (idx, respuesta) in enumerate(seccion):
        if idx%2 != 0 and respuesta == True:
            puntaje += 2
    return puntaje

def CalcularPuntajeSeccion2(seccion):
    puntaje = 0
    for respuesta in seccion:
        if respuesta == True:
            puntaje += 2.5
    return puntaje

def CalcularPuntajeSeccion3Y4(seccion):
    if seccion[0] == True:
        puntaje = 5
    else:
        puntaje = 0
    return puntaje

def CalcularPuntajeSeccion5(seccion):
    diferenciaDeRuido = seccion[1] - seccion[0]
    if diferenciaDeRuido <= 0:
        puntaje = 0
    elif 0 < diferenciaDeRuido <= 5:
        puntaje = 2
    elif 5 < diferenciaDeRuido <= 10:
        puntaje = 4
    elif 10 < diferenciaDeRuido <= 15:
        puntaje = 6
    elif 15 < diferenciaDeRuido <= 20:
        puntaje = 8
    else:
        puntaje = 10
    return puntaje

def CalcularPuntajeSeccion6(seccion):
    porcentajeDeRestauracion = (seccion[2]/((seccion[0])-seccion[1])) * 100
    if porcentajeDeRestauracion >= 100:
        puntaje = 0
    elif 100 > porcentajeDeRestauracion >= 90:
        puntaje = 1
    elif 90 > porcentajeDeRestauracion >= 80:
        puntaje = 2
    elif 80 > porcentajeDeRestauracion >= 70:
        puntaje = 3
    elif 70 > porcentajeDeRestauracion >= 60:
        puntaje = 4
    elif 60 > porcentajeDeRestauracion >= 50:
        puntaje = 5
    elif 50 > porcentajeDeRestauracion >= 40:
        puntaje = 6
    elif 40 > porcentajeDeRestauracion >= 30:
        puntaje = 7
    elif 30 > porcentajeDeRestauracion >= 20:
        puntaje = 8
    elif 20 > porcentajeDeRestauracion >= 10:
        puntaje = 9
    else:
        puntaje = 10
    return puntaje

def CalcularPuntajeSeccion7(seccion):
    puntaje = 0
    for respuesta in seccion:
        if respuesta == False:
            puntaje += 1.25
    return puntaje

def CalcularPuntajeSeccion8(seccion):
    puntaje = 0
    for respuesta in seccion:
        if respuesta == True:
            puntaje += 2.5
    return puntaje

def CalcularPuntajeSeccion10(seccion):
    puntaje = 0
    for (idx, respuesta) in enumerate(seccion):
        if (idx == 0 or idx == 1) and respuesta == True:
            puntaje += 5
    return puntaje
                        
def CalcularPuntajeSeccion11(seccion):
    if seccion[0] == True:
        puntaje = 5
    else:
        puntaje = 0
    return puntaje

def CalcularPuntajeSeccion12(seccion):
    if seccion[0] == True:
        puntaje = 10
    else:
        puntaje = 0
    return puntaje

def CalcularPuntajeSeccion13(seccion):
    puntaje = 0
    for respuesta in seccion:
        if respuesta == True:
            puntaje += 5
    return puntaje

def CalcularPuntajeSeccion14(seccion):
    puntaje = 0
    for (idx, respuesta) in enumerate(seccion):
        if (idx == 0 or idx == 1) and respuesta == True:
            puntaje += 2.5
    return puntaje

def resultados(request):
    id = request.session.get('saved_id', None)
    resultados = EvaluacionAmbiental.objects.get(id=id)
    return render(request, 'resultados.html', {'resultados':[resultados]})

def evaluacion_ambiental(request):
    if request.method == 'POST':
        # Seccion 1
        seccion1 = [bool(request.POST.get('sec1_1')), bool(request.POST.get('sec1_2')), bool(request.POST.get('sec1_3')), bool(request.POST.get('sec1_4')), bool(request.POST.get('sec1_4')), bool(request.POST.get('sec1_5')), bool(request.POST.get('sec1_6')), bool(request.POST.get('sec1_7')), bool(request.POST.get('sec1_8')), bool(request.POST.get('sec1_9')), bool(request.POST.get('sec1_10'))]
        # Seccion 2
        seccion2 = [bool(request.POST.get('sec2_1')), bool(request.POST.get('sec2_2'))]
        # Seccion 3
        seccion3 = [bool(request.POST.get('sec3_1')), bool(request.POST.get('sec3_2'))]
        # Seccion 4
        seccion4 = [bool(request.POST.get('sec4_1')), bool(request.POST.get('sec4_2'))]
        # Seccion 5
        seccion5 = [float(request.POST.get('sec5_1')), float(request.POST.get('sec5_2'))]
        # Seccion 6
        seccion6 = [float(request.POST.get('sec6_1')), float(request.POST.get('sec6_2')), float(request.POST.get('sec6_3'))]
        # Seccion 7
        seccion7 = [bool(request.POST.get('sec7_1')), bool(request.POST.get('sec7_2')), bool(request.POST.get('sec7_3')), bool(request.POST.get('sec7_4'))]
        # Seccion 8
        seccion8 = [bool(request.POST.get('sec8_1')), bool(request.POST.get('sec8_2'))]
        # Seccion 9
        seccion9 = bool(request.POST.get('sec9_1'))
        # Seccion 10
        seccion10 = [bool(request.POST.get('sec10_1')), bool(request.POST.get('sec10_2')), bool(request.POST.get('sec10_3')), bool(request.POST.get('sec10_4'))]
        # Seccion 11
        seccion11 = [bool(request.POST.get('sec11_1')), bool(request.POST.get('sec11_2'))]
        # Seccion 12
        seccion12 = [bool(request.POST.get('sec12_1')), bool(request.POST.get('sec12_2'))]
        # Seccion 13
        seccion13 = [bool(request.POST.get('sec13_1')), bool(request.POST.get('sec13_2'))]
        # Seccion 14
        seccion14 = [bool(request.POST.get('sec14_1')), bool(request.POST.get('sec14_2')), bool(request.POST.get('sec14_3')), bool(request.POST.get('sec14_4'))]
        # Seccion 15
        seccion15 = [bool(request.POST.get('sec15_1')), bool(request.POST.get('sec15_2')), bool(request.POST.get('sec15_3'))]
        puntajeSeccion1 = CalcularPuntajeSeccion1(seccion1)
        puntajeSeccion2 = CalcularPuntajeSeccion2(seccion2)
        puntajeSeccion3 = CalcularPuntajeSeccion3Y4(seccion3)
        puntajeSeccion4 = CalcularPuntajeSeccion3Y4(seccion4)
        puntajeSeccion5 = CalcularPuntajeSeccion5(seccion5)
        puntajeSeccion6 = CalcularPuntajeSeccion6(seccion6)
        puntajeSeccion7 = CalcularPuntajeSeccion7(seccion7)
        puntajeSeccion8 = CalcularPuntajeSeccion8(seccion8)
        if seccion9 == True:
            puntajeSeccion9 = 5
        else:
            puntajeSeccion9 = 0
        puntajeSeccion10 = CalcularPuntajeSeccion10(seccion10)
        puntajeSeccion11 = CalcularPuntajeSeccion11(seccion11)
        puntajeSeccion12 = CalcularPuntajeSeccion12(seccion12)
        puntajeSeccion13 = CalcularPuntajeSeccion13(seccion13)
        puntajeSeccion14 = CalcularPuntajeSeccion14(seccion14)
        resultado = puntajeSeccion1 + puntajeSeccion2 + puntajeSeccion3 + puntajeSeccion4 + puntajeSeccion5 + puntajeSeccion6 + puntajeSeccion7 + puntajeSeccion8 + puntajeSeccion9 + puntajeSeccion10 + puntajeSeccion11 + puntajeSeccion12 + puntajeSeccion13 + puntajeSeccion14
        datosParaBD = {
            'PuntajeSeccion1': puntajeSeccion1,
            'PuntajeSeccion2': puntajeSeccion2,
            'PuntajeSeccion3': puntajeSeccion3,
            'PuntajeSeccion4': puntajeSeccion4,
            'PuntajeSeccion5': puntajeSeccion5,
            'PuntajeSeccion6': puntajeSeccion6,
            'PuntajeSeccion7': puntajeSeccion7,
            'PuntajeSeccion8': puntajeSeccion8,
            'PuntajeSeccion9': puntajeSeccion9,
            'PuntajeSeccion10': puntajeSeccion10,
            'PuntajeSeccion11': puntajeSeccion11,
            'PuntajeSeccion12': puntajeSeccion12,
            'PuntajeSeccion13': puntajeSeccion13,
            'PuntajeSeccion14': puntajeSeccion14,
            'PuntajeTotal': resultado
        }
        form = EvaluacionAmbientalForm(datosParaBD)
        if form.is_valid():
            instance = form.save()
            id = instance.pk
            request.session['saved_id'] = id
            return redirect('resultados')
        
    else:
        form = EvaluacionAmbientalForm()

    return render(request, 'ambiental.html')

# def results(request, pk):
