import os
import datetime
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()

from vacancies.data import specialties, companies, jobs
from vacancies.models import Company, Specialty, Vacancy


if __name__ == '__main__':
    Specialty.objects.all().delete()
    Company.objects.all().delete()
    Vacancy.objects.all().delete()

    for company in companies:
        Company.objects.create(
            name=company['title'],
            logo='https://place-hold.it/100x60',
            employee_count=1
        )

    for speciality in specialties:
        Specialty.objects.create(
            code=speciality['code'],
            title=speciality['title'],
            picture='https://place-hold.it/100x60',
        )

    for vacancy in jobs:
        Vacancy.objects.create(
            title=vacancy['title'],
            specialty=Specialty.objects.get(code=vacancy['cat']),
            company=Company.objects.get(name=vacancy['company']),
            description=vacancy['desc'],
            salary_min=vacancy['salary_from'],
            salary_max=vacancy['salary_to'],
            published_at=datetime.date.fromisoformat(vacancy['posted']),
        )
