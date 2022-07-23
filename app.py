from flask import Flask, request
from conf import *
from tools.Bot.messenger import Messenger
from tools import database
import json

app = Flask(__name__)
Rimuru = Messenger(ACCESS_TOKEN)

@app.route("/", methods=['GET'])
def handle_verification():
        if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
            print("Verified")
            return request.args.get('hub.challenge', '')
        else:
            print("Wrong token")
            return "Error, wrong validation token"
    
@app.route('/', methods=['POST'])
def main():
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                sender_id = messaging_event["sender"]["id"]
                Rimuru.send_action(sender_id,"mark_seen")
                user_state = database.getState(sender_id)
                usergeted = database.getAllUser()
                print('get all user ====>')
                print(usergeted)
                if messaging_event.get("message"):
                    if 'text' in messaging_event['message'] and 'quick_reply' not in messaging_event['message']:
                        query = messaging_event["message"]["text"]
                        if user_state == 'START':
                            # recipient_id = messaging_event["recipient"]["id"]  
                            # Rimuru.send_action(sender_id,"mark_seen")
                            # Rimuru.send_text(sender_id,message_text)
                            Rimuru.main_menu(sender_id)
                            Rimuru.send_action(sender_id,"typing_off")
                        else:
                            if user_state == 'HOSPITAL':
                                database.updateState(sender_id,'HOSPITAL',query=query)


                    if 'quick_reply' in messaging_event['message']:
                        Rimuru.send_action(sender_id,"mark_seen")
                        payload = messaging_event['message']['quick_reply']['payload']
                        if is_json(payload):
                            payload = json.loads(payload)
                            if 'menu' in payload:
                                if payload['menu'] == 'hopital':
                                    Rimuru.send_text(sender_id,'Hopital : Developpement du projet en cours')
                                    # database.insertUser(sender_id)
                                    database.updateState(sender_id,'HOSPITAL')
                                    Rimuru.send_text(sender_id,"ENtrer votre localisation")
                                    
                                elif payload['menu'] =='COVID19':
                                    Rimuru.send_action(sender_id,"typing_off")
                                    Rimuru.send_text(sender_id,'Covid-19 : Developpement du projet en cours')
                                    
                                elif payload['menu'] =='pharmacie':
                                    Rimuru.send_text(sender_id,'pharmacie : Developpement du projet en cours')

                                elif payload['menu'] =='Conseil_du_jour':
                                    Rimuru.send_text(sender_id,'Conseil du jour : Developpement du projet en cours')
                                elif payload['menu'] =='Apropos':
                                    Rimuru.send_text(sender_id,'Devollopé par RANDRIAMANANTENA Luca Zo Haingo')
                            elif 'actualite_covid19' in payload:
                                    Rimuru.send_text(sender_id,'Actualité covid : Developpement du projet en cours')
                                    print("asdf")
                            elif 'conseil_covid19' in payload:
                                
                                Rimuru.send_text(sender_id, 'CONSEIL : Developpement du projet en cours')
                            elif 'query_hosp' in payload:
                                print('tonga ========')
                                query_hosp= database.getquery(sender_id)
                                res= query_hosp + '  == >Resulta'
                                Rimuru.send_text(sender_id,res)
                                print(res)
                elif 'postback' in messaging_event:
                    if 'payload' in messaging_event['postback']:
                        pload = messaging_event['postback']['payload']
                    if 'get_started' == pload:
                        Rimuru.send_text(sender_id, "Bonjour je suis Rimuru")  
                        Rimuru.main_menu(sender_id)  
                    if is_json(pload):
                        pload_json = json.loads(pload)
                        print(pload_json)
                        


    return 'ok'
    
Rimuru.get_stared()

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
