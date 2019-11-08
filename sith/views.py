from django.shortcuts import render


def main(request):
    return render(request, 'sith/index.html')
# Create your views here.
