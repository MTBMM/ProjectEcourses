from django.urls import path, re_path, include

from . import views
from django.contrib import admin
from .admin import admin_site

from rest_framework import routers
#
# # routerLesson = routers.DefaultRouter()
# # routerCourses = routers.DefaultRouter()
# routerLesson.register('lessons', views.LessonViewSet)
# routerCourses.register('courses', views.CourseViewSet)
router = routers.DefaultRouter()
# router.register('users', views.UserViewSet)
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)
urlpatterns = [
    # path('', views.index, name="index"),
    # path("hello/<int:year>/", views.Hello, name="Hello"),
    # re_path(r'^detail/(?P<year>[0-9]{3,6})/$', views.detail, name='detail'),
    # # path('test/', views.TestView.as_view),
    # re_path(r'^test_view/(?P<year>[0-9]{2,5})/$', views.TestView.as_view()),
    # path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls',
                        namespace='oauth2_provider')),
    path('admin/', admin_site.urls),
    # path('home/', views.home, name='home'),

    path('', include(router.urls))
]