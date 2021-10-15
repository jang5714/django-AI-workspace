from django.conf.urls import url
from admin.crime import views


urlpatterns = {
    url(r'create-model',views.create_crime_model),
    url(r'create-police',views.create_police_position),
    url(r'create-cctv',views.create_cctv_model),
    url(r'create-population',views.create_population_model),
    url(r'create-merge',views.merge_cctv_pop),
    url(r'sum-succes',views.sum_crime),
    url(r'process',views.process),
    url(r'crime_police',views.crime_police)

}