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

# def indexPageView(request):
#     jeremy = 'test1'
#     ty = 'test1'
#     dalyn = 'test1'
#     chase = 'test1'
#     if request.POST.get('name') == 'chase' :
#         chase = 'test2'
#     if request.POST.get('name') == 'ty' :
#         ty = 'test2'
#     if request.POST.get('name') == 'dalyn' :
#         dalyn = 'test2'
#     if request.POST.get('name') == 'jeremy' :
#         jeremy = 'test2'
#     data = {
#         'jeremy': jeremy,
#         'ty': ty,
#         'dalyn': dalyn,
#         'chase': chase,
#     }
#     return render(request, 'whatilearned.html', data)