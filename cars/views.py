from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form = CarForm()
	msg = "The car has been created."
	if request.method == "POST":
		form = CarForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Car Created!!!!')
			return redirect("car-list")
	context = {
		"form":form,
		"msg": msg,

	}
	return render(request, 'create.html', context)


def car_update(request, car_id):
	car_obj = Car.objects.get(id=car_id)
	form = CarForm(instance=car_obj)
	msg = "The car has been updated."
	if request.method == "POST":
		form = CarForm(request.POST, request.FILES or None, instance=car_obj)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.INFO, 'Car Updated!!')
			return redirect('car-list')
	context = {
		"form":form,
		"obj":car_obj,
		"msg": msg,
	}
	return render(request, 'update.html', context)


def car_delete(request, car_id):
	Car.objects.get(id=car_id).delete()
	messages.add_message(request, messages.INFO, 'Car Deleted!!')
	return redirect("car-list")