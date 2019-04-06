from blog_app import views
from django.urls import path

urlpatterns=[
# path('',views.index,name='index')
path('new',views.form_name_view,name='form'),
path('viewposts',views.PostListView.as_view(),name='detail')
]
