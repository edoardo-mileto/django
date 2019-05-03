from django.db import models

# Create your models here.

class Attore(models.Model):
    #idAttore = models.IntegerField()
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    dataNascita = models.DateField()
    nazionalita = models.CharField(max_length=20)

    def __str__(self):
        return self.cognome + " " + self.nome 

    class Meta:
        verbose_name = "Attore"
        verbose_name_plural = "Attori"

class Regista(models.Model):
    #idRegista = models.IntegerField()
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    dataNascita = models.DateField()
    nazionalita = models.CharField(max_length=20)

    def __str__(self):
        return self.cognome + " " + self.nome 

    class Meta:
        verbose_name = "Regista"
        verbose_name_plural = "Registi"

class Genere(models.Model):
    #idGenere = models.IntegerField()
    denominazione = models.CharField(max_length=30)
    img = models.URLField()

    def __str__(self):
        return self.denominazione

    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class Film(models.Model):
    #idFilm = models.IntegerField()
    titolo = models.CharField(max_length=100)
    annoUscita = models.DateField()
    trama = models.TextField()
    durata = models.FloatField()
    generi = models.ManyToManyField(Genere)
    attori = models.ManyToManyField(Attore)
    registi = models.ManyToManyField(Regista)
    lingua = models.CharField(max_length=20)
    img = models.URLField()
    url = models.URLField()
    disponibile = models.BooleanField(default='true')

    def __str__(self):
        return self.titolo 

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Film"