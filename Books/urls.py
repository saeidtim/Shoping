from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from.views import BookListView, BookDetailView, BookCreateView, BookUpdateView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail_view'),
    path('create/', BookCreateView.as_view(), name='create_view'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='update_view'),

]
