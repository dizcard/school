from django.urls import path
from .views import HomeView, UserView , BookView , UserBookView , DetailBookView
urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('books/', BookView.as_view(),name='books'),
    path('book/<int:pk>', DetailBookView.as_view(), name='book'),
    path('users/', UserView.as_view(), name='user'),
    path('userbooks/', UserBookView.as_view(), name='userbook'),
]
