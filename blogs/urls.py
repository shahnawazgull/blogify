from django.contrib import admin
from django.urls import path
from home.views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from home.views import *
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
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm,template_name='password_reset_confirm.html',),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)