from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
                  url(r'^user/', admin.site.urls),
                  url(r'^company/', include('company.urls')),
                  url(r'^customer/', include('Customer.urls')),
                  url(r'^ledgers/', include('ledgers.urls')),
                  url(r'^activity/', include('activity.urls')),
                  url(r'^journal/', include('journal.urls')),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
