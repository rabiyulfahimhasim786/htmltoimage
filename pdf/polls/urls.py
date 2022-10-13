from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdfurl/', views.pdfurl, name='pdfurl'),
    path('pdf/', views.PdfList.as_view()),
    path('pdf/<int:pk>/', views.PdfDetail.as_view()),
    #path('fileuploading/', views.uploadings, name='uploadings'),
]


urlpatterns = format_suffix_patterns(urlpatterns)