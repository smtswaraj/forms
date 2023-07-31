from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.review),
    path('',views.review.as_view()),
    path('thanks',views.thanks)
]