from django.urls import path
from demo import views

urlpatterns = [
    path('ping/', views.DemoAPIPost.as_view()),
    path('info/', views.DemoAPIGet.as_view()),
]
