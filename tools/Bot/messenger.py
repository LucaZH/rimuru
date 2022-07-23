import json,requests
from flask import request
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
    
    def memu(self,dest_id,text,title_text,title_menu,menu_text):
        print("ggg")
        payloads=[{
        'content_type': 'text',
        'title': title_text[i],
        "payload": {
        "title_menu": menu_text[i],
            }
        } for i in range(len(title_text))]
        print(payloads)
        self.send_response_quickreply(dest_id,text,payloads)
        
    def main_menu(self,dest_id):
        self.send_response_quickreply(dest_id, "Qu'est ce que je peux faire pour vous?", [
        {
            'content_type': 'text',
            'title': 'Conseil du jour',
            "payload": json.dumps({
                'menu': 'Conseil_du_jour',
                
            })
        },
        {
            'content_type': 'text',
            'title': 'Hopital',
            "payload": json.dumps({
                'menu': 'hopital',
                
            })
        },
        {
            'content_type': 'text',
            'title': 'Pharmacie',
            "payload": json.dumps({
                'menu': 'pharmacie',
            })
        },
        {
            'content_type': 'text',
            'title': 'COVID-19',
            "payload": json.dumps({
                'menu': 'COVID19',
            })
        },
        {
            'content_type': 'text',
            'title': 'A propos',
            "payload": json.dumps({
                'menu': 'Apropos',
            })
        }
        ])
    def menu_hospital(self,dest_id):
        self.send_response_quickreply(dest_id, "Votre choix", [
        {
            'content_type': 'text',
            'title': 'Continuer',
            "payload": json.dumps({
                'query_hosp': 'Continuer',
            })
        },
        {
            'content_type': 'text',
            'title': 'Aider',
            "payload": json.dumps({
                'query_hosp': 'Aider',
            })
        }
        ])
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