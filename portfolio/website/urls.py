from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home, name = "home"),
    path("coffee/", coffee, name = "coffee"),
    path("coding/", coding, name = "coding"),

    ## url boilerplate
    # path("coffee/", coffee, name = "coffee")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
