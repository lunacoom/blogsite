from django.shortcuts import render

from .models import Gallery,Timeline, About, ContactInfo


def home_page(request):
    context = {}
    gallery = Gallery.objects.all()
    context = {'gallery':gallery}
    return render(request, 'index.html', context=context)


def timeline_page(request):
    timeline = Timeline.objects.all()
    context = {'timeLine': timeline}
    return render(request, 'timeline.html', context=context)

def about_page(request):
    about = About.objects.all()
    context = {'about': about}
    return render(request, 'about.html', context=context)


def contact_page(request):
    contact_info = ContactInfo.objects.all().first()
    context = {
        "info":contact_info
    }
    return render(request, 'contact.html',context=context)
