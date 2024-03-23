from django.shortcuts import render
def index(request):
	return render(request,'apps/index.html')
def about(request):	
    return render(request,'apps/about.html')
def service(request):
    return render(request,'apps/service.html')
def booking(request):
    return render(request,'apps/booking.html')
def contact(request):
    return render(request,'apps/contact.html')            