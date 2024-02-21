from rest_framework.serializers import ModelSerializer
from .models import Course, Lesson, Tag, User


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'active', 'category']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class LessonSerializers(ModelSerializer):
    # tags = TagSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'course', "tags"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'avatar', 'first_name', 'last_name', 'email']