from django.shortcuts import render
from .models import Districts, Divisions

# Create your views here.

def district_list(request):
	districts = Districts.objects.all()
	return render(request, 'information/district_list.html', {'districts':districts })


def division_list(request):
	divisions = Divisions.objects.all()
	return render(request, 'information/division_list.html', {'divisions': divisions })

def dists_of_div(request, div_id):
	division = Divisions.objects.get(pk=div_id)
	district = Districts.objects.filter(division=division)
	context ={
		'district' : district,
	    'division' : division,
	}
 
	return render(request, 'information/dists_of_div.html', context)



