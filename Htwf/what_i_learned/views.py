from django.shortcuts import render

# Create your views here.


def indexPageView(request):
    jeremy = ''
    ty = ''
    dalyn = ''
    chase = ''
    if request.post.get('name') == 'chase' :
        chase = ''
    if request.post.get('name') == 'ty' :
        ty = ''
    if request.post.get('name') == 'dalyn' :
        dalyn = ''
    if request.post.get('name') == 'jeremy' :
        jeremy = ''
    data = {
        'jeremy': jeremy,
        'ty': ty,
        'dalyn': dalyn,
        'chase': chase,
    }
    return render(request, 'whatilearned.html', data)
