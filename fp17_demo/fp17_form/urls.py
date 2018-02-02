from django.urls import path

from . import views


app_name = 'fp17_form'

urlpatterns = [
    path('', views.FP17FormWizard.as_view(), name='index'),
]
