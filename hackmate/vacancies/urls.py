import django.urls

import vacancies.views


app_name = "vacancies"

urlpatterns = [
    django.urls.path(
        "create/",
        vacancies.views.VacancyCreateView.as_view(),
        name="vacancy_create",
    ),
    django.urls.path(
        "",
        vacancies.views.VacancyView.as_view(),
        name="vacancies",
    ),
    django.urls.path(
        "<int:pk>/",
        vacancies.views.VacancyDetailView.as_view(),
        name="vacancy_detail",
    ),
]
