from django.shortcuts import render
from earth.models import kullanici
from django.shortcuts import redirect
from earth.models import randevu
from django.conf.urls import url
from django.contrib import admin
from earth import views
from django.db.models import Q

# Create your views here.

def home_view(request):
    return render(request, "home.html", {})

def hakkimizda_view(request):
    return render(request, "hakkimizda.html", {})

def iletisim_view(request):
    return render(request, "iletisim.html", {})

def geridonusum_view(request):
    return render(request, "geridonusum.html", {})

def kayiol_view(request):
    if request.method == 'POST':
        q = kullanici(
            kAdi=request.POST.get("kAdi"),
            kSoyadi=request.POST.get("kSoyadi"),
            kTel=request.POST.get("kTel"),
            keMail=request.POST.get("keMail"),
            ktc=request.POST.get("ktc"),
            kimage=request.POST.get("kimage"),
            ksehir=request.POST.get("ksehir"),
            kilce=request.POST.get("kilce"),
            kmahalle=request.POST.get("kmahalle"),
            ksokak=request.POST.get("ksokak"),
            kno=request.POST.get("kno"),
            kullaniciA=request.POST.get("kullaniciA"),
            kullaniciS=request.POST.get("kullaniciS"),
            kullaniciTS=request.POST.get("kullaniciTS"),
        )
        q.save()
        return redirect('/index')
    return render(request, 'kayitol.html', {})

def randevu_view(request):
    return render(request, "randevu.html", {})

def randevuu_view(request):
    if request.method == 'POST':
        atr = request.POST.get('aTuru')
        if atr != '':
            firmaid = "1"
        q = randevu(
            kId_id=request.user.id,
            fId_id=firmaid,
            aTuru=request.POST.get('aTuru'),
            rTarih=request.POST.get('datepicker'),
            rSaat=request.POST.get('time'),
            aciklama=request.POST.get('message'),
        )
        q.save()
        return redirect('/index')
    return render(request, "randevuu.html")

def index_view(request):
    randevular = randevu.objects.all()
    return render(request, "index.html", {'randevular': randevular})

def duzenle(request, kId):
    q = kullanici.objects.get(kId=kId)
    if request.method == 'POST':
        q.kAdi = request.POST.get("kAdi"),
        q.kSoyadi = request.POST.get("kSoyadi"),
        q.kTel = request.POST.get("kTel"),
        q.keMail = request.POST.get("keMail"),
        q.ktc = request.POST.get("ktc"),
        q.kimage = request.POST.get("kimage"),
        q.ksehir = request.POST.get("ksehir"),
        q.kilce = request.POST.get("kilce"),
        q.kmahalle = request.POST.get("kmahalle"),
        q.ksokak = request.POST.get("ksokak"),
        q.kno = request.POST.get("kno"),
        q.kullaniciA = request.POST.get("kullaniciA"),
        q.kullaniciS = request.POST.get("kullaniciS"),
        q.kullaniciTS = request.POST.get("kullaniciTS"),
        q.save()
        return redirect('/index')
    return render(request, 'kayitol.html', {})

def sil(request, kId):
    q = kullanici.objects.get(kId=kId)
    q.delete()
    return redirect('/index')

