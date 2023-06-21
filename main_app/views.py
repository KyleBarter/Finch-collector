from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from.forms import FeedingForm

#makeshift model 
# finches = [
#     {
#         'species': 'Zebra Finch',
#         'color': 'Gray',
#         'size': 'Small',
#         'habitat': 'Australia',
#         'diet': 'Seeds',
#         'lifespan': 5,
#         'population': 'Common'
#     },
#     {
#         'species': 'Goldfinch',
#         'color': 'Yellow',
#         'size': 'Small',
#         'habitat': 'North America',
#         'diet': 'Seeds, Insects',
#         'lifespan': 10,
#         'population': 'Stable'
#     },
#     {
#         'species': 'Gouldian Finch',
#         'color': 'Red, Green, Yellow',
#         'size': 'Small',
#         'habitat': 'Australia',
#         'diet': 'Seeds, Insects',
#         'lifespan': 6,
#         'population': 'Endangered'
#     },
#     {
#         'species': 'Purple Finch',
#         'color': 'Red, Brown',
#         'size': 'Medium',
#         'habitat': 'North America',
#         'diet': 'Seeds, Insects',
#         'lifespan': 7,
#         'population': 'Stable'
#     },
#     {
#         'species': 'Society Finch',
#         'color': 'White, Brown',
#         'size': 'Small',
#         'habitat': 'Domesticated',
#         'diet': 'Seeds, Pellets',
#         'lifespan': 7,
#         'population': 'Common'
#     },
#     {
#         'species': 'Crimson Finch',
#         'color': 'Red',
#         'size': 'Small',
#         'habitat': 'Australia',
#         'diet': 'Seeds, Insects',
#         'lifespan': 6,
#         'population': 'Stable'
#     },
#     {
#         'species': 'European Goldfinch',
#         'color': 'Red, Black, White',
#         'size': 'Small',
#         'habitat': 'Europe, Asia, Africa',
#         'diet': 'Seeds, Insects',
#         'lifespan': 12,
#         'population': 'Stable'
#     },
#     {
#         'species': 'Java Sparrow',
#         'color': 'Gray',
#         'size': 'Small',
#         'habitat': 'Indonesia',
#         'diet': 'Seeds',
#         'lifespan': 7,
#         'population': 'Endangered'
#     },
#     {
#         'species': 'Bengalese Finch',
#         'color': 'White, Brown',
#         'size': 'Small',
#         'habitat': 'Domesticated',
#         'diet': 'Seeds, Insects',
#         'lifespan': 5,
#         'population': 'Common'
#     },
#     {
#         'species': 'Red-cheeked Cordon-bleu',
#         'color': 'Blue, Red',
#         'size': 'Small',
#         'habitat': 'Sub-Saharan Africa',
#         'diet': 'Seeds, Insects',
#         'lifespan': 5,
#         'population': 'Stable'
#     }
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def all_finches(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    #instantiate feeding form to be rendered in detail.html
    feeding_form = FeedingForm()
    return render(request, 'finches/details.html', {
        'finch' : finch, 'feeding_form' : feeding_form
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('details', finch_id=finch_id)

#class based views below
class FinchCreate(CreateView):
    model = Finch
    #all, we want the form to render all fields defined on finch model
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['location', 'color']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('details', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('details', finch_id=finch_id)