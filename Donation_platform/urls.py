
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',include("users.urls")),
    path('api/campaign/',include("campaigns.urls")),
    path("api/transactions/",include("transactions.urls")),
    path("api/notification/",include("notification.urls")),
    path("api/manager/",include("manager.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
