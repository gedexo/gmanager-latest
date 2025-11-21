from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path("", views.ClientListView.as_view(), name="client_list"),
    path("client/<str:pk>/", views.ClientDetailView.as_view(), name="client_detail"),
    path("new/client/", views.ClientCreateView.as_view(), name="client_create"),
    path(
        "client/<str:pk>/update/",
        views.ClientUpdateView.as_view(),
        name="client_update",
    ),
    path(
        "client/<str:pk>/delete/",
        views.ClientDeleteView.as_view(),
        name="client_delete",
    ),
]
