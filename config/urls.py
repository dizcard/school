from django.contrib import admin
from django.urls import path, include
from library.views import BookView, UserView, UserBookView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    path('book/', BookView.as_view(), name='book'),
    path('user/', UserView.as_view(), name='user'),
    path('userbook/', UserBookView.as_view(), name='userbook'),
]
