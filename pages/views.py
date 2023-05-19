from django.shortcuts import render
from django.views import generic
from .models import PublicModel
from accounts.models import CustomUser

def handler404(request, exception):
    return render(request, '404.html', status=404)


class HomePageView(generic.ListView):
    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for
            print(ip)
        else:
            ip = request.META.get('REMOTE_ADDR')
            print(ip)
        number = PublicModel()
        number.view += 1
        number.save()
        view_count = PublicModel.objects.count()
        return render(request, template_name='pages/home.html',context={'view_count': view_count,
                                                                        'user_ip': ip})


# def HomePageView(request):
#     public = PublicModel()
#     public.view += 1
#     public.save()
#     view = PublicModel.objects.count()
#     return render(request, template_name='pages/home.html', context={'public': view})
