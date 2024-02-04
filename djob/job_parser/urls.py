from django.urls import path
from . import views

urlpatterns = [
    path('some/', views.ExampleView.as_view(template_name='some.html')),
    path('base/<str:lang>/', views.fill_base),
    path('get/<str:lang>/', views.get_vbl)
]
