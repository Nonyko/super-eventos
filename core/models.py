from django.db import models
from customauthentication.models import User
# Create your models here.
class Evento(models.Model):

    nome = models.CharField(blank=True, max_length=100)
    descricao = models.CharField(blank=True, max_length=700)
    startdate = models.DateTimeField(max_length=100, null=True, blank=True)
    enddate = models.DateTimeField(max_length=100, null=True, blank=True)
    local = models.CharField(blank=True, max_length=300)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='eventoscriados')
    convidados = models.ManyToManyField(User, blank=True, related_name='convidadoemeventos')

    class Meta:
        verbose_name_plural = 'eventos'
        verbose_name = 'evento'

    def __str__(self):
        return self.nome


    def isEventRelatedtouser(self, user):
        isrelated = False
        if self.owner == user:
            isrelated = True
        else:
            if user in self.convidados.all():
                isrelated = True
        return isrelated


class Atracao(models.Model):
    nome = models.CharField(blank=True, max_length=100)
    descricao = models.CharField(blank=True, max_length=700)
    evento = models.ForeignKey(Evento, null=True, on_delete=models.CASCADE, related_name='atracoes')
    date = models.DateTimeField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'atracao'
        verbose_name = 'atracao'

    def __str__(self):
        return self.nome