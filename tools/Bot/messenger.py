import json,requests
from flask import request

from tools.Bot.utils import *
class Messenger:
    def __init__(self, ACCESS_TOKEN):
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.url = "https://graph.facebook.com/v13.0/me/messages?access_token=" + ACCESS_TOKEN
        

    
            
    def send_text(self,dest_id, text):
        self.send_action(dest_id,"typing_on")
        data = {
            "recipient": {
                "id": dest_id
            },
            "messaging_type": "RESPONSE",
            "message": {
                "text": text,
            }
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
        self.send_action(dest_id,"typing_off")
    
    def send_action(self,dest_id,action):
        if action not in ['mark_seen', 'typing_on', 'typing_off']:
            return None
        obj = {
            "recipient": {
            "id": dest_id
            },
            "sender_action": action 
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=json.dumps(obj), headers=headers)
    
    def send_response_quickreply(self,dest_id, text, payloads):
        data = {
        "recipient":{
            "id":dest_id
        },
        "messaging_type": "RESPONSE",
        "message":{
            "text": text,
            "quick_replies": payloads
            
        }
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
    
    def send_file(self,dest_id,url):
        data={
            'messaging_type': "RESPONSE",
            'recipient': {
                "id": dest_id
            },
            'message': {
                'attachment': {
                    'type':"file",
                    'payload': {
                        "url": url,
                        "is_reusable": True
                    }
                }
            }
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
    
    def send_menu(self,dest_id,menu,message):
        return self.send_response_quickreply(dest_id,message,menu)
    def get_stared(self):
        data = { 
                "get_started":{
                    "payload": "get_started"
                }
            }

        headers = {"Content-Type": "application/json"}
        r = requests.post('https://graph.facebook.com/v10.0/me/messenger_profile?access_token=' + self.ACCESS_TOKEN, data=json.dumps(data), headers=headers)
    def get_username(self,user_id):
        name = requests.get('https://graph.facebook.com/v2.6/' + user_id +'?access_token=' + self.ACCESS_TOKEN)
    def send_news_suggestion(self,dest_id):
        list_news = get_news()
        if len(list_news)>=12:
            current_list_news = list_news[:12]
            splited_list_news = list_news[12:len(list_news)]
            
        else : 
            current_list_news = list_news[:len(list_news)/2]
            splited_list_news = list_news[len(list_news)/2:len(list_news)]

        print(current_list_news)
        data1 = {
            "recipient": {
                "id": f'{dest_id}'
            },
            "messaging_type": "response",
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": f"{news['title']}",
                                "image_url": f"{news['thumbnail']}",
                                "publishedTime": f"{news['publishedTime']}",

                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Lire",
                                        "payload": json.dumps({
                                            'read': news['url']
                                        })
                                    },
                                ]
                            } for news in current_list_news
                        ]
                    },
                    
                },
            }
        }
        data2 = {
            "recipient": {
                "id": f'{dest_id}'
            },
            "messaging_type": "response",
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": f"{news['title']}",
                                "image_url": f"{news['thumbnail']}",
                                "publishedTime": f"{news['publishedTime']}",

                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Lire",
                                        "payload": json.dumps({
                                            'read': news['url']
                                        })
                                    },
                                ]
                            } for news in splited_list_news
                        ]
                    },
                    
                },
            }
        }
        headers = {"Content-Type": "application/json"}
        r1 = requests.post(self, data=json.dumps(data1), headers=headers)
        r2 = requests.post(self, data=json.dumps(data2), headers=headers)
        print(r1.content)
        print(r2.content)
    # def send_info_fact(self,dest_id):
    #     tittreinfo=["De quoi s’agit-il ?","Quelle est sa fréquence ?","Comment le reconnaître ?","Comment le diagnostic est-il posé ?","Que pouvez-vous faire ?","Que peut faire votre médecin ?"]
    #     info1="Le paludisme est une maladie infectieuse causée par le parasite Plasmodium. Ce parasite se transmet à l'homme par la piqûre d’un moustique bien spécifique : l’anophèle."
    #     info2 ="Le paludisme est l’une des infections les plus répandues sur la planète. On compte chaque année plus de 200 millions de cas de paludisme et, selon les estimations, la maladie fait plus de 400 000 morts par an, essentiellement parmi les enfants d’Afrique."
    #     info3= "La période d'incubation, c’est-à-dire l’intervalle entre la piqûre de moustique et l'apparition des premiers symptômes, varie de 10 jours à 1 mois. Il se peut donc que vous soyez rentré chez vous depuis un moment avant de tomber malade."
    #     info4= "Toute personne ayant voyagé dans une région touchée par le paludisme et ayant de la fièvre est suspectée d’être infectée par le paludisme."
    #     info5="La principale mesure à prendre est d’empêcher les moustiques de vous piquer. C’est après la tombée de la nuit qu’ils sévissent le plus. Portez des vêtements de couleur claire et recouvrant vos bras et vos jambes (manches longues, pantalons longs ou jupes longues)."
    #     info6="Si vous vous rendez dans une région touchée par le paludisme, le médecin vous prescrira un médicament à titre préventif. Il évaluera le médicament qui vous convient le mieux. Il est donc tout à fait possible que vous ne preniez pas le même traitement que vos compagnons de voyage. À partir de 40 kg, la dose pour adultes doit être administrée. Pour un poids inférieur à 40 kg, la dose doit être calculée en fonction du poids."
    #     linfo=[info1,info2,info3,info4,info5,info6]
    #     listinfofact=[]
    #     for i in range(6):
    #         listinfofact.append({
    #         "titre":tittreinfo[i],
    #         "text": linfo[i],
    #     })
    #     print(listinfofact)
    #     data = {
    #         "recipient": {
    #             "id": f'{dest_id}'
    #         },
    #         "messaging_type": "response",
    #         "message": {
    #             "attachment": {
    #                 "type": "template",
    #                 "payload": {
    #                     "template_type": "generic",
    #                     "elements": [
    #                         {
    #                             "title": f"{info['titre']}",
    #                             "image_url": "https://cdn-icons-png.flaticon.com/512/2764/2764545.png",
    #                             "info": f"{info['text']}",

    #                             "buttons": [
    #                                 {
    #                                     "type": "postback",
    #                                     "title": "Lire",
    #                                     "payload": json.dumps({
    #                                         'read': info['text']
    #                                     })
    #                                 },
    #                             ]
    #                         } for info in listinfofact
    #                     ]
    #                 },            
    #     },
    #     "quick_replies": [
    #             {	
	#                 'content_type': 'text',
	# 	    		'title': 'Page suivante',
	# 	    		'payload': json.dumps({
	# 	    			'page': 'page+1',
	# 	    			'query': 'query'
	# 	    			})
    # 			}
    #         ]
    #         },
    #     }
    #     headers = {"Content-Type": "application/json"}
    #     r = requests.post(self.url, data=json.dumps(data), headers=headers)
    #     print("arrived")
def send_info_fact(self,dest_id):
    data = {
        "recipient": {
            "id": f'{dest_id}'
        },
        "messaging_type": "response",
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": 
                        {
                            "title": f'title',
                            "image_url": f"https://cdn-icons-png.flaticon.com/512/2764/2764545.png",
                            "subtitle": f"test",

                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Regarder",
                                    "payload": json.dumps({
                                        'watch': 'url'
                                    })
                                }
                            ]
                        } 
                },
                
            },
        }
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post(self.url, data=json.dumps(data), headers=headers)
    print(r.content)
