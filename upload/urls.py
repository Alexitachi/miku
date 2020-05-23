from django.conf.urls import url
from . import views
from django.urls import path
from miku import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('register/', views.register_page, name='register_page'),
    path('profile/',views.profile, name='profile'),
    path('profile/update',views.profileupdate, name='profileupdate'),
    path('logout/',views.logout_view, name='logout'),
    path('books/', views.book_list, name='book_list'),
    path('books/all', views.book_all, name='book_all'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('delete/all/<pk>/', views.delete_city, name='delete_city'),
    path('topics/<int:pk>', views.topics, name='topics'),
    path('topics/add/<pk>/', views.topic, name='topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry,name='edit_entry'),
    path('query', views.query, name='query'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)