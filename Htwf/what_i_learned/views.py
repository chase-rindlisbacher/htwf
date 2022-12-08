from django.shortcuts import render

# Create your views here.


def indexPageView(request):
    response = 'none'
    if request.POST.get('name') == 'chase' :
        response = 'chase'
    if request.POST.get('name') == 'ty' :
        response = 'ty'
    if request.POST.get('name') == 'dalyn' :
        response = 'dalyn'
    if request.POST.get('name') == 'jeremy' :
        response = 'jeremy'
    data = {
        'response' : response,
    }
    return render(request, 'whatilearned.html', data)