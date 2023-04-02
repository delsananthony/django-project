from django.urls import path

from core import views


urlpatterns = [
    path('login/', views.DjangoLoginView.as_view(), name='login'),
    path('logout/', views.DjangoLogoutView.as_view(), name='logout'),
    path('dashboard/', views.home, name='home'),
]
