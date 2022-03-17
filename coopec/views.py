from urllib import response
from django.http import HttpResponse
import random

""" RENDRE DES PAGES HTML """



def home_view(request):
    """ 
    Enregistrer une demande (envoyée par Django)
    Retourner du HTML comme réponse (response)
    
    """
    number = random.randint(10,8652)
    nom = "Abouma"
    HTML_STRING = f"hu {nom} - {number}" 
    return HttpResponse(HTML_STRING)

    