# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Need-Help(models.Model):

    #__Need-Help_FIELDS__
    category = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    request = models.TextField(max_length=255, null=True, blank=True)

    #__Need-Help_FIELDS__END

    class Meta:
        verbose_name        = _("Need-Help")
        verbose_name_plural = _("Need-Help")



#__MODELS__END
