from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('insurances/', views.InsuranceList.as_view(), name='insurance_list'),
    path('insurances/<int:pk>', views.InsuranceDetail.as_view(), name='insurance_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('coverages/', views.CoverageList.as_view(), name='coverage_list'),
    path('coverages/<int:pk>', views.CoverageDetail.as_view(), name='coverage_detail'),
]
