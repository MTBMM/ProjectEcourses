from django.db import models
from django .contrib.auth.models import AbstractUser
# Create your models here.
from django.template.backends import django
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%y/%m')


class ModelsBase(models.Model):
    class Meta:
        abstract = True
        ordering = ['-id']
    subject = models.CharField(max_length=100, null=False, default=None)
    image = models.ImageField(upload_to='courses/%y/%m', default=None)
    # created_date = models.DateTimeField(auto_now_add=True)
    # update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class Course(ModelsBase):
    class Meta:
        unique_together = ('subject', 'category')
    # description = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Lesson(ModelsBase):
    class Meta:
        unique_together = ('subject', 'course')
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


if __name__ == "__main__":

    c = Category(name='Cong nghe thong tin')
    c.save()
    co = Course(subject="Lap Trinh Java", description="good", category=c)
    co.save()
    category = Category.objects.get(name='Công nghệ thông tin')

        # Lấy tất cả các khóa học thuộc danh mục "Công nghệ thông tin"
    courses_in_category = Course.objects.filter(category=category)

        # In ra thông tin về từng khóa học
    for course in courses_in_category:
        print(f"Tên khóa học: {course.subject}, Mô tả: {course.description}")

    c = Course(subject="Lap Trinh Java", category_id=2)
    l = Lesson(subject="Phat trien he thong web", content="good", course=c)




