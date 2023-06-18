from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.all_finches, name='finches'),
    path('finches/<int:finch_id>/', views.finches_detail, name="details"),
    path('finches/create/', views.FinchCreate.as_view(), name="create"),
    #by convention, CBV's that work with individual models instances will expect a parameter of PK
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="update"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="delete"),
    path('finches/<int:finch_id>/add_feeding_', views.add_feeding, name="add_feeding"),
]