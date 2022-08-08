import json,requests
from flask import request

from tools.Bot.utils import get_news, info
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
        r = requests.post(self, data=json.dumps(data), headers=headers)
    
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
    def send_info_fact(self,dest_id):
        listinfofact=info()
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
                                "title": f"{info['titre']}",
                                "image_url": f"https://cdn-icons-png.flaticon.com/512/2764/2764545.png",
                                "info": f"{info['text']}",

                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": "Lire",
                                        "payload": json.dumps({
                                            'read': info['text']
                                        })
                                    },
                                ]
                            } for info in listinfofact
                        ]
                    },
                    
                },
            }
        }
        headers = {"Content-Type": "application/json"}
        r1 = requests.post(self, data=json.dumps(data1), headers=headers)
        print("fait")