from django.urls import path

from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('payments/', views.payments, name='payments'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('complete/<list_id>', views.complete, name='complete'),
    path('uncomplete/<list_id>', views.uncomplete, name='uncomplete'),

]
