from django.shortcuts import render
from petfeeder.models import Pet
from petfeeder.forms import PetForm
# from petfeeder.LEDs import LED_Blink
from petfeeder.arduinoInterface import writeToArduino, readFromArduino

def index(request):
    updateDataText()
    containerStatus = str(readFromArduino())
    print("it should have said read")

    context = {}
    form = PetForm()
    pets = Pet.objects.all()
    context['containerStatus'] = containerStatus
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
            # LED_Blink()
            pk = request.POST.get('feed')
            pet = Pet.objects.get(id=pk)
            print("views.py is sending command")
            writeToArduino(pet.servingSize)

    context['form'] = form
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)

def updateDataText():
    pets = Pet.objects.all()
    dataFile = open("petfeeder/timingData.txt","w")
    for pet in pets:
        
        dataFile.write(pet.servingTime1)
        dataFile.write(",")
        dataFile.write(str(pet.servingSize))
        dataFile.write("\n")

        dataFile.write(pet.servingTime2)
        dataFile.write(",")
        dataFile.write(str(pet.servingSize))
        dataFile.write("\n")

    dataFile.close()
