from django.urls import path,include
from . import views

urlpatterns=[
  path('', include('djoser.urls')),
  # path('new',views.NewHome.as_view())
]