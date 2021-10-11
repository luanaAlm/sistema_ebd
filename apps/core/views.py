from django.shortcuts import render

# página so entra com login


def index(request):
    return render(request, 'core/index.html')
