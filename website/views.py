from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def oferta(request):
    return render(request, "oferta.html", {})


def onas(request):
    return render(request, "onas.html", {})


def kontakt(request):
    return render(request, "kontakt.html", {})


@csrf_exempt
def zamowienie(request):
    return render(request, 'zamowienie.html')


@csrf_exempt
def wyslij(request):

    tlumaczenie_z = request.POST['tlumaczenie_z']
    tlumaczenie_do = request.POST['tlumaczenie_do']
    dane = request.POST['dane']
    liczba_znakow = request.POST['liczba_znakow']
    cena_hidden = request.POST['cena']
    rodzaj = request.POST['rodzaj']
    imie = request.POST['imie']
    nazwisko = request.POST['nazwisko']
    email = request.POST['email']
    telefon = request.POST['telefon']
    firma = request.POST['firma']
    firma_adres = request.POST['firma_adres']
    firma_nip = request.POST['firma_nip']
    plik = request.FILES.get('plik')
    termin = request.POST['termin']
    informacje = request.POST['informacje']

    message = '-'

    ctx = {
        'tlumaczenie_z': tlumaczenie_z,
        'tlumaczenie_do': tlumaczenie_do,
        'liczba_znakow': liczba_znakow,
        'cena_hidden': cena_hidden,
        'dane': dane,
        'rodzaj': rodzaj,
        'imie': imie,
        'nazwisko': nazwisko,
        'email': email,
        'telefon': telefon,
        'firma': firma,
        'firma_adres': firma_adres,
        'firma_nip': firma_nip,
        'termin': termin,
        'informacje': informacje,
    }

    try:
        html_body = get_template('email.html').render(ctx)

        subject, from_email, to = 'hello', 'hello@verbalegal.pl', 'ksurowiecki@icloud.com'

        msg = EmailMessage(subject, html_body, from_email=from_email, to=[to])
        msg.content_subtype = 'html'
        #msg.attach(plik.name, plik.read(), plik.content_type())
        msg.send()

    except BaseException as e:
        print(str(e))
        message = 'error'
        plik = 'error2'


    return render(request, 'wyslij.html', {'message': message, 'plik': plik})
