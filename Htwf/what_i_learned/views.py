from django.shortcuts import render

# Create your views here.


def indexPageView(request):
    jeremy = ''
    ty = ''
    dalyn = ''
    chase = ''
    if request.Post.get('name') == 'chase' :
        chase = ''
    if request.Post.get('name') == 'ty' :
        ty = ''
    if request.Post.get('name') == 'dalyn' :
        dalyn = ''
    if request.Post.get('name') == 'jeremy' :
        jeremy = ''
    data = {
        'jeremy': jeremy,
        'ty': ty,
        'dalyn': dalyn,
        'chase': chase,
    }
    return render(request, 'whatilearned.html', data)
