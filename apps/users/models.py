# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')

        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=255)
    email = models.EmailField('Correo Electrónico', unique=True, max_length=255)
    name = models.CharField('Nombre(s)', max_length=200, blank=True, null=True)
    last_name = models.CharField('Apellido(s)', max_length=200, blank=True, null=True)
    image = models.ImageField('Imagen de Perfil', upload_to='perfil/',
                              max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historial = HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD = 'username'  # para identificar al usuario
    REQUIRED_FIELDS = ['email', 'name', 'last_name']  # valores pedidos en consola al crear usuario

    def natural_key(self):
        return self.username

    def __str__(self):
        return f'{self.name} {self.last_name}'

    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     return True
