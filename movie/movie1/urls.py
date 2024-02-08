from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('killer/', views.killer, name='killer'),
                  path('haunt/', views.haunt, name='haunt'),
                  path('world/', views.world, name='world'),
                  path('reptile', views.reptile, name='reptile'),
                  path('tetris', views.tetris, name='tetris'),
                  path('plane', views.plane, name='plane')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
