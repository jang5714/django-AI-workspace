from django.conf.urls import url
from admin.jarviis import views


urlpatterns = {
    url(r'jarviis-model',views.create_jarviis_model),
    url(r'jarviis-message',views.create_message_model),

}