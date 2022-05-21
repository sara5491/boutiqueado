from django.shortcuts import render

# Create your views here.
def custom(request):
    """ Contact form to request custom bake """

    return render(request, 'custom/custom.html')