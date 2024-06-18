from django.shortcuts import render

# Create your views here.
def home(request):

    context = {}

    return render(request, 'website/home.html', context)


def coffee(request):

    context = {}

    return render(request, 'website/coffee.html', context)


def coding(request):

    context = {}

    return render(request, 'website/coding.html', context)


## boilerplate for view
# def coding(request):

#     context = {}

#     return render(request, 'website/coding.html', context)

