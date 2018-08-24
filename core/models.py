from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Funcao(models.Model):
    nome = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.nome


class Profile(models.Model):
    acesso = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    nomeCompleto = models.CharField(max_length=50, null=True, blank=True, unique=True)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, null=True)
    rg = models.IntegerField(null=True, blank=True, unique=True)
    cpf = models.IntegerField(null=True, blank=True, unique=True)
    ctps = models.IntegerField(null=True, blank=True, unique=True)
    matricula = models.IntegerField(null=True, blank=True, unique=True)
    dataNascimento = models.DateField(null=True, blank=True)
    dataAdmissao = models.DateField(null=True, blank=True)
    observacao = models.TextField(max_length=500, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()