
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
urlpatterns = [
    path('admin_viktoria/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(

    path('', include('main.urls')),
    # path('appointment/', include('schedule.urls'))
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)S',
            serve, {'document_root': settings.MEDIA_ROOT}),
        path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)S',
            serve, {'document_root': settings.STATIC_ROOT}),
    ]
