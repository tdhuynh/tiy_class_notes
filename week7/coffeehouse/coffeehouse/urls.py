from django.conf.urls import url
from django.contrib import admin

from menu_api.views import SpecialListCreateAPIView, SpecialUpdateDestroyAPIView, IngredientListAPIView, IngredientDetailAPIView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^obtain-token/$', obtain_auth_token),
    url(r'^ingredients/$', IngredientListAPIView.as_view(), name='ingredient_list_api_view'),
    url(r'^ingredients/(?P<pk>\d+)/$', IngredientDetailAPIView.as_view(), name='ingredient_detail_api_view'),
    url(r'^specials/$', SpecialListCreateAPIView.as_view(), name='special_list_create_api_view'),
    url(r'^specials/(?P<pk>\d+)/$', SpecialUpdateDestroyAPIView.as_view(), name='special_update_destroy_api_view'),
    url(r'^/$',)    
]
