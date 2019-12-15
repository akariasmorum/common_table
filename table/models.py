from django.db import models

# Create your models here.
class unblockings(models.Model):

	STATUSES = (
				("Р","Разблокирован"),
				("П", "Перенесен"),
				)
	fir_ci = models.CharField(max_length=10)
	incident_num = models.CharField(max_length=20)
	status = models.CharField(max_length=1, choices=STATUSES)
	date = models.CharField(max_length=10)
	row_adder = models.CharField(max_length=200)
	note = models.CharField(max_length=300)

	def validate(self):
		pass
