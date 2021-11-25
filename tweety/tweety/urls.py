from django.contrib import admin
from django.urls import path
from twt.views import *
from django.conf import settings
from django.conf.urls.static import static

"""URL функции названия"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name='home'),
    path('info/', info, name="info"),
    path('addpost/', Addpost.as_view(), name='addpost'),
    path('login/', LoginUser.as_view(), name='login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name="post"),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
