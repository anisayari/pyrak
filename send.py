# coding: utf-8

import requests

# POUR GENERER DES PAYLOAD :

def send_share(sender):
  texte = "Pyrak est un chatbot permettant de demander le menu du RAK, restaurant de l'IMT Atlantique"
  return {"recipient":{"id":sender },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"button",
        "text":"Click pour permettre à tes potes de savoir ce qu'il y a au RAK!",
        "buttons":[
            {
            "type": "element_share",
            "share_contents": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [{
                            "title": "Pyrak Chatbot",
                            "subtitle": texte,
                            "default_action": {"type": "web_url","url": 'https://m.me/menupyrak/'},
                            "buttons": [{
                                  "type": "web_url",
                                  "url": 'https://m.me/menupyrak/',
                                  "title": 'Se lancer !'
                                }]
                            }]
                        }
                    }
                }
            }]
        }
    }}}
def send_text (sender,texte):

    return {'recipient': {'id': sender}, 'message': {'text': texte}}
def send_choix_multiple5(sender,texte,choix_dict):
  return {
  "recipient":{
    "id":sender
  },
  "message":{
    "text":texte,
    "quick_replies":[
      {
        "content_type":"text",
        "title":choix_dict[0],
        "payload":choix_dict[0],
      },
      {
        "content_type":"text",
        "title":choix_dict[1],
        "payload":choix_dict[1],
      },
      {
        "content_type":"text",
        "title":choix_dict[2],
        "payload":choix_dict[2],
      },
      {
        "content_type":"text",
        "title":choix_dict[3],
        "payload":choix_dict[3],
      },
      {
        "content_type":"text",
        "title":choix_dict[4],
        "payload":choix_dict[4],
      }
    ]
  }
 }

# ENVOYER UN PAYLOAD
def send_paquet(token,payload):
    r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
    print(r.text) #affiche la reponse a l'envoi; pratique si veut l'ID ou voir si bien envoye
    return 'nothing'

def senderator(token, sender, texte, choix_dict):
    payload = send_choix_multiple5(sender, texte, choix_dict)
    send_paquet(token, payload)
    print('Repas')
    return 'nothing'