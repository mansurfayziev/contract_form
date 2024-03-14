from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('new-dogovor/', views.d_admin, name='d_admin'),
    path('cilent-dogovor/<int:dog_id>/', views.d_cilent, name='d_cilent'),
    path('list-dogovori/', views.list_dog, name='list_dog'),
    path('detail/<int:dog_id>/', views.detail, name='detail')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)