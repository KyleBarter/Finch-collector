from django.shortcuts import render
from .models import Finch

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
    return render(request, 'finches/details.html', {
        'finch' : finch
    })