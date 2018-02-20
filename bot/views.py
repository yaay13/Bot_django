from .forms import DiscussionForm
from .models import Reponse
from django.shortcuts import render
from EcpBtBot.MainClass import *


def home(request):
    instance = Reponse.objects.filter(name=request.user.username).all()
    instance.delete()

    return render(request, 'bot/accueil.html', locals())

def view_discussion(request, sujet):

    if sujet not in dico_connexions:
        connexion = API_reponse(sujet)
        dico_connexions[sujet] = connexion
    else:
        connexion = dico_connexions[sujet]

    form = DiscussionForm(request.POST or None)
    objets = Reponse.objects.filter(name=request.user.username).order_by('created_at')

    if form.is_valid():

        message = form.cleaned_data['texte']
        envoi = True
        message_sauvegarde = Reponse(reponse = message, source = "user", name = request.user.username)
        message_sauvegarde.save()
        repBot = connexion.reponseBot(message)
        repBot_sauvegarde = Reponse(reponse=repBot, source = "bot", name = request.user.username)
        repBot_sauvegarde.save()

        return render(request, 'bot/discussion.html', locals())

    return render(request, 'bot/discussion.html', locals())
