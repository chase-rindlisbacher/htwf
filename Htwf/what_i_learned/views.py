from django.shortcuts import render

# Create your views here.


def indexPageView(request):
    data = {
        'jeremy':,
        'ty':,
        'dalyn':,
        'chase':,
    }
    return render('whatilearned.html')
