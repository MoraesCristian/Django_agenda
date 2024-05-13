from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name= 'index' ),
    path('search/', views.search, name= 'search' ),
# CRUD
    path('contact/<int:contact_id>/detail/', views.contact2, name= 'contact2' ),
    path('contact/create/', views.create, name= 'create' ),
    # path('contact/<int:contact_id>/update/', views.contact2, name= 'contact2' ),
    # path('contact/<int:contact_id>/delete/', views.contact2, name= 'contact2' ),
    
]
