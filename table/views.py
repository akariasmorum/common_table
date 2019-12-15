from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import unblockings
from .forms import UnblockingsForm
from time import time
import os

def index(request):
	form = UnblockingsForm()
	if request.method == 'POST':
		form = UnblockingsForm(request.POST)
		if form.is_valid():
			form.save()
		
	all_rows = list(unblockings.objects.all().values())
	return render(request, 'index.html', {
		'name': 'Michael',
		'table': all_rows,
		'form': form,
		})
	
def download(request):	
	try:
		import pandas as pd
		all_rows = list(unblockings.objects.all().values())
		df = pd.DataFrame(all_rows)
		file_path = 'temp-file{}.xlsx'.format(str(int(time())))
		df.to_excel(file_path, index=False)
		with open(file_path, 'rb') as file:
			response = HttpResponse(file.read(), content_type='application/vnd.ms-excel')
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
		
	except Exception:
		print(Exception)
