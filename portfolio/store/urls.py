from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    ## store --- instead of path "" --- home.html -------sn-----john isn=
    path("store/", store, name = "store"),
   
    ## url boilerplate
    # path("coffee/", coffee, name = "coffee")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
