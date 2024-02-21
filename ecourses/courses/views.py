from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .serializers import LessonSerializers, CourseSerializer, UserSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .models import Lesson, Course, User
from rest_framework.parsers import MultiPartParser
# from django.shortcuts import render_to_response
from django.template.context import RequestContext

#
# class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView):
#         queryset = User.objects.get(is_active=True)
#         serializer_class = UserSerializer
#         parser_classes = [MultiPartParser, ]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]

    @action(methods=["post"], detail=True)
    def get_course(self, request):
        try:
            stats = Course.objects \
                .annotate(lesson_count=Count('id')) \
                .values('id', 'subject', 'image', 'active', 'category')

        except Course.DoesNotExits:
            return Response(status=HTTP_400_BAD_REQUEST)
        return Response(data=LessonSerializers(stats, context={'request': request}).data, status=HTTP_200_OK)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializers
    # permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action in ["list", "create", "retrieve"]:
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]

    @action(methods=['post'], detail=True, url_path="hide-lesson", url_name="hide-lesson")
    ## sẽ có đường dẫn hàm này:
    def hide_lesson(self, request, pk=None):
        try:
                c = Lesson.objects.get(pk=pk)
                c.active = False
                c.save()
        except Lesson.DoesNotExits:
            return Response(status=HTTP_400_BAD_REQUEST)

        return Response(data=LessonSerializers(c, context={'request': request}).data, status=HTTP_200_OK)

    @action(methods=["post"], detail=True)
    def get_lesson(self, request, pk=None):
        try:
            # d = Lesson.objects.anontate(lesson_count=Count('id')).values('id', 'subject', 'lesson_count')
            d = Lesson.objects.get(pk=pk)

        except Lesson.DoesNotExits:
            return Response(status=HTTP_400_BAD_REQUEST)
        return Response(data=LessonSerializers(d, context={'request': request}).data, status=HTTP_200_OK)

def index(request):
    return render(request, template_name='index.html', context={'name': 'Nguyen Trung Kien'})


def Hello(request, year):
    return HttpResponse("Hello Nguyen Trung Kien" + str(year))


def detail(request, year):
    return HttpResponse("Xin chào Nguyễn Trung Kiên" + str(year))


class TestView(View):
    def get(self, request, year):
        return HttpResponse("Testing" + str(year))

    def post(self, request):
        pass


def home(request):

   context = RequestContext(request,
                           {'user': request.user})
   return render(request, template_name='thirdauth/home.html',
                             context_instance=context)