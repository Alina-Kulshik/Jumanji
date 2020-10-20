from django.urls import path

from vacancies import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('vacancies/<int:vacancy_id>/', views.vacancy, name='vacancy'),
    path('vacancies/cat/<str:category>/', views.category, name='category'),
    path('companies/<int:company_id>/', views.company, name='company'),
]
