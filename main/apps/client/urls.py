from django.urls import path
from . import views



urlpatterns = [
    path(
        "client-statistics/<int:pk>/", 
        view=views.client_statistics_api_view,
        name="client_statistics"
    )
]
