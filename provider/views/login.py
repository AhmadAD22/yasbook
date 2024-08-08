from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from auth_login.models import Provider

def login_view(request):
    if request.user.is_authenticated:
        return redirect('provider-main-dashboard')
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            try:
                provider=Provider.objects.get(phone=user.phone)
            except Provider.DoesNotExist:
                error_message = 'Is Not a provider account'
                return render(request, 'provider/provider_login.html', {'error_message': error_message})
            login(request, user)
            return redirect('provider-main-dashboard')
        else:
            error_message = 'Invalid phone number or password'
            return render(request, 'provider/provider_login.html', {'error_message': error_message})
    else:
        return render(request, 'provider/provider_login.html')