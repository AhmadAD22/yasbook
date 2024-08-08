from django.shortcuts import render,redirect

def provider_main_dashboard(request):
    return render(request,'provider/provider_main.html')