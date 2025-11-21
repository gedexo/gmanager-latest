from django.urls import path

from . import views

app_name = "marketing"

urlpatterns = [
    path("", views.EnquiryListView.as_view(), name="enquiry_list"),
    path("enquiry/<str:pk>/", views.EnquiryDetailView.as_view(), name="enquiry_detail"),
    path("new/enquiry/", views.EnquiryCreateView.as_view(), name="enquiry_create"),
    path(
        "enquiry/<str:pk>/update/",
        views.EnquiryUpdateView.as_view(),
        name="enquiry_update",
    ),
    path(
        "enquiry/<str:pk>/delete/",
        views.EnquiryDeleteView.as_view(),
        name="enquiry_delete",
    ),
    path(
        "followup/",
        views.EnquiryFollowupListView.as_view(),
        name="enquiryfollowup_list",
    ),
    path(
        "followup/<str:pk>/",
        views.EnquiryFollowupDetailView.as_view(),
        name="enquiryfollowup_detail",
    ),
    path(
        "new/followup/",
        views.EnquiryFollowupCreateView.as_view(),
        name="enquiryfollowup_create",
    ),
    path(
        "followup/<str:pk>/update/",
        views.EnquiryFollowupUpdateView.as_view(),
        name="enquiryfollowup_update",
    ),
    path(
        "followup/<str:pk>/delete/",
        views.EnquiryFollowupDeleteView.as_view(),
        name="enquiryfollowup_delete",
    ),
]
