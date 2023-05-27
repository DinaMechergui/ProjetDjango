from django.db import models
from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class Portfolio(models.Model):
    TYPE_CHOICES=[('acheve','acheve'),('en cours','en cours'),('request','request')]
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    description = models.TextField()
    services = models.CharField(max_length=200)
    completion_date = models.DateField()
    Img=models.ImageField(upload_to='static/assets/img/' ,blank=True)
    etat=models.CharField(max_length=50,choices=TYPE_CHOICES,default='request')
    
    desProjets = models.URLField(blank=True)
    def __str__(self):
        return self.title




class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    portfolio_examples = models.ManyToManyField('Portfolio', related_name='portfolio_examples')
    Img=models.ImageField(upload_to='static/assets/img/' ,blank=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    expertise = models.CharField(max_length=200)
    bio = models.TextField()
  
    linkedin_url = models.URLField(blank=True)
    personal_website = models.URLField(blank=True)
    Img=models.ImageField(upload_to='static/assets/img/' ,blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_embed_code = models.TextField(blank=True)

    def __str__(self):
        return self.address


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Mot de passe'}))
class BaseUserManager(BaseUserManager):
        def create_user(self, email, username, password=None):
            if not email:
                raise ValueError('Users must have an email address')
            if not username:
                raise ValueError('Users must have a username')

            user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self, email, username, password):
            user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
        )
            user.is_admin = True
            user.save(using=self._db)
            return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    


class ProjectRequestModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    contact = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
