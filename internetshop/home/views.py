from django.shortcuts import get_object_or_404, render
from django.views import generic


def index(request):
    return render(request, 'index.html', {})

# class IndexView(generic.ListView):
#     template_name = 'index.html'
#
#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return ""


class ContactsView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ""
