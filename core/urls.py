from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView, TemplateView

from django.contrib.staticfiles.storage import staticfiles_storage

favicon_view = RedirectView.as_view(url=staticfiles_storage.url("favicons/dev_1.jpg"))
urlpatterns = [
    path("auth/", include("user.urls")),
    path(
        "api/",
        include(
            [
                path(
                    "auth/",
                    include(
                        [
                            path(
                                "",
                                include(
                                    "api_auth.urls",
                                ),
                            ),
                            path(
                                "",
                                include(
                                    "api_auth.registration.urls",
                                ),
                            ),
                        ]
                    ),
                ),
                path(
                    "auth_urls/",
                    include(
                        "user.api.urls",
                    ),
                ),
            ]
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path("favicon.ico", favicon_view),
        path("admin/", admin.site.urls),
        path("", TemplateView.as_view(template_name="index.html"), name="home"),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path("db/", admin.site.urls),
    ]
