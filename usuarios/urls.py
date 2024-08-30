from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',views.Register.as_view(), name='signup'),
    path('login/',views.registro, name='login'),
    path('logout/',views.singout, name='logout'),
    path('me/', views.tu, name='tu'),
    path('edit/', views.editar, name="edit"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='recuperación/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='recuperación/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recuperación/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='recuperación/password_reset_complete.html'), name='password_reset_complete'),

    ]
