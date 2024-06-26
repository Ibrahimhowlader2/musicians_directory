
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homeView.as_view(), name="home"),
    path('musician/', include('musicians.urls')),
    path('album/', include('album.urls')),
]
