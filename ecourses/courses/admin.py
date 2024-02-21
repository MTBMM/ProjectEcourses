from django.contrib import admin
from django.template.response import TemplateResponse, HttpResponse
from django.urls import path
from .models import *
from django.utils.html import mark_safe
# Register your models here.
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.views import View  # Thêm import này


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonTagInlineAdmin(admin.TabularInline):
    model = Lesson.tags.through


class LessonInlineAdmin(admin.StackedInline):
        model = Lesson
        fk_name = 'course'


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject']
    search_fields = ['subject', 'content']
    list_filter = ['subject']
    readonly_fields = ['avatar']
    form = LessonForm
    inlines = [LessonTagInlineAdmin, ]

    def avatar(self, obj):
        return mark_safe(
               "<img src='/static/{img_url}' />".format(img_url=obj.image.name)
        )

    class Media:
        css = {
            'all': ('/static/css/main.css', )
        }


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin, ]
    list_display = ['id', 'subject']


class CategoryAdmin(admin.ModelAdmin):
        list_display = ['id', 'name']


class TagAdmin(admin.ModelAdmin):
    # inlines = [LessonInlineAdmin, ]
    inlines = [LessonTagInlineAdmin, ]



class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "password", "email"]


class CourseAppAdminSite(admin.AdminSite):
        site_header = "Hệ thống khóa học trực tuyến"
        #
        # def get_urls(self):
        #     return [path('courses-stats/', self.stats_view)] + super().get_urls()
        #
        # def stats_view(self, request):
        #     count = Course.objects.filter(active=True).count()
        #     return TemplateResponse(request, 'admin/courses-stats.html',{
        #                             'count_stats': count})


        def get_urls(self):
            urls = super().get_urls()
            custom_urls = [
                path('courses-stats/', self.stats_view, name="courses-stats"),
                path('lesson/', self.lesson),
                path('logout/', self.admin_view(LogoutView.as_view()), name='admin_logout')
            ]
            return custom_urls + urls

        def stats_view(self, request):
            count = Course.objects.filter(active=True).count()
            return TemplateResponse(request, 'admin/courses-stats.html', {'count_stats': count})

        def lesson(self, request):
            count_lesson = Lesson.objects.filter(active=True).count()
            return TemplateResponse(request, 'admin/lessons-stats.html', {'count_lesson': count_lesson})


class LogoutView(View):
    def logout_view(self, request):
        # Điều chỉnh nội dung view tùy thuộc vào yêu cầu của bạn
        count_lesson = Lesson.objects.filter(active=True).count()
        return TemplateResponse(request, 'admin/lessons-stats.html', {'count_lesson': count_lesson})


admin_site = CourseAppAdminSite(name='myadmin')
admin_site.register(Category)
admin_site.register(Course, CourseAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Lesson, LessonAdmin)
admin_site.register(Tag, TagAdmin)
# admin_site.register(LogoutView(name="Logout"))

# class CourseAppAdminSite(admin.AdminSite):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.register(Category)
#         self.register(Course, CourseAdmin)
#         self.register(User, UserAdmin)
#         self.register(Lesson, LessonAdmin)
#         self.register(Tag)
#         self.register(LogoutView(name='my_logout'))  # Đăng ký LogoutView


# admin.site = CourseAppAdminSite(name='myadmin')
# admin.site.register(Category)
# admin.site.register(Course, CourseAdmin)
# admin.site.register(User)
# admin.site.register(Lesson, LessonAdmin)
# admin.site.register(Tag)

