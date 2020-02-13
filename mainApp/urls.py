from django.urls import path
from . import views

app_name = "pdf"

urlpatterns = [
    path("", views.index, name="home"),
    path("generate/", views.MyPDFView.as_view(), name="make_pdf")
]