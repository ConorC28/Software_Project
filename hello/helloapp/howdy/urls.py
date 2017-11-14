# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
	url(r'^$', views.homePageView.as_view()),
	url(r'about/$', views.AboutPageView.as_view()),
]