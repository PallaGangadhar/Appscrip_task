from django.shortcuts import render
from trivia_app.models import *
from django.shortcuts import redirect

# Create your views here.

def homepage(request):
    """ Store player name """
    if request.method == 'POST':
        name_saved = Person.objects.create(name=request.POST['name'])
        name_saved.save()
        return redirect('select_cricketer', pk=name_saved.id)
    return render(request, 'trivia_app/index.html',{})

def select_cricketers(request,pk):
    """ Save crcketers name  """
    if request.method == 'POST':
        person_object = Person.objects.get(id=pk)
        cricketers_name = BestCrickter.objects.create(player_name=request.POST['cricketers'],person=person_object)
        cricketers_name.save()
        return redirect('select_flag_colors', pk=pk)
    return render(request, 'trivia_app/select_cricketer.html')

def select_flag_colors(request,pk):
    """ Save Flag Colors  """
    error_msg = ''
    if request.method == 'POST':
        person_object = Person.objects.get(id=pk)
        colors = request.POST.getlist('colors[]')
        if len(colors) == 0:
            error_msg = 'Please select one or more colors'
        else:
            for color in colors:
                flag_color = IndianFlagcolor.objects.create(flag_color=color, person=person_object)
                flag_color.save()
            return redirect('summary', pk=pk)
    return render(request, 'trivia_app/select_flag_color.html',{'error_msg':error_msg})

def summary(request,pk):
    """ Show selected answer details for a person """
    person_object = Person.objects.get(id=pk)
    return render(request, 'trivia_app/summary.html',{'answer_details':person_object})

def history(request):
    """ Show all details of each person related data """
    persons_details = Person.objects.all()
    return render(request, 'trivia_app/history.html',{'persons_details':persons_details})