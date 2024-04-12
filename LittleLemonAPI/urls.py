from django.urls import path,include
from . import views

urlpatterns=[
  path('', include('djoser.urls')),
  path('menu-items',views.MenuItems.as_view()),
  path('menu-items/<int:pk>',views.MenuItemsPathUpdate.as_view()),
  path('users/users/me/',views.me),
  # path('new',views.NewHome.as_view())
]