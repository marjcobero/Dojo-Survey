from django.shortcuts import render, redirect

LOCATIONS = (
    'Burbank',
    'Seattle',
    'Chicago',
    'Dallas'
)

LANGS = (
    'Python',
    'JavaScript',
    'C#',
    'Mern',
    'Java',
    'C'
)
def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'form.html', context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'index.html', context)
