
from django.contrib import admin
from django.urls import path,include
from trail import urls as u1
from trail2 import urls as u2
from trail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trail/',include(u1)),
    path('trail2/',include(u2)),
    path('', include('trail.urls'))
]
