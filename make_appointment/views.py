from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def services_single(request):
    return render(request, 'services-single.html')

def contact(request):
    return render(request, 'contact.html')

def adoption(request):
    return render(request, 'adoption.html')
from django.shortcuts import render
from .models import Appointment

def make_appointment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        consultation = True if request.POST.get("consultation") == "on" else False
        if not all([name, email, phone, service, subject, message]):
            return render(request, "contact.html", {"error": "Please fill all required fields."})

        Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            service=service,
            subject=subject,
            message=message,
            consultation=consultation
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")
