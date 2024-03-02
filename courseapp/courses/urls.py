from django.urls import path, include
from rest_framework import routers
from courses import views


router = routers.DefaultRouter()
router.register('categories', views.CategoryView, basename='categories')
router.register('courses', views.CourseView, basename='courses')
router.register('lessons', views.LessonViewSet, basename='lessons')
router.register('users', views.UserViewSet, basename='users')
router.register('comments', views.CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls',
    namespace='oauth2_provider')),

]