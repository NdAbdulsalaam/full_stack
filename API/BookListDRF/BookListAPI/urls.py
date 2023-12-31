from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name='BookView'),
    path('books/<int:pk>/', views.SingleBookView.as_view(), name='SingleBookView'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('category/', views.CategoriesView.as_view()),
]