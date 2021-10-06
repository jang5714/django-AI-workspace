from django.conf.urls import url
from admin.crime import views


urlpatterns = {
    url(r'create-model',views.create_crime_model),
}