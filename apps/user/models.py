# -*- coding: utf-8 -*-
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.db.models import Avg, Count, Case, When, Q, Sum, F 
import statistics
# from .models  import User


class UserManager(BaseUserManager):

    def create_user(self, email, name, password, **kwargs):

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, password=password, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **kwargs):
        user = self.create_user(email, name, password, **kwargs)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(_('Отображаемое имя'), max_length=255, unique=True)
    last_name = models.CharField(_('Фамилия'), max_length=255, blank=True, null=True, default='')
    phone = models.BigIntegerField(_('Номер телефона'), unique=True, blank=True, null=True)
    email = models.EmailField(_('Электропочта'), max_length=255, unique=True)
    avatar = models.ImageField(_('Аватар'), upload_to='media/avatars', blank=True, null=True)
    is_active = models.BooleanField(_('Активный'), default=True)
    is_staff = models.BooleanField(_('Доступ в админ панель'), default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','last_name']

    def __unicode__(self):
        return u'{}'.format(self.name)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


