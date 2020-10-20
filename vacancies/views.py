from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render

from vacancies.models import Company, Specialty, Vacancy


def index(request):
    categories = Specialty.objects.all()
    vacancies = Vacancy.objects.all()
    companies = Company.objects.all()
    return render(request, 'index.html', context={
        'categories': categories,
        'vacancies': vacancies,
        'companies': companies,
    })


def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies.html', context={
        'vacancies': vacancies,
    })


def vacancy(request, vacancy_id):
    try:
        vacancies = Vacancy.objects.get(pk=vacancy_id)
    except vacancies.DoesNotExist:
        raise Http404
    return render(request, 'vacancy.html', context={
        'vacancies': vacancies,
    })


def category(request, category):
    try:
        categories = Specialty.objects.get(code=category)
    except categories.DoesNotExist:
        raise Http404
    return render(request, 'category.html', context={
        'categories': categories,
    })


def company(request, company_id):
    try:
        companies = Company.objects.get(pk=company_id)
    except companies.DoesNotExist:
        raise Http404
    return render(request, 'company.html', context={
        'companies': companies,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
