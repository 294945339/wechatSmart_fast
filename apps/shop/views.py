from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        # all_banners = Banner.objects.all().order_by('index')
        # courses = Course.objects.filter(is_banner=False)[:6]
        # banner_courses = Course.objects.filter(is_banner=True)[:3]
        # course_orgs = CourseOrg.objects.all()[:15]

        return render(request, 'index.html')

    # , {
        # 'all_banners': all_banners,
        # 'courses': courses,
        # 'banner_courses': banner_courses,
        # 'course_orgs': course_orgs,
    # }