from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.views.generic import View
from django.db.models.functions import Lower
from .models import Macrame, Category
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    """ A view to return the homepage """
    return render(request, 'macrames/index.html')


def all_macrames(request):
    """ A view to show all macrames, including sorting and search queries """

    macrame = Macrame.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                macrame = macrame.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            macrame = macrame.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            macrame = macrame.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('macrame'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            macrame = macrame.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'macrame': macrame,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'macrames/macrames_items.html', context)


def macrame_detail(request, item_id):
    """ A view to show individual macrame details """

    macrame = get_object_or_404(Macrame, pk=item_id)

    context = {
        'macrame': macrame,
    }

    return render(request, 'macrames/macrame-detail.html', context)


class MacrameLike(LoginRequiredMixin, View):
    
    def post(self, request, pk, *args, **kwargs):
        macrame_ = Macrame.objects.get(pk=pk)
        is_like = False
        for like in macrame_.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            macrame_.likes.add(request.user)
        if is_like:
            macrame_.likes.remove(request.user)
            
        next_ = request.POST.get('next_', '/')
        return HttpResponseRedirect(next_)

