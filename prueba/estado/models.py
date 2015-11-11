from django.db import models
from django.contrib.auth.models import User
from mascota.models import Perfil_Mascota
from status.models import Status
from models import *

class Estado(models.Model):
	 Usuario=models.ForeignKey(User, null=False)
	 Mascota=models.ForeignKey(Perfil_Mascota, null=False) 


	 def __unicode__(self):
	 	return self.Mascota.nombre