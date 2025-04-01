from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return render(request, 'welcome_page.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def d_management(request):
    return render(request, 'doctor_management_booking.html')


def p_dashboard(request):
    return render(request, 'patient_dashboard.html')


def d_appointment(request):
    return render(request, 'doctor_appointments.html')


def d_dashboard(request):
    return render(request, 'doctor_dashboard.html')


def p_management(request):
    return render(request, 'patient_management.html')


def p_prescription(request):
    return render(request, 'patient_prescription.html')


def p_records(request):
    return render(request, 'patient_records.html')


def p_booking(request):
    return render(request, 'patient_booking.html')
