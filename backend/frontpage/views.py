from django.shortcuts import render

def front_view(request):
    context = {}
    context["title"] = "Front Page!"
    return render(request, 'index.html', context)
