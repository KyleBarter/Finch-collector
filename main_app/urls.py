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
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]