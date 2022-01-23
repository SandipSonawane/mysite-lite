from django.urls import path

from My_Portfolio import views as index_app_views
# from Top_Skills import views as top_skills_app_views

urlpatterns = [
    path('', index_app_views.index, name='index'),
]
