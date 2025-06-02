from django.contrib import admin
from django.urls import path
from home.views import*
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/',register,name='register'),
    path('user_logout/',user_logout,name='user_logout'),
    path('upload_blogs/',upload_blogs,name='upload_blogs'),
    path('',landing,name='landing'),
    path('view_blogs/<int:id>',view_blogs,name='view_blogs'),
    path('update_blogs/<int:id>',update_blogs,name="update_blogs"),
    path('delete_blogs/<int:id>',delete_blogs, name="delete_blogs"),
    path('login/', user_log,name= 'login'),
    path('comments/<int:id>',comments,name="comments"),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)