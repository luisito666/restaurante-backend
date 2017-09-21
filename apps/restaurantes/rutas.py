from django.conf.urls import  include, url

from .views import RestauranteLista, RestauranteDetalle, ImgUpload, ramdom_rest, delete_rest

from rest_framework import routers

router = routers.DefaultRouter()
router.register('imagen', ImgUpload, 'imagen')

urlpatterns = [
    	url(r'^api/$', RestauranteLista.as_view()),
		url(r'^api/(?P<pk>[0-9]+)/$', RestauranteDetalle.as_view()),
		url(r'^api/', include(router.urls)),
		url(r'^api/ramdon',ramdom_rest, name='rest-random' ),
		url(r'^api/delete/(?P<pk>[0-9]+)/$',delete_rest, name='delete_rest' ),
]
