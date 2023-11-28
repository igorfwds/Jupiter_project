from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import CadastroForm, ReciboForm
from .models import *
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse


def paciente_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Pega o email do campo username
            email = form.cleaned_data['username']
            senha = form.cleaned_data['password']
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('homePaciente')
            else:
                print("Usuário ou senha incorreto!")
                messages.error(request, "Usuário ou senha incorreto!")
        else:
            print("Usuário ou senha incorreto!")
            messages.error(request, "Usuário ou senha incorreto!")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, './pagina_inicial.html')


def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            try:
                # Crie um usuário User separado
                user = User.objects.create_user(
                    username=form.cleaned_data['email'], password=form.cleaned_data['senha'])

                # Crie uma instância do paciente a partir do formulário
                paciente = form.save(commit=False)

                # Associe o usuário ao paciente
                paciente.user = user

                # Salve o paciente no banco de dados
                paciente.save()

                return redirect('sucessoCadastro')
            except Exception as e:
                print("Exceção ao tentar salvar o paciente:", str(e))
                return redirect('falhaCadastro')
        else:
            print("Erro ao cadastrar:", form.errors)
            return redirect('falhaCadastro')
    else:
        form = CadastroForm()
        return render(request, 'cadastrar.html', {'form': form})


def homePaciente(request):
    return render(request, 'homePaciente.html')


def sucessoCadastroView(request):
    return render(request, 'sucessoCadastro.html')


def falhaCadastroView(request):
    return render(request, 'falhaCadastro.html')


def exibir_exames(request):
    exames = Exame.objects.all()

    return render(request, 'exames.html', {'exames': exames})


def exibir_receituarios(request):
    receitas = Receituario.objects.all()

    return render(request, 'receituarios.html', {'receitas': receitas})


def examehemograma(request):
    return render(request, 'examehemograma.html')


def exameurina(request):
    return render(request, 'exameurina.html')


def receita(request):
    return render(request, 'receitavisu.html')


def exibir_recibos(request):
    recibos = Recibo.objects.all()

    return render(request, 'recibos.html', {'recibos': recibos})


def recibopag(request):
    return render(request, 'recibopag.html')


# Marcar Consulta

def booking(request):
    # Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.success(request, "Selecione o Médico!")
            return redirect('booking')

        # Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service

        return redirect('bookingSubmit')

    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
    })

# alteração para comitar pra azure
def bookingSubmit(request):
    times = [
        "8 AM", "8:30 AM", "9 AM", "9:30 AM", "10 AM", "10:30 AM", "11 AM", "11:30 AM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    maxDate = (today + timedelta(days=21)).strftime('%Y-%m-%d')

    # Recupera 'service' e 'day' da sessão
    service = request.session.get('service')
    day = request.session.get('day')

    # Verifica se os valores foram armazenados na sessão
    if not service or not day:
        messages.error(request, "Informações de serviço ou data não encontradas.")
        return redirect('booking')

    if request.method == 'POST':
        paciente_cpf = request.POST.get('paciente_cpf')
        time = request.POST.get('time')

        try:
            paciente = Paciente.objects.get(cpf=paciente_cpf)

            # Verifica se o horário e o dia estão disponíveis
            if day <= maxDate and day >= minDate:
                if Appointment.objects.filter(day=day, time=time).exists():
                    messages.error(request, "O Horário Selecionado já foi reservado!")
                else:
                    # Cria um novo agendamento
                    Appointment.objects.create(
                        user=paciente,
                        service=service,
                        day=day,
                        time=time,
                    )
                    messages.success(request, "Agendamento Salvo!")
                    return redirect('homePaciente')
            else:
                messages.error(request, "A data selecionada não está no período correto!")
        except Paciente.DoesNotExist:
            messages.error(request, "Nenhum paciente encontrado com o CPF fornecido.")

    return render(request, 'bookingSubmit.html', {
        'times': times,
        'minDate': minDate,
        'maxDate': maxDate,
    })


def userPanel(request):
    user = request.user
    appointments = Appointment.objects.filter(
        user=user.id).order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'user': user.id,
        'appointments': appointments,
    })

def userCancel(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.delete()
    return redirect('userPanel')


def userUpdate(request, id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day
    # Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    # 24h if statement in template:
    delta24 = (userdatepicked).strftime(
        '%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    # Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    # Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')

        # Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service

        return redirect('userUpdateSubmit', id=id)

    return render(request, 'userUpdate.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'delta24': delta24,
        'id': id,
    })


def userUpdateSubmit(request, id):
    user = request.user
    times = [
        "8 AM", "8:30 AM", "9 AM", "9:30 AM", "10 AM", "10:30 AM", "11 AM", "11:30 AM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')

    # Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, day, id)
    appointment = Appointment.objects.get(pk=id)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            paciente = get_object_or_404(Paciente, id=user.id)
                            AppointmentForm = Appointment.objects.filter(pk=id).update(
                                user=paciente,
                                service=service,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Agendamento Editado!")
                            return redirect('homePaciente')
                        else:
                            messages.success(
                                request, "O Horário Selecionado já foi reservado!")
                    else:
                        messages.success(
                            request, "A Data selecionada está cheia!")
                else:
                    messages.success(
                        request, "A Data selecionada está incorreta")
            else:
                messages.success(
                    request, "A data selecionada não está no período correto!")
        else:
            messages.success(request, "Selecione um Médico!")
        return redirect('userPanel')

    return render(request, 'userUpdateSubmit.html', {
        'times': hour,
        'id': id,
    })


def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    # Only show the Appointments 21 days from today
    items = Appointment.objects.filter(
        day__range=[minDate, maxDate]).order_by('day', 'time')

    return render(request, 'staffPanel.html', {
        'items': items,
    })


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    # Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range(0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def checkEditTime(times, day, id):
    # Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
