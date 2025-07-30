from django.urls import path
from . import views

urlpatterns = [
    # Define your employee app URLs here
    # Example: path('list/', views.employee_list, name='employee_list'),
    # path('detail/<int:id>/', views.employee_detail, name='employee_detail'),
    path('<int:pk>/', views.employee_details),  # Example for detail view
]