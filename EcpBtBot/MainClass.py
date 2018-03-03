
import os
from .DialogFlow.API import *
from .DialogFlow.Response import *
from .Conversational_Integration import *

print("Dire Bonjour pour commencer \n")

dico_users = {}
#dictionnaire (var globale): pour chaque clé (user), on a un dictionnaire de connexions API en fonction des thèmes

class API_reponse:

    def __init__(self, sujet):
        if sujet == "sepresenter":
            self.ai = API_SePresenter()
        elif sujet == "hotel":
            self.ai = API_Hotel()
        elif sujet == "restaurant":
            self.ai = API_Restaurant()
        elif sujet == "boulangerie":
            self.ai = API_Boulangerie()

    def reponseBot(self, message):
        #user_id = user
        user_message = message

        rep = Response(self.ai._get_json_response(user_message))
        QuickReplies=[]

        reponseAndQuickReplies=["",[]]
        reponseAndQuickReplies[0]=rep.result.fulfillment.speech
        
        for QuickReply in rep.result.fulfillment.messages:
            if QuickReply['type']==2:
                reponseAndQuickReplies[1]=QuickReply['replies']

        return reponseAndQuickReplies

