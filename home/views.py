from django.views.generic.list import ListView
from .models import Bio
 
class BioList(ListView):
 
    # specify the model for list view
    model = Bio


