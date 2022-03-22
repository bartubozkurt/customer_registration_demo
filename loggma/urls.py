import django
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from customer import views 

def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('customer.urls')),
  path('', views.index, name='index'),
  path('user/', include('user.urls')),
  path("404/", custom_page_not_found),
]