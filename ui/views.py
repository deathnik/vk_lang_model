from django.shortcuts import render

# Create your views here.
from ui.models import Person


def render_person(request, vk_id):
    return render(request, 'person.html', {'person': Person.objects.filter(vk_id=vk_id)[0]})