from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import LocalPlane, InternationalPlane, CargoPlane, Emergency

@login_required
def index(request):
    num_localplane=LocalPlane.objects.all().count()
    num_internationalplane=InternationalPlane.objects.all().count()
    num_cargoplane=CargoPlane.objects.all().count()
    num_emergency=Emergency.objects.all().count()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    context = {
        'num_localplane':num_localplane,
        'num_internationalplane':num_internationalplane,
        'num_cargoplane':num_cargoplane,
        'num_emergency':num_emergency,
        'num_visits':num_visits,
    }
    return render(
        request,
        'index.html',
        context,
    )



from django.views import generic

class AprononeListView(LoginRequiredMixin, generic.ListView):
    model = LocalPlane
    
class AprononeDetailView(LoginRequiredMixin, generic.DetailView):
    model = LocalPlane
    
class AprontwoListView(LoginRequiredMixin, generic.ListView):
    model = InternationalPlane
    
class AprontwoDetailView(LoginRequiredMixin, generic.DetailView):
    model = InternationalPlane
    
class ApronthreeListView(LoginRequiredMixin, generic.ListView):
    model = CargoPlane
    
class ApronthreeDetailView(LoginRequiredMixin, generic.DetailView):
    model = CargoPlane
    
class EmergencyListView(LoginRequiredMixin, generic.ListView):
    model = Emergency
    
class EmergencyDetailView(LoginRequiredMixin, generic.DetailView):
    model = Emergency
    
def contact(request):
    return render(
        request,
        'contact.html',
    )
def about(request):
    return render(
        request,
        'about.html',
    )
def tandc(request):
    return render(
        request,
        'tandc.html',
    )
def privacy(request):
    return render(
        request,
        'privacy.html',
    )

from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import UserForm

class UserFormView(View):
    form_class = UserForm
    template_name = 'catalog/registration_form.html'
    
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form':form})

        