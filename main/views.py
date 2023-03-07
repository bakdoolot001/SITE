from django.shortcuts import render


# BASHKY-BET
def home(request):
    return render(request, 'main/BASHKY-BET/base.html')


def bishkek(request):
    return render(request, 'main/BASHKY-BET/bishkek.html')


def batken(request):
    return render(request, 'main/BASHKY-BET/batken.html')


def jalal_abad(request):
    return render(request, 'main/BASHKY-BET/jalal-abad.html')


def talas(request):
    return render(request, 'main/BASHKY-BET/talas.html')


def naryn(request):
    return render(request, 'main/BASHKY-BET/naryn.html')


def yssyk_kol(request):
    return render(request, 'main/BASHKY-BET/yssyk-kol.html')


def chuy(request):
    return render(request, 'main/BASHKY-BET/chuy.html')


# KITEPTER
def kitepter(request):
    return render(request, 'main/KITEPTER/main.html')


# INSANDAR
def belgiluu_insandar(request):
    return render(request, 'main/INSANDAR/belgiluu-insandar.html')


def iskak_razzakov(request):
    return render(request, 'main/INSANDAR/iskak-razzakov.html')


def jusup_abdrahmanov(request):
    return render(request, 'main/INSANDAR/jusup-abdrahmanov.html')


def alykul_osmonov(request):
    return render(request, 'main/INSANDAR/alykul-osmonov.html')


def bubusara_beyshenalieva(request):
    return render(request, 'main/INSANDAR/bubusara-beyshenalieva.html')


def cholponbay_tuloberdiev(request):
    return render(request, 'main/INSANDAR/cholponbay-tuloberdiev.html')


def gapar_aytiev(request):
    return render(request, 'main/INSANDAR/gapar-aytiev.html')


def tattybubu_tursunbaeva(request):
    return render(request, 'main/INSANDAR/tattybubu-tursunbaeva.html')


def chyngyz_aytmatov(request):
    return render(request, 'main/INSANDAR/chyngyz-aytmatov.html')


def kasym_tynystanov(request):
    return render(request, 'main/INSANDAR/kasym-tynystanov.html')


def absamat_masaliev(request):
    return render(request, 'main/INSANDAR/absamat-masaliev.html')


def bekmamat_osmonov(request):
    return render(request, 'main/INSANDAR/bekmamat-osmonov.html')


def torobay_kulatov(request):
    return render(request, 'main/INSANDAR/torobay-kulatov.html')