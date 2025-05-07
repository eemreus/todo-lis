from django.contrib import admin
from django.urls import path, include  # include fonksiyonu eklendi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Anasayfa artık tasks uygulamasına yönleniyor
]
