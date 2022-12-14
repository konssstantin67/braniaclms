from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from mainapp import models as mainapp_models


from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"
<<<<<<< HEAD
=======

>>>>>>> aafd0af (Lesson_4)


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"
<<<<<<< HEAD

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_qs"] = mainapp_models.News.objects.all()[:5]
        return context

=======
    
>>>>>>> aafd0af (Lesson_4)
    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_qs"] = mainapp_models.News.objects.all()[:5]
        return context



class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"
<<<<<<< HEAD

=======
    
>>>>>>> aafd0af (Lesson_4)
    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context


class CoursesListView(TemplateView):
    template_name = "mainapp/courses_list.html"
<<<<<<< HEAD

=======
    
>>>>>>> aafd0af (Lesson_4)
    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"
<<<<<<< HEAD

=======
    
>>>>>>> aafd0af (Lesson_4)
    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(course=context["course_object"])
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
<<<<<<< HEAD
    template_name = "mainapp/doc_site.html"
=======
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
>>>>>>> aafd0af (Lesson_4)
