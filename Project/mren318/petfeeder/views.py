from django.shortcuts import render
from petfeeder.models import Pet
from petfeeder.forms import PetForm
from petfeeder.LEDs import LED_Blink

def index(request):
    context = {}
    form = PetForm()
    pets = Pet.objects.all()
    context['pets'] = pets
    context['title'] = 'Home'

    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = PetForm(request.POST, instance=Pet(consumptionToday=0, visitationsToday=0, avgTimeAtFeeder=0))
            else:
                pet = Pet.objects.get(id=pk)
                form = PetForm(request.POST, instance=pet)
            form.save()
            form = PetForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            pet = Pet.objects.get(id=pk)
            pet.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            pet = Pet.objects.get(id=pk)
            form = PetForm(instance=pet)
        elif 'feed' in request.POST:
            LED_Blink()
    context['form'] = form
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)
