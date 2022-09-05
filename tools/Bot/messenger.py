import json,requests
from tools.Bot.utils import *
from tools.scrapping import *
class Messenger:
    def __init__(self, ACCESS_TOKEN):
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.url = f"https://graph.facebook.com/v14.0/me/messages?access_token={ACCESS_TOKEN}"
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
        r = requests.post('https://graph.facebook.com/v14.0/me/messenger_profile?access_token=' + self.ACCESS_TOKEN, data=json.dumps(data), headers=headers)

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
    def send_info(self,dest_id,URLSANTE):
        scrap = ScrapInfoSante()
        tittreinfo=["De quoi s’agit-il ?","Quelle est sa fréquence ?","Comment le reconnaître ?","Comment le diagnostic est-il posé ?","Que pouvez-vous faire ?","Que peut faire votre médecin ?"]
        listinfofact=[]
        linfo=scrap.GetInfoSante(URLSANTE)
        for i in range(6):
            listinfofact.append({
                "titre":tittreinfo[i],
                "text": linfo[i],
            })

        data = {
            "recipient": {
                "id": f'{dest_id}'
            },
            "messaging_type": "response",
            "message":{
            "attachment":{
            "type":"template",
            "payload":{
                    "template_type":"generic",
                    "elements":[
                        {
                            "title":f"{info_fact['titre']}",
                            "image_url":"https://cdn-icons-png.flaticon.com/512/2764/2764545.png",
                            "subtitle":f"{info_fact['text']}",
                            "buttons":[
                                {
                                    "type":"postback",
                                    "title":"Lire",
                                    "payload":json.dumps({
                                        'read': info_fact['text']
                                    })
                                }              
                            ]      
                        }for info_fact in listinfofact
                    ]
                }
        }
    }
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
        print(r.content)
    def send_res_info_fact(self,dest_id):
        listinfofact=[]
        # print(listinfofact)
        for i in range(len(resultat_info)):
                listinfofact.append({
                    "text": resultat_info[i],
                })
        data = {
            "recipient": {
                "id": f'{dest_id}'
            },
            "messaging_type": "response",
            "message":{
            "attachment":{
            "type":"template",
            "payload":{
                    "template_type":"generic",
                    "elements":[
                        {
                            "title":f"Résultats",
                            "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCDL2AaXe1Jc7dqPmYZp_oXzXk_nyhrz38lw&usqp=CAU",
                            "subtitle":f"{res_info_fact['text']}",
                            "buttons":[
                                {
                                    "type":"postback",
                                    "title":"Voir",
                                    "payload":"Voir"
                                }              
                            ]      
                        }for res_info_fact in listinfofact
                    ]
                }
        }
    }
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
        print(r.content)
    def send_res_info(self,dest_id,search):
        scrap = ScrapInfoSante()
        listinfofact=scrap.Get_result_search(f"{search}")[:10]
        # listinfofact=[]
        # print(listinfofact)
        data = {
            "recipient": {
                "id": f'{dest_id}'
            },
            "messaging_type": "response",
            "message":{
            "attachment":{
            "type":"template",
            "payload":{
                    "template_type":"generic",
                    "elements":[
                        {
                            "title":f"{res_info['titre']}",
                            "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCDL2AaXe1Jc7dqPmYZp_oXzXk_nyhrz38lw&usqp=CAU",
                            "subtitle":f"{res_info['url']}",
                            "buttons":[
                                {
                                    "type":"postback",
                                    "title":"Voir",
                                    "payload":json.dumps({
                                        'voir': res_info['url']
                                    })
                                }              
                            ]      
                        }for res_info in listinfofact
                    ]
                }
        }
    }
        }
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)
        print(r.content)            
