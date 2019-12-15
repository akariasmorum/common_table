from django.forms import ModelForm, Textarea, DateField, CharField
from .models import unblockings
from django import forms
import re
#attrs = {'class': 'form-control', 'placeholder':"date" , 'aria-label':"date",  'aria-describedby': "basic-addon1"}

class UnblockingsForm(ModelForm):
	class Meta:
		model = unblockings
		fields =   ["fir_ci",
					"incident_num",
					"status",
					"date",
					"row_adder",
					"note",]
		widgets = {
			'fir_ci': 		forms.TextInput(attrs={'class': 'custom-input no-border'}),
			'incident_num': forms.TextInput(attrs={'class': 'custom-input no-border'}),			
			'date':   		forms.TextInput(attrs = {'class': 'custom-input no-border'}),
			'row_adder': 	forms.TextInput(attrs={'class': 'custom-input no-border'}),
			'status': 		forms.Select(attrs={'class': 'custom-input no-border'}),
			'note': 		forms.TextInput(attrs={'class': 'custom-input no-border'}),
		}
		#form-control no-border
	
	def clean_fir_ci(self):
		ci = self.cleaned_data['fir_ci']
		if not re.findall('^CI\d+$', ci):
			raise forms.ValidationError("КЭ не соответствует паттерну ^CI\d+$")			
		return ci
		
	def clean_incident_num(self):
		data = self.cleaned_data['incident_num']
		if not re.findall('^IM\d+$|^ЗНО\d+$', data):
			raise forms.ValidationError("Инцидент не соответствует паттерну ^IM\d+$|^ЗНО\d+$")			
		return data
		
	def clean_date(self):
		data = self.cleaned_data['date']
		if not re.findall('^\d{4}-\d{2}-\d{2}$', data):
			raise forms.ValidationError("Дата должна быть в формате YYYY-MM-DD")			
		return data	
	