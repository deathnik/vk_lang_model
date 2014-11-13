from django.shortcuts import render

# Create your views here.
from ui.models import Person


def render_person(request, vk_id):
    persons = Person.objects.filter(vk_id=vk_id);
    if len(persons) == 0:
        return render(request, 'not-found.html')
    return render(request, 'person.html', {'person': persons[0]})
    