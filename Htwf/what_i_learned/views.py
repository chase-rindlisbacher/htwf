from django.shortcuts import render

# Create your views here.


def indexPageView(request):
    result = ''
    if request.POST.get('name') == 'chase' :
        result = ''
    if request.POST.get('name') == 'ty' :
        result = ''
    if request.POST.get('name') == 'dalyn' :
        result = ''
    if request.POST.get('name') == 'jeremy' :
        result = ''
    data = {
        'result' : result
    }
    return render(request, 'whatilearned.html', data)
