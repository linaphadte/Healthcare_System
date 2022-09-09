from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)    
from .models import Device


"""Device =[
{
        
        'Name': 'Ventilator',
        'Company': 'GE',
        'Content': 'First post',
        'Category': 'Respiratory',
        'Author':'testuser1',
        
},
{    

        
        'Name': 'Defibrillator',
        'Company': 'Philips',
        'Content': 'Second post',
        'Category': 'Cardiology',
        'Author':'testuser1',
        
}
 ]"""

def home(request):
    context = {
        'Device': Device.objects.all
    }
    
    return render(request, 'medical_devices/home.html', context)

class DeviceListView(ListView):
    model=Device 
    template_name =  'medical_devices/home.html' 
    context_object_name = 'Device'

class DeviceDetailView(DetailView):
    model= Device

class DeviceCreateView(LoginRequiredMixin, CreateView):
    model= Device
    fields= ['Name', 'Category', 'Company','Content','image']  

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)
        
class DeviceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Device
    fields= ['Name', 'Category', 'Company', 'Content','image']   

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Device = self.get_object()
        if self.request.user == Device.Author:
            return True
        return False    

class DeviceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Device 
    success_url= '/'    

    def test_func(self):
        Device = self.get_object()
        if self.request.user == Device.Author:
            return True
        return False          

def about(request):
    return render(request, 'medical_devices/about.html',{'TITLE':'About'})
