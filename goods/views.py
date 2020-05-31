import logging
from django.views import generic
from .models import Goods

logger = logging.getLogger(__name__)


class GoodsView(generic.ListView):
    template_name = 'product_list.html'
    model = Goods


class GoodsPropsView(generic.DetailView):
    template_name = 'single-product.html'
    model = Goods
