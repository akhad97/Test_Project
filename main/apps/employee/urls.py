from django.urls import path
from . import views



urlpatterns = [
    path(
        "employee-statistics/<int:pk>/", 
        view=views.employee_statistics_api_view,
        name="employee_statistics"
    ),
    path(
        "allemployee-statistics/",
        view=views.all_employee_statistics_api_view,
        name="all_employee_statistics" 
    )
]
