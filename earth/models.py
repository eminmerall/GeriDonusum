from django.db import models


# Create your models here.

image = models.ImageField(null=True, blank=True)

# verbose_name : Form, admin sayfalarında görünecek ad, girilmezse alan adı kullanılır.
# db_column : veritabanında kullanılacak ismi belirler, kullanılmazsa alan adı kullanılır.

# default : Boş gelirse eklenecek değer.
# blank : form için kullanılır, true girilirse boş geçilmesine izin verir.
# null : true girilirse veri tabanında boş değer alabilir.
# unique : true girilirse değerlerin tekrar etmesine izin vermez(primary key mantığı)
# editable : false seçilirse ilgi alan form ve admin panellerde gözükmez
# db_index : index oluşturmak için kullanılır, true seçilir
# help_text : ürün ismi için açıklayıcı metin
# related_name : ilişki kurulacak ifade

"""
DateTimeField: Tarih veZaman
            auto_now_add= "true" Eklendiğinde otomatik oluşur
            auto_now= "true" güncellendiğinde tarihi günceller
        DateField : Tarih
        TimeField : Zaman

BooleanField: doğru, yanlış ve boş değerleri alabilir



"""
class kullanici(models.Model):
    kId = models.AutoField(primary_key=True)
    kAdi = models.CharField(max_length=100, verbose_name='Adı', db_column='Adı')
    kSoyadi = models.CharField(max_length=100, verbose_name='Soyadı', db_column='Soyadı')
    kTel = models.CharField(max_length=20, verbose_name='Telefon', db_column='Telefon')
    keMail = models.EmailField(verbose_name='E-Mail', db_column='Email')
    ktc = models.CharField(max_length=11, verbose_name='T.C.', db_column='T.C.')
    kimage = models.FileField(null=True, blank=True)
    ksehir = models.CharField(max_length=400, verbose_name='Şehir', db_column='Şehir')
    kilce = models.CharField(max_length=100, verbose_name='İlçe', db_column='İlçe')
    kmahalle = models.CharField(max_length=100, verbose_name='Mahalle', db_column='Mahalle')
    ksokak = models.CharField(max_length=100, verbose_name='Sokak', db_column='Sokak')
    kno = models.CharField(max_length=50, verbose_name='No', db_column='No')
    kullaniciA = models.CharField(max_length=50, verbose_name='Kullanıcı Adı', db_column='Kullanıcı Adı')
    kullaniciS = models.CharField(max_length=50, verbose_name='Şifre', db_column='Şifre')
    kullaniciTS = models.CharField(max_length=50, verbose_name='Tekrar Şifre', db_column='Tekrar Şifre')


class firma(models.Model):
    fId = models.AutoField(primary_key=True)
    fAdi = models.CharField(max_length=200, verbose_name='Adı', db_column='Adı')
    fTel = models.CharField(max_length=20, verbose_name='Telefon', db_column='Telefon')
    fAdres = models.CharField(max_length=400, verbose_name='Adres', db_column='Adres')
    feMail = models.EmailField(verbose_name='E-Mail', db_column='Email')

class randevu(models.Model):
    rId = models.AutoField(primary_key=True)
    kId = models.ForeignKey(kullanici, on_delete=models.CASCADE)
    fId = models.ForeignKey(firma, on_delete=models.CASCADE)
    aTuru = models.CharField(max_length=50, verbose_name='Atık Türü', db_column='Atık Türü')
    rTarih = models.DateField(verbose_name='Tarih', db_column='Tarih')
    rSaat = models.TimeField(verbose_name='Saat', db_column='Saat')
    aciklama = models.CharField(max_length=100, verbose_name="Açıklama", db_column='Açıklama', null=True)



