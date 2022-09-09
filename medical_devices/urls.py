from django.urls import path
from .views import (
    DeviceListView, 
    DeviceDetailView, 
    DeviceCreateView,
    DeviceUpdateView,
    DeviceDeleteView,
)    
from . import views


urlpatterns = [
    path('', DeviceListView.as_view(), name='medical_devices-home'),
    path('Device/<int:pk>/', DeviceDetailView.as_view(), name='Device-detail'),
    path('Device/new/', DeviceCreateView.as_view(), name='Device-create'),
    path('Device/<int:pk>/update/', DeviceUpdateView.as_view(), name='Device-update'),
    path('Device/<int:pk>/delete/', DeviceDeleteView.as_view(), name='Device-delete'),
    path('about/', views.about, name='medical_devices-about'),
    
]

