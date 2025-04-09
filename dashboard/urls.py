from django.urls import path
from . import views

urlpatterns = [

    path("",views.admin_low,name='admin_low'),
    path("createplacement",views.createplacement,name='createplacement'),
    path("viewplacement",views.viewplacement,name='viewplacement'),
    path("updateplacement",views.updateplacement,name='updateplacement'),
    path("readplacement/<int:id>/view/",views.read_placement.as_view(),name='readplacement'),
    path('create_placement_opportunity/', views.create_placement_opportunity, name='create_placement_opportunity'),
    path('view_placement',views.view_placement.as_view(),name='view_placement'),
    path('update_placement',views.update_placement.as_view(),name='update_placement'),
    path('edit_placement/<int:id>/', views.edit_placement.as_view(), name='edit_placement'),
    path("delete_placement",views.delete_placement.as_view(),name="delete_placement"),

    #siri's urls

    path('create_course/', views.create_course, name='create_course'),
    path('create_course_opportunity/', views.create_course_opportunity, name='create_course_opportunity'),
    path('course_view/', views.course_view.as_view(), name='course_view'),
    path('delete_course/',views.delete_course.as_view(), name='delete_course'),
    path('edit_course/<int:course_id>/', views.edit_course.as_view(), name='edit_course'),
    path("read_course/<int:course_id>/view/",views.read_course.as_view(),name='read_course'),
    path('update_course/', views.update_course.as_view(), name='update_course'),
    path('category/', views.category_page, name='category_page'),
    path('create_category/', views.create_category, name='create_category'),
    path('category_view/', views.category_view.as_view(), name='category_view'),
    path('delete_category/',views.delete_category.as_view(), name='delete_category'),
    path('edit_category/<str:name>',views.edit_category.as_view(), name='edit_category'),
    path("read_category/<str:name>/view/",views.read_category.as_view(),name='read_category'),
   
]