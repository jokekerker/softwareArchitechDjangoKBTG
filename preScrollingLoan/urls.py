from django.urls import path

from . import views

app_name = 'preScrollingLoan'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('<int:profile_id>/change_status/', views.change_status, name='change_status'),
]
