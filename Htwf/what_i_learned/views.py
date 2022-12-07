from django.shortcuts import render

# Create your views here.


def indexPageView(request):
    jeremy = ''
    ty = ''
    dalyn = ''
    chase = ''
    if request.POST.get('name') == 'chase' :
        chase = ''
    if request.POST.get('name') == 'ty' :
        ty = ''
    if request.POST.get('name') == 'dalyn' :
        dalyn = ''
    if request.POST.get('name') == 'jeremy' :
        jeremy = ''
    data = {
        'jeremy': jeremy,
        'ty': ty,
        'dalyn': dalyn,
        'chase': chase,
    }
    return render(request, 'whatilearned.html', data)
