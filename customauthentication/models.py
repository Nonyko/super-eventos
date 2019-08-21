from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyUserManager(BaseUserManager):
    def create_user(self, username, cpf, email, password=None):
        """
        Creates and saves a User with the given email, nome, username and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.username = username
        user.cpf = cpf

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, cpf, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')


        user = self.model(
            email=self.normalize_email(email),
        )

        user.username = username
        user.cpf = cpf

        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    username = models.CharField(max_length=255, unique=True,)
    cpf = models.CharField('cpf', max_length=255, unique=True)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    aluno = models.BooleanField(default=True)
    avaliador = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf', 'email']

    class Meta:
        verbose_name_plural = 'usuarios'
        verbose_name = 'usuario'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_aluno(self):
        "Is the user a aluno?"
        # Simplest possible answer: All admins are staff
        return self.aluno

    @property
    def is_avaliador(self):
        "Is the user a avaliador?"
        # Simplest possible answer: All admins are staff
        return self.avaliador








class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    '''
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
    )
    '''


