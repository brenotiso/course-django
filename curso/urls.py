from django.contrib import admin
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('blog.urls'))
]
