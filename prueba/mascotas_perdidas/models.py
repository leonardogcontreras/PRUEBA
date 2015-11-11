from django.db import models
from django.contrib.auth.models import User
from estado.models import Estado
from status.models import Status
from models import *

class Mascotas_Perdidas(models.Model):
	 estado=models.ForeignKey(Estado, null=False)
	 status=models.ForeignKey(Status, null=False) 
	 recompenza=models.IntegerField()

	 def __unicode__(self):
	 	return self.estado.Mascota.nombre