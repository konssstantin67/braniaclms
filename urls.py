from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig


app_name = MainappConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='mainapp/')),
    path('maimapp/', include('mainapp.urls')),
]