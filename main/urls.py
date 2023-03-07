from django.urls import path
from . import views

urlpatterns = [
    # BASHKY-BET
    path('', views.home, name='home'),
    path('bishkek/', views.bishkek, name='bishkek'),
    path('batken/', views.batken, name='batken'),
    path('jalal-abad/', views.jalal_abad, name='jalal_abad'),
    path('talas/', views.talas, name='talas'),
    path('naryn/', views.naryn, name='naryn'),
    path('yssyk-kol/', views.yssyk_kol, name='yssyk_kol'),
    path('chuy/', views.chuy, name='chuy'),
    # KITEPTER
    path('kitepter/', views.kitepter, name='kitepter'),
    # INSANDAR
    path('belgiluu-insandar/', views.belgiluu_insandar, name='belgiluu-insandar'),
    path('iskak-razzakov/', views.iskak_razzakov, name='iskak-razzakov'),
    path('jusup-abdrahmanov/', views.jusup_abdrahmanov, name='jusup-abdrahmanov'),
    path('alykul-osmonov/', views.alykul_osmonov, name='alykul-osmonov'),
    path('bubusara-beyshenalieva/', views.bubusara_beyshenalieva, name='bubusara-beyshenalieva'),
    path('cholponbay-tuloberdiev/', views.cholponbay_tuloberdiev, name='cholponbay-tuloberdiev'),
    path('gapar-aytiev/', views.gapar_aytiev, name='gapar-aytiev'),
    path('tattybubu-tursunbaeva/', views.tattybubu_tursunbaeva, name='tattybubu-tursunbaeva'),
    path('chyngyz-aytmatov/', views.chyngyz_aytmatov, name='chyngyz-aytmatov'),
    path('kasym-tynystanov/', views.kasym_tynystanov, name='kasym-tynystanov'),
    path('absamat-masaliev/', views.absamat_masaliev, name='absamat-masaliev'),
    path('bekmamat-osmonov/', views.bekmamat_osmonov, name='bekmamat-osmonov'),
    path('torobay-kulatov/', views.torobay_kulatov, name='torobay-kulatov'),
]