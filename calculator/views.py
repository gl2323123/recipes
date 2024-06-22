from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, kг': 0.3,
        'сыр, kг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'burger': {
        'булочка, ломтик': 2,
        'котлета': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
        'огурец, ломтик': 3,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def home_view(request):
    return HttpResponse('Привет, здесь собраны лушие рецепты!')

def calculator(request, recipe):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe':{}}
    for ingredient, amount in DATA[recipe].items():
        context['recipe'][ingredient] = round((amount * servings), 2)
    return render(request, 'calculator/index.html', context)