from django.urls import path 
from . import views
urlpatterns = [
    path('', views.main),
    path('register', views.register),
    path('dashboard_login', views.dashboard_login),
    path('dash', views.dash),
    path('clearsession', views.clearSession),
    path('save_pie', views.save_pie),
    path('login', views.dashboard_login),
    path('delete/<int:id>', views.delete_by_id),
    path('edit/<int:id>', views.edit_by_id),
    path('update', views.update),
    path('show_all', views.show_all),
    path('details/<int:id>', views.details),

]