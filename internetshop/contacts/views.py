from django.views import generic
from .models import Contacts


class IndexView(generic.ListView):
    template_name = 'contact.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Contacts.objects.all()
