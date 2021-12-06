from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.contrib import messages


from .models import *

# Create your views here.
def index(request):
    return redirect('employee_view')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')


class LoginView(View):
    template_name = "employee/login.html"

    def get(self, request):
        next = self.request.GET.get('next')
        context = {'next': next}
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = self.request.GET.get('next')

        user = authenticate(request, username=username, password=password)
        print(username, password, user)
        if user is not None:
            login(request, user)
            if not next:
                return redirect('employee_view')
            else:
                return redirect(self.request.GET.get('next'))
        else:
            messages.error(request, 'Invalid username and/or password.')
            context = {'next': next}
            return render(request, self.template_name, context)

class EmployeeView(TemplateView):
    template_name = "employee/profile.html"
    #model = PersonalData

class EmployeeRegister(TemplateView):
    template_name = "employee/register.html"