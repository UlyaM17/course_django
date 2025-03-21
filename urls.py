from django.urls import path

from hr.views import generic_views as views


urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employees/profile/<int:pk>/', EmployeeProfileView.as_view(), name='employee_profile'),

]

# from hr.views.function_views import (
#     employee_create,
#     employee_delete,
#     employee_list,
#     employee_update,
# )
#
#
# urlpatterns = [
#     path('employees/', employee_list, name='employee_list'),
#     path('employees/create/', employee_create, name='employee_create'),
#     path('employees/update/<int:pk>/', employee_update, name='employee_update'),
#     path('employees/delete/<int:pk>/', employee_delete, name='employee_delete'),
# ]

